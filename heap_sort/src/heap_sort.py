from .make_binary_heap import binary_heap
class heap_sort(binary_heap):
  def __init__(self, to_sort: list[int] = []) -> None:
    """This init the code:
    to_sort: the list
    heap_size: the size of the atual heap
    max_heapify: view the function in make_binary_heap
    heapify_down: view the function in make_binary_heap
    last_parent_limit: the last parent node"""
    
    self.heap_size = len(to_sort) - 1
    self._max_heapify(to_sort, self.heap_size)
    self.last_parent_limit = self._get_last_parent_node(to_sort)

    while self.heap_size > 0:
      to_sort[0], to_sort[self.heap_size] = to_sort[self.heap_size], to_sort[0]
      self.heap_size -= 1
      self._heapify_down(0, to_sort, heap_size=self.heap_size)