def SelectionSort(arr, n):
    for i in range(n):
        Min = i
        for j in range(i + 1, n):
            if (arr[j] < arr[Min]):
                Min = j
        temp = arr[i]
        arr[i] = arr[Min]
        arr[Min] = temp
    print(arr)

def BubbleSort(arr, n):
    i = 0
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if (arr[j] > arr[j + 1]):
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
    print(arr)
    print("Top Five Scores are...")
    for i in range(len(arr) - 1, 1, -1):
        print(arr[i])

print("How many students are there?")
n = int(input())
array = []
i = 0
for i in range(n):
    print("Enter percentage marks")
    item = float(input())
    array.append(item)
print("You have entered following scores...")
print(array)
while (True):
    print("Main Menu")
    print("1. Selection Sort")
    print("2. Bubble Sort")
    print("3. Exit")
    print("Enter your Choice: ")
    choice = int(input())
    if (choice == 1):
        print("The sorted Scores using Seletion Sort...")
        SelectionSort(array, n)
    elif (choice == 2):
        print("The sorted Scores using Bubble sort...")
        BubbleSort(array, n)
    else:
        print("Program is terminated :)")
        break