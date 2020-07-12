def high_and_low(numbers):
    new_nums = numbers.split(" ")
    lst = [int(i) for i in new_nums]
    numbers = [max(lst), min(lst)]
    print(' '.join(str(i) for i in numbers))
    return numbers

high_and_low("1460 269 1333 955 1014 1158 1802 2940 972 2223 2057 2665 2295 560 1052 2937 1642 2729 2456 2322 3347 749")