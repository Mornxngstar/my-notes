# from typing import Tuple, List

# def white_spacing(num1: str, num2: str) -> Tuple[str,str,str] :
#   if len(num1) >= len(num2): 
#     dashes = '-' * (len(num1) + 2)
#     white_spc = len(num1) - len(num2)
#     for i in range(white_spc): num2 += " "
#     num2 = num2[::-1]
#     return num1, num2, dashes
#   else:
#     dashes = '-' * (len(num2) + 2)
#     white_spc = len(num2) - len(num1)
#     for i in range(white_spc): num1 += " "
#     num1 = num1[::-1]
#     return num1, num2, dashes

# def arithmetic_arranger(problems, show_answrs=False):
#   arranged_problems = ""
#   counter = 0
    
  
      
#   for i in problems:
#     if i.find('-') >= 0:
#       index = i.find('-')
      
#     elif i.find('+') >= 0:
#       index = i.find('+')
      
#     num1 = i[:index-1]
#     num2 = i[index+1:]

#     try:
#       int(num1)
#     except ValueError:
#       return "Error: Numbers must only contain digits."

#     try:
#       int(num2)
#     except ValueError:
#       return "Error: Numbers must only contain digits."

#     if len(num1) > 4 or len(num2) > 4:
#       return "Error: Numbers cannot be more than four digits."
      
#     if len(problems) == 1:
#       nums: Tuple[str,str,str] = white_spacing(num1,num2)
#       return f'  {nums[0]}\n- {nums[1]}\n{nums[2]}'
#     elif len(problems) == 2:
#       pass
#     elif len(problems) == 3:
#       pass
#     elif len(problems) == 4:
#       pass
#     elif len(problems) == 5:
#       pass
#     elif len(problems) > 5:
#       return "Error: Too many problems."

# problems: List[str] = ['3801 - 2']

# print(arithmetic_arranger(problems))

hour = "12:32:AM"
h = hour.split(":")
print(h)