from subnetMask import prefixToMask
from ipAddress import ipAddressMask, ipAddressClass
from flIP import calcRed, calcDifusion, calcLastIP, calcFirstIP
from segmentos import networkHost
from amountAddresses import amountAddresses

#ip | mask | red | Difusion | primera ip | ultima ip | cantidad direccines

def receive(ip,prefijo):
    resultado={}
    mask=0
    if(prefijo!=None):
        mask= prefixToMask(prefijo)
    else:
        mask=ipAddressMask(ip)
    resultado['ip']=ip
    resultado['mask']=mask
    resultado['red']=calcRed(ip,mask)                                     #RED
    resultado['difusion']=calcDifusion(ip,mask)                           #DIFUSION
    resultado['primeraip']=calcFirstIP(resultado['red'])                  #FirstIP
    resultado['ultimaip']=calcLastIP(resultado['difusion'])               #LastIP
    resultado['cantidaddirecciones']=amountAddresses(resultado['mask'])
    resultado['tipoclaseip']=ipAddressClass(resultado['ip'])

    return resultado


if(__name__=='__main__'):
    print(receive("192.168.1.2/30"))
    print('\n')
    print(receive("192.168.1.2"))
