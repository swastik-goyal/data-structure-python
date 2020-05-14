####################################################################################
##                       https://ide.geeksforgeeks.org/WRQaCnVRYC                 ##
####################################################################################

###################################################################################
##           Above is the ink to see the code onluine on web browser!            ##
###################################################################################


arr = [1, 2, 3 ,4 , 5, 6, 7, 8, 9, 10]

x = 78
found = False
for i in arr:
    for l in arr:
        if i + l == x:
            print("There's a pair of", l, 'and', i, 'with sum as', x)
            found = True
            break
    if found == True:
        break
if found == False:
    print('There\'s no pair of numbers with sum as ', x)
