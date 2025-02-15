a = int(input("Enter a number: "))
b = int(input("Enter a number: "))

def ev(a, b):
    for i in range(a, b+1):
        yield i**2  
            
my_nums = ev(a, b)
for i in my_nums:
    print(i)