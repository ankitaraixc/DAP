import string

def is_pangram(s):
    s = s.lower()
    return set(string.ascii_lowercase).issubset(set(s))

text = input("Enter a string: ")
if is_pangram(text):
    print("It's a pangram.")
else:
    print("It's not a pangram.")
