from typing import List


def find_max_in_each_list(nested_arr: List[List[int]]) -> List[int]:
    newMax = []
    #create empty array

    for lists in nested_arr:
        # loop through the arrays in the arrrays
        maxs = 0
        #create max variable in first loop
        for ints in lists:
            #loop through the ints in each array
            
            current = ints#check current and update 
            if current > maxs:
                maxs = current
                #at the end of the loop append the max
        newMax.append(maxs)
        # return the list of maxs
    return newMax


# do not modify below this line
print(find_max_in_each_list([[1, 2], [3, 4, 2]]))
print(find_max_in_each_list([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
print(find_max_in_each_list([[5, 6, 2, 8], [9], [9, 10], [11, 10, 11]]))
