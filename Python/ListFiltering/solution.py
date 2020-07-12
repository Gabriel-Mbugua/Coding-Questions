def filter_list(l):
    return [i for i in l if type(i) == int]

filter_list([1,'a','b',0,15]) == [1,2]
