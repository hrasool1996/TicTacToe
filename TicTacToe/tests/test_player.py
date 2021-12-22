from tictactoe import __version__
from tictactoe.player import Player


def test_version():
    assert __version__ == '0.1.0'

def test_func():
    p = Player()
    assert p.func(3) == 4