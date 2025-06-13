## README do Projeto: PokeAPI-exercicios

Este repositório contém exercícios e exemplos de como interagir com a [PokeAPI](https://pokeapi.co/), uma API RESTful abrangente para dados de Pokémon. O objetivo é explorar diferentes funcionalidades da API, como a recuperação de informações de Pokémon, tipos, habilidades e o armazenamento desses dados localmente.

### 🚀 Tecnologias Utilizadas

  * **Python**: Linguagem de programação principal utilizada nos scripts e notebooks.
  * **Jupyter Notebook**: Ambiente interativo para desenvolver e executar os exercícios (`Exercicios.ipynb`).
  * **PokeAPI**: A fonte de dados para todas as informações de Pokémon.
  * **SQLite**: Utilizado para o banco de dados local (`pokemon.db`), para persistir os dados obtidos da PokeAPI.

### 📁 Estrutura do Projeto

  * `Exercicios.ipynb`: O notebook principal contendo os exercícios e exemplos de código.
  * `Request_poke_API.py`: Um script Python que contém funções para fazer requisições à PokeAPI.
  * `poke_api.py`: Um script Python relacionadas à execução das funções criadas para a interação com a API.
  * `pokemon.db`: O arquivo do banco de dados SQLite onde os dados de Pokémon podem ser armazenados.
  * `.gitignore`: Arquivo para ignorar arquivos e pastas que não devem ser versionados pelo Git.
  * `tempCodeRunnerFile.py`: Um arquivo temporário gerado por IDEs ou editores de código.

### 💻 Como Usar

1.  **Clone o repositório:**

    ```bash
    git clone https://github.com/Ligia-lab/PokeAPI-exercicios.git
    cd PokeAPI-exercicios
    ```

2.  **Instale as dependências:**
    Este projeto pode requerer bibliotecas Python como `requests` para interagir com a API e `sqlite3` para o banco de dados. Se você encontrar erros de módulo não encontrado, instale-os:

    ```bash
    pip install requests
    ```

3.  **Abra o Jupyter Notebook:**

    ```bash
    jupyter notebook
    ```

    Isso abrirá uma interface no seu navegador. Navegue até o arquivo `Exercicios.ipynb` e abra-o para ver e executar os exercícios.

4.  **Execute os scripts Python:**
    Você pode executar os scripts Python diretamente (ex: `python Request_poke_API.py`) para testar funcionalidades específicas.

### 📝 Exercícios

O notebook `Exercicios.ipynb` guiará você através de diferentes tarefas, que podem incluir:

  * Fazer requisições GET para obter informações de Pokémon.
  * Parsing e manipulação dos dados JSON retornados pela API.
  * Armazenar dados de Pokémon no arquivo `pokemon.db`.
  * Consultar dados armazenados no banco de dados.

### 🤝 Contribuições

Contribuições são bem-vindas\! Se você tiver melhorias, correções de bugs ou novos exercícios, sinta-se à vontade para abrir um *pull request*.

