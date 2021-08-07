num = int(input("enter number:"))
i=1
prime = 0
if i < num:
    for x in range(num):
        for n in range(1, x):
            if n != 1 and n != x:
                if x % n == 0:
                    result = " not a prime"
                    prime = 0
                    break
                else:
                    result = " prime number"
                    prime = x
        if prime != 0:
            print(prime)