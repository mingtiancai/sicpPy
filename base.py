from abc import ABCMeta, abstractmethod

class base_sicp_class(metaclass=ABCMeta):
    @abstractmethod
    def valid_func(self):
        pass

    @abstractmethod
    def test_func(self):
        pass
