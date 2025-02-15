def squares(n):
    for i in range(1, n+1):
        yield i*i
        

my_nums = squares(4)
for i in my_nums:
    print(i)

print(my_nums)