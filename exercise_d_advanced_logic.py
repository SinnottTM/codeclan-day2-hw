
# For the following list of numbers:
numbers = [1, 6, 2, 2, 7, 1, 6, 13, 99, 7]

# 1. Print out a list of the even integers:
even_ints = []
for num in numbers:
    if num % 2 == 0:
       even_ints.append(num)
print(even_ints)

# 2. Print the difference between the largest and smallest value:
largest_minus_smallest = max(numbers)-min(numbers)
print(largest_minus_smallest)

# 3. Print True if the list contains a 2 next to a 2 somewhere.
for i in range(len(numbers)):
    while numbers[i] == 2 and numbers[i+1] == 2:
        print(True)
        break

# 4. Print the sum of the numbers,
#    BUT ignore any section of numbers starting with a 6 and extending to the next 7.
#    So [11, 6, 4, 99, 7, 11] would have sum of 22
no_six_to_seven = 0
between_six_to_seven = False

for num in numbers:
    if(num == 6):
        between_six_to_seven = True
        continue
    if(num == 7 and between_six_to_seven is True):
        between_six_to_seven = False
        continue
    if(between_six_to_seven is False):
       no_six_to_seven += num

print(no_six_to_seven)

# 5. HARD! Print the sum of the numbers.
#    Except the number 13 is very unlucky, so it does not count.
#    And numbers that come immediately after a 13 also do not count.
#    HINT - You will need to track the index throughout the loop.
#    So [5, 13, 2] would have sum of 5.
complex_total = 0
complex_total_thirteen_checker = False

for num in numbers:
    if(num == 13):
        complex_total_thirteen_checker = True
        continue
    if(num != 13 and complex_total_thirteen_checker is True):
        complex_total_thirteen_checker = False
        continue
    if(complex_total_thirteen_checker is False):
       complex_total += num

print(complex_total)
