class binary_heap:
    @staticmethod
    def _get_last_parent_node(to_sort) -> int:
      """this function get's the last parent node"""
      return (len(to_sort) // 2) - 1
    @staticmethod
    def _get_left_child_node(parent_node: int) -> int:
       """This function get the left child node
       
       Parameters:
       
       parent node(int): the index of the parent node"""
       return (parent_node * 2) + 1
    @staticmethod
    def _get_right_child_node(parent_node: int, ) -> int:
      """This function get the right child node, return -1 if the parent don't have a right child
      
      Parameters:
      
      parent node(int): the index of the parent node"""
      return (parent_node * 2) + 2
    def _heapify_down(self, current_node: int, to_sort) -> None | int:
      """This function makes the changed node go to the right place after replaced

      Parameters:

      current node(int): the index of the changed node to heapify again"""
      largest_index = current_node
      left_child, right_child = self._get_left_child_node(largest_index), self._get_right_child_node(largest_index)
      if left_child < len(to_sort) and to_sort[left_child] > to_sort[largest_index]:
        largest_index = left_child
      if right_child < len(to_sort) and to_sort[right_child] > to_sort[largest_index]:
        largest_index = right_child
      if current_node != largest_index:
        to_sort[largest_index], to_sort[current_node] = to_sort[current_node], to_sort[largest_index]
        return largest_index
      else:
        return None
    def _max_heapify(self, to_sort):
      """This function makes the binary heap, it's make a max heapify, but there is also a min heapify
      heap_last_parent: get the last node with childs
      current index: get the current node to verify
      left/right child: get the left and the right child(if the parent have a right child)
      heapified index: makes the changed child get in the right place after replaced"""
      current_node = self._get_last_parent_node(to_sort)
      while current_node >= 0:
        largest_index = current_node
        left_child, right_child = self._get_left_child_node(current_node), self._get_right_child_node(current_node)
        if to_sort[largest_index] < to_sort[left_child]:
          largest_index = left_child
        if right_child < len(to_sort) and to_sort[largest_index] < to_sort[right_child]:
          largest_index = right_child
        if largest_index != current_node:
          to_sort[current_node], to_sort[largest_index] = to_sort[largest_index], to_sort[current_node]
          adjust_node = largest_index
          while adjust_node != None:
            adjust_node = self._heapify_down(adjust_node, to_sort)
        current_node -= 1
class list_verification:
  @staticmethod
  def __init__(to_verify_list: list[int]) -> bool | ValueError | IndexError | TypeError:
      """This function is a safety function
      thats verify if list only have numbers
      if the list have more than two numbers 
      and if it's really a list"""
      if isinstance(to_verify_list, list):
        if len(to_verify_list) < 2:
          raise IndexError("You need to pass a list with more than one item")
        for item in to_verify_list:
          if isinstance(item, (int, float)):
            continue
          else:
            raise ValueError("Your list can only have numbers!")
        return True
      else:
        raise TypeError("Your item need to be a list!")