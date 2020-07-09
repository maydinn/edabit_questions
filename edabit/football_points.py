def football_points(wins, draws, losses):
    """
    a function that takes the number of wins, draws and losses
    and calculates the number of points a football team has obtained so far.
    A win receives 3 points, a draw 1 point and a loss 0 points.
    """
    return wins * 3 + draws * 1 + losses * 0


print(football_points(2, 1, 0))
