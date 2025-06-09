from typing import List

'''

Problem Link: https://leetcode.com/problems/two-sum/

Problem 1: Two Sum

Problem Statement:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]

 

Constraints:

    2 <= nums.length <= 104
    -109 <= nums[i] <= 109
    -109 <= target <= 109
    Only one valid answer exists.

 
Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
'''


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        data = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in data:
                return [data[complement], i]
            data[num] = i


def run_test_cases():
    sol = Solution()
    test_cases = [
        # (nums, target, expected_output)
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
        ([1, 2, 3], 7, None),  # No solution
        ([0, 4, 3, 0], 0, [0, 3]),
        ([-1, -2, -3, -4, -5], -8, [2, 4]),
        ([1, 5, 1, 5], 10, [1, 3]),
        ([1], 2, None),  # Not enough elements
        ([], 0, None),   # Empty list
        # Duplicate value test cases
        ([1, 2, 3, 2], 4, [0, 2]),  # 2+2=4, first two 2's
        ([2, 2, 2, 2], 4, [0, 1]),  # all 2's, first two
        ([1, 1, 1, 2], 2, [0, 1]),  # first two 1's
        ([1, 2, 1, 2], 3, [0, 1]),  # 1+2=3, first pair
        ([1, 2, 3, 1, 2], 3, [0, 1]),  # 1+2=3, first pair
    ]
    print(f"{'Case':<5} {'Input':<25} {'Target':<8} {'Expected':<12} {'Got':<12} {'Result'}")
    print("-" * 70)
    for i, (nums, target, expected) in enumerate(test_cases):
        try:
            result = sol.twoSum(nums, target)
        except Exception:
            result = None
        status = "PASS" if result == expected else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"
        reset = "\033[0m"
        print(f"{i+1:<5} {str(nums):<25} {str(target):<8} {str(expected):<12} {str(result):<12} {color}{status}{reset}")


if __name__ == "__main__":
    run_test_cases()
