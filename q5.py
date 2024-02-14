#Approach 3
def doubleG(n):
        for i in range(n):
            yield i * 2

for i in doubleG(5):
        print(i, end=' : ')