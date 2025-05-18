print("Enter the Number : ")
num = int(input())

num_str = str(num)
digit_sum = 0

for digit in num_str:
    digit_sum = digit_sum + int(digit)

print(digit_sum)