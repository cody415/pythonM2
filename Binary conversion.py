decimal_num = int(input("Enter a decimal number: "))
binary_num = ""

temp = decimal_num
while temp > 0:
    binary_num = str(temp % 2) + binary_num
    temp //= 2

print(f"The binary representation of {decimal_num} is: {binary_num}")
