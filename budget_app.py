class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        return False

    def get_balance(self):
        return sum(item["amount"] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {category.name}")
            category.deposit(amount, f"Transfer from {self.name}")
            return True
        return False

    def check_funds(self, amount):
        return amount <= self.get_balance()

    def __str__(self):
        # Título centralizado
        title = f"{self.name:*^30}\n"
        items = ""
        for item in self.ledger:
            # Descrição (23 caracteres) e Valor (7 caracteres, 2 decimais)
            desc = f"{item['description'][:23]:23}"
            amt = f"{item['amount']:>7.2f}"
            items += f"{desc}{amt}\n"
        
        total = f"Total: {self.get_balance():.2f}"
        return title + items + total


def create_spend_chart(categories):
    # 1. Calcular gastos totais e por categoria (apenas saques, ignorando transferências de entrada)
    spendings = []
    for cat in categories:
        spent = sum(item['amount'] for item in cat.ledger if item['amount'] < 0)
        spendings.append(abs(spent))
    
    total_spent = sum(spendings)
    # Porcentagem arredondada para baixo para a dezena mais próxima
    percentages = [(s / total_spent * 100) // 10 * 10 for s in spendings]

    # 2. Construir o gráfico (parte superior)
    res = "Percentage spent by category\n"
    for i in range(100, -1, -10):
        res += f"{i:>3}| "
        for p in percentages:
            res += "o  " if p >= i else "   "
        res += "\n"

    # 3. Linha horizontal
    res += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 4. Nomes das categorias verticalmente
    max_len = max(len(cat.name) for cat in categories)
    names = [cat.name.ljust(max_len) for cat in categories]
    
    for i in range(max_len):
        res += "     "
        for name in names:
            res += name[i] + "  "
        if i < max_len - 1:
            res += "\n"

    return res