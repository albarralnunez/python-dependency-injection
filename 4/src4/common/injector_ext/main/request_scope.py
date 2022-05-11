from injector import ScopeDecorator

from src4.common.injector_ext.main.aiotask_scope import AioTaskScope

request = ScopeDecorator(AioTaskScope)
