class Converte:
    def __init__(self,valor):
        
        print('O tipo incial e:',type(valor), 'com valor',valor)
        self.valor = str(valor)
        print('Convertido!!!!')
        
        
    def imprime(self):
        print('ao Usar a CLasse o valor agora e do tipo',type(self.valor))
        
lista = [1,2.5,3,'v',2.5]
val2 = []
for i in lista:
    val2=Converte(i)
    val2.imprime()
    print('______________')   
