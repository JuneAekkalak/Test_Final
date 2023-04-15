from function import sum_of_price

input_orange = input("orange: ")
input_mango = input("mango: ")
input_watermelon = input("watermelon: ")

try:
    input_orange = int(input_orange)
except ValueError:
    try:
        input_orange = float(input_orange)
    except ValueError:
        input_orange = str(input_orange)

try:
    input_mango = int(input_mango)
except ValueError:
    try:
        input_mango = float(input_mango)
    except ValueError:
        input_mango = str(input_mango)

try:
    input_watermelon = int(input_watermelon)
except ValueError:
    try:
        input_watermelon = float(input_watermelon)
    except ValueError:
        input_watermelon = str(input_watermelon)

result = sum_of_price(input_orange, input_mango, input_watermelon)
print("Total Price is: ", result)
