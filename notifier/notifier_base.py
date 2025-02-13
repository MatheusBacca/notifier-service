from notifier.config import ConfigManager


class NotifierBase:
    def __init__(self):
        config_manager = ConfigManager()
        self.config = config_manager.get_config()
