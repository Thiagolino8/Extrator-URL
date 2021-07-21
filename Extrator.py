import re

class Extrator:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()
        self.base_url = self.get_base_url()
        self.parâmetros_url = self.get_parâmetros_url()
        self.itens = {"moedaOrigem": "", "moedaDestino": "", "quantidade": "", "divisória": "&"}
        self.separa_itens()
        self.imprime_itens()

    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        padrão_url = re.compile("(http(s)?://)?(www.)?bytebank.com(.br)?/cambio")
        match = padrão_url.match(self.url)
        if not self.url or not match:
            raise ValueError("Url Inválida!")

    def get_base_url(self):
        return self.url[:(self.url.find("separador_de_parâmetro"))]

    def get_parâmetros_url(self):
        return self.url[(self.url.find("separador_de_parâmetro")) + 1:]

    def acha_e(self, inicio_da_busca):
        return self.parâmetros_url.find(self.itens["divisória"], inicio_da_busca)

    def acha_item(self, item):
        inicio_da_busca = self.parâmetros_url.find(item) + len(item) + 1
        if self.acha_e(inicio_da_busca) == -1:
            item = self.parâmetros_url[inicio_da_busca:]
        else:
            item = self.parâmetros_url[inicio_da_busca:self.acha_e(inicio_da_busca)]
        return item

    def separa_itens(self):
        for chave in self.itens:
            self.itens[chave] = self.acha_item(chave)

    def imprime_itens(self):
        print("A conversão é de " + self.itens["quantidade"] + " unidades de " + 
            self.itens["moedaOrigem"].title() + " em " + self.itens["moedaDestino"].title())


url = "https://bytebank.com/cambio?moedaOrigem=real&moedaDestino=dolar&quantidade=100"

url = Extrator(url)
