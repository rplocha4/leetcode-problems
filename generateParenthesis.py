def generateParenthesis(n):
    solutions = []
    state = []
    search(state, solutions, n)
    return solutions


def search(state, solutions, n):
    if is_valid_solution(state, n):
        solutions.append("".join(state))
        return

    for candidate in get_candidates(state, n):
        state.append(candidate)
        search(state, solutions, n)
        state.pop()


def is_valid_solution(state, n):
    return len("".join(state)) == 2 * n


def get_candidates(state, n):
    if not state:
        return ["("]

    candidates = ["(", ")"]
    open_parenthesis = 0
    close_parenthesis = 0
    for i in range(len(state)):
        if state[i] == "(":
            open_parenthesis += 1
        else:
            close_parenthesis += 1

    if open_parenthesis == n:
        candidates.remove("(")

    if open_parenthesis == close_parenthesis:
        candidates.remove(")")

    return candidates


print(generateParenthesis(3))
