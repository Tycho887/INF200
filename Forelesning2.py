import re

out = re.findall(r"\Ai", "I can see the red rose and the purple lilac")
print(out)

# \w* matches any number of word characters
# \b matches a word boundary
# \w*e\b matches any word ending with e
# re.findall returns a list of all matches
# "\w{4,}" matches any word with at least 4 characters
# "A[I-K]+" matches any word starting with A followed by at least one character in the range I-K
# \A matches the start of a string
# \Z matches the end of a string
# [I-K] matches any character in the range I-K
# [^I-K] matches any character not in the range I-K
# \A.{4,5}\b matches any word with 4 or 5 characters
# {4,5} matches the preceding pattern 4 or 5 times
# * means 0 or more times
# \A\w* matches any word at the start of a string, spaces are not word characters
