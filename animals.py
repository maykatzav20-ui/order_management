from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self, legs: int):
        self._legs = legs

    @property
    def legs(self):
        return self._legs

    def walk(self):
        print(f"Walking on {self.legs} legs")

    def eat(self):
        print("Animal is eating")


class Pet(ABC):
    @abstractmethod
    def getName(self) -> str:
        pass

    @abstractmethod
    def setName(self, name: str):
        pass

    @abstractmethod
    def play(self):
        pass


class Spider(Animal):
    def __init__(self):
        super().__init__(8)

    def eat(self):
        print("Spider is eating insects")


class Cat(Animal, Pet):
    def __init__(self, name: str = ""):
        super().__init__(4)
        self._name = name

    def getName(self) -> str:
        return self._name

    def setName(self, name: str):
        self._name = name

    def play(self):
        print(f"{self._name} is playing")

    def eat(self):
        print(f"{self._name} is eating cat food")


class Fish(Animal, Pet):
    def __init__(self, name: str = ""):
        super().__init__(0)
        self._name = name

    def getName(self) -> str:
        return self._name

    def setName(self, name: str):
        self._name = name

    def play(self):
        print(f"{self._name} is swimming and playing")

    def walk(self):
        print("Fish cannot walk on legs")

    def eat(self):
        print(f"{self._name} is eating fish food")
