from function import sum_of_price
input_orange = input("orange: ")
input_mango = input("mango: ")
input_watermelon = input("watermelon: ")

try:
    input_orange = float(input_orange)
    input_mango = float(input_mango)
    input_watermelon = float(input_watermelon)
except:
    input_orange = str(input_orange)
    input_mango = str(input_mango)
    input_watermelon = str(input_watermelon)


result = sum_of_price(input_orange,input_mango,input_watermelon)
print(result)
