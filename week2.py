# ============================================================
# Week 2 - Python Basics
# All Practice Tasks + Weekly Challenges
# ============================================================


# ============================================================
# 2.1 Variables and Data Types
# ============================================================

print("--- 2.1 Variables and Data Types ---")

x = 10
print(x)

y = 3.14
print(type(y))

message = "Hello"
message = message + " World"
print(message)


# ============================================================
# 2.2 Basic Operators
# ============================================================

print("\n--- 2.2 Basic Operators ---")

length = 5
width = 3
area = length * width
print("Area:", area)

num = 7
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


# ============================================================
# 2.3 Input and Output
# ============================================================

# (Input tasks are shown with fixed values to run without user input)

print("\n--- 2.3 Input and Output ---")

num1 = 10
num2 = 5
print("Sum:", num1 + num2)

name = "Alice"
age = 20
print("Hello", name + "! You are", age, "years old.")

num = 5
print("Square:", num ** 2)


# ============================================================
# 3.1 Conditional Statements
# ============================================================

print("\n--- 3.1 Conditional Statements ---")

num = 7
if num > 0:
    print("Positive")
elif num == 0:
    print("Zero")
else:
    print("Negative")

num = 10
if num % 5 == 0:
    print("Divisible by 5")
else:
    print("Not divisible by 5")

a = 4
b = 9
c = 6
if a >= b and a >= c:
    print("Largest:", a)
elif b >= a and b >= c:
    print("Largest:", b)
else:
    print("Largest:", c)


# ============================================================
# 3.2 Loops
# ============================================================

print("\n--- 3.2 Loops ---")

for i in range(1, 11):
    print(i, end=" ")
print()

count = 0
num = 2
while count < 10:
    print(num, end=" ")
    num += 2
    count += 1
print()

n = 10
total = 0
for i in range(1, n + 1):
    total += i
print("Sum:", total)


# ============================================================
# 3.3 Loop Control Statements
# ============================================================

print("\n--- 3.3 Loop Control ---")

for i in range(1, 11):
    if i == 5:
        continue
    print(i, end=" ")
print()

for i in range(5):
    if i == 2:
        pass
    print(i, end=" ")
print()


# ============================================================
# Weekly Challenges
# ============================================================

print("\n--- Weekly Challenge 1: Swap, Concatenate, Sum ---")

a = 10
b = 5.5
a, b = b, a
print("Concatenated:", str(a) + str(int(b)))
print("Sum:", int(a + b))


print("\n--- Weekly Challenge 2: Word Count and Reverse ---")

sentence = "Python is fun to learn"
words = sentence.split()
print("Number of words:", len(words))
words.reverse()
print("Reversed sentence:", " ".join(words))


print("\n--- Weekly Challenge 3: Grade Classifier ---")

score = 85
if score < 0 or score > 100:
    print("Invalid Score")
elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 50:
    print("C")
elif score >= 35:
    print("D")
else:
    print("Fail")


print("\n--- Weekly Challenge 4: Prime Numbers ---")

n = 10
primes = []

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(", ".join(map(str, primes)))

total = 0
i = 0
while i < len(primes):
    total += primes[i]
    i += 1
print("Sum of primes:", total)


print("\n--- Weekly Challenge 5: First Divisible Number ---")

start = -5
end = 20
divisor = 7

found = False
for num in range(start, end + 1):
    if num < 0:
        continue
    if num % divisor == 0:
        print("First divisible number:", num)
        found = True
        break

if not found:
    pass
    print("No valid number found")