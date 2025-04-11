from make_binary_heap import binary_heap
class heap_sort(binary_heap):
  def __init__(self, to_sort: list[int] = []):
    """This init the code:
    items: the list
    end_index: the last item in the list
    max_heapify: view the function in make_binary_heap
    heapify_limit: the last parent node
    heapify_steps: the ready part of all list"""
    self.items = to_sort
    self.end_index = len(self.items) - 1
    self._max_heapify()
    self.heapify_limit = self._get_last_parent_node()
    self.heapify_steps = 1
    while self.end_index > 0:
      self.items[0], self.items[self.end_index] = self.items[self.end_index], self.items[0]
      self._heapify_after_sort()
      self.end_index -= 1
  def __str__(self):
    """This only return the list, str can only return a string"""
    return str(self.items)
  def _heapify_after_sort(self):
    """this make a new heapify after a part of the sort
    current index: the greater number
    node: the current node"""
    for node in range(self.heapify_limit):
      current_index = node
      left_child, right_child = self._get_left_child_node(node), self._get_right_child_node(node)
      if self.items[current_index] < self.items[left_child] and self.end_index > left_child:
        current_index = left_child
      if self.items[current_index] < self.items[right_child] and self.end_index > right_child:
        current_index = right_child
      if self.items[current_index] != self.items[node]:
        self.items[node], self.items[current_index] = self.items[current_index], self.items[node]
    self.heapify_steps += 1
    if self.heapify_steps % 2 == 0:
      self.heapify_limit -= 1