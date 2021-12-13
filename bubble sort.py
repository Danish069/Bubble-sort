length = int(input("Enter the length of array: "))
array =[]
for i in range(length):
    x = input("Enter the number: ")
    array.append(x)
for i in range(length):
    for j in range(length - i - 1):
        if array[j] > array[j+1]:
            swap = array[j]
            array[j] = array[j+1]
            array[j+1] = swap
print(array)            


