num sum(List<num> arr) {
  return arr.fold(0, (previous, current) => previous + current);
}

main() {
  sum([1, 5.2, 4, 0, -1]);
}
