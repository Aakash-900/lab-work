def sum(x, y, z):
    if x == y or y == z or x==z:
        sum = 0
    else:
        sum = x + y + z
    return sum

print(sum(4, 1, 4))
print(sum(5, 2, 5))
print(sum(7, 2, 7))
print(sum(3, 4, 5))
