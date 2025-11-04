from src.grade_calculator import grade_calculator


def test_grade_calculator_is_empty_returns_error():
    assert grade_calculator([]) == "Error: no scores provided"


def test_grade_calculator_returns_invalid_scores_below_0_returns_error():
    assert grade_calculator([-4]) == "Error: scores cannot be negative"


def test_single_score_should_return_correct_grade1():
    assert grade_calculator([1]) == "F"


def test_single_score_should_return_correct_grade2():
    assert grade_calculator([2]) == "F"


def test_single_score_should_return_correct_grade3():
    assert grade_calculator([3]) == "F"


def test_single_score_should_return_correct_grade4():
    assert grade_calculator([4]) == "F"
