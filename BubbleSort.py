
def bubble_sort(num):
    print("Bubble sort starts")

    for i in range(len(num)):
        print("i = ", i)
        for j in range(len(num)-1, i, -1):
            print("j = ", j)
            print("num[j] = ", num[j])
            print("num[j-1] = ", num[j-1])

            if num[j] < num[j-1]:
                print("swap!")
                num[j], num[j-1] = num[j-1], num[j]
    return(num)

def bubble_sort_reverse(num):
    for i in range(len(num)):
        for j in range(len(num)-(i+1)):
            if num[j] > num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return(num)

def bubble_sort_dec(num):
    for i in range(len(num)):
        for j in range(len(num)-(i+1)):
            if num[j] < num[j+1]:
                num[j], num[j+1] = num[j+1], num[j]
    return(num)


num = [1,4,6,2,7,8,4,2,5,6,9,8]

result = bubble_sort(num)
print(result)

result = bubble_sort_reverse(num)
print(result)

result = bubble_sort_dec(num)
print(result)

