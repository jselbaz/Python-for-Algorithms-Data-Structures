def insertion_sort(arr):
        for i in range(1,len(arr)):
                current = arr[i]
                position = i
                
                while position > 0 and arr[position-1] > current:
                        arr[position] = arr[position-1]
                        position = position-1
                        
                arr[position] = current
        return arr
        
arr = [4,6,2,7,4,1,9,11,23,13,2]
print(insertion_sort(arr))