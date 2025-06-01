from typing import List


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