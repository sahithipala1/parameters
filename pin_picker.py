def pinPicker(number):
    import random
    pin = ""
    for i in range(number):
        pin += str(random.randint(0, 9))
    return pin


myPin = pinPicker(5)
print(myPin)
