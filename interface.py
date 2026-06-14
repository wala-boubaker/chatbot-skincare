import tkinter as tk
import subprocess
import tkinter as tk
import os

def launch_chatbot1():
    subprocess.Popen(['start', 'cmd', '/k', 'python first_code.py'], shell=True)

def launch_chatbot2():
    subprocess.Popen(['start', 'cmd', '/k', 'python using_chatterbot.py'], shell=True)

def launch_chatbot3():
    subprocess.Popen(['start', 'cmd', '/k', 'python exp.py'], shell=True)
# Création de la fenêtre principale
root = tk.Tk()
root.title("Interface Multi-Chatbot")
root.geometry("400x250")
root.configure(bg="#f0f0f0")

# Titre
title = tk.Label(root, text="Lanceur de Chatbots", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
title.pack(pady=20)

# Boutons pour chaque chatbot
btn1 = tk.Button(root, text="NLTK", command=launch_chatbot1, width=25, height=2, bg="#cce5ff")
btn1.pack(pady=5)

btn2 = tk.Button(root, text="Chatterbot", command=launch_chatbot2, width=25, height=2, bg="#d4edda")
btn2.pack(pady=5)

btn3 = tk.Button(root, text="Chatterbot supervisé", command=launch_chatbot3, width=25, height=2, bg="#f8d7da")
btn3.pack(pady=5)

# Boucle principale
root.mainloop()




