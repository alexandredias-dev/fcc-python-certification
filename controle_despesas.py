class despesa:
    def __init__(self, descrição, categoria, valor):
        self.descrição = descrição
        self.valor = valor


class controle_despesas:
    def __init__(self):
        self.despesas = []

    def adicionar_despesas(self, despesas):
        self.despesas.append(despesas)

    def listar_despesas(self):
        if self.despesas:
            for index, despesa in enumerate(self.despesas, start=1):
                print(f"{index}. Descrição: {despesa.descrição}, Valor: R${despesa.valor:.2f}")