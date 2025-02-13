import os
from configobj import ConfigObj


class ConfigManager:
    _instance = None
    _config = None

    DEFAULT_CONFIG_PATH = os.path.join(
        os.path.dirname(__file__), "../config/config_default.cfg"
    )
    CONFIG_PATH = os.path.join(os.path.dirname(__file__), "../config/config.cfg")

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ConfigManager, cls).__new__(cls)
            cls._instance._load_config()
        return cls._instance

    def _load_config(self):
        """Carrega o arquivo de configuração, criando um novo se não existir."""
        if not os.path.exists(self.CONFIG_PATH):
            default_config = ConfigObj(self.DEFAULT_CONFIG_PATH, encoding="utf-8")
            self._config = ConfigObj(
                self.CONFIG_PATH, encoding="utf-8", write_empty_values=True
            )
            self._config.update(default_config)
            self._config.write()
        else:
            self._config = ConfigObj(self.CONFIG_PATH, encoding="utf-8")

    def get_config(self):
        """Retorna a configuração carregada."""
        return self._config

    def set_config(self, new_config):
        """Permite modificar e salvar configurações dinamicamente."""
        self._config.update(new_config)
        self._config.write()
