num = int(input("Enter a number: "))
limit = int(input("Enter the limit: "))

print("\n----- MULTIPLICATION TABLE -----")

for i in range(1, limit + 1):
    print(num, "x", i, "=", num * i)
