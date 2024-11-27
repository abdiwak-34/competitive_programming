class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(speed)
        pos_speed = [(position[i],speed[i]) for i in range(n)]
        pos_speed.sort(reverse=True, key= lambda x: x[0])
        ans = []
        print(pos_speed)
        for pospeed in pos_speed:
            t = (target - pospeed[0])/pospeed[1]
            if not ans:
                ans.append(t)
            elif ans and ans[-1] < t:
                ans.append(t)
        return len(ans)