#Write your code below this row 👇

sum_of_even = 0

for number in range (2, 101, 2):
  sum_of_even += number

print(sum_of_even)

sum_of_even2 = 0
for number in range(1,101):
  if number % 2 == 0:
    sum_of_even2 += number

print(sum_of_even2)