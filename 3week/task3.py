"""
https://leetcode.com/problems/maximum-product-subarray/description/
?envType=problem-list-v2&envId=array
"""


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        max_product: int = max(nums)
        product: int = 1
        for i in range(len(nums)):
            product *= nums[i]
            max_product = max(product, max_product)
            if product == 0:
                product = 1
        product = 1
        for i in range(len(nums) - 1, -1, -1):
            product *= nums[i]
            max_product = max(product, max_product)
            if product == 0:
                product = 1
        return max_product
