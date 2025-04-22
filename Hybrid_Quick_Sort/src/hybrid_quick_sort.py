def insertion_sort(list_to_sort: list[int], left: int, right: int):
    for index in range(left, right + 1):
        position = index
        item = list_to_sort[index]
        while position > left:
            position -= 1
            if item < list_to_sort[position]:
                list_to_sort[index], list_to_sort[position] = list_to_sort[position], list_to_sort[index]
                index = position
            else:
                break
def quick_sort(list_to_sort: list[int]):
    quick_sort_stack = [(0,len(list_to_sort)-1)]
    while quick_sort_stack:        
        left, right = quick_sort_stack.pop()
        if right - left <= 6:
            insertion_sort(list_to_sort, left, right)
        else:
            pivo = partition(list_to_sort, left, right)
            quick_sort_stack.append((left, pivo - 1))
            quick_sort_stack.append((pivo + 1, right))
def partition(list_to_sort: list[int], left: int, right: int) -> int:
    list_to_sort[(left + right) // 2], list_to_sort[right] = list_to_sort[right], list_to_sort[(left + right) // 2]
    pivo = list_to_sort[right]
    start = left - 1
    for item in range(left, right):
        if list_to_sort[item] <= pivo:
            start += 1
            list_to_sort[item], list_to_sort[start] = list_to_sort[start], list_to_sort[item]
    list_to_sort[right], list_to_sort[start + 1] = list_to_sort[start + 1], list_to_sort[right]
    return start + 1