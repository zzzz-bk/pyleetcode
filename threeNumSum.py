class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        l, r = 0, len(nums) - 1
        qs(nums, l, r)
        ans = []
        for s in range(r + 1):
            # ans.add(list(twoSum(nums,i+1,-nums[i])))
            if s > 0 and nums[s] == nums[s - 1]:
                continue
            i, j = s + 1, len(nums) - 1
            sum = -nums[s]
            curr = []
            while i < j:
                if nums[i] + nums[j] < sum:
                    i += 1
                elif nums[i] + nums[j] > sum:
                    j -= 1
                else:
                    if len(curr) == 0 or (nums[i] != curr[0] or nums[j] != curr[1]):
                        ans.append([-sum, nums[i], nums[j]])
                        if len(curr) == 0:
                            curr.append(nums[i])
                            curr.append(nums[j])
                        else:
                            curr[0], curr[1] = nums[i], nums[j]
                    i += 1
        return ans


def qs(s: list, l: int, r: int) -> None:
    if l < r:
        i, j = l, r
        p = s[i]
        while i < j:
            while i < j and p <= s[j]:
                j -= 1
            if i < j:
                s[i] = s[j]
                i += 1
            while i < j and p >= s[i]:
                i += 1
            if i < j:
                s[j] = s[i]
                j -= 1
        s[i] = p
        qs(s, l, i)
        qs(s, i + 1, r)


if __name__ == '__main__':
    obj = Solution()
    ans = obj.threeSum([-1,0,1,2,-1,-4])
    print(ans)
