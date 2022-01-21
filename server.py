
import time, socket, sys
from RSA_tool import calcule_d, decrypt,encrypt


# Driver code    

p=5
q=7
rest=calcule_d(p,q)
d=rest[0]
n=rest[1]
e=rest[2]
publicKey1=(e,n)
new_socket = socket.socket()
host_name = socket.gethostname()
s_ip = socket.gethostbyname(host_name)
 
port = 8080
 
new_socket.bind((host_name, port))
print( "on listening !")

 
name = "Serveur"+','+str(e)+','+str(n)
 
new_socket.listen(1) 
 
 
conn, add = new_socket.accept()
 
print("Received connection from ", add[0])
print('Connection Established. Connected From: ',add[0])
 
client = (conn.recv(1024)).decode()
print(client + ' has connected.')
 
conn.send(name.encode())
while True:
    clientsplit =client.split(',')
    eOther=clientsplit[1]
    nOther=clientsplit[2]
    nameOther=clientsplit[0]
    message = input('Me : ')
    messageEncrypted=encrypt((int(eOther),int(nOther)),message)
    listToStr = ','.join(map(str, messageEncrypted))
    messageEncryptedList= listToStr 
    print("messageEncrypred:",messageEncryptedList)


    #sned message encrypted server to client


    conn.send(str(messageEncryptedList).encode())

    #receive  from client


    message = (conn.recv(1024)).decode()

    messageDecrypted=decrypt((d,n),message)
    print(nameOther, ':', messageDecrypted)