"""
#1
Google
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
"""

def bruteforce(numbers, neededSum):
    l = len(numbers)
    for i in range(l-1):
        for j in range(i+1, l):
            if numbers[j] + numbers[i] == neededSum:
                return True, [numbers[j], numbers[i]]
    return False

def check_sum_pair(numbers, neededSum):
    knownNumbers = set()
    for number in numbers:
        diff = neededSum - number
        if diff in knownNumbers:
            return True, [diff, number]
        else:
            knownNumbers.add(number)
    return False

def main():
    numbers = [10, 15, 3, 7, 18, 10, 15, 10, 15, 3, 7, 18, 10, 15, 10, 15, 3, 7, 18, 10, 15, 10, 15, 3, 7, 18, 10, 15, 10, 15, 3, 7, 18, 10, 15]
    print(bruteforce(numbers, 30)) # big O of n^2
    print(check_sum_pair(numbers, 21)) # big O of n

if __name__ == '__main__':
    main()