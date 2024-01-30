class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        if n == 0:
            return nums1
        
        if m == 0:
            for i in xrange(n):
                nums1[i] = nums2[i]
            return nums1

        for i in xrange(n):
            for j in xrange(m):
                if nums2[i]<nums1[j]:
                    nums1[m+i] = nums1[j]
                    nums1[j] = nums2[i]
                    break
                else:
                    nums1[m+i] = nums2[i]

        for j in xrange(m+n):
            for i in xrange((m+n)-1):
                while nums1[i]>nums1[i+1]:
                    temp = nums1[i+1]
                    nums1[i+1] = nums1[i]
                    nums1[i] = temp

        return nums1  
            