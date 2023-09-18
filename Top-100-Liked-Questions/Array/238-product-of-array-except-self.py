""" https://leetcode.com/problems/product-of-array-except-self/
Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 

Constraints:

2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
 

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
 """

# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         res = [1] * len(nums)
#         c = 1
#         for i in range(len(nums)):
#             res[i] = c
#             c = c * nums[i]
#             res[:i] = [a * nums[i] for a in res[:i]]
#         return res
    
# class Solution(object):
#     def productExceptSelf(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[int]
#         """
#         n = len(nums)
#         left_products = [1] * n
#         right_products = [1] * n
#         results = [1] * n
        
#         left_product = 1
#         for i in range(n):
#             left_products[i] = left_product
#             left_product *= nums[i]

#         right_product = 1
#         for i in range(n-1, -1, -1):
#             right_products[i] = right_product
#             right_product *= nums[i]

#         for i in range(n):
#             results[i] = left_products[i] * right_products[i]

#         return results

# O(1) space complexity 
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        results = [1] * n
        
        left_product = 1
        for i in range(n):
            results[i] *= left_product
            left_product *= nums[i]

        right_product = 1
        for i in range(n-1, -1, -1):
            results[i] *= right_product
            right_product *= nums[i]

        return results

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4] #Output: [24,12,8,6]
    # nums = [-1,1,0,-3,3] #Output: [0,0,9,0,0]
    print(s.productExceptSelf(nums))