num = int(input())
count = 0
n = abs(num)   
if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10   
        count += 1
print( count)
