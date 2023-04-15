
def validate_weight(number):
    if not isinstance(number, (int, float)):
        return "input number"
    elif number < 0:
        return "Not valid"
    else:
        return number


def caculate(weight, price):
    return weight * price


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
        orange = caculate(orange, 75)
        mango = caculate(mango, 80)
        watermelon = caculate(watermelon, 50)
        return orange + mango + watermelon
