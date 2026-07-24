from employee_class import Employee
import pytest

@pytest.fixture
def employee_info():# this function name 
    employee=Employee("John","Doe",90000)
    return employee

def test_give_default_raise(employee_info):# and this parameter has to be same
    employee_info.give_raise()
    assert employee_info.salary==95000

def test_give_custom_raise(employee_info):# parameter should match fixture function name
    employee_info.give_raise(20000)
    assert employee_info.salary==110000