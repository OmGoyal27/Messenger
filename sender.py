# Client script (run on the sending computer)
import socket
import pyautogui as pg

ip_add = '192.168.1.13'  # IP address of the receiver's computer

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((ip_add, 12345))

message = pg.prompt(text="Please enter your message.", title="Om's app")

client.sendall(message.encode('utf-8')) # Sends the message

client.close()