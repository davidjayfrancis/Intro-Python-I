import math

def primeChecker(num):
    # assume num is 100
    currentPrime = 2

    nums = {}
    for i in range(1,num+1):
        nums[i] = True
    
    for i in range(2, math.ceil(math.sqrt(num))):
        print(i)
        
            

    return nums
    # add every prime multiple while the prime * 2 < num


print(primeChecker(100))