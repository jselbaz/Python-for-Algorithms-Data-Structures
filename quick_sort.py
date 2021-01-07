def quick_sort(arr):
        
        quick_sort_helper(arr, 0, len(arr) - 1)
        return arr
        
def quick_sort_helper(arr, first, last):
        if first < last:
                splitpoint = partition(arr, first, last)
                quick_sort_helper(arr, first, splitpoint - 1)
                quick_sort_helper(arr, splitpoint + 1, last)
        
def partition(arr, first, last):
        
        pivotvalue = arr[first]
        leftmark = first + 1
        rightmark = last
        done = False
        while not done:
                while leftmark <= rightmark and arr[leftmark] <= pivotvalue:
                        leftmark += 1
                while arr[rightmark] >= pivotvalue and rightmark >= leftmark:
                        rightmark -= 1
                if rightmark < leftmark:
                        done = True
                else:
                        temp = arr[leftmark]
                        arr[leftmark] = arr[rightmark]
                        arr[rightmark] = temp
                        
        temp = arr[first]
        arr[first] = arr[rightmark]
        arr[rightmark] = temp
        
        return rightmark
        
arr = [2,5,4,6,7,3,1,4,12,11]
print(quick_sort(arr)) 