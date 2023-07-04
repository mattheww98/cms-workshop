import geom_analysis as ga
import pytest
def test_calculate_distance():
    coord1 = [0,0,0]
    coord2 = [1,0,0]
    expected = 1.0
    observed = ga.calculate_distance(coord1,coord2)
    assert observed == expected
def test_bond_check_true():
    distance = 1
    expected = True
    observed = ga.bond_check(distance)
    assert observed == expected 
def test_bond_check_false():
    distance = 2
    expected = False
    observed = ga.bond_check(distance)
    assert observed == expected
def test_bond_check_0():
    distance = 0
    expected = False
    observed = ga.bond_check(distance)
    assert observed == expected
def test_bond_check_1_5():
    distance = 1.5
    expected = True
    observed = ga.bond_check(distance)
    assert observed == expected
def test_bond_check_negative():
    distance = -1
    expected = False
    with pytest.raises(ValueError):
        calculated = ga.bond_check(distance)
def test_open_xyz():
    filename = "hello.txt"
    with pytest.raises(ValueError):
        calculated = ga.open_xyz(filename)