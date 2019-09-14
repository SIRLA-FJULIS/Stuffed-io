import socket
from _thread import *
from settings import *
from random import randint
import _pickle as pickle

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5555

try:
    s.bind(('', port))
except socket.error as e:
    print(str(e))
    
s.listen(2)
print("Waiting for a connection")

id = 0
players = {}

def threaded_client(conn, id):
    global players
    
    current_id = id
    
    data = conn.recv(16)
    name = data.decode("utf-8")
    print("[LOG]", name, "connected to the server.")
    
    color = COLORS[current_id]
    x, y = randint(100, 1100), randint(100, 500)
    players[current_id] = {"x": x, "y": y, "color": color, "score": 0, "name": name}
    
    conn.send(str.encode(str(current_id)))
    
    while True:
        try:
            data = conn.recv(32)
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            data = data.decode("utf-8")
            data = data.split()
            print(data)
            
            if data[0] == "get_players":
                send_data = pickle.dumps(players)
            elif data[0] == "move":
                if data[2] == "right":
                    players[int(data[1])]["x"] += START_SPEED
                elif data[2] == "left":
                    players[int(data[1])]["x"] -= START_SPEED
                elif data[2] == "up":
                    players[int(data[1])]["y"] -= START_SPEED
                elif data[2] == "down":
                    players[int(data[1])]["y"] += START_SPEED
                send_data = pickle.dumps(players)
            else:
                send_data = ''
            
            conn.send(send_data)
            
        except:
            break
        
    print("Connection Closed")
    conn.close()
    
while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)
    
    start_new_thread(threaded_client, (conn, id))
    id += 1