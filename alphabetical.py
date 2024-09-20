nums = [5,30,99,60,5,10]
jar1 = 0
jar2 = 0
for i in range(0,len(nums)):
    temp = max(jar1+nums[i], jar2)
    jar1 = jar2
    jar2 = temp

print(jar2)