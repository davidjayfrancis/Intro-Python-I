import math

def primeChecker(num):
    if num % 2 == 0:
        return False
    if num % 3 == 0:
        return False

    n = 5
    for i in range(5,math.ceil(math.sqrt(num))):
        if num % i == 0:
            print(f"{num} is not prime. {num} is divisible by {i}.")
            return False
    
    return True


    
        
            

    return nums
    # add every prime multiple while the prime * 2 < num


print(primeChecker(100))
print(primeChecker(95))