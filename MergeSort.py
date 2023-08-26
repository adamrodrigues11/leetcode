def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    if n == 0:
        return nums1
    i, j = (0, 0)
    while i < m + n and j < n:
        if nums2[j] < nums1[i]:
            nums1[i+1:] = nums1[i:-1]
            nums1[i] = nums2[j]
            j += 1
        elif (m + n) - i == n - j:
            nums1[i:] = nums2[j:]
            break
        i += 1
    return nums1

# A cleaner solution to merge two sorted arrays is to work from the end
def merge(nums1, m, nums2, n):
    """
    :type nums1: List[int]
    :type m: int
    :type nums2: List[int]
    :type n: int
    :rtype: None Do not return anything, modify nums1 in-place instead.
    """
    x = m - 1
    y = n - 1
    z = m + n - 1
    while y >= 0:
        if x >= 0 and nums1[x] > nums2[y]:
            nums1[z] = nums1[x]
            x -= 1
        else:
            nums1[z] = nums2[y]
            y -= 1
        z -= 1
    return nums1