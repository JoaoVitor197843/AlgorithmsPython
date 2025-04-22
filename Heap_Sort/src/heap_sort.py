from make_binary_heap import binary_heap
class heap_sort(binary_heap):
  def __init__(self, to_sort: list[int] = []):
    """This init the code:
    items: the list
    end_index: the last item in the list
    max_heapify: view the function in make_binary_heap
    heapify_limit: the last parent node
    heapify_steps: the ready part of all list"""
    self.end_index = len(to_sort) - 1
    self._max_heapify(to_sort)
    self.last_parent_limit = self._get_last_parent_node(to_sort)
    while self.end_index > 0:
      if to_sort[0] > to_sort[self.end_index]:
        to_sort[0], to_sort[self.end_index] = to_sort[self.end_index], to_sort[0]
        self._heapify_after_sort(to_sort)
      self.end_index -= 1
  def _heapify_after_sort(self, to_sort):
    """This make a new heapify after a part of the sort
    largest: the greater number
    current item: the current node index
    left, right: left and right childs"""
    current_item = 0
    while current_item <= self.end_index - 1:
      largest = current_item
      left, right = self._get_left_child_node(largest), self._get_right_child_node(largest)
      if left >= self.end_index - 1:
        break
      if to_sort[largest] < to_sort[left]:
        largest = left      
      if right <= len(to_sort) and to_sort[largest] < to_sort[right]:
        largest = right
      if largest == current_item:
        break
      else:
        to_sort[current_item], to_sort[largest] = to_sort[largest], to_sort[current_item]
        current_item = largest