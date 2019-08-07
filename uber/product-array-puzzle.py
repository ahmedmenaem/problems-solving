"""
#2
Uber
Given an array of integers, return a new array such that each element at index i of the new array is the product of 
all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24].
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
"""

def bruteforce(arr):
    prod = []
    for i, outer_value in enumerate(arr):
        product = 1
        for j, inner_value in enumerate(arr):
            if i != j:
                product *= inner_value
        prod.append(product)
    return prod

def using_division(arr):
    product = 1
    for number in arr:
        product *= number
    prod = [product//x for x in arr]
    return prod

def without_division(arr):
    l = len(arr)
    left = [1 for _ in range(l)]
    right = [1 for _ in range(l)]
    prod = [1 for _ in range(l)]

    for i in range(1,l):
        left[i] = arr[i-1] * left[i-1]

    for i in range(l-2, -1, -1):
        right[i] = arr[i+1] * right[i+1]

    for i in range(l):
        prod[i] = left[i] * right[i]
    
    return prod
    


def main():
    arr = [4, 2, 8]
    bruteforce_result = bruteforce(arr) # big O of n^2
    print(bruteforce_result)
    using_division_result = using_division(arr)
    print(bruteforce_result)
    without_division_result = without_division(arr)
    print(without_division_result)


if __name__ == '__main__':
    main()