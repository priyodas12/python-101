# check palindrome string: ex- madam, MadAm
# Never odd or even

import re


def is_palindrome(s1):
    # way 1
    reversed_s1 = re.sub(r"\s+", " ", s1)[::-1].lower()
    # way 2
    reversed_s2 = "".join(reversed(s1.strip().lower()))
    # way 3
    reversed_s3 = ""
    for char in s1.strip().lower():
        print(reversed_s3)
        reversed_s3 = char + reversed_s3
    print(reversed_s3)
    return s1.lower() == reversed_s3


print(is_palindrome(s1="Never odd or even"))
