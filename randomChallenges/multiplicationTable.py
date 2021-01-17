#Write a program that prints a multiplication table for numbers up to 12.
print("What multiplication table do you want? Write a number.")
n = int(input())
def multiplyPrint(n):
    highest = n*12
    i = 1
    while i <= highest:
        print (n * i)
        i += 1
multiplyPrint(n)
