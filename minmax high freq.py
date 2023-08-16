def display(m):
    print(m)

def average(m):
    sum = 0
    absent = 0
    for i in range(0, len(m)):
        if (type(m[i]) == type(" ")):
            absent = absent + 1
    else:
        sum = sum + m[i]
    avg = sum / (len(m) - absent)
    print("Average marks are : ", avg)

def HighestAndLowestScore(m):
    high = 0
    low = 100
    for i in range(0, len(m)):
        if (type(m[i]) != type(" ")):
            if (m[i] > high):
                high = m[i]
    if ((m[i] < low) and type(m[i]) != type(" ")):
        low = m[i]
    print("\n Highest Score is: ", high)
    print("\n Lowest Score is: ", low)

def Frequency(m):
    f = [0]  # not storing the frequency at 0th location
    for j in range(1, 100):
        count = 0
    for i in range(1, len(m)):
        if (type(m[i]) != type(" ")):
            if (m[i] == j):
                count = count + 1
    f.append(count)
    print("\nThe marks in the subject 'Fundamentals of Data Structures' are...")
    print(m)
    # counting the highest frequency of the marks
    high = 0
    for cnt in f:
        if (cnt > high):
            high = cnt
    print("\n Highest Frequency is: ", high)

    # obtaining marks of highest frequency
    for k in range(1, len(f)):
        if (f[k] == high):
            highest_marks = k
    print("\n Highest Frequency Marks are: ", highest_marks)

# driver code
marks = ["NA", 59, 62, 58, 62, 93, "AB", 58, 62, "AB", 34]
print("The marks in the subject 'Fundamentals of Data Structures' are...")
display(marks)
average(marks)
HighestAndLowestScore(marks)
Frequency(marks)