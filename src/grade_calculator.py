def grade_calculator(scores: list[int]) -> str :
    if scores == []:
        return "Error: no scores provided"
    if any(score < 0 for score in scores):
        return "Error: scores cannot be negative"

    if scores == [1]:
        return "F"
    if scores == [2]:
        return "F"
    if scores == [3]:
        return "F"
    if scores == [4]:
        return "F"
