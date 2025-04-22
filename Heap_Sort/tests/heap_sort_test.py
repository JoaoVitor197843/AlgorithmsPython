import random, pytest
from src.heap_sort import heap_sort
from src.make_binary_heap import list_verification
class lists:
    list100k = random.sample(range(1000000), 100000)
    list200k = random.sample(range(1000000), 200000)
    list300k = random.sample(range(1000000), 300000)
    list_ordened = list(range(100000))
    list_repeated = list(1 for i in range(100000))
def hundred_thousand_elements(benchmark):
    benchmark(lambda: heap_sort(lists.list100k))
    assert lists.list100k == sorted(lists.list100k)
def two_hundred_thousand_elements(benchmark):
    benchmark(lambda: heap_sort(lists.list200k))
    assert lists.list200k == sorted(lists.list200k)
def three_hundred_thousand_elements(benchmark):
    benchmark(lambda: heap_sort(lists.list300k))
    assert lists.list300k == sorted(lists.list300k)
def ordened_elements(benchmark):
    benchmark(lambda: heap_sort(lists.list_ordened))
    assert lists.list_ordened == list(range(100000))
def repeated_elements(benchmark):
    benchmark(lambda: heap_sort(lists.list_repeated))
    assert lists.list_repeated == list(1 for i in range(100000))
def one_item_list():
    list_one_element = [1]
    with pytest.raises(IndexError):
        list_verification(list_one_element)
def two_itens_list():
    list_two_elements = [9,2]
    heap_sort(list_two_elements)
    assert list_two_elements == [2,9]
def list_with_string():
    list_with_strings = [4, 5, 6, 7, "a", "b", "c", 1, 2, 3]
    with pytest.raises(ValueError):
        list_verification(list_with_strings)
def string_test():
    non_list = "a"
    with pytest.raises(TypeError):
        list_verification(non_list)