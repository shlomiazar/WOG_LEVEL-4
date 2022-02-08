import fileinput
import sys
import re
import linecache


def Winning_Points(diff):
    Points_Of_Winning = (diff * 3) + 5
    return Points_Of_Winning


def add_score(diff):
    with open("Scores.txt") as f:
        if len(f.readlines()) > 0:
            points = linecache.getline("Scores.txt", 1)
            score = Winning_Points(diff)
            points = int(points)
            new_score = points + score
            new_score = str(new_score)
            fout = open("Scores.txt", "w")
            fout.write(new_score)
            fout.close()
        else:
            score = Winning_Points(diff)
            score = str(score)
            fout = open("Scores.txt", "w")
            fout.write(score)
            fout.close()
    return True
