from typing import List

def is_prime(nums:List[int]) -> List[int]:
    primes: List[int] = []

    for i in nums:
        if i == 1: continue
        if i == 2: 
            primes.append(i)
            continue
        count = 0

        for j in range(2, i):
            if (i%j == 0):
                count += 1
        
        if count == 0: primes.append(i)

    return primes

def run():
    nums: List[int] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]

    print(is_prime(nums))


if __name__ == '__main__':
    run()