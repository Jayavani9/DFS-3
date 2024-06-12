
#Tc: O(4^N)  Sc: O(N)
class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        if not matchsticks:
            return False

        total_length = sum(matchsticks)
        if total_length % 4 != 0:
            return False

        side_length = total_length // 4
        matchsticks.sort(reverse=True)
    
        sides = [0] * 4
    
        def backtrack(index):
            if index == len(matchsticks):
                return sides[0] == sides[1] == sides[2] == sides[3] == side_length

            for i in range(4):
                if sides[i] + matchsticks[index] <= side_length:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]
                if sides[i] == 0:
                    break
            return False

        return backtrack(0)


