import sys

totalOpciones=2

def main():
    n = len(sys.argv)
    if(n==totalOpciones):
        print("calc "+ str(sys.argv[1]))
    else:
        print("Uso:\n\tpython3 main.py [clase de direccion] [mascara] [bits red] [bits host]")

main()
