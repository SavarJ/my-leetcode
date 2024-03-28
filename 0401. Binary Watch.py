class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        blocks = [0]*10
        res = []
        def addTimeToResult():
            hours = str(int(''.join(map(str, blocks[:4])), 2))
            mins = str(int(''.join(map(str, blocks[4:])), 2))
            if int(hours) < 12 and int(mins) < 60:
                time = hours + ":" + ("0" if len(mins) < 2 else "") + mins
                res.append(time)
        
        def bt(i, c):
            if c == turnedOn: return addTimeToResult()
            if i >= len(blocks): return
            blocks[i] = 1
            bt(i+1, c+1)
            blocks[i] = 0
            bt(i+1, c)
        
        bt(0, 0)
        return res
