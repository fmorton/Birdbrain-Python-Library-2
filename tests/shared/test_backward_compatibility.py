from birdbrain.constant import Constant
from birdbrain.finch import Finch
from birdbrain.hummingbird import Hummingbird
from birdbrain.tasks import Tasks


def test_instantiating_devices_old_way():
    try:
        from BirdBrain import Constant, Finch, Hummingbird, Tasks

        Constant()
        Finch('B')
        Hummingbird('A')
        Tasks()

        Constant()
        Finch('B')
        Hummingbird('A')
        Tasks()

        assert Constant().LEFT == 'L'
    except ImportError:
        pass
