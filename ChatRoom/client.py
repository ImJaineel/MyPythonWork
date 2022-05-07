from http import server
import socket
import threading
from tkinter import *
from tkinter import font
from tkinter import ttk

# from chat import *

port = 5000
server = input("Enter server IP: ")
address = (server, port)
format = "utf-8"