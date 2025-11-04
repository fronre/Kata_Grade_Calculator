from src.grade_calculator import grade_calculator

def test_grade_calculator_is_empty_returns_error():
        assert grade_calculator([]) == "Error: no scores provided"


