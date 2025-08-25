# service.py
from datetime import datetime

# Hardcoded gold price (per gram in INR)
GOLD_PRICE_PER_GRAM = 10000

def get_gold_price() -> float:
    """Return the current gold price per gram."""
    return GOLD_PRICE_PER_GRAM

def calculate_investment(username: str, grams: float) -> dict:
    """
    Calculate total investment for a given user and gold amount.
    Returns a dictionary with investment details.
    """
    try:
        grams = float(grams)
        if grams <= 0:
            raise ValueError("Grams must be positive.")
        total_cost = grams * GOLD_PRICE_PER_GRAM
        investment_data = {
            "username": username,
            "grams": grams,
            "gold_price_per_gram": GOLD_PRICE_PER_GRAM,
            "total_cost": total_cost,
            "date_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        return investment_data
    except Exception as e:
        raise ValueError(f"Error calculating investment: {e}")
