def prefixToMask(prefix):
    resultado=''
    prefix=int(prefix)
    for x in range(4,0,-1):
        binary=''
        for y in range(8,0,-1):
            if(prefix>0):
                binary+='1'
                prefix-=1
            else:
                binary+='0'
        resultado+=str(int(binary,2))+'.'

    return resultado[:-1]

def maskToPrefix(mask):
    mask=mask.split('.')
    for x in range(0,4):
        mask[x]="{0:b}".format(int(mask[x]))
    mask=''.join(mask)
    cont=0
    for x in mask:
        if(x=='1'):
            cont+=1
    return cont


if(__name__=='__main__'):
    print(prefixToMask(24))
    print(maskToPrefix("255.255.255.0"))
