# Q4. {Extension: Filename1, Filename2, Filename3, ...}

def func():
    dataset = ['amazon.in','gmail.com','python.py','flipkart.com']
    d = {}

    for data in dataset:
        l = data.split('.')
        if l[1] in d:
            d[l[1]].append(l[0])
        else:
            d[l[1]] = [l[0]]
    return d

print(func())