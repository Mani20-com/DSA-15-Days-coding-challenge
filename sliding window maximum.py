from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        q = deque() 

        for i in range(len(nums)):
          
            if q and q[0] <= i - k:
                q.popleft()

  
            while q and nums[q[-1]] < nums[i]:
                q.pop()

            q.append(i)

          
            if i >= k - 1:
                result.append(nums[q[0]])

        return result

if __name__ == "__main__":
    sol = Solution()
    nums = [1, 3, -1, -3, 5, 3, 6, 7]
    k = 3
    print("Input:", nums)
    print("Window size (k):", k)
    print("Output:", sol.maxSlidingWindow(nums, k))
