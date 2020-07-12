import 'dart:math';

int squareSum(List numbers) {
  var lst = [for(var i in numbers) pow(i,2)];
  return lst.fold(0, (a,b) => a+b);
}

void main() {
  squareSum([1, 2, 2]);
}
