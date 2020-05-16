############################################################################
#                 ide.geeksforgeeks.org/va9sa7ARh6#                        #
############################################################################

###################################################################
#            Above is the URL to see the code online.             #
###################################################################

# Code

arr = [2, 3, 7, 11]
fib = []

def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def check_fibonacci2(n):
    for i in range(n+1):
        if fibonacci(i) == n:
            fib.append(i)
            break
        
def check_fibonacci(n):
    for i in range(n+1):
        if fibonacci(i) == n:
            return True
            

for i in arr:
    check_fibonacci2(i)

add = 0
for i in fib:
    add += i
    
if check_fibonacci(add):
    print('True')
else:
    print('False')


#print(check_fibonacci(2))

#print(fibonacci(4))
