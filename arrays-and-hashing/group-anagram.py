from typing import List
from collections import defaultdict

'''

Problem Link: https://leetcode.com/problems/group-anagrams/

Problem 49: Group Anagrams

Problem Statement:
Given an array of strings strs, group the anagrams

together. You can return the answer in any order.



Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]

Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:

    There is no string in strs that can be rearranged to form "bat".
    The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
    The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:

Input: strs = [""]

Output: [[""]]

Example 3:

Input: strs = ["a"]

Output: [["a"]]



Constraints:

    1 <= strs.length <= 104
    0 <= strs[i].length <= 100
    strs[i] consists of lowercase English letters.


'''


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1

            res[tuple(count)].append(s)

        #print(res)

        return list(res.values())


def run_test_cases():
    sol = Solution()
    test_cases = [
        (["eat", "tea", "tan", "ate", "nat", "bat"], [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]),
        ([""], [[""]]),
        (["a"], [["a"]]),
        (["abc", "bca", "cab", "xyz", "zyx", "yxz"], [["abc", "bca", "cab"], ["xyz", "zyx", "yxz"]]),
        (["abc", "def", "ghi"], [["abc"], ["def"], ["ghi"]]),
        ([], []),
    ]
    print(f"{'Case':<5}\t\t{'Input':<55}\t\t{'Expected':<55}\t\t{'Got':<55}\t\t{'Result'}")
    print("-" * 260)
    for i, (input_strs, expected) in enumerate(test_cases):
        result = sol.groupAnagrams(input_strs)
        # Sort inner lists and outer list for comparison (order doesn't matter)
        result_sorted = sorted([sorted(group) for group in result])
        expected_sorted = sorted([sorted(group) for group in expected])
        status = "PASS" if result_sorted == expected_sorted else "FAIL"
        color = "\033[92m" if status == "PASS" else "\033[91m"
        reset = "\033[0m"
        print(f"{i+1:<5}\t\t{str(input_strs):<55}\t\t{str(expected):<55}\t\t{str(result):<55}\t\t{color}{status}{reset}")


if __name__ == "__main__":
    run_test_cases()
