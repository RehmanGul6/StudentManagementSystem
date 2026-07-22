import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from grading import calculate_grade

def test_grade_A():
    assert calculate_grade(95) == "A"

def test_grade_B():
    assert calculate_grade(85) == "B"

def test_grade_C():
    assert calculate_grade(75) == "C"

def test_grade_D():
    assert calculate_grade(65) == "D"

def test_grade_F():
    assert calculate_grade(40) == "F"