n = int(input("Enter a number: "))

my_nums = (x for x in range(n, -1, -1))

for x in my_nums:
    print(x)