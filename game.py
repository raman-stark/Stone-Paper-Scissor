import random
import tkinter as tk
from PIL import Image, ImageTk


# INIT window, along with Title.
window = tk.Tk()
window.geometry("290x500")
window.title("Scissor Paper Rock")

# INIT IMG @ window.
image = Image.open('aa.jpg')
image.thumbnail((290, 290), Image.ANTIALIAS)
photo = ImageTk.PhotoImage(image)
label_image = tk.Label(image=photo)
label_image.grid(column=15, row=0)

# global variables
RPS = {'scissor': 0, 'paper': 1, 'rock': 2}
USER_SCORE = 0
CPU_SCORE = 0


# The main function.
def function(user_choice, cpu_choice):
    global USER_SCORE
    global CPU_SCORE

    user = RPS[user_choice.lower()]
    comp = RPS[cpu_choice.lower()]

    if(user == comp):
        print("Tie.")
    elif((user-comp) % 3 == 1):
        print("Sorry! CPU won.")
        CPU_SCORE += 1
    else:
        print("Congarts!! YOU won.")
        
        USER_SCORE += 1

    # Text
    text_area = tk.Text(master=window, height=12, width=30)
    text_area.grid(column=15, row=4)
    answer = 'You: {}\n'.format(user_choice)
    answer += "CPU: {}\n".format(cpu_choice)
    answer += '-'*30+'\n'
    answer += "Your's Score: {}\n".format(USER_SCORE)
    answer += "CPU's Score:  {}".format(CPU_SCORE)
    text_area.insert(tk.END, answer)


# Event Handling
def event(user_choice):
    cpu_choice = random.choice(list(RPS.keys()))
    function(user_choice, cpu_choice)


def rock():
    event('Rock')


def paper():
    event('Paper')


def scissor():
    event('Scissor')


# Buttons
button1 = tk.Button(text="Scissor", bg="#81CDDA", fg='#FFFFFF',
                    command=scissor, height=1, width=8,
                    font=('arial', 15, 'bold'))
button1.grid(column=15, row=1)
button2 = tk.Button(text="Paper", bg="#FFDF4C", fg='#FFFFFF',
                    command=paper, height=1, width=8,
                    font=('arial', 15, 'bold',))
button2.grid(column=15, row=2)
button3 = tk.Button(text="Rock", bg="#F5527B", fg='#FFFFFF',
                    command=rock, height=1, width=8,
                    font=('arial', 15, 'bold'))
button3.grid(column=15, row=3)


window.mainloop()
