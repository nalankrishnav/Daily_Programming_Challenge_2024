def reverseWords(s: str) -> str:
    words = s.split()
    reversed_words = words[::-1]
    return ' '.join(reversed_words)

# Test cases
print(reverseWords("the sky is blue"))         # Output: "blue is sky the"
print(reverseWords("  hello world  "))         # Output: "world hello"
print(reverseWords("a good   example"))        # Output: "example good a"
print(reverseWords("    "))                    # Output: ""
print(reverseWords("word"))                    # Output: "word"
