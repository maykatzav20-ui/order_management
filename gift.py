from abc import ABC, abstractmethod


class Gift(ABC):
    @abstractmethod
    def open_gift(self):
        pass


class SurpriseGift(Gift):
    def open_gift(self):
        print("Congratulations! you got a new gift! Enjoy!")
