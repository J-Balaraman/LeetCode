class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        for x in range(k):
            nums.insert(0, (nums[-1]))
            nums.pop()
        