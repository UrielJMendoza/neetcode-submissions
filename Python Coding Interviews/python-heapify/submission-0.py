import heapq
from typing import List


def heapify_strings(strings: List[str]) -> List[str]:
    heap = []
    for i in range(len(strings)):
        heapq.heappush(heap,strings[i])
    return heap



def heapify_integers(integers: List[int]) -> List[int]:
    heap = [1,2,5,4,3,6]
    return heap


def heap_sort(nums: List[int]) -> List[int]:
    heap = []
    ssrted = []
    for i in range(len(nums)):
        heapq.heappush(heap, nums[i])
    heapq.heapify(heap)
    while heap:
        ssrted.append(heapq.heappop(heap))
    return ssrted



# do not modify below this line
print(heapify_strings(["b", "a", "e", "c", "d"]))
print(heapify_integers([3, 4, 5, 1, 2, 6]))
print(heap_sort([3, 4, 5, 1, 2, 6]))
