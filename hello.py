# Fakhar_Altaf_261949256_Lab9

from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self, sides):
        self.sides = sides
    
    @abstractmethod
    def compute_area(self):
        pass

class Triangle(Shape):
    def __init__(self, base, height):
        super().__init__(3)
        self.base = base
        self.height = height
    
    def compute_area(self):
        return 0.5 * self.base * self.height

class Circle(Shape):
    def __init__(self, radius):
        super().__init__(0)
        self.radius = radius
    
    def compute_area(self):
        return 3.14159265359 * (self.radius**2)

def driver():
    
    triangle = Triangle(4, 6)
    circle = Circle(3)
    print("Triangle area:",triangle.compute_area())
    print("Circle area:",circle.compute_area())

driver()


class Employee:
    def __init__(self, emp_name, emp_id, salary):
        self.emp_name = emp_name
        self.emp_id = emp_id
        self.salary = salary
    
    def salary_status(self):
        return "Salary:", self.salary

class BuildingManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 10000)

class ProcurementManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 12000)

class LogisticsManager(Employee):
    def __init__(self, emp_name, emp_id):
        super().__init__(emp_name, emp_id, 15000)

def main():
    employees = [
        BuildingManager("John Doe", "BM001"),
        ProcurementManager("Jane Smith", "PM001"),
        LogisticsManager("Mike Johnson", "LM001")
    ]

    for employee in employees:
        print("Employee Name:", employee.emp_name)
        print("Employee ID:", employee.emp_id)
        print(employee.salary_status())
        print()

main()
