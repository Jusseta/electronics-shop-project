import pytest
from src.keyboard import Keyboard


@pytest.fixture
def item3():
    return Keyboard('Dark Project KD87A', 9600, 5)


def test_language(item3):
    assert item3.language == 'EN'


def test_change_lang(item3):
    assert item3.language == "EN"
    item3.change_lang()
    assert item3.language == "RU"
