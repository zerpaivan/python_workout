# script para convertir un numero hexadecimal a decimal

class HextoDec():
    def __init__(self, num: str):
        self.num = num
    
    def conv_to_dec(self):
        self.num = self.num.upper() 
        self.num = self.num[::-1] # al reves la cadena para facilitar el loop
        d = {"A":"10", "B":"11", "C":"12", "D":"13", "E":"14", "F":"15"}
        dec_num = 0
        for n, i in enumerate(self.num):
            if i in d:
                val = d[i]
            else:
                val = i
            
            val = int(val)
            dec_num = dec_num + val * 16**n
            print("i: ", i, "n: ", n, "val: ", val)
        return dec_num


operacion1 = HextoDec("a03f")
print(operacion1.conv_to_dec())