def searchMatrix(matrix, target):
    def divide(lo, hi, target):
        if lo[0]<hi[0] and lo[1]<hi[1]:
            mid = [(lo[0]+hi[0])//2, (lo[1]+hi[1])//2]
            if matrix[mid[0]][mid[1]] == target:
                return True

            if matrix[mid[0]][mid[1]]>target:
                ret1 = divide(lo, mid, target)
                ret2 = divide([lo[0], mid[1]], [mid[0], hi[1]], target)
                ret3 = divide([mid[0], lo[1]], [hi[1], mid[1]], target)
            else:
                ret1 = divide(mid, hi, target)
                ret2 = divide([lo[0], mid[1]], [mid[0], hi[1]], target)
                ret3 = divide([mid[0], lo[1]], [hi[1], mid[1]], target)
            return ret1 or ret2 or ret3
        else:
            return False

    row = len(matrix)
    col = len(matrix[0])
    lo = [0,0]
    hi = [row-1, col-1]
    return divide(lo, hi, target)

matrix = [[1, 4,  7, 11, 15],[2,   5,  8, 12, 19],[3,   6,  9, 16, 22],[10, 13, 14, 17, 24],[18, 21, 23, 26, 30]]
target = 5
searchMatrix(matrix, target)
