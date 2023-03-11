from random import Random
from datetime import datetime
from abc import abstractmethod, ABC

from typing import Any

class MaxCapacityReachedException(Exception):
    pass

class NoRegisterInstanceException(Exception):
    pass

class BaseInstance(ABC):
    def __init__(self, address: str):
        self.address = address


class BaseLoadBalancer(ABC):
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.instances = []

    def _validate_maximum_capacity(self):
        if len(self.instances) >= self.capacity:
            raise MaxCapacityReachedException(f"Maximum capacity of load balancer has reached")

    def register(self, instance: BaseInstance):
        self._validate_maximum_capacity()
        self.instances.append(instance)

    @abstractmethod
    def _get_instance(self) -> BaseInstance:
        pass

    def get(self) -> BaseInstance:
        if not self.instances:
            raise NoRegisterInstanceException("The load balancer has no registered instance")
        return self._get_instance()

class SimpleInstance(BaseInstance):
    pass


class SimpleLoadBalancer(BaseLoadBalancer):
    def _get_instance(self) -> BaseInstance:
        return self.instances[0]


class RandomGetLoadBalancer(BaseLoadBalancer):
    def __init__(self, capacity: int, initial_seed: Any = datetime.now()):
        super().__init__(capacity)
        self.randomizer = Random(initial_seed)

    def _get_instance(self) -> BaseInstance:
        return self.randomizer.choice(self.instances)


class RoundRibbonLoadBalancer(BaseLoadBalancer):
    def __init__(self, capacity: int):
        super().__init__(capacity)
        self.round_ribbon_counter = 0
        self.round_ribbon_mod = 0

    def register(self, instance: BaseInstance):
        super().register(instance)
        self.round_ribbon_mod += 1

    def _get_instance(self) -> BaseInstance:
        inst = self.instances[self.round_ribbon_counter % self.round_ribbon_mod]
        self.round_ribbon_counter += 1
        return inst
