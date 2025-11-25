def solveNQueens(n):
    solutions = []
    points = []

    cols = set()
    diag1 = set()  # r - c
    diag2 = set()  # r + c

    def backtrack(r):
        if r == n:
            solutions.append(points.copy())
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)
            points.append((r, c))

            backtrack(r + 1)

            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)
            points.pop()

    backtrack(0)
    return solutions



