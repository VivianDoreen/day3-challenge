"""
A function that takes a list and returns a
dictionary with keys evens, odds, and chars.
"""
def list_sort(my_list):
    "A function that returns a dictionary"
    #retrieving only strings from the list
    list_char = [each for each in my_list if isinstance(each, str)]
    char_sort = sorted(list_char)
    #retrieving only decimal numbers from the list
    list_float = [each for each in my_list if isinstance(each, float)]
    #retrieving only integers from the list
    list_integers = [each for each in my_list if isinstance(each, int)]
    list_even = [num for num in list_integers if num % 2 == 0]
    list_odd = [num for num in list_integers if num % 2 == 1]

    #storing the results in a dictionary
    dict_result = {}
    dict_result["evens"] = list_even
    dict_result["olds"] = list_odd
    dict_result["char"] = char_sort
    dict_result["floats"] = list_float

    print(dict_result)
mylist = [2, 0, 6, 5, 1, 7, 0.1, 2.5, 'z', 'a']
list_sort(mylist)
