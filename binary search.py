def binary_search(arr, ele):
        first = 0
        last = len(arr) - 1
        found = False
        
        while first <= last and not found:
                mid = (first + last)//2
                if arr[mid] == ele:
                        found = True
                else:
                        if ele < arr[mid]:
                                last = mid - 1
                        else:
                                first = mid + 1
        return found
        
        
arr = [1,2,3,4,5,6,7,8,9,10,11]
print(binary_search(arr, 4))
print(binary_search(arr, 13))

def recursive_binary_search(arr, ele):
        if len(arr) == 0:
                return False
        else:
                mid = len(arr)//2
                
                if arr[mid] == ele:
                        return True
                else:
                        if ele < arr[mid]:
                                return recursive_binary_search(arr[:mid], ele)
                        else:
                                return recursive_binary_search(arr[mid+1:], ele)
                        
print(recursive_binary_search(arr, 13))
print(recursive_binary_search(arr, 5))