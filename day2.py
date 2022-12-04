class MoveSolverA:
    def __init__(self, move, beats, draws, points):
        self.move = move
        self.beats = beats
        self.draws = draws
        self.points = points

    def face_opponent(self, opponent):
        if opponent == self.beats:
            return self.points + 6
        elif opponent == self.draws:
            return self.points + 3
        else:
            return self.points


class MoveSolverB:
    def __init__(self, opponent_move, beat_points, draw_points, lose_points):
        self.opponent_move = opponent_move
        self.beat_points = beat_points
        self.draw_points = draw_points
        self.lose_points = lose_points

    def calculate_points(self, outcome):
        if outcome == "X":
            return self.lose_points
        elif outcome == "Y":
            return self.draw_points + 3
        else:
            return self.beat_points + 6


def solve_a(content):
    rock = MoveSolverA("X", "C", "A", 1)
    paper = MoveSolverA("Y", "A", "B", 2)
    scissors = MoveSolverA("Z", "B", "C", 3)
    moves = [rock, paper, scissors]
    score = 0
    for line in content:
        input_move = str.strip(line).split()
        for move in moves:
            if move.move == input_move.__getitem__(1):
                score = score + move.face_opponent(input_move.__getitem__(0))
    return score


def solve_b(content):
    rock = MoveSolverB("A", 2, 1, 3)
    paper = MoveSolverB("B", 3, 2, 1)
    scissors = MoveSolverB("C", 1, 3, 2)
    moves = [rock, paper, scissors]
    score = 0
    for line in content:
        input_move = str.strip(line).split()
        for move in moves:
            if move.opponent_move == input_move.__getitem__(0):
                score = score + move.calculate_points(input_move.__getitem__(1))
    return score


if __name__ == '__main__':
    with open("input/input2.txt") as file:
        file_content = file.readlines()
        print(solve_b(file_content))
