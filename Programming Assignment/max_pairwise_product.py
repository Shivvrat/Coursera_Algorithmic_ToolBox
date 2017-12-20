# Uses python3
n = int(input())
a = [int(x) for x in input().split()]
assert (len(a) == n)

result = 0


max1 = max(a)
a.remove(max(a))
max2 = max(a)
result = max1 * max2

print(result)
