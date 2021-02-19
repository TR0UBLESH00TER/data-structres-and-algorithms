def BubbleSort(Array):

    for i in range(len(Array)): 

        for j in range(0, len(Array)-i-1): 

            if Array[j] > Array[j+1] : 
                Array[j], Array[j+1] = Array[j+1], Array[j] 
                
    return Array

print(BubbleSort([1,3,2,5,4,7,8,5,4,3,9,0]))