num = int(input("Enter a number: "))
count = 0
temp = abs(num)

if temp == 0:
    count = 1
else:
    while temp > 0:
        temp //= 10
        count += 1

print(f"The number {num} has {count} digits.")
