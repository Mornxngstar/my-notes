from typing import List


def run():
    try:
        times = int(input("How many numbers do you want this sequence to have? "))
    except ValueError:
        run()

    nums: List[int] = [0]

    current_num: int = 1
    previous_num: int = 0
    aux: int = 0

    for i in range(times + 1):
        nums.append(current_num)
        aux, previous_num = current_num, aux
        current_num += previous_num
    
    print(nums)


if __name__ == '__main__':
    run()