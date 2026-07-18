class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        left = 0
        res = []
        queue = []

        for right in range(len(arr)):
            while queue and arr[right] > queue[-1]:
                queue.pop()
            
            queue.append(arr[right])

            if right - left + 1 == k:
                res.append(queue[0])

                if queue[0] == arr[left]:
                    queue.pop(0)
                
                left += 1
        
        return res



        
