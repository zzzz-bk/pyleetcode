class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l,r = 0,len(nums)-1
        MAX_INT = 1 << 63 -1
        qs(nums,l,r)
        near = MAX_INT
        ans = []
        for s in range(r+1):
            t = target - nums[s] #nums[s] + nums[i] + nums[j] == target
            i,j = s+1,r
            while i<j:
                if abs(nums[i] + nums[j] - t) < near:
                    near = abs(nums[i] + nums[j] - t)
                    ans = [nums[s],nums[i],nums[j]]
                    if nums[i] + nums[j] - t == 0:
                        return sum(ans)
                if nums[i] + nums[j] > t:
                    j -= 1
                else:
                    i += 1
        return sum(ans)

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
    nearly = obj.threeSumClosest([-1,2,1,-4],1)
    print(nearly)