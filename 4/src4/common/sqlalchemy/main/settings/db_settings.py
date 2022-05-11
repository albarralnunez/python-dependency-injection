from src4.common.conf_settings.main.settings import BaseSettings


class DbSettings(BaseSettings):
    @property
    def mapping(self):
        return {
            "url": str,
            "migrations_dir": str,
            "testing": bool,
            "automigrate": bool
        }
