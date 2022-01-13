class ContaCorrente:
    def __init__(self, codigo):
        self.codigo = codigo
        self.saldo = 0

    def deposita(self,valor):
        self.saldo += valor

    def __str__(self):
        return "[>>Codigo {} Saldo {} <<]".format(self.codigo, self.saldo)

conta_gab = ContaCorrente(10)
conta_gab.deposita(400)

conta_jana = ContaCorrente(20)
conta_jana.deposita(150)

contas = [conta_gab, conta_jana]
for conta in contas:
    print(conta) # deve ser passado para string se não ele vai aparecer sua alocação de memoria quando foi mostrar uma list de dois objetos

gabriel = ("gabriel", 22, 1999) #tupla
conta_x = (1, 2)

# print(conta_gab)

gab = ('gabriel', 22, 1999)
jana = ('janaina', 49, 1972)

usuarios = [gab, jana]

def __str__(self, usuarios):
    return "[usuarios: {}]".format(usuarios)