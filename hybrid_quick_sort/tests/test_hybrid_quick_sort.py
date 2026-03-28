import random, pytest
from hybrid_quick_sort.src.hybrid_quick_sort import quick_sort
class TestLists:
    list100k = random.sample(range(1000000), 100000)
    list200k = random.sample(range(1000000), 200000)
    list300k = random.sample(range(1000000), 300000)
    list_ordened = list(range(100000))
def test_hundred_thousand_elements(benchmark):
    benchmark(lambda: quick_sort(TestLists.list100k))
    assert TestLists.list100k == sorted(TestLists.list100k)
def test_two_hundred_thousand_elements(benchmark):
    benchmark(lambda: quick_sort(TestLists.list200k))
    assert TestLists.list200k == sorted(TestLists.list200k)
def test_three_hundred_thousand_elements(benchmark):
    benchmark(lambda: quick_sort(TestLists.list300k))
    assert TestLists.list300k == sorted(TestLists.list300k)
def test_ordened_elements(benchmark):
    benchmark(lambda: quick_sort(TestLists.list_ordened))
    assert TestLists.list_ordened == list(range(100000))