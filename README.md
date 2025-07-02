# Pandemic (Refatorado)

Este projeto é uma implementação refatorada do popular jogo de tabuleiro Pandemic, provavelmente uma versão baseada em texto ou terminal, dado o diretório `terminal_view`. O objetivo é fornecer uma base de código limpa e modular para a lógica do jogo.

## Estrutura do Projeto

-   `config.py`: Configurações do jogo.
-   `controller/`: Contém os controladores da lógica do jogo, como `game_map_controller.py` e `jogo_controller.py`.
-   `diagramas e escopo/`: Documentação, diagramas UML e detalhes do escopo do projeto.
-   `domain/`: Entidades centrais do jogo e lógica de negócios, incluindo `baralho.py`, `cidade.py`, `doenca.py`, `jogador.py`, `mao.py` e vários tipos de cartas em `carta/`.
-   `enuns/`: Enumerações usadas em todo o projeto, como `cor.py` e `baralho.py`.
-   `game_loop.py`: O loop principal do jogo.
-   `terminal_view/`: Lida com a interface de usuário baseada em terminal, incluindo `header.py`, `menu.py`, `painel.py` e `view_map.py`.
-   `test/`: Testes unitários para vários componentes do jogo.

## Como Executar

1.  **Pré-requisitos:** Certifique-se de ter o Python 3.x instalado.

2.  **Clonar o repositório:**
    ```bash
    git clone <url_do_repositorio>
    cd Pandemic-Refatorado
    ```
    (Substitua `<url_do_repositorio>` pela URL real deste repositório.)

3.  **Instalar dependências (se houver):**
    Atualmente, não há arquivos `requirements.txt` explícitos ou similares, sugerindo dependências externas mínimas. Se houver necessidade, elas seriam instaladas aqui.

4.  **Executar o jogo:**
    ```bash
    python game_loop.py
    ```

## Testes

Para executar os testes, navegue até a raiz do projeto e execute:

```bash
python -m unittest discover test
```