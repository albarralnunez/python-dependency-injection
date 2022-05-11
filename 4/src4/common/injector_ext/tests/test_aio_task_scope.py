import asyncio
from asyncio import current_task, gather

import pytest
from injector import Injector, Module
from pytest import fixture

from src4.common.injector_ext.main.request_scope import request


class DummyClass:
    ...


class DummyModule(Module):
    def configure(self, binder):
        binder.bind(DummyClass, scope=request)


async def dummy_class_coroutine_factory(injector):
    task = current_task()
    dummy_instance = injector.get(DummyClass)
    return dummy_instance, task


def dummy_class_factory(injector):
    task = current_task()
    dummy_instance = injector.get(DummyClass)
    return dummy_instance, task


@fixture
def injector():
    _injector = Injector(modules=[DummyModule])
    yield _injector


@pytest.mark.asyncio
async def test_aio_task_scope_different_instance_different_task(injector):
    coroutine_1 = dummy_class_coroutine_factory(injector)
    coroutine_2 = dummy_class_coroutine_factory(injector)
    result = await gather(coroutine_1, coroutine_2)
    dummy_instance_1, task_1 = result[0]
    dummy_instance_2, task_2 = result[1]
    assert dummy_instance_1 is not dummy_instance_2
    assert task_1 is not task_2


@pytest.mark.asyncio
async def test_aio_task_same_instance_same_task_in_different_coroutine(injector):
    coroutine_1 = dummy_class_coroutine_factory(injector)
    coroutine_2 = dummy_class_coroutine_factory(injector)
    dummy_instance_1, task_1 = await coroutine_1
    dummy_instance_2, task_2 = await coroutine_2
    assert dummy_instance_1 is dummy_instance_2
    assert task_1 is task_2


@pytest.mark.asyncio
async def test_aio_task_scope_same_instance_same_task(injector):
    dummy_instance_1, task_1 = await dummy_class_coroutine_factory(injector)
    dummy_instance_2, task_2 = dummy_class_factory(injector)
    assert dummy_instance_1 is dummy_instance_2
    assert task_1 is task_2


@pytest.mark.asyncio
async def test_aio_task_scope_same_instance_different_task_child(injector):
    dummy_instance_2, task_2 = dummy_class_factory(injector)
    dummy_instance_1, task_1 = await asyncio.create_task(
        dummy_class_coroutine_factory(injector)
    )
    assert dummy_instance_1 is dummy_instance_2
    assert task_1 is not task_2


@pytest.mark.asyncio
async def test_aio_task_scope_different_instance_different_task_child(injector):
    dummy_instance_1, task_1 = await asyncio.create_task(
        dummy_class_coroutine_factory(injector)
    )
    dummy_instance_2, task_2 = dummy_class_factory(injector)
    assert dummy_instance_1 is not dummy_instance_2
    assert task_1 != task_2
    assert task_1 is not task_2
