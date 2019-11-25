userInput = int(input("Price :"))
def vatCalculate(userInput):
    totalPrice = userInput*7/100 + userInput
    return totalPrice
print(vatCalculate(userInput))