import pytest

from src.load_balancer import BaseInstance
from src.load_balancer import SimpleInstance, SimpleLoadBalancer
from src.load_balancer import RandomGetLoadBalancer
from src.load_balancer import RoundRibbonLoadBalancer

from src.load_balancer import MaxCapacityReachedException, NoRegisterInstanceException


@pytest.fixture
def simple_load_balancer():
    return SimpleLoadBalancer(capacity=10)


@pytest.fixture
def random_get_load_balancer():
    lb = RandomGetLoadBalancer(capacity=3, initial_seed=0)
    lb.register(SimpleInstance(address="0"))
    lb.register(SimpleInstance(address="1"))
    lb.register(SimpleInstance(address="2"))
    return lb


@pytest.fixture
def round_ribbon_load_balancer():
    lb = RoundRibbonLoadBalancer(capacity=3)
    lb.register(SimpleInstance(address="0"))
    lb.register(SimpleInstance(address="1"))
    lb.register(SimpleInstance(address="2"))
    return lb


def test_simple_load_balancer_can_register_intance(
    simple_load_balancer: SimpleLoadBalancer,
):
    assert simple_load_balancer.instances == []

    simple_instance = SimpleInstance(address="1")
    simple_load_balancer.register(simple_instance)

    assert simple_load_balancer.instances == [simple_instance]


def test_simple_load_balancer_cannot_register_beyond_capacity(
    simple_load_balancer: SimpleLoadBalancer,
):
    simple_instances = [SimpleInstance(address=str(i)) for i in range(10)]
    extra_instance = SimpleInstance(address="10")

    for inst in simple_instances:
        simple_load_balancer.register(inst)

    with pytest.raises(MaxCapacityReachedException):
        simple_load_balancer.register(extra_instance)


def test_exception_will_raise_if_no_instance_was_registered(simple_load_balancer):
    with pytest.raises(NoRegisterInstanceException):
        simple_load_balancer.get()


def test_random_get_load_balancer(random_get_load_balancer: RandomGetLoadBalancer):
    instances: list[BaseInstance] = []
    for _ in range(10):
        instances.append(random_get_load_balancer.get())

    result = [i.address for i in instances]
    expected = ["1", "1", "0", "1", "2", "1", "1", "1", "1", "1"]

    assert result == expected


def test_round_robbin_load_balancer_give_instance(
    round_ribbon_load_balancer: RoundRibbonLoadBalancer,
):
    instance_addresses: list[str] = []
    for _ in range(10):
        instance_addresses.append(round_ribbon_load_balancer.get().address)

    expected = ["0", "1", "2", "0", "1", "2", "0", "1", "2", "0"]

    assert instance_addresses == expected
