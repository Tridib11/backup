def prime_checker(number):
    isprime=True
    for i in range(2,number):
        if number %i==0:
            isprime=False
    if isprime:
        print("Prime")
    else:
        print("Not a prime number")

prime_checker(52)