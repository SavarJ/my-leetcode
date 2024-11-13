class Solution:
    def robotSim(self, commands, obstacles) -> int:
        o_x = defaultdict(list)
        o_y = defaultdict(list)
        for x,y in obstacles:
            o_x[x].append(y)
            o_y[y].append(x)
        
        for x in o_x:
            o_x[x].sort()
        for y in o_y:
            o_y[y].sort()
        
        
        def bs(arr, target, direc):
            l,r = 0, len(arr)-1
            while l <= r:
                m = (l+r)//2
                if target == arr[m]: return arr[m]
                if target > arr[m]:
                    l = m+1
                else:
                    r = m-1

            if direc < 0:
                # return the next smaller value
                return None if r == -1 else arr[r]
            elif direc > 0:
                return None if l == len(arr) else arr[l]
        
        x, y = 0, 0
        face = 0
        directions = [ [0,1], [1,0], [0,-1], [-1,0] ]
        res = 0
        zerozero = 0 in o_x[0]

        for i, command in enumerate(commands):
            if command == -1:
                face = (face+1)%4
            elif command == -2:
                face = (face-1)%4
            else:
                k = command
                dx, dy = directions[face][0]*k, directions[face][1]*k
                new_x, new_y = x+dx, y+dy 
                # check for obstacles in between this path
                # depending on the direction, we need to binary search accordingly.
                # ie search for obstacle at target and return any greater, or return any smaller
                if not(zerozero and i==0) and x == new_x: # check y
                    direc = directions[face][1]
                    next_step = y+direc
                    next_obs = bs(o_x[x], next_step, direc)
                    if next_obs != None:
                        # stop before the obstacle found if obstacle in path
                        if direc < 0 and next_obs >= new_y:
                            new_y = next_obs+1
                        elif direc > 0 and next_obs <= new_y:
                            new_y = next_obs-1

                elif not(zerozero and i==0) and y == new_y: # check x
                    direc = directions[face][0]
                    next_step = x+direc
                    next_obs = bs(o_y[y], next_step, direc)
                    if next_obs != None:
                        if direc < 0 and next_obs >= new_x:
                            new_x = next_obs+1
                        elif direc > 0 and next_obs <= new_x:
                            new_x = next_obs-1
            
                x, y = new_x, new_y

            res = max(res, x**2+y**2)
        
        return res
