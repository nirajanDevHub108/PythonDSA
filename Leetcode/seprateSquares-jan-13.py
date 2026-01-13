class Solution:
    def separateSquares( self,squares):
        low = min(y for _, y, _ in squares)
        high = max(y + l for _, y, l in squares)

        def diff(Y):
            above = 0.0
            below = 0.0
            for _, y, l in squares:
                top = y + l
                if Y <= y:
                    above += l * l
                elif Y >= top:
                    below += l * l
                else:
                    above += (top - Y) * l
                    below += (Y - y) * l
            return above - below

        for _ in range(60):  # enough precision for 1e-5
            mid = (low + high) / 2.0
            if diff(mid) > 0:
                low = mid
            else:
                high = mid

        return (low + high) / 2.0
squares =[[0,0,1],[2,2,1]]
sol=Solution()
print(sol.separateSquares(squares))