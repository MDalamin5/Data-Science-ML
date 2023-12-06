# def sum(num1, num2, num=0):
#     result = num1 + num2
#     return result

# total = sum(1, 2, 3)

def all_sum(num1, num2, *numbers):
    # print(numbers)
    sum = 0 
    sum = num1 + num2
    for num in numbers:
        sum += num
    print(sum)

all_sum(1, 3, 4, 5, 6)