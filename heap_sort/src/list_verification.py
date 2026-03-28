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