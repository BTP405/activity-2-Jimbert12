def isPrime(n):
    if n < 2: # checks if anything is below 2
         return False
    if n % 2 == 0: # checks if the number is even
         return False
    for i in range(3, int(n**0.5)+1): # I set the endpoint to be square root of the n in order to check divisibility by numbers up to the square root of n
        if n%i==0:
            return False    
    return True

def getPrimeNumbers(num):
    return [i for i in range(2, num+1) if isPrime(i)] # returning a comprehension list of only prime numbers

print(getPrimeNumbers(20))