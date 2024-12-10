import pytest
from city import City

def test_department_01(city01):
    assert '01' == city01.department()

def test_department_31(city31):
    assert '31' == city31.department()

def test_department_95(city95):
    assert '95' == city95.department()

def test_department_2A(city2A):
    assert '2A' == city2A.department()

def test_department_2B(city2B):
    assert '2B' == city2B.department()

def test_department_97a(city97a):
    assert '972' == city97a.department()

def test_department_97b(city97b):
    assert '971' == city97b.department()

def test_department_98(city98):
    assert '987' == city98.department()

def test_incr_population(city01):
    city01.incr_population(100)
    assert 41625 == city01.population


def test_parse_nominal():
    city_str = 'Toulouse,31000,477000'
    c = City.parse(city_str)
    assert 'Toulouse' == c.name
    assert '31000' == c.zipcode
    assert 477000 == c.population

@pytest.mark.parametrize(
        "city_str",
        [
            'Toulouse,31000',
            'Toulouse',
            'Toulouse,31000,77000,ville rose',
        ]
)
def test_parse_wrong_number_of_fields(city_str):
    with pytest.raises(ValueError) as ex_info:
        City.parse(city_str)
    assert 'wrong format of city' == str(ex_info.value)