# core/scoring.py
def calculate_match_score(similarity: float) -> float:
    return round(similarity * 100, 2)