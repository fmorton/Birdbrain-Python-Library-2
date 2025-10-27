from birdbrain_python_library_2.birdbrain_constant import BirdbrainConstant
from birdbrain_python_library_2.birdbrain_finch import BirdbrainFinch
from birdbrain_python_library_2.birdbrain_hummingbird import BirdbrainHummingbird
from birdbrain_python_library_2.birdbrain_tasks import BirdbrainTasks

from BirdBrain import Constant, Finch, Hummingbird, Tasks


def test_instantiating_devices_old_way():
    BirdbrainConstant()
    BirdbrainFinch('B')
    BirdbrainHummingbird('A')
    BirdbrainTasks()

    Constant()
    Finch('B')
    Hummingbird('A')
    Tasks()

    assert Constant().LEFT == 'L'
