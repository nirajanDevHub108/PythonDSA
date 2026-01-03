def numOfWays(n: int) -> int:
    MOD=10**9+7
    same=6
    diff=6

    for _ in range(2,n+1):
        new_same=(same * 3 + diff * 2) % MOD
        new_dif=(same * 2 + diff * 2) % MOD
        same,diff=new_same,new_dif
    return (same+diff) % MOD

n=1
print(numOfWays(n))