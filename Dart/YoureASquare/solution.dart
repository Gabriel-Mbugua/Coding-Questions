import 'dart:math';

isSquare(n) {
  var l = sqrt(n)%1 ==0 ? true : false;
  return sqrt(n) is int ? true : false;
}

main() {
  isSquare(121);
}
