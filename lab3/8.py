def sss(nums):
    code= [0 , 0, 7]

    for i in nums:
        if i == code[0]:
            code.pop(0)
        if not code:
            return True

    return False
    
print(sss([1, 2, 4, 0, 0, 7, 5]))   
print(sss([1, 0, 2, 4, 0, 5, 7])) 
print(sss([1, 7, 2, 0, 4, 5, 0])) 