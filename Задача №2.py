
numbers=[]
sum_list_a=0
sum_list_b=0
for i in range(1,1001,2):
    numbers.append(i**3)

def sum_list_cube (numbers):
    total = 0
    for number in numbers:
        sum = 0
        number_sum = number
        while number > 0:
            sum += number % 10
            number = number // 10
        if sum % 7 == 0:
            total += number_sum
    return total

print('a:', sum_list_cube (numbers))
print('b,c:', sum_list_cube ([number + 17 for number in numbers]))
