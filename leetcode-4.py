# Given two strings s and t , write a function to determine if t is an anagram of s.

# Example 1:

# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:

# Input: s = "rat", t = "car"
# Output: false
# Note:
# You may assume the string contains only lowercase alphabets.

def makeHistogram(word):
    histogram = {}
    for char in word:
        histogram[char] = histogram.get(char, 0) + 1
    return histogram
# print(makeHistogram('anagram'))
# print(makeHistogram('nagaram'))
# if makeHistogram('anagram') == makeHistogram('nagaram'):
#     print(True)
# # print(False)
def compareHistograms(word, word2):
    histogram = {}
    for char in word:
        histogram[char] = histogram.get(char, 0) + 1
    for char in word2:
        histogram[char] = histogram.get(char, 0) - 1
        if histogram[char] == 0:
            del histogram[char]
    return True if histogram == {} else False

print(compareHistograms('anagram', 'nagaram'))

# Time complexity: O(n + m)
# Space complexity O(n + m)