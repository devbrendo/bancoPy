from models.cliente import Cliente
from models.conta import Conta

felicity: Cliente = Cliente('Felicity Jones', 'felicity@gmail.com', "456.214.187-60", '02/07/1985')

brendo: Cliente = Cliente('Brendo Gaigher', 'brendo@gmail.com', '454.545.454-54', '12/10/1994')

print(felicity)
print(brendo)

contaf:Conta = Conta(felicity)
contaa: Conta = Conta(brendo)

print(contaf)
print(contaa)