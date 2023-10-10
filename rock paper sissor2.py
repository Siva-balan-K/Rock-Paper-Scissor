import random
print("Rock vs Paper => Paper\n")
print("Rock vs Sissor => Rock\n")
print("Paper vs Sissor => Sissor\n")
print("Rock => 1\n")
print("Paper => 2\n")
print("Sissor => 3\n")
n = int(input("Enter a number: \n"))
if n < 1 and n > 3:
    print("Invalid!")
    exit()
elif n == 1:
    print("You choosed 'Rock'!\n")
elif n == 2:
    print("You choosed 'Paper'!\n")
elif n==3:
    print("You choosed 'sissor'!\n")
if(n<=3 and n>=1):
    m = random.randint(1,3)
    if m == 1:
        print("computer choosed 'Rock'!\n")
    elif m == 2:
        print("computer choosed 'Paper'!\n")
    elif m == 3:
        print("computer choosed 'sissor!'\n")
    else:
        exit()
    if (n == m):
        print("The match was drawn!\n")
    elif n == 1 and m == 2:
        print("The computer win's the match!\n")
    elif n==2 and m==1:
        print("The user win's the match!\n")
    elif n == 3 and m == 1:
        print("The computer win's the match!\n")
    elif n==1 and m==3:
        print("The user win's the match!\n")
    elif n == 2 and m == 3:
        print("The computer win's the match!\n")
    elif n==3 and m==2:
        print("The user win's the match!\n")
else:
    print("Invalid!")
    exit()