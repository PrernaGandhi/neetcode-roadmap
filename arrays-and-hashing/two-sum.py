from typing import List


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
