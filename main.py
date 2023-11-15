import tkinter as tk
import random
import time
from tkinter import messagebox

# SCREEN
window = tk.Tk()
window.config(bg="Grey")
window.title("ROCK PAPER SCISSOR")
window.minsize(400,500)

# SCORE
player_score = 0
pc_score = 0
round_end_text = ""

# FUNCTIONS

def game_end_check():
    global player_score
    global pc_score
    if player_score == 3 or pc_score == 3 :
        if player_score == 3:
            messagebox.showinfo("MATCH POINT!",message="YOU WIN !!!")

        else:
            messagebox.showinfo("MATCH POINT!",message="PC WIN !!!")
        player_score = 0
        pc_score = 0
        score_label.config(text="PC | {} : {} | PLAYER".format(pc_score, player_score),
                           font=("Ariel", 12, "bold"))

    else:
        pass

def score_counter(player_decision , pc_decision):
    global pc_score
    global player_score
    global round_end_text
    global end_screen_label

    if pc_decision == player_decision:
        round_end_text = "TIE !!"
    elif player_decision == 1 :
        if pc_decision == 2:
            pc_score += 1
            round_end_text = "PC WIN !! \n ROCK VS PAPER"
        else:
            player_score +=1
            round_end_text = "PLAYER WIN !! \n ROCK VS SCISSOR"

    elif player_decision == 2:
        if pc_decision == 1:
            player_score +=1
            round_end_text = "PLAYER WIN !! \n PAPER VS ROCK"
        else:
            pc_score += 1
            round_end_text = "PC WIN !! \n PAPER VS SCISSOR"
    elif player_decision == 3:
        if pc_decision == 1:
            round_end_text = "PC WIN !! \n SCISSOR VS ROCK"
        else:
            player_score += 1
            round_end_text = "PLAYER WIN \n SCISSOR VS PAPER"
    else:
        pass

    end_screen_label.config(text=round_end_text)
    score_label.config(text="PC | {} : {} | PLAYER".format(pc_score,player_score),
                       font=("Ariel",12,"bold"))
    game_end_check()


def button_disabeler():
    rock_button.config(state="disabled")
    paper_button.config(state="disabled")
    scissor_button.config(state="disabled")
    time.sleep(2)
    rock_button.config(state="normal")
    paper_button.config(state="normal")
    scissor_button.config(state="normal")
def rock():
    global rock_button
    global paper_button
    global scissor_button
    player_decison = 1
    pc_decision = random.randint(1, 4)
    score_counter(player_decision=player_decison , pc_decision=pc_decision)
    button_disabeler()
def paper():
    global rock_button
    global paper_button
    global scissor_button
    player_decison = 2
    pc_decision = random.randint(1, 4)
    score_counter(player_decision=player_decison, pc_decision=pc_decision)
    button_disabeler()
def scissor():
    global rock_button
    global paper_button
    global scissor_button
    player_decison = 3
    pc_decision = random.randint(1, 4)
    score_counter(player_decision=player_decison, pc_decision=pc_decision)
    button_disabeler()

#  ROCK BUTTON
rock_button = tk.Button(text="Rock",
                        width=7,
                        height=3,
                        command=rock)
rock_button.place(x=100,y=350)

# PAPER BUTTON
paper_button = tk.Button(text="Paper",
                         width=7,
                         height=3,
                         command=paper)
paper_button.place(x=175,y=350)

# SCISSOR BUTTON
scissor_button = tk.Button(text="Scissor",
                           width=7,
                           height=3,
                           command=scissor)
scissor_button.place(x=250,y=350)


# COMPUTER DECISION LABEL
comp_dec_label = tk.Label(text="RPS MASTER(BOT)")
comp_dec_label.place(x=150,y=60)

# SCORE LABEL
score_label = tk.Label(text="PC | 0 : 0 | PLAYER",
                       font=("Ariel",12,"bold"))
score_label.place(x=130 , y= 140)

# END SCREEN
end_screen_label = tk.Label(text="End Screen",
                            bg="Orange",
                            width=20,
                            height=7)
end_screen_label.place(x=130,y=175)





window.mainloop()