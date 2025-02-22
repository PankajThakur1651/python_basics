from datetime import datetime


def validate_card(exp_date):
    current_date = datetime.now().date()
    print("Current date:", current_date)
    print("Expiration date:", exp_date)

    if exp_date < current_date:
        raise RuntimeError("Card has Expired")
    else:
        return "Valid"