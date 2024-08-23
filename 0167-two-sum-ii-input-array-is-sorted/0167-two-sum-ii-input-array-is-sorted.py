class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        copy = numbers.copy()
        t1 = 0
        t2 = -1
        for x in numbers:
            if numbers[t1] + numbers[t2] == target:
                return [(t1 + 1), ((len(numbers) + 1) + t2)]
            elif numbers[t1] + numbers[t2] > target:
                t2 -= 1
            else:
                t1 += 1