count = 10**5
nums = []

# Method 1
for i in range(count):
    nums.append(i)
nums.reverse()

# Method 2
for i in range(count):
    nums.insert(0, i)
