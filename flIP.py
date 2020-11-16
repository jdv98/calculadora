def calcFirstIP(ip):
    ip=ip.split('.')
    ip[-1]=str(int(ip[-1])+1)
    return '.'.join(ip)

def calcLastIP(ip):
    ip=ip.split('.')
    ip[-1]=str(int(ip[-1])-1)
    return '.'.join(ip)

def calcRed(ip,mask):
    ip=ip.split('.')
    mask=mask.split('.')
    resultado=[]

    for x in range(0,len(ip)):
        resultado.append(str( int(ip[x]) & int(mask[x])) )
   
    return '.'.join(resultado)

def calcDifusion(ip,mask):
    ip=ip.split('.')
    mask=mask.split('.')

    for x in range(0,len(mask)):
        temp=''
        maskbin="{0:08b}".format(int(mask[x]))
        for y in maskbin:
            if(y=='1'):
                temp+='0'
            else:
                temp+='1'
        mask[x]=int(temp,2)

    resultado=[]

    for x in range(0,len(ip)):
        resultado.append(str( int(ip[x]) | int(mask[x])) )
   
    return '.'.join(resultado)

if( __name__=='__main__'):
    ip="172.30.239.145"
    mask="255.255.192.0"
    red=calcRed(ip,mask)
    difusion= calcDifusion(ip,mask)
    print(calcFirstIP(red))
    print(calcLastIP(difusion))

