class Solution(object):
    def containsDuplicate(self, nums):
        count_map={}
        for num in nums:
            if num in count_map:
                count_map[num] += 1
            else:
                count_map[num] = 1
        for num in count_map:
            if count_map[num] >= 2:
                return True
        return False

        