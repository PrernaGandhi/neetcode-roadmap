from typing import List

'''

Problem Link: https://leetcode.com/problems/contains-duplicate/

LeetCode Problem 217: Contains Duplicate

Problem Statement:
Given an integer array nums, return true if any value appears at least twice in the array, 
and return false if every element is distinct.


Example 1:

Input: nums = [1,2,3,1]

Output: true

Explanation:

The element 1 occurs at the indices 0 and 3.

Example 2:

Input: nums = [1,2,3,4]

Output: false

Explanation:

All elements are distinct.

Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]

Output: true


Constraints:

    1 <= nums.length <= 105
    -109 <= nums[i] <= 109


'''


class Solution:

    def containsDuplicate(self, nums: List[int]) -> bool:
        dup = set()
        for n in nums:
            if n in dup:
                return True
            dup.add(n)
        return False


def run_test_cases():
    sol = Solution()
    test_cases = [
        ([1, 2, 3, 1], True),
        ([1, 2, 3, 4], False),
        (["a", "b", "a"], True),
        (["a", "b", "c"], False),
        ([1.1, 2.2, 1.1], True),
        ([1.1, 2.2, 3.3], False),
        ([1, "a", 1], True),
        ([1, "a", "b"], False),
        ([], False),
        ([None, None], True),
        ([None, 1, "a"], False)
    ]
    print(f"{'Case':<5} {'Input':<25} {'Expected':<10} {'Got':<10} {'Result'}")
    print("-" * 60)
    for i, (nums, expected) in enumerate(test_cases):
        result = sol.containsDuplicate(nums)
        status = "PASS" if result == expected else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"
        reset = "\033[0m"
        #input_str = pprint.pformat(nums, compact=True)
        print(f"{i+1:<5} {str(nums):<25} {str(expected):<10} {str(result):<10} {color}{status}{reset}")


if __name__ == "__main__":
    run_test_cases()