from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        return Counter(s) == Counter(t)


def run_test_cases():
    sol = Solution()
    test_cases = [
        ("anagram", "nagaram", True),  # Basic anagram
        ("rat", "car", False),  # Not an anagram
        ("listen", "silent", True),  # Anagram with same length
        ("a", "a", True),  # Single character match
        ("", "", True),  # Empty strings
        ("abc", "cba", True),  # Reversed string
        ("abc", "ab", False),  # Different lengths
        ("aabbcc", "abcabc", True),  # Repeated characters
        ("aabbcc", "aabbc", False),  # Missing one character
        ("123", "321", True),  # Numeric characters
        ("abc!", "!abc", True),  # Special characters
        ("abc", "def", False),  # Completely different strings
        ("a"*1000, "a"*1000, True),  # Large identical strings
        ("a"*1000, "b"*1000, False),  # Large different strings
        ("abcd", "dcba", True),  # Anagram with all unique characters
        ("abcd", "abcc", False),  # Same length but different characters
        ("a b c", "c b a", True),  # Anagram with spaces
        ("a b c", "abc", False),  # Spaces matter
        ("aabbcc", "ccbbaa", True),  # Reordered repeated characters
        ("aabbcc", "ccbba", False),  # Missing one character
    ]
    print(f"{'Case':<5} {'s':<12} {'t':<12} {'Expected':<10} {'Got':<10} {'Result'}")
    print("-" * 60)
    for i, (s, t, expected) in enumerate(test_cases):
        try:
            result = sol.isAnagram(s, t)
            status = "PASS" if result == expected else "FAIL"
            color = "\033[92m" if status == "PASS" else "\033[91m"
            reset = "\033[0m"
            print(f"{i+1:<5} {s:<12} {t:<12} {str(expected):<10} {str(result):<10} {color}{status}{reset}")
        except Exception as e:
            print(f"{i+1:<5} {s:<12} {t:<12} {str(expected):<10} Exception: {e} \033[91mFAIL\033[0m")


if __name__ == "__main__":
    run_test_cases()