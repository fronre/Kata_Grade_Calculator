from src.grade_calculator import grade_calculator

def test_grade_calculator_is_empty_returns_error():
        assert grade_calculator([]) == "Error: no scores provided"

def test_grade_calculator_returns_invalid_scores_below_0_returns_error():
  assert grade_calculator([-8,-4]) == "Error: scores cannot be negative"