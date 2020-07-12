String noSpace(String x) {
  return x.replaceAll(RegExp(r"\s"), "");
}

main() {
  noSpace("'Testing for B'8 j 8   mBliB8g  imjB8B8  jl  '");
}
