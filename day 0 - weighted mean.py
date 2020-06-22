# Enter your code here. Read input from STDIN. Print output to STDOUT
n,s=int(input()),0
a=list(map(int,input().split()))
b=list(map(int,input().split()))
for i in range(n): s+=a[i]*b[i]
print(round(s/sum(b),1))
