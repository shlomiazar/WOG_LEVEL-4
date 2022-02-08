from os import system, name

SCORES_FILE_NAME = "Scores.txt"
Bad_Return_Code = -1


def Clear_screen():
    if name == "nt":
        system("cls")
    elif name == "posix":
        system("clear")
