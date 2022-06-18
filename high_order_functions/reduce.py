from functools import reduce
from typing import List

my_list: List[int] = [2,2,2,2,2]

all_multiplied = reduce(lambda a,b: a * b, my_list)

print(all_multiplied)
