# Import library xmlrpc
import xmlrpc.server

# Inisiasi server
server = xmlrpc.server.SimpleXMLRPCServer( ("0.0.0.0", 7778) )

# Definisi procedure atau fungsi
#fungsi penjumlahan
def penjumlahan(a,b):
    return (a+b)

#fungsi pengurangan
def pengurangan(a,b):
    return (a-b)

#fungsi pembagian
def pembagian(a,b):
    return (a/b)

#fungsi perkalian
def perkalian(a,b):
    return (a*b)

#fungsi pengecekan bilangan prima
def isPrima(a):
    if a > 1:
        for i in range(2, a):
            temp = a % i
            if temp == 0 & a == 2:
                return False
            else:
                return True
            break
        i= i+1
    else: return False

# register fungsinya
server.register_multicall_functions()
server.register_function(penjumlahan, "penjumlahan")
server.register_function(pengurangan, "pengurangan")
server.register_function(perkalian, "perkalian")
server.register_function(pembagian, "pembagian")
server.register_function(isPrima, "isPrima")

# Running server RPC
server.serve_forever()