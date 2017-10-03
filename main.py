from state import State
from queue import PriorityQueue

def main():
    goal = State(
        [[1, 2, 3],
         [4, 5, 6],
         [7, 8, 0]]
    )

    start = State(
        [[1, 5, 0],
         [2, 8, 7],
         [4, 6, 3]],
        goal
    )


    solution = solve(start, goal)
    print_solution(solution)

def print_solution(solution):
    steps = []
    state = solution

    while state.parent:
        steps.append(state.last_move)
        state = state.parent

    steps.reverse()
    print(','.join(steps))

def solve(start, goal):
    queue = PriorityQueue()
    visited = []

    queue.put(start)

    while not queue.empty():
        state = queue.get()
        visited.append(state)

        next = state.get_next_states()

        for s in next:
            if s.distance == 0:
                return s
            if s not in visited:
                queue.put(s)


if __name__ == '__main__':
    main()