def open_or_senior(data):
    lst = ['Senior' if item[0] >= 55 and item[1] > 7 else 'Open' for item in data]
    print(lst)
    return lst

# open_or_senior([[18, 20],[45, 2],[61, 12],[37, 6],[21, 21],[78, 9]])
# open_or_senior([(16, 23),(73,1),(56, 20),(1, -1)])
open_or_senior([(45, 12),(55,21),(19, -2),(104, 20)])