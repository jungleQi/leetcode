def generateParenthesis(n):
    solutions = []
    def travel(n, m,res):
        if n==0 and m == 0:
            solutions.append(res)
            return

        if n > m or n<0 or m<0:
            return

        travel(n-1, m, res+'(')
        travel(n, m-1, res + ')')

    travel(n, n, "")
    return solutions

print generateParenthesis(3)

#调用栈近似tree，每个node认为是累积的当前路径的当前结果
#backtracking：当前调用分支 返回 到上一层调用，重新遍历父节点(同一level)其他路径的情况