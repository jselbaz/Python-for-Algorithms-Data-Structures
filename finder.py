'''
def finder(arr1, arr2):
    seen = []
    missing = []
    for num in arr1:
        if num in arr2:
                seen.append(num)
        else:
                missing.append(num)
    return(str(missing).strip('[]') + " is the missing number")

print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))
'''
def finder(arr1, arr2):

        arr1.sort()
        arr2.sort()
        
        for num1, num2 in zip(arr1, arr2):
                if num1!= num2:
                        return num1
        return arr1[-1]
        
print(finder([1,2,3,4,5,6,7],[3,7,2,1,4,6]))