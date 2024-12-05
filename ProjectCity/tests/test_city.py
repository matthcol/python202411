import pytest
from city import City

@pytest.fixture
def city01() -> City:
    return City(name='Bourg-en-Bresse', zipcode='01000', population=41525)

def test_department_01(city01):
    assert '01' == city01.department()

def test_incr_population(city01):
    city01.incr_population(100)
    assert 41625 == city01.population


def test_parse():
    city_str = 'Toulouse,31000,477000'
    c = City.parse(city_str)
    assert 'Toulouse' == c.name
    assert '31000' == c.zipcode
    assert 477000 == c.population