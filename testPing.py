
    
import subprocess
import os
import socket
##from firebase import firebase
import random
import time
import _thread as thread
from getmac import get_mac_address

def pingExecute(ping):
    h = input ("insert addresse:")
    try :
        ##d = subprocess.check_output("ping "+h, shell=True).decode()
        ##print(d)
        test= subprocess.Popen("ping "+h,stdout=subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
        out,err=test.communicate()
        s.send(out)
        ##s.send(d.encode("cp1252"))
        print (out)
        print (err)
        print ("done")
    except Exception as e :
        s.send("cannot execute ping".encode("cp1252"))
        print(e)
        print(stderr)



        
def listen ( socket , data,rvmac) :
    while (True):
        data,add = socket.recvfrom(1024)
        ##rvmac=data[0:17]
        print("server:")
        print(data)
        
        instructions.append(data.decode("cp1252"))
def sendit(socket ):
    i=0
    while(i<10):
        try :
                print("send")
                s.send("send".encode("cp1252"))
                test= subprocess.Popen("ping 127.0.0.1",stdout=subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
                out,err=test.communicate()
                ##out=out.decode("cp1252")+"\n"
                ##print(out)
                v = out.decode("cp1252")
                vi = v.replace("\n"," ")
                vi = vi.replace("\r"," ")
            
                        ##print(vi.encode("cp1252"))
                vi=vi+"\n"
                s.send(vi.encode("cp1252"))
               ## s.send(out.encode("cp1252"))
                ##print(out)
                print("done")
                i=i+1
                time.sleep(5)
        except Exception as e :
                socket.send("cannot execute ping".encode("cp1252"))
                print(e)
                print(stderr)
                i=i+1
def senditaskedt(socket,data,instructions):
    t=0
    print("send it")
    ##h=data[18:len(data)]
    ##h="127.0.0.1"
    for dat in instructions:
        try :
            t=dat.index("add=")
            print(t)
    
            if(t!=0):
                k=dat.index(" ",t)
                print(k)
                if(k!=0):
                    h=dat[t+4:k-1]
                    try :
                            ping = "ping "+h
                            print(ping)
                            test= subprocess.Popen(ping,stdout=subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
                            out,err=test.communicate()
                            ##print(out)
                            v = out.decode("cp1252")
                            vi = v.replace("\n"," ")
                            vi = vi.replace("\r"," ")
            
                            ##print(vi.encode("cp1252"))
                            vi=vi+"\n"
                            s.send(vi.encode("cp1252"))
                            print("done")
                            ##instructions.remove(dat)   
                            time.sleep(5)
                    except Exception as e :
                        s.send("cannot execute ping".encode("cp1252"))
                        print(e)
                        print(stderr)
        except Exception as e :
            ##break
            print(e)
    instructions.clear()

    
def sub ():
    try :
        print("thread listen is starting")
        thread.start_new_thread( listen, (s, data,rvmac, ) )
        print("thread listen is working")
    except :
        print("error starting thread listen")
    
    if (outmac.find(rvmac)==-1):
##if(True):
        try :
            print("thread send it is starting")
            thread.start_new_thread( sendit, (s, ) )
            print("thread send it is working")
        except Exception as e :
            print(e)
            print("error starting thread send")
    else :
        try :
            print("thread send tasked is starting")
            thread.start_new_thread( senditaskedt, (s, data, ) )
            print("thread send tasked is working")
        except Exception as e :
            print(e)
            print("error starting thread send asked by server")
            sub()
def sendever(socket,data,rvmac,username,instructions):
    while(True):
        ##if (outmac.find(rvmac)==-1):
        ##if(data.find(username)==-1):
        ##if(True):
        if(len(instructions)==0):
            try :
                print("thread send every 5 second for 10 times is starting")
                sendit(socket)
                print("thread send every 5 second for 10 times is working")
            except Exception as e :
                print(e)
                print("error starting thread send every 5 second for 10 times")
        else :
            try :
                print("thread send as tasked is starting")
                senditaskedt(s,data,instructions)
                print("thread send as tasked is working")
            except Exception as e :
                print(e)
                print("error starting thread send asked by server")
                sub()
        
##resultone=firebase.post('/automaticPing',{random.randint(1,100):d})
##print (d)
    




s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server="10.89.72.99"
port = 3000
add=(server,port)
s.connect(add)
stderr = ""
rvmac=""
data =""
outmac=""
instructions=[]

user= subprocess.Popen("hostname",stdout=subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
out,err=user.communicate()
##print(out)
username=out.decode("cp1252")
v = out.decode("cp1252")
v = "usrname:"+v
       
##print(vi.encode("cp1252"))
v=v+"\n"
s.send(v.encode("cp1252"))
macadd=get_mac_address()
##print(macadd)
t = macadd+"\n"

s.send(t.encode("cp1252"))
##data,add=s.recvfrom(1024)
##print (data)
##firebase=firebase.FirebaseApplication('https://pyvp-9c415.firebaseio.com/')
##result=firebase.get('/automaticPing',None)
##print (result)

##t = os.system('dir c:\\ping 127.0.0.1 >d:\test.txt')
##g=open("d:\test.txt","r",encoding="utf8").read()
##for line in g :
    
    ##print(line)
##p=subprocess.Popen('cmd.exe', stdin = subprocess.PIPE, stdout = subprocess.PIPE)
##print (t)
##g = subprocess.call(['ping', '127.0.0.1','>>d:\test.txt'])
##print (g)
##result = subprocess.run(['ping 127.0.0.1'], stdout=subprocess.PIPE)
##result.stdout.decode('utf-8')
##print (result)
##mac = subprocess.Popen("getmac",stdout=subprocess.PIPE,stderr = subprocess.PIPE,shell=True)
##outmac,errmac=mac.communicate()
##print (outmac)
##while (True) :
try :
    print("thread listen is starting")
    thread.start_new_thread( listen, (s, data,rvmac, ) )
    print("thread listen is working")
except :
    print("error starting thread listen")
if(True):
    try :
        print("thread send it is starting")
        thread.start_new_thread( sendever, (s,data,rvmac,username,instructions, ) )
        print("thread send it is working")
    except Exception as e :
        print(e)
        print("error starting thread send")
##resultone=firebase.post('/automaticPing',{random.randint(1,100):d})
##print (d)
