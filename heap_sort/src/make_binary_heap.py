class binary_heap:
    @staticmethod
    def _get_last_parent_node(to_sort: list[int]) -> int:
      """this function get's the last parent node of the binary heap.
      to_sort: the list to get the last parent node."""

      return (len(to_sort) // 2) - 1
    
    @staticmethod
    def _get_left_child_node(parent_node: int) -> int:
       """This function get the left child node of the binary heap.
       parent node: the index of the parent node."""

       return (parent_node * 2) + 1
    
    @staticmethod
    def _get_right_child_node(parent_node: int) -> int:
      """This function get the right child node of the binary heap.
      parent node: the index of the parent node."""

      return (parent_node * 2) + 2
    
    def _heapify_down(self, current_node: int, to_sort: list[int], heap_size: int) -> None:
      """This function makes the changed node go to the right place after replaced;
      current_node: the index of the changed node to heapify again;
      left/right child index: get the right and left child index;
      largest_node_index: get the atual largest node index;
      heap_size: the atual heap size;
      to_sort: the list to sort."""

      largest_node_index = current_node

      while True:
        left_child_index, right_child_index = self._get_left_child_node(largest_node_index), self._get_right_child_node(largest_node_index)
        
        if left_child_index > heap_size:
          break

        if to_sort[left_child_index] > to_sort[largest_node_index]:
          largest_node_index = left_child_index

        if right_child_index <= heap_size and to_sort[right_child_index] > to_sort[largest_node_index]:
          largest_node_index = right_child_index

        if current_node != largest_node_index:
          to_sort[largest_node_index], to_sort[current_node] = to_sort[current_node], to_sort[largest_node_index]
          current_node = largest_node_index
        else:
          break
      
    def _max_heapify(self, to_sort: list[int], heap_size: int) -> None:
      """This function makes the binary heap, it's make a max heapify
      current_node: get the current node to verify (first is the last parent node)"""

      current_node = self._get_last_parent_node(to_sort)
      
      while current_node >= 0:
        self._heapify_down(current_node, to_sort, heap_size)
        current_node -= 1