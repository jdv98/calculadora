from subnetMask import maskToPrefix

def amountAddresses(mask):
    return pow(2,maskToPrefix(mask))-2

if(__name__=='__main__'):
    print(amountAddresses("255.255.255.0"))
