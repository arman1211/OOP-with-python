nums = input()
nums2 = nums[::-1]
# for ch in nums:
#     print(ch)
#     nums2.append(ch)
# nums3 = nums2[::-1]
print(nums2,nums)
i=0
if nums2 == nums:
    print(nums)
    print("YES")
else:
    
            
    tmp = nums2.lstrip('0') 
    print(tmp)
    print("NO")

# print(nums)