# Code to demonstrate how to make a game board/map using a list of lists.
big_list = [
    ['1', '2', '3', '4', '5'], ['1', '.', '3', '4', '5'],
    ['1', '2', '3', '4', '5']
    ] 

for i in big_list:
    x = " ".join(i)
    print(x)