def ipAddressClass(ip):
    ip=int(ip.split('.')[0])
    if(1<=ip and ip<=127):
        return("Clase A")
    elif(128<=ip and ip<=191):
        return("Clase B")
    elif(192<=ip and ip<=223):
        return("Clase C")
    elif(224<=ip and ip<=239):
        return("Clase D")
    elif(240<=ip and ip<=255):
        return("Clase E")


if(__name__=="__main__"):
    ipAddressClass("192.168.1.2")
