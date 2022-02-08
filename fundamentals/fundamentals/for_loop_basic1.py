# 1
for i in range(151):
    print(i)

# 2
for x in range(5, 1005, 5):
    print(x)

# 3
for y in range(1, 101):
    if y % 10 ==0:
        print("Coding Dojo")
    elif y % 5 == 0:
        print("Coding")
    else:
        print(y)

# 4
sum = 0
for z in range(500000):
    if (z+1) % 2 == 0:
        sum = sum + z
print(sum)

# 5
for i in range(2018, 0, -4):
    print(i)

# 6
lowNum = 2
highNum = 9
mult = 3
for x in range(lowNum, highNum+1):
    if x % mult == 0:
        print(x)