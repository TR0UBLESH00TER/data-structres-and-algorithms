// Linear Search - Sorted Array

function search(Array,Element){
    /* Linear Search Algorithm implemented in JS */
    for (let i = 0; i < Array.length; i++) {
        if (Element == Array[i]){
            return i;
        };       
    };
    return -1;
};