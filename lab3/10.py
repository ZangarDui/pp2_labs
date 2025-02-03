def kait_func(san):
    b=[]
    for i in san:
        if i is not b:
            b.append(i)
    return b

print(kait_func([1, 2, 2, 3, 4, 4, 5]))  
print(kait_func([7, 7, 8, 9, 9, 10])) 