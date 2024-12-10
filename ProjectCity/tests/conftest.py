import pytest

from city import City


@pytest.fixture
def city01() -> City:
    return City(name='Bourg-en-Bresse', zipcode='01000', population=41525)

@pytest.fixture
def city31() -> City:
    return City(name='Toulouse', zipcode='31000')

@pytest.fixture
def city95() -> City:
    return City(name='Cergy', zipcode='95000')

@pytest.fixture
def city97a() -> City:
    return City(name='Le Lamentin', zipcode='97232')

@pytest.fixture
def city97b() -> City:
    return City(name='Pointe-à-Pitre', zipcode='97110')

@pytest.fixture
def city98() -> City:
    return City(name='Fakarava', zipcode='98790')

@pytest.fixture
def city2A() -> City:
    return City(name='Ajaccio', zipcode='20000')

@pytest.fixture
def city2B() -> City:
    return City(name='Bastia', zipcode='20200')