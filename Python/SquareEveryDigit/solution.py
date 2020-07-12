def square_digits(num):
    lst = [str(int(n)**2) for n in str(num)]
    new_num = "".join(lst)
    print(int(new_num))

square_digits(9119)