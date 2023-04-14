def validate_weight(number):
    if not isinstance(number, (int, float)):
        return "input number"
    elif number < 0:
        return "Not valid"
    else:
        return number


def process_weight(weight, price):
    result = validate_weight(weight)
    if isinstance(result, str):
        return result
    else:
        return result * price


def sum_of_price(orange, mango, watermelon):
    orange = validate_weight(orange)
    mango = validate_weight(mango)
    watermelon = validate_weight(watermelon)

    if isinstance(orange, str):
        return orange
    elif isinstance(mango, str):
        return mango
    elif isinstance(watermelon, str):
        return watermelon
    else:
        orange = process_weight(orange, 75)
        mango = process_weight(mango, 80)
        watermelon = process_weight(watermelon, 50)
        return orange + mango + watermelon
