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

def ipAddressMask(ip):
    ip=int(ip.split('.')[0])
    if(1<=ip and ip<=127):
        return("255.0.0.0")
    elif(128<=ip and ip<=191):
        return("255.255.0.0")
    elif(192<=ip and ip<=223):
        return("255.255.255.0")
    elif(224<=ip and ip<=239):
        return("255.255.255.255")
    elif(240<=ip and ip<=255):
        return("255.255.255.255")

if(__name__=="__main__"):
    ipAddressClass("192.168.1.2")
    ipAddressMask("192.168.1.2")