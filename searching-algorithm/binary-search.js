// Binary Search - Sorted Array

function search(Array,Element){
    /* Binary Search Algorithm implemented in JS */
    let mid;
    let low = 0;
    let high = Array.length;
    while (low <= high) {
        mid = Math.floor((low + high)/2);
        if (Array[mid] == Element){
            return mid;
        } else if (Array[mid] < Element) {
            low = mid + 1;
        } else {
            high = mid - 1;
        };
    };
    return -1;
};