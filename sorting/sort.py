from typing import List

class Solution:

    def selectionSort(self, arr: List[int]) -> List[int]:

        n = len(arr)

        for i in range(n):
            min_idx = i

            for j in range(i + 1, n):
                if arr[j] < arr[min_idx]:
                    min_idx = j

            arr[i], arr[min_idx] = arr[min_idx], arr[i]

        return arr


arr = [5, 7, 8, 4, 1, 6, 9, 2]

obj1 = Solution()

print(obj1.selectionSort(arr))