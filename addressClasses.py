def ipAddressClass(ip):
    ip=int(ip.split('.')[0])
    if(1<=ip or ip>=127):
        print("Clase A")
    elif(128<=ip or ip>=191):
        print("Clase B")
    elif(192<=ip or ip>=223):
        print("Clase C")
    elif(224<=ip or ip>=239):
        print("Clase D")
    elif(240<=ip or ip>=255):
        print("Clase E")


if(__name__=="__main__"):
    ipAddressClass("192.168.1.2")
