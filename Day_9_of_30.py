def longestCommonPrefix(strs):
    if not strs:
        return ""
    
    # Take the first string as the base
    prefix = strs[0]
    
    # Compare the prefix with each string in the list
    for s in strs[1:]:
        # Update the prefix to be the common prefix between prefix and s
        while not s.startswith(prefix):
            # Reduce the prefix by removing one character from the end
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Test cases
print(longestCommonPrefix(["flower", "flow", "flight"])) # Output: "fl"
print(longestCommonPrefix(["dog", "racecar", "car"]))    # Output: ""
print(longestCommonPrefix(["apple", "ape", "april"]))    # Output: "ap"
print(longestCommonPrefix([""]))                        # Output: ""
print(longestCommonPrefix(["alone"]))                    # Output: "alone"