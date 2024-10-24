import tkinter as tk
import customtkinter as ctk
import pygame as pg
import threading
from tkinter import messagebox  
import cv2
import numpy as np
#import time
from time import sleep

logo1 = 'des1.png'
logo2 = 'ng.png'


def iniciar_juego(peso):
    
    pg.init()
    scream = pg.display.set_mode((600, 400))
    pg.display.set_caption('Graficos')


    logo = pg.image.load(logo2)
    logo = pg.transform.scale(logo, (400, 400))
    rec = logo.get_rect(center=(300, 200))
    angulo = 0
    reloj = pg.time.Clock()

    pg.mixer.music.load('toll.mp3')
    pg.mixer.music.play(-1)

    while True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                pg.quit()
                return  # Salir de la función

        angulo += 1
        imagen_rotada = pg.transform.rotate(logo, angulo)
        rec_rotado = imagen_rotada.get_rect(center=rec.center)

        scream.fill((7, 4, 19))
        scream.blit(imagen_rotada, rec_rotado.topleft)

        pg.display.flip()
        reloj.tick(60)

def iniciar_juego2(peso):
    pg.init()
    scream = pg.display.set_mode((720, 480))
    pg.display.set_caption('Graficos')

    # Abre el video
    video = cv2.VideoCapture('meme.mp4')  
    reloj = pg.time.Clock()

    pg.mixer.music.load('sad.mp3')
    pg.mixer.music.play(-1)

    while True:
        for evento in pg.event.get():
            if evento.type == pg.QUIT:
                video.release()  
                pg.quit()
                return


        ret, frame = video.read()
        if not ret:
            video.set(cv2.CAP_PROP_POS_FRAMES, 0)  
            continue

   
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    
        frame_surface = pg.surfarray.make_surface(np.transpose(frame, (1, 0, 2)))

 
        scream.fill((7, 4, 19))
        scream.blit(frame_surface, (0, 0)) 

        pg.display.flip()
        reloj.tick(60) 
    
    

def iniciar():
    peso = peso_entry.get()
    if peso >= '70':
        messagebox.showerror("Error", "¡No seas pendejo, tas obeso papi!")  
        #time.sleep(2)
        threading.Thread(target=iniciar_juego, args=(peso,)).start()  


    elif peso == '':
        messagebox.showerror("Error", "¡No seas pendejo, ingrese un número!") 

    else:
        messagebox.showerror("Error", "¡No seas pendejo, tas desnutrido papi!")  
        threading.Thread(target=iniciar_juego2, args=(peso,)).start()  




ctk.set_appearance_mode("dark")  
ctk.set_default_color_theme("blue")  

root = ctk.CTk()
root.title("Balanza")
root.geometry("300x200")


peso_label = ctk.CTkLabel(root, text="Ingrese su peso:")
peso_label.pack(pady=10)


peso_entry = ctk.CTkEntry(root)
peso_entry.pack(pady=10)


iniciar_button = ctk.CTkButton(root, text="¡Listo!", command=iniciar)
iniciar_button.pack(pady=20)

root.mainloop()