# URL to see code on browser : 
##########################################################################################################################
#                                      https://ide.geeksforgeeks.org/vdaQiRFGwT                                          #
##########################################################################################################################

test = int(input("Please enter the number of test cases  :  "))

for i in range(test):
    leng = int(input("Please enter the length of the array : "))
    arr = []
    failiure = True
    for i in range(leng-1):
        arr.append(int(input("Please enter the element : ")))
    # print(arr)
    count = 1
    for l in arr:
        if l != count:
            print("Element found at : ", l)
            failiure = False
            break
        count += 1
    if failiure == True:
        print("Element found at : "leng)
