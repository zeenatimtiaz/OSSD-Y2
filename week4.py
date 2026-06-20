# ============================================================
# Week 4 & 5 - Data Structures in Python
# All Practice Tasks + Weekly Challenges
# ============================================================


# ============================================================
# SECTION 3.1 - LISTS PRACTICE TASKS
# ============================================================

# Task 1: Create a list of favorite movies and print first three
print("--- List Task 1 ---")
movies = ["Inception", "Interstellar", "The Dark Knight", "Avatar", "Titanic"]
print("First three movies:", movies[:3])


# Task 2: Remove all occurrences of a given number from a list
print("\n--- List Task 2 ---")
numbers = [1, 2, 3, 2, 4, 2, 5]
remove_num = 2
numbers = [x for x in numbers if x != remove_num]
print("After removing all 2s:", numbers)


# Task 3: Reverse a list without using reverse() or slicing
print("\n--- List Task 3 ---")
original = [1, 2, 3, 4, 5]
reversed_list = []
for i in range(len(original) - 1, -1, -1):
    reversed_list.append(original[i])
print("Reversed list:", reversed_list)


# ============================================================
# SECTION 3.2 - TUPLES PRACTICE TASKS
# ============================================================

# Task 1: Create a tuple with five numbers, find max and min
print("\n--- Tuple Task 1 ---")
nums_tuple = (15, 42, 7, 93, 28)
print("Tuple:", nums_tuple)
print("Max:", max(nums_tuple))
print("Min:", min(nums_tuple))


# Task 2: Convert tuple to list, modify, convert back
print("\n--- Tuple Task 2 ---")
my_tuple = (10, 20, 30, 40, 50)
my_list = list(my_tuple)
my_list[2] = 99
my_tuple = tuple(my_list)
print("Modified tuple:", my_tuple)


# Task 3: Swap two values stored in a tuple
print("\n--- Tuple Task 3 ---")
values = (5, 10)
print("Before swap:", values)
values = (values[1], values[0])
print("After swap:", values)


# ============================================================
# SECTION 3.3 - DICTIONARIES PRACTICE TASKS
# ============================================================

# Task 1: Create a dictionary to store student names and grades
print("\n--- Dictionary Task 1 ---")
grades = {
    "Ali": 85,
    "Sara": 92,
    "Hamza": 78,
    "Zara": 95,
    "Usman": 88
}
print("Student grades:", grades)


# Task 2: Find the highest-scoring student
print("\n--- Dictionary Task 2 ---")
top_student = max(grades, key=lambda name: grades[name])
print("Highest scoring student:", top_student, "with", grades[top_student], "marks")


# Task 3: Merge two dictionaries into one
print("\n--- Dictionary Task 3 ---")
dict1 = {"Alice": 90, "Bob": 75}
dict2 = {"Charlie": 88, "Diana": 95}
merged = {**dict1, **dict2}
print("Merged dictionary:", merged)


# ============================================================
# SECTION 3.4 - SETS PRACTICE TASKS
# ============================================================

# Task 1: Remove duplicates from a list using a set
print("\n--- Set Task 1 ---")
with_duplicates = [1, 2, 2, 3, 4, 4, 5, 1]
no_duplicates = list(set(with_duplicates))
print("Original:", with_duplicates)
print("Without duplicates:", no_duplicates)


# Task 2: Find common elements between two sets
print("\n--- Set Task 2 ---")
set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}
common = set_a & set_b
print("Set A:", set_a)
print("Set B:", set_b)
print("Common elements:", common)


# Task 3: Check if one set is a subset of another
print("\n--- Set Task 3 ---")
small_set = {2, 3}
big_set = {1, 2, 3, 4, 5}
print("Is", small_set, "a subset of", big_set, "?", small_set.issubset(big_set))


# ============================================================
# WEEKLY CHALLENGES
# ============================================================

# Challenge 1: Find max and min in a list
print("\n--- Challenge 1: Max and Min ---")
my_list = [34, 7, 23, 32, 5, 62]
max_val = my_list[0]
min_val = my_list[0]
for num in my_list:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num
print("List:", my_list)
print("Max:", max_val, "| Min:", min_val)


# Challenge 2: Count occurrences of a given element
print("\n--- Challenge 2: Count Occurrences ---")
items = [1, 3, 2, 3, 4, 3, 5]
target = 3
count = 0
for item in items:
    if item == target:
        count += 1
print(f"Element {target} appears {count} times")


# Challenge 3: Check if a list is sorted in ascending order
print("\n--- Challenge 3: Is List Sorted? ---")
def is_sorted(lst):
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    return True

print(is_sorted([1, 2, 3, 4, 5]))   # True
print(is_sorted([1, 3, 2, 4, 5]))   # False


# Challenge 4: Sum of all even numbers in a list
print("\n--- Challenge 4: Sum of Even Numbers ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_sum = 0
for n in numbers:
    if n % 2 == 0:
        even_sum += n
print("Sum of even numbers:", even_sum)


# Challenge 5: Return the second largest number
print("\n--- Challenge 5: Second Largest ---")
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2]

nums = [10, 20, 4, 45, 99, 99]
print("Second largest:", second_largest(nums))


# Challenge 6: Merge two sorted lists without sorted()
print("\n--- Challenge 6: Merge Two Sorted Lists ---")
def merge_sorted(a, b):
    merged = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            merged.append(a[i])
            i += 1
        else:
            merged.append(b[j])
            j += 1
    merged.extend(a[i:])
    merged.extend(b[j:])
    return merged

list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
print("Merged:", merge_sorted(list1, list2))


# Challenge 7: Rotate a list n times to the right
print("\n--- Challenge 7: Rotate List ---")
def rotate_right(lst, n):
    n = n % len(lst)
    return lst[-n:] + lst[:-n]

original = [1, 2, 3, 4, 5]
print("Rotated 2 times:", rotate_right(original, 2))


# Challenge 8: Remove duplicates without using set()
print("\n--- Challenge 8: Remove Duplicates (no set) ---")
def remove_duplicates(lst):
    seen = []
    for item in lst:
        if item not in seen:
            seen.append(item)
    return seen

dupes = [1, 2, 2, 3, 4, 4, 5]
print("Without duplicates:", remove_duplicates(dupes))


# Challenge 9: Intersection of two lists (common elements)
print("\n--- Challenge 9: List Intersection ---")
def intersection(a, b):
    return [x for x in a if x in b]

a = [1, 2, 3, 4, 5]
b = [3, 4, 5, 6, 7]
print("Common elements:", intersection(a, b))


# Challenge 10: Split a list into two halves
print("\n--- Challenge 10: Split List ---")
def split_list(lst):
    mid = len(lst) // 2
    return lst[:mid], lst[mid:]

my_list = [1, 2, 3, 4, 5, 6]
first_half, second_half = split_list(my_list)
print("First half:", first_half)
print("Second half:", second_half)


# Challenge 11: Find all pairs that sum to a given target
print("\n--- Challenge 11: Pairs with Target Sum ---")
def find_pairs(lst, target):
    pairs = []
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] + lst[j] == target:
                pairs.append((lst[i], lst[j]))
    return pairs

numbers = [1, 2, 3, 4, 5, 6]
target = 7
print("Pairs that sum to", target, ":", find_pairs(numbers, target))


# Challenge 12: Circular shift (left and right)
print("\n--- Challenge 12: Circular Shift ---")
def circular_shift(lst, n, direction="right"):
    n = n % len(lst)
    if direction == "right":
        return lst[-n:] + lst[:-n]
    else:
        return lst[n:] + lst[:n]

lst = [1, 2, 3, 4, 5]
print("Right shift by 2:", circular_shift(lst, 2, "right"))
print("Left shift by 2:", circular_shift(lst, 2, "left"))


# Challenge 13: Longest increasing subsequence
print("\n--- Challenge 13: Longest Increasing Subsequence ---")
def longest_increasing(lst):
    if not lst:
        return []
    best = []
    current = [lst[0]]
    for i in range(1, len(lst)):
        if lst[i] > lst[i - 1]:
            current.append(lst[i])
        else:
            if len(current) > len(best):
                best = current
            current = [lst[i]]
    if len(current) > len(best):
        best = current
    return best

nums = [1, 2, 3, 1, 2, 8, 9, 10, 3]
print("Longest increasing subsequence:", longest_increasing(nums))


# Challenge 14: Stack using a list (push, pop, peek)
print("\n--- Challenge 14: Stack Implementation ---")
class Stack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        self.stack.append(item)
        print("Pushed:", item)

    def pop(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        item = self.stack.pop()
        print("Popped:", item)
        return item

    def peek(self):
        if self.is_empty():
            print("Stack is empty!")
            return None
        print("Top item:", self.stack[-1])
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

s = Stack()
s.push(10)
s.push(20)
s.push(30)
s.peek()
s.pop()
s.peek()


# Challenge 15: Check if a list is a palindrome
print("\n--- Challenge 15: Palindrome Check ---")
def is_palindrome(lst):
    return lst == lst[::-1]

print(is_palindrome([1, 2, 3, 2, 1]))   # True
print(is_palindrome([1, 2, 3, 4, 5]))   # False
print(is_palindrome(["a", "b", "a"]))   # True