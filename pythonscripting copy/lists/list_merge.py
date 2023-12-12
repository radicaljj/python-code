
def merge_arrays(arrayA, arrayB):
    return sorted(set(arrayA + arrayB))
    


list_1 = [1,2,3,4,5,6]
list_2 = [4,5,6,7,8,9]

list_3 = merge_arrays(list_1, list_2)

print(list_3)