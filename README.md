# Programa de Gestão de Cidades e Conexões em Grafos

Este projeto é um programa em Python que permite gerenciar cidades e conexões entre elas usando a estrutura de grafos. Com este programa, você pode cadastrar cidades, criar conexões entre elas com distâncias especificadas, listar as cidades cadastradas, visualizar as conexões existentes, e encontrar cidades vizinhas ordenadas pela distância.

## Funcionalidades

1. **Cadastrar cidade**: Adiciona uma nova cidade ao grafo.
2. **Cadastrar conexão**: Cria uma conexão entre duas cidades com uma distância especificada, evitando duplicações.
3. **Listar cidades**: Exibe todas as cidades cadastradas no grafo.
4. **Listar conexões**: Mostra todas as conexões cadastradas entre as cidades.
5. **Listar cidades vizinhas**: Lista as cidades vizinhas de uma cidade específica, ordenadas pela distância.
6. **Sair**: Encerra o programa.

## Estrutura do Código

### Classes Principais

- **Vertice**: Representa uma cidade no grafo.
  - `adicionar_conexao(aresta)`: Adiciona uma conexão a partir de uma aresta.
  - `info_conexoes()`: Retorna informações das conexões da cidade.
  - `info_vertice()`: Retorna o nome da cidade.

- **Aresta**: Representa uma conexão entre duas cidades no grafo.
  - `info_aresta()`: Retorna informações da conexão (cidades e distância).

- **Grafo**: Gerencia o grafo com cidades e conexões.
  - `cadastra_cidade(nomeCidade)`: Cadastra uma nova cidade.
  - `cadastra_conexao(cidade1, cidade2, distancia)`: Cria uma nova conexão entre duas cidades.
  - `listar_cidades()`: Retorna a lista de todas as cidades cadastradas.
  - `listar_conexoes()`: Retorna a lista de todas as conexões cadastradas.
  - `listar_cidades_vizinhas(cidade)`: Lista as cidades vizinhas ordenadas pela distância.
  - `encontrar_cidade(nomeCidade)`: Encontra e retorna um objeto cidade pelo nome.

### Menu Interativo

O programa apresenta um menu interativo para facilitar o uso:
```plaintext
Menu:
1. Cadastrar cidade
2. Cadastrar conexão
3. Listar cidades
4. Listar conexões
5. Listar cidades vizinhas
6. Sair
