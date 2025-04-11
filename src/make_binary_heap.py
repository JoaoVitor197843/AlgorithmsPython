class binary_heap:
    def _verify_list(self) -> bool | ValueError | IndexError | TypeError:
        """This function is a safety function
        thats verify if list only have numbers
        if the list have more than two numbers 
        and if it's really a list"""
        if isinstance(self.items, list):
          if len(self.items) < 2:
            raise IndexError("You need to pass a list with more than one item")
          for __item in self.items:
            if isinstance(__item, (int, float)):
              continue
            else:
              raise ValueError("Your list can only have numbers!")
          return True
        else:
          raise TypeError("Your item need to be a list!")
    def _get_last_parent_node(self) -> int:
      """this function get's the last parent node"""
      return (len(self.items) // 2) - 1
    def _get_left_child_node(self, parent_node: int) -> int:
       """This function get the left child node
       
       Parameters:
       
       parent node(int): the index of the parent node"""
       return (parent_node * 2) + 1
    def _get_right_child_node(self, parent_node: int) -> int:
      """This function get the right child node, return -1 if the parent don't have a right child
      
      Parameters:
      
      parent node(int): the index of the parent node"""
      return (parent_node * 2) + 2 if (parent_node * 2) + 2 < len(self.items) else -1
    def _heapify(self, current_node: int) -> None | int:
      """This function makes the changed node go to the right place after replaced

      Parameters:

      current node(int): the index of the changed node to heapify again"""
      if current_node > self._get_last_parent_node():
        return None
      candidate_index = current_node
      left_child, right_child = self._get_left_child_node(candidate_index), self._get_right_child_node(candidate_index)
      if self.items[left_child] > self.items[candidate_index]:
        current_node = left_child
      if right_child != -1:
        if self.items[right_child] > self.items[current_node]:
          current_node = right_child
      if current_node != candidate_index:
        self.items[candidate_index], self.items[current_node] = self.items[current_node], self.items[candidate_index]
        return current_node
      else:
        return None
    def _max_heapify(self):
      """This function makes the binary heap, it's make a max heapify, but there is also a min heapify
      heap_last_parent: get the last node with childs
      current index: get the current node to verify
      left/right child: get the left and the right child(if the parent have a right child)
      heapified index: makes the changed child get in the right place after replaced"""
      if self._verify_list():
        heap_last_parent = self._get_last_parent_node()
        while heap_last_parent >= 0:
          current_index = heap_last_parent
          left_child, right_child = self._get_left_child_node(heap_last_parent), self._get_right_child_node(heap_last_parent)
          if self.items[current_index] < self.items[left_child]:
              current_index = left_child
          if right_child != -1:
            if self.items[current_index] < self.items[right_child]:
              current_index = right_child
          if self.items[current_index] != self.items[heap_last_parent]:
            self.items[heap_last_parent], self.items[current_index] = self.items[current_index], self.items[heap_last_parent]
            while True:
              heapified_index = self._heapify(current_index)
              if heapified_index is None:
                break
              else:
                current_index = heapified_index
          heap_last_parent -= 1