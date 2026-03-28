import random, pytest
from heap_sort.src.heap_sort import heap_sort
from heap_sort.src.list_verification import list_verification
class TestLists:
    list100k = random.sample(range(1000000), 100000)
    list200k = random.sample(range(1000000), 200000)
    list300k = random.sample(range(1000000), 300000)
    list_ordened = list(range(100000))
    list_repeated = list(1 for i in range(100000))
def test_hundred_thousand_elements(benchmark):
    benchmark(lambda: heap_sort(TestLists.list100k))
    assert TestLists.list100k == sorted(TestLists.list100k)
def test_two_hundred_thousand_elements(benchmark):
    benchmark(lambda: heap_sort(TestLists.list200k))
    assert TestLists.list200k == sorted(TestLists.list200k)
def test_three_hundred_thousand_elements(benchmark):
    benchmark(lambda: heap_sort(TestLists.list300k))
    assert TestLists.list300k == sorted(TestLists.list300k)
def test_ordened_elements(benchmark):
    benchmark(lambda: heap_sort(TestLists.list_ordened))
    assert TestLists.list_ordened == list(range(100000))
def test_repeated_elements(benchmark):
    benchmark(lambda: heap_sort(TestLists.list_repeated))
    assert TestLists.list_repeated == list(1 for i in range(100000))
def test_one_item_list():
    list_one_element = [1]
    with pytest.raises(IndexError):
        list_verification(list_one_element)
def test_two_itens_list():
    list_two_elements = [9,2]
    heap_sort(list_two_elements)
    assert list_two_elements == [2,9]
def test_list_with_string():
    list_with_strings = [4, 5, 6, 7, "a", "b", "c", 1, 2, 3]
    with pytest.raises(ValueError):
        list_verification(list_with_strings)
def test_string():
    non_list = "a"
    with pytest.raises(TypeError):
        list_verification(non_list)