
def bubble_sort(num):
    print("Bubble sort starts")

    for i in range(len(num)):
        for j in range(len(num)-1, i, -1):
            if num[j] < num[j-1]:
                num[j], num[j-1] = num[j-1], num[j]
    return(num)

result = bubble_sort([1,4,6,2,7,4,8,2,0,9,8,5,3])
print(result)
