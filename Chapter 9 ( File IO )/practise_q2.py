import random
def game():
    print("Welcome to Game :")
    score = random.randint(1, 62)
    # Fetch the highscore
    with open("highscore.txt") as f :
        highscore = f.read()
        if(highscore!= ""):
            highscore = int(highscore)
        else:
            highscore = 0

    print(f"Your socre is : {score} ")

    if(score>highscore):
        # Write this highscore in xt file
        with open("highscore.txt" , "w") as f:
            f.write(str(score))   
    return score

game()