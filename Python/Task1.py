# 11-04-2026 (Saturday)

# Q1. Check Anagrams

def is_anagrams():
    a = input("Enter first value: ")
    b = input("Enter second value: ")

    if sorted(a) == sorted(b):
        return True
    else:
        return False

print(is_anagrams())