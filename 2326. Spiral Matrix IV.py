class Solution:
    def spiralMatrix(self, R: int, C: int, head: Optional[ListNode]) -> List[List[int]]:
        res = [[-1] * C for _ in range(R)]
        directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        face = 0

        r = c = 0
        while head:
            res[r][c] = head.val
            head = head.next

            rr = r + directions[face][0]
            cc = c + directions[face][1]

            if rr not in range(R) or cc not in range(C) or res[rr][cc] != -1:
                face = (face+1)%4
            
            r += directions[face][0]
            c += directions[face][1]

        return res
