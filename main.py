# initializing dictionary
colors = {
    "Green": 10,
    "Yellow": 5,
    "Pink": 5,
    "Brown": 6,
    "Blue": 30,
    "Orange": 9,
    "Red": 9,
    "Cream": 2,
    "White": 16,
    "Ash": 1,
    "Black": 1
}

# Question 1
res = 0
for val in colors.values():
    res += val

mean = res / len(colors)
approx_mean = round(mean)
shirt_color = [k for k, v in colors.items() if v == approx_mean]
print("The color of shirt with the mean color are " + str(shirt_color))

# Question 2
mode = max(colors, key=colors.get)
print(mode)

# Question 3
median = res/2
print(median)

# Question 4
x = 0
for val in colors.values():
    x += (val**2)
    y = mean**2
    z = len(colors) - 1
    
variance = (x - y) / z
print("The variance of the colors is " + str(variance))

# Question 5
find_key = "Red"
red = list(colors.keys()).index(find_key)
probability = red / res
print("The probability that the color chosen at random is red is " + str(probability))

# Question 9
First = 0
Second = 1
Sum = 0

for num in range(0, 50):
    Sum = Sum + First
    Next = First + Second
    First = Second
    Second = Next

print("The Sum of the first 50 Fibonacci Series Numbers = " + str(Sum))