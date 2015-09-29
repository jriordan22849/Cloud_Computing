ans = 0

for i in xrange(1, 10):
    if i%3 == 0:
        ans += i
    elif i%5 == 0:
        ans += i

print ans