def twoSum(nums, target):
    hashmap ={}
    for i in range(len(nums)):
        j = target - nums[i]
        if j in hashmap:
            return [hashmap[j],i]
        hashmap[nums[i]] = i
    return hashmap

nums=[1,2,3,4,5]

target = 6
a = twoSum(nums,target)
print(a)