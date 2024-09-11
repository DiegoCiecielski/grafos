class Vertice:
    def __init__(self, nomeCidade):
        self.nomeCidade = nomeCidade
        self.conexoes = []

    def adicionar_conexao(self, aresta):
        self.conexoes.append(aresta)

    def info_conexoes(self):
        return [(aresta.cidade2.nomeCidade if aresta.cidade1 == self else aresta.cidade1.nomeCidade, aresta.distancia)
                for aresta in self.conexoes]

    def info_vertice(self):
        return self.nomeCidade

class Aresta:
    def __init__(self, cidade1, cidade2, distancia):
        self.cidade1 = cidade1
        self.cidade2 = cidade2
        self.distancia = distancia

    def info_aresta(self):
        return (self.cidade1.nomeCidade, self.cidade2.nomeCidade, self.distancia)

class Grafo:
    def __init__(self):
        self.cidades = []
        self.conexoes = []

    def cadastra_cidade(self, nomeCidade):
        if self.encontrar_cidade(nomeCidade):
           print(f'Cidade {nomeCidade} já está cadastrada.')
           return None
        vertice = Vertice(nomeCidade)
        self.cidades.append(vertice)
        print(f'Cidade {nomeCidade} cadastrada com sucesso.')
        return vertice

    def cadastra_conexao(self, cidade1, cidade2, distancia):
        for aresta in self.conexoes:
            if (aresta.cidade1 == cidade1 and aresta.cidade2 == cidade2) or \
               (aresta.cidade1 == cidade2 and aresta.cidade2 == cidade1):
                print(f'Conexão entre {cidade1.nomeCidade} e {cidade2.nomeCidade} já existe com distância {aresta.distancia}km.')
                return
        aresta = Aresta(cidade1, cidade2, distancia)
        cidade1.adicionar_conexao(aresta)
        cidade2.adicionar_conexao(aresta)
        self.conexoes.append(aresta)
        print(f'Conexão entre {cidade1.nomeCidade} e {cidade2.nomeCidade} com distância {distancia} cadastrada com sucesso.')

    def listar_cidades(self):
        return sorted([cidade.info_vertice() for cidade in self.cidades])

    def listar_conexoes(self):
        return [aresta.info_aresta() for aresta in self.conexoes]

    def listar_cidades_vizinhas(self, cidade):
        vizinhos = cidade.info_conexoes()
        for i in range(1, len(vizinhos)):
            chave = vizinhos[i]
            j = i - 1
            while j >= 0 and chave[1] < vizinhos[j][1]:
                vizinhos[j + 1] = vizinhos[j]
                j -= 1
            vizinhos[j + 1] = chave
        return vizinhos

    def encontrar_cidade(self, nomeCidade):
        nomeCidade_lower = nomeCidade.lower()
        for cidade in self.cidades:
            if cidade.info_vertice().lower() == nomeCidade_lower:
                return cidade
        return None

def menu():
    grafo = Grafo()

    while True:
        print('\nMenu:')
        print('1. Cadastrar cidade')
        print('2. Cadastrar conexão')
        print('3. Listar cidades')
        print('4. Listar conexões')
        print('5. Listar cidades vizinhas')
        print('6. Sair')

        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            nomeCidade = input('Nome da cidade: ')
            grafo.cadastra_cidade(nomeCidade)

        elif opcao == '2':
            nomeCidade1 = input('Nome da primeira cidade: ')
            nomeCidade2 = input('Nome da segunda cidade: ')
            distancia = float(input('Distância entre as cidades: '))

            cidade1 = grafo.encontrar_cidade(nomeCidade1)
            cidade2 = grafo.encontrar_cidade(nomeCidade2)

            if cidade1 and cidade2:
                grafo.cadastra_conexao(cidade1, cidade2, distancia)
            else:
                print('Uma das cidades não foi cadastrada.')

        elif opcao == '3':
            cidades = grafo.listar_cidades()
            print('Cidades:', cidades)

        elif opcao == '4':
            conexoes = grafo.listar_conexoes()
            if conexoes:
                print('Conexões:')
                for con in conexoes:
                    print(f'{con[0]} - {con[1]}: {con[2]}km')
            else:
                print('Nenhuma conexão cadastrada.')

        elif opcao == '5':
            nomeCidade = input('Nome da cidade para listar vizinhos: ')
            cidade = grafo.encontrar_cidade(nomeCidade)

            if cidade:
                vizinhos = grafo.listar_cidades_vizinhas(cidade)
                print(f'Vizinhos de {nomeCidade}:')
                for vizinho in vizinhos:
                    print(f'{vizinho[0]}: {vizinho[1]}km')
            else:
                print('Cidade não encontrada.')

        elif opcao == '6':
            break

        else:
            print('Opção inválida. Tente novamente.')

menu()
