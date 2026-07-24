from employee_class import Employee

def test_give_default_raise():
    employee=Employee("John","Doe",90000)
    employee.give_raise()
    assert employee.salary==95000

def test_give_custom_raise():
    employee=Employee("John","Doe",90000)
    employee.give_raise(20000)
    assert employee.salary==110000