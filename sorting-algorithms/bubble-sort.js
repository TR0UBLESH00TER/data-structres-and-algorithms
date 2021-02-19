function BubbleSort(Array){
    
    for (i = 0, len = Array.length; i < len; i++){

        for (j = 0, len = Array.length; j < len; j++){

            if (Array[j] > Array[j+1]){
                let temp = Array[j];
                Array[j] = Array[j+1];
                Array[j+1] = temp;
            }; 
        };
    };
    return Array;
};

console.log(BubbleSort([1,3,2,5,4,7,8,5,4,3,9,0]));