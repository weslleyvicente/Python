class Estoque:
    def __init__(self):
        self.produtos = {"salgados": 50, "refrigerantes": 30, "frutas": 20}
    def atualizar_estoque(self, produto, quantidade):
        if produto in self.produtos:
            self.produtos[produto] = quantidade
            print(f"Estoque de {produto} atualizado para {quantidade} unidades.")
            if quantidade <= 10:
                print(f"Atenção! O estoque de {produto} está baixo, reabasteça!")
        else:
            print("O produto não foi encontrado!")
    def exibir_estoque(self):
        print("\nEstoque Atual:")
        for produto, quantidade in self.produtos.items():
            print(f"{produto}: {quantidade} unidades")
        print()
estoque = Estoque()
estoque.exibir_estoque()
estoque.atualizar_estoque("salgados", 47)
estoque.atualizar_estoque("refrigerantes", 6)
estoque.atualizar_estoque("frutas", 17)