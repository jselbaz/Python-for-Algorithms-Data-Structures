def merge_sort(arr):
        if len(arr) > 1:
                mid = len(arr)//2
                leftHalf = arr[:mid]
                rightHalf = arr[mid:]
                merge_sort(leftHalf)
                merge_sort(rightHalf)
                
                i,j,k = 0, 0, 0 
                
                while i < len(leftHalf) and j < len(rightHalf):
                        if leftHalf[i] < rightHalf[j]:
                                arr[k] = leftHalf[i]
                                i += 1
                        else:
                                arr[k] = rightHalf[j]
                                j += 1
                        k += 1
                        
                while i < len(leftHalf):
                        arr[k] = leftHalf[i]
                        i += 1
                        k += 1
                        
                while j < len(rightHalf):
                        arr[k] = rightHalf[j]
                        j += 1
                        k += 1
        return arr
        
arr = [11,2,5,4,7,56,2,12,23]
print(merge_sort(arr))