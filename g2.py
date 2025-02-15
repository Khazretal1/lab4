n = int(input("Enter a number: "))

def ev(n):
    for i in range(0, n+1, 2):
            yield i
            
my_nums = ev(n)

print(", ".join(map(str, my_nums)))
