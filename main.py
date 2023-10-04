from typing import List

def twoSum(nums, target):
  number_list = nums
  length = len(nums) 
  for i in range(0, length):
    for j in range(i+1, length):
      if number_list[i]+number_list[j]== target:
        return_list = [i,j]

  return return_list

nums = [2,7,11,15]
target = 9
return_list = twoSum(nums, target)
print("Output: [%d, %d]" %(return_list[0], return_list[1]))
print("Explanation: Because nums[%d] +nums[%d] == 9, we return [%d, %d]" %(return_list[0], return_list[1], return_list[0], return_list[1]))

nums = [3,2,4]
target = 6
return_list = twoSum(nums, target)
print("Output: [%d, %d]" %(return_list[0], return_list[1]))
print("Explanation: Because nums[%d] +nums[%d] == 9, we return [%d, %d]" %(return_list[0], return_list[1],return_list[0], return_list[1]))

nums = [3,3]
target = 6
return_list = twoSum(nums, target)
print("Output: [%d, %d]" %(return_list[0], return_list[1]))
print("Explanation: Because nums[%d] +nums[%d] == 9, we return [%d, %d]" %(return_list[0], return_list[1], return_list[0], return_list[1])) 