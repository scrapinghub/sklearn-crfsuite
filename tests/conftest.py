import pytest


@pytest.fixture()
def xseq():
    return [
        {"walk": 1, "shop": 0.5},
        {"walk": 1},
        {"walk": 1, "clean": 0.5},
        {"shop": 0.5, "clean": 0.5},
        {"walk": 0.5, "clean": 1},
        {"clean": 1, "shop": 0.1},
        {"walk": 1, "shop": 0.5},
        {},
        {"clean": 1},
        {"солнце": "не светит".encode(), "clean": 1},
    ]


@pytest.fixture
def yseq():
    return [
        "sunny",
        "sunny",
        "sunny",
        "rainy",
        "rainy",
        "rainy",
        "sunny",
        "sunny",
        "rainy",
        "rainy",
    ]
