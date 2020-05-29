#######################################################################
#     URL to see code online with python interpreter available.       #
#           https://ide.geeksforgeeks.org/bfZ0qJeSyB                  #
#######################################################################

# code
def get_correct_output(arr):
    leng = len(arr)
    desire = []
    for i in range(leng):
        desire.append(i)
    return desire
    
def make_output(desire, arr):
    index = -1
    for i in desire:
        index += 1
        if i not in arr:
            desire[index] = -1
    return desire

if __name__ == '__main__':
    # Input(array)
    arr = [1, 2, 4534, 3, 5, 978, 7]
    # Desired Output
    # [-1, 1, 2, 3, -1, 5, -1]
    desire = get_correct_output(arr)
    result = make_output(desire, arr)
    print(result)
