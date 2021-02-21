search(Array, Element) {
  /* Binary Search Algorithm implemented in Dart */
  num mid;
  num low = 0;
  num high = Array.length - 1;
  while (low <= high) {
    mid = ((low + high) / 2).floor();
    if (Array[mid] == Element) {
      return mid;
    } else if (Array[mid] < Element) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
    ;
  }
  ;
  return -1;
}

main() {
  //
}
