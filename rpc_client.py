# Import library xmlrpc
import xmlrpc.client

# Inisiasi proxy ke server
proxy = xmlrpc.client.ServerProxy("http://localhost:7778/")
# Inisiasi multicall dengan parameter variable proxy
multicall = xmlrpc.client.MultiCall(proxy)

multicall.penjumlahan(7,10)
multicall.pengurangan(7, 10)
multicall.perkalian(7, 10)
multicall.pembagian(7, 10)
multicall.isPrima(7)
hasil= multicall()

print("Penjumlahan =%d"
      "\nPengurangan =%d"
      "\nperkalian = %d"
      "\npembagian = %d"
      "\nisPrima? = %s"%tuple(hasil))
