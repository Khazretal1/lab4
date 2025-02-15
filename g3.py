n = int(input("Enter a number: "))

def ev(n):
    for i in range(0, n+1):
            if i % 3 == 0 and i % 4 == 0:
                yield i
            
my_nums = ev(n)
for i in my_nums:
    print(i)