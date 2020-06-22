import math

mu, sig = [float(num) for num in input().split(" ")]
Cutoff1 = float(input())
Cutoff2 = float(input())

def phi(x, mu, sig):
    return (1.0 + math.erf((x - mu) / (sig * math.sqrt(2.0)))) / 2.0

# Question 1
print(round(100 - (phi(Cutoff1, mu, sig) * 100), 2))

# Question 2
print(round(100 - (phi(Cutoff2, mu, sig) * 100), 2))

# Question 3
print(round(phi(Cutoff2, mu, sig) * 100, 2))