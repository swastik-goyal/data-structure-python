###########################################################################################################################################################
##                                                 https://ide.geeksforgeeks.org/5q9mcjnpeQ                                                              ##
###########################################################################################################################################################
##############################################################
### Above is the URL to see the code online on web browser ###
#############################################################

def rotate(arr, d, n):
    for i in range(d):
        arr.append(arr[0])
        arr.pop(0)
    return arr

test = int(input("Please entrer the number of test cases : "))
for i in range(test):
    num = str(input("Please enter the length and no. of rotations : seprating by a space : "))
    num = num.split(' ', 1)
    #
    #print(type(num))
    n = int(num[0])
    d = int(num[1])
    arr = str(input("Please enter the array with each element seprated by a space : "))
    arr = arr.split(' ')
    arr = rotate(arr, d, n)
    for i in range(len(arr)):
        print(int(arr[i]), end=' ')
    print()
