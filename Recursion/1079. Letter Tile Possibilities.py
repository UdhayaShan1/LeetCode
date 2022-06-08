class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []
        dp = {}
        def recurse(arr,arr_index_ignore):
            key = tuple(arr)
            if len(arr) <= len(tiles):
                if key in dp:
                    return False
                res.append(''.join(arr))
                dp[key] = 1
            if len(arr) > len(tiles):
                return False

            for i in range(len(tiles)):
                if i in arr_index_ignore:
                    continue
                arr.append(tiles[i])
                arr_index_ignore[i] = 1
                recurse(arr,arr_index_ignore)
                arr.pop()
                del arr_index_ignore[i]

        recurse([],{})

        return len(res)-1
