import os
import openai
import pygame
import sys
import json
import shutil
import os
from random import shuffle, choice
import time
from pygame.locals import *
import tkinter
from tkinter import filedialog
import os
import openai



openai.api_key = "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"
openai.Model.list()


def get_response(question):
    prompt = f"Q: {question}\nA:"
    completions = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7
    )
    message = completions.choices[0].text.strip()
    return message

question1 = "Fait moi un qcm en 10 questions sur les HashMap en java en suivant le modèle suivant :  Question | Réponse 1 | Réponse 2 | Réponse 3 ?"

retQuestion1 = get_response(question1)

print(retQuestion1)

questions_and_answers = []

for line in retQuestion1.splitlines():
    if "|" in line:
        question, *answers = line.split(" | ")
        questions_and_answers.append([question, answers])


repQuestion1 = "Quelle est la réponse à la question suivante :" + retQuestion1

repQuestion1 = get_response(repQuestion1)

print(repQuestion1)

trueAnswers = []

for line in repQuestion1.splitlines():
    substring = line.split(". ", 1)[1]
    for i in range(len(questions_and_answers)):
        for j in range(len(questions_and_answers[i][1])):
            if(questions_and_answers[i][1][j] == substring):
                trueAnswers.append(j+1)











def get_response(question):
    prompt = f"Q: {question}\nA:"
    completions = openai.Completion.create(
        model="text-davinci-003", prompt=prompt, max_tokens=1024, n=1, stop=None, temperature=0.7
    )
    message = completions.choices[0].text.strip()
    return message

pygame.init()
pygame.font.init()
#gameIcon = pygame.image.load('assets/flag.ico')
#pygame.display.set_icon(gameIcon)
pygame.display.set_caption('MemoQuiz')
screen = pygame.display.set_mode((1490, 750), pygame.RESIZABLE)

buttonFont = pygame.font.SysFont('impact', 80)
sButtonTxt = buttonFont.render('Save & Play', True, (255, 255, 255))
#back = pygame.image.load("assets/back.gif")

lastDir = os.path.expanduser('~/Documents/')

def browse_pdf(path):
    main_win = tkinter.Tk()
    main_win.withdraw()
    main_win.overrideredirect(True)
    main_win.geometry('0x0+0+0')
    main_win.lift()
    main_win.focus_force()
    filename = filedialog.askopenfilename(initialdir=path,
                                          title="Select a pdf document",
                                          filetypes=(("*.pdf*", "*txt*"),
                                                     (" ", "*.*")))
    main_win.destroy()
    return path

class button():
    _t = 0
    def __init__(self, color, x,y,width,height, c, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.correct = c

    def draw(self,win,outline=None):
        #Call this method to draw the button on the screen
        if outline:
            pygame.draw.rect(win, outline, (self.x-2,self.y-2,self.width+4,self.height+4),0)
            
        pygame.draw.rect(win, self.color, (self.x,self.y+ button._t,self.width,self.height),0)
        
        if self.text != '':
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (0,0,0))
            win.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y+ button._t + (self.height/2 - text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y+button._t and pos[1] < self.y+button._t + self.height:
                return True
            
        return False
    
    def validate(self):
        if self.correct:
            self.color = (0, 255, 0)
        else:
            self.color = (255, 0, 0)

#qs = browse_pdf(lastDir)


buttons = []
txts = []
d = 0
i = -1

print(questions_and_answers)
print(trueAnswers)
for q in questions_and_answers:
    txts.append(button((60, 60, 85), 200, d, 1000, 50, False, text=q[0]))
    d += len(q)%400+100
    i += 1

    for a in range(len(q[1])):
        try:
            buttons.append(button((255, 255, 255), 200, d, 300, 50, int(trueAnswers[i])==a, q[1][a]))
            d+=100
        except:
            pass

browse_pdf(lastDir)
while True:
    menu = True
    while menu:
        pygame.time.delay(100)
        screen.fill((60, 60, 85))
        width, height = screen.get_size()
        mx, my = pygame.mouse.get_pos()

        for mb in buttons:
            mb.draw(screen)
        for mb in txts:
            mb.draw(screen)
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                for b in buttons:
                    if b.isOver(pygame.mouse.get_pos()):
                        b.validate()

        if my >= screen.get_height()-10:
            button._t -= 10
        elif my <= 10:
            button._t += 10


        pygame.display.update()