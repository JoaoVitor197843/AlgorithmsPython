from make_binary_heap import binary_heap
import random, time
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
    print(self.items)
    self.last_parent_limit = self._get_last_parent_node()
    while self.end_index > 0:
      if self.items[0] > self.items[self.end_index]:
        self.items[0], self.items[self.end_index] = self.items[self.end_index], self.items[0]
        self._heapify_after_sort()
      self.end_index -= 1
  def __str__(self):
    """This only return the list, str can only return a string"""
    return str(self.items)
  def _heapify_after_sort(self):
    """This make a new heapify after a part of the sort
    largest: the greater number
    current item: the current node index
    left, right: left and right childs"""
    largest = 0
    current_item = 0
    while largest <= self.end_index - 1:
      left, right = self._get_left_child_node(largest), self._get_right_child_node(largest)
      if left >= self.end_index - 1:
        break
      if self.items[largest] < self.items[left]:
        largest = left      
      if right != -1 and self.items[largest] < self.items[right]:
        largest = right
      if self.items[largest] != self.items[current_item]:
        self.items[current_item], self.items[largest] = self.items[largest], self.items[current_item]
        current_item = largest
      else:
        break
lista = random.sample(range(1000000),200000)
init_time = time.perf_counter()
ordened_list = heap_sort(lista)
end_time = time.perf_counter()
print(ordened_list,ordened_list.items==sorted(lista), end_time-init_time)