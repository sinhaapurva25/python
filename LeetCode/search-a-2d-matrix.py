class Solution:

    def binary_search(self, matrix_m_mid, target):
        s = 0
        e = len(matrix_m_mid) - 1
        while s <= e:
            mid = (s+e) // 2
            if target < matrix_m_mid[mid]:
                e = mid - 1
            elif target >matrix_m_mid[mid]:
                s = mid + 1
            else:# target == matrix_m_mid[mid]:
                return mid
        return -1

    def matrix_binary_search(self, matrix: list, target: int) -> (int, int):
        m_start = 0
        m_end = len(matrix) - 1
        while m_start <= m_end:
            m_mid = (m_start + m_end) // 2

            if target < matrix[m_mid][0]:
                m_end = m_mid - 1
            elif target > matrix[m_mid][len(matrix[0]) - 1]:
                m_start = m_mid + 1
            else:
                #if matrix[m_mid][0] <= target <= matrix[m_mid][len(matrix[0]) - 1]:
                found_in_mth_row = self.binary_search(matrix[m_mid], target)
                return m_mid, found_in_mth_row
        return -1, -1

    # def matrix_binary_search(self, matrix: list, target: int, m_start, m_end) -> (int, int):
    #     m_mid = (m_start + m_end) // 2
    #     if m_mid < 0 or m_mid > len(matrix) - 1 or m_start > m_end:
    #         return -1, -1
    #     if target < matrix[m_mid][0]:
    #         m_end = m_mid - 1
    #         return self.matrix_binary_search(matrix, target, m_start, m_end)
    #     elif target > matrix[m_mid][len(matrix[0]) - 1]:
    #         m_start = m_mid + 1
    #         return self.matrix_binary_search(matrix, target, m_start, m_end)
    #     else:
    #         #if matrix[m_mid][0] <= target <= matrix[m_mid][len(matrix[0]) - 1]:
    #         found_in_mth_row = self.binary_search(matrix[m_mid], target)
    #         if found_in_mth_row > -1:
    #             return m_mid, found_in_mth_row
    #         return self.matrix_binary_search(matrix, target, m_start, m_end)

    def searchMatrix(self, matrix: list, target: int) -> bool:
        idx = self.matrix_binary_search(matrix, target)#, 0, len(matrix))
        print(idx)
        if -1 in idx:
            return False
        return True


s = Solution()
print(s.binary_search([23, 30, 34], 30))
print(s.searchMatrix(matrix=[[1, 3, 5], [10, 11, 16], [23, 30, 34]], target=30) is (2, 1))
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3) is (0, 1))
print(s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13) is (1, -1))
print(s.searchMatrix(matrix=[[23, 30, 34, 60]], target=60) is (0, 3))
