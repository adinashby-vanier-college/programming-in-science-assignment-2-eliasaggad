import math 

# Function 1: Lists - Finding the Maximum and Second Maximum in a List
# This function takes a list of numbers as input and returns the maximum and second maximum values.
def max_two_in_list(numbers):

    reverselist = sorted(numbers, reverse = True)

    if len(reverselist) == 1:

      max1 = reverselist[0]

      max2 = None

    elif len(reverselist) == 0:

        max1 = None

        max2 = None
    

    else:

        max1 = reverselist[0]

        max2 = None

        for i in reverselist:
            if i != max1:
                max2 = i
                
                break


    
    return (max1, max2) #REVIEW

print(max_two_in_list([1, 2, 3, 4, 5]))


# Function 2: Lists - Removing Duplicates and Sorting
# This function takes a list of numbers and returns a sorted list with duplicates removed.
def remove_duplicates_and_sort(numbers):

    Truelist = list(set(numbers))

    Truelist = sorted(Truelist)
    
    return Truelist


# Function 3: Single-Dimensional Arrays - Cumulative Sum
# This function takes an array (list) of numbers and returns a new list where each element is the cumulative sum of the previous elements.
def cumulative_sum(arr):

    result = []

    runningtotal = 0

    for i in arr:

        runningtotal += i

        result.append(runningtotal)
    
    return result 

# Function 4: Two-Dimensional Arrays - Matrix Transpose
# This function takes a 2D list (matrix) and returns its transpose.
def transpose_matrix(matrix):

   result = []
   rows = len(matrix)
   columns = len(matrix[0])

   for i in range(columns):      # loop through columns
        new_row = []
        for p in range(rows):     # loop through rows
            new_row.append(matrix[p][i])
        result.append(new_row)

   return result


    
# Function 5: Slicing - Extracting Every Nth Element
# This function takes a list and a step value N and returns every Nth element.
def slice_every_nth(lst, step):

    return lst[0::step]



# Function 6: Arithmetic Operations with Arrays - Dot Product
# This function takes two lists of the same length and returns their dot product.
def dot_product(list1, list2):

    

    result = 0
    for i in range(len(list1)):

        result += list1[i] * list2[i]
       
    return result

# Function 7: Arithmetic Operations with Arrays - Matrix Multiplication
# This function takes two 2D lists (matrices) and returns their matrix product.
def matrix_multiplication(matrix1, matrix2):

    # matrix1 is a × b
    # matrix2 is b × c

    a = len(matrix1)
    b = len(matrix1[0]) 
    c = len(matrix2[0])
    
    result = [[0 for _ in range(a)] for _ in range(c)]

    for i in range(a):
        
        for j in range(c):

            for k in range(b):

                result[i][j] += matrix1[i][k] * matrix2[k][j]

    return result