from abc import  ABC,abstractmethod


class AbstractPlatform(ABC):
    @abstractmethod
    def storage_config(self):
        pass

    @abstractmethod
    def notification_config(self):
        pass

    @abstractmethod
    def ui_config(self):
        pass

class AbstractConfiguration(ABC):

    @abstractmethod
    def do_something_cool(self):
        pass

class WindowsPlatform(AbstractPlatform):

    def storage_config(self):
        return " Storage Config for windows"
    def storage_config(self):
        return " Storage Config for windows"
    def storage_config(self):
        return " Storage Config for windows"
