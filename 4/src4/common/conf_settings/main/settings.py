import abc
import os
from pathlib import Path

import yaml
from munch import Munch

from src4.common.conf_settings.main.exception import SettingAttributeError, MappingKeyMissingError, \
    MappingWrongTypeError


class BaseSettings:
    def __init__(self, name: str):
        self._conf_dict: dict = self._load(name)
        self._settings = self._check_and_build_dict_with_mappings(
            self._conf_dict, self.mapping
        )

    def __getattr__(self, item):
        try:
            return self._conf_dict[item]
        except KeyError:
            attributes = ", ".join(self.mapping.keys())
            raise SettingAttributeError(
                f'"{item}" does not exist in settings. Available settings are: {attributes}'
            )

    @property
    @abc.abstractmethod
    def mapping(self) -> dict:
        ...

    @classmethod
    def _load(cls, name: str) -> dict:
        conf_dir = Path(os.environ["FORTH_CONF_DIR"])
        conf_path = conf_dir / f"{name}.yml"
        conf_path_resolved = conf_path.resolve()
        with conf_path_resolved.open() as settings_file:
            data = yaml.safe_load(settings_file.read())
        return data

    @staticmethod
    def _check_and_build_dict_with_mappings(my_dict, mappings_dict) -> dict:
        ret = {}
        for (mapping_key, mapping_type) in mappings_dict.items():
            if mapping_key not in my_dict.keys():
                raise MappingKeyMissingError(f'"{mapping_key}" missing in config')
            if type(my_dict[mapping_key]) == dict:
                item = Munch.fromDict(
                    BaseSettings._check_and_build_dict_with_mappings(
                        my_dict[mapping_key], mappings_dict[mapping_key]
                    )
                )
            elif type(my_dict[mapping_key]) == mapping_type:
                item = my_dict[mapping_key]
            else:
                raise MappingWrongTypeError(
                    f'"{mapping_key}" should be of type {mapping_type}'
                )

            ret[mapping_key] = item
        return ret
