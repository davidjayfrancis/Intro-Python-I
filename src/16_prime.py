import math

def primeChecker(num):
    if num == 1:
        return False
    elif num == 2:
        return True
    elif num == 3:
        return True
    else:
        if num % 2 == 0 or num % 3 == 0:
            return False

        n = 5
        for i in range(5,math.ceil(math.sqrt(num))):
            if num % i == 0:
                return False
        return True
        # add every prime multiple while the prime * 2 < num


print(primeChecker(1))
print(primeChecker(2))
print(primeChecker(3))
print(primeChecker(4))
print(primeChecker(5))
print(primeChecker(6))
print(primeChecker(7))
print(primeChecker(21))
print(primeChecker(29))
print(primeChecker(97))
print(primeChecker(52363))
