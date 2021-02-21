// Linear Search - Sorted Array

search(Array, Element) {
  /* Linear Search Algorithm implemented in Dart */
  for (num i = 0; i < Array.length; i++) {
    if (Element == Array[i]) {
      return i;
    }
    ;
  }
  ;
  return -1;
}

main() {
  //
}
