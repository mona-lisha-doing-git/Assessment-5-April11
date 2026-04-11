# Q3. Frequency dictionary

def dictionary():
    s = input("Enter: ")
    d = {}
    for i in s:
        if i == ' ':
            continue
        if i in d:
            d[i] += 1
        else:
            d[i] = 1

    return d

print(dictionary())