from numpy.ma.extras import average


def grade_calculator(scores: list[int]) -> str :
    if scores == []:
        return "Error: no scores provided"
    if any(score < 0 for score in scores):
        return "Error: scores cannot be negative"

    if any (score <60 for score in scores):
        return "F"

    if average(scores) < 60:
         return "F"
