# Q2. Take a sentence as input and return dictionary based on a condition

def string_len():
    s = input("Enter: ")
    d = {}

    l = s.split(' ')

    for i in l:
        cnt = 0
        for j in i:
            if j != 'a':
                cnt +=1
        d[i] = cnt

    return d

print(string_len())