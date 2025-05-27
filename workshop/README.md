<h1 align="center">Data + GitHub Copilot para soluções avançadas de dados</h1>
<em align="center">O combinação perfeito ™</em>

## Introdução

Este repositório contém o código-fonte para o workshop. Você seguirá o guia passo a passo abaixo, completando todas as etapas enquanto trabalha com dados e GitHub Copilot dentro do Codespaces.

> [!NOTE]
> Este repositório tem como objetivo apresentar vários recursos do **GitHub Copilot**, como o **Copilot Chat** e o **chat inline**. Portanto, os guias passo a passo abaixo contêm a descrição geral do que precisa ser feito, e o Copilot Chat ou chat inline podem ajudá-lo a gerar os comandos necessários.
>
> Cada etapa (quando aplicável) também contém um `Cheatsheet` que pode ser usado para validar as sugestões do Copilot contra o comando correto.
>
> 💡 Experimente diferentes prompts e veja como isso afeta a precisão das sugestões do GitHub Copilot. Por exemplo, ao usar o chat inline, você pode usar um prompt adicional para refinar a resposta sem precisar reescrever todo o prompt.

## Recursos do Projeto de Dados

Neste workshop, você trabalhará com dados de um arquivo CSV incluído neste repositório, bem como um arquivo de script Python que interagirá com o arquivo CSV. Aqui estão alguns recursos do projeto com os quais você trabalhará:

1. Consumir um conjunto de dados CSV e realizar transformações
1. Identificar e implementar validações
1. Criar uma ferramenta de linha de comando que pode ser usada em ambientes CI/CD

## Preparação

Este repositório está pronto para Codespaces e está pré-configurado para que você tenha todas as dependências instaladas, incluindo as extensões do Visual Studio Code necessárias para trabalhar com GitHub Copilot e Python:

- GitHub Copilot
- Extensão Python
- Dependências Python pré-instaladas com um Ambiente Virtual ativado

> [!NOTE]
> Utilize uma conta pessoal no GitHub.

### 1. Crie um novo repositório a partir deste template

Progresso: [🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪] 1/12 (8%)

⏳ **~2min**

- Clique em `Use this template` :point_right: `Create a new repository`
- Defina o proprietário como seu nome de usuário do GitHub
- Dê um nome ao repositório como `data-with-copilot`
- Adicione uma descrição como `Data + GitHub Copilot para soluções avançadas de dados`
- Defina a visibilidade como `Public`
- Clique em `Create repository`

❗Se quiser, você pode utilizar o botão abaixo para criar um repositório a partir deste template. Certifique-se de que o nome do repositório seja `data-with-copilot` e que a visibilidade seja `Public`.

[![start-course](https://raw.githubusercontent.com/dev-pods/introduction-to-secret-scanning/873eb13decfe79fd486ff84bd97de0dab4912d9a/images/botao.svg)](https://github.com/new?template_owner=dev-pods&template_name=data-with-copilot&owner=%40me&name=data-with-copilot&description=Data+%2B+GitHub+Copilot+para+soluções+avançadas+de+dados&visibility=public)

### 2. Crie um Codespace usando o template fornecido

Progresso: [🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪] 2/12 (16%)

⏳ **~3min**

- No repositório recém-criado, clique em `Code` :point_right: `Codespaces` :point_right: `[menu de reticências]` :point_right: `New with options` :point_right: _Certifique-se de que `Dev container configuration` esteja definido como `Python 3`_ :point_right: `Machine type` como `2-core` :point_right: `Create codespace`

- ❗Se você estiver tendo problemas para iniciar o Codespace como descrito acima, clique em `Code` :point_right: `Codespaces` :point_right: `Create codespace on main`

### 3. Verifique se o Python está instalado e configurado corretamente

Progresso: [🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪⚪] 3/12 (25%)

⏳ **~2min**

- Use a paleta de comandos para alternar o terminal (procure por "Create new terminal")
- Execute `which python` e certifique-se de que ele aponta para o Ambiente Virtual (`home/vscode/venv/bin/python`)
- Execute `which pip` e certifique-se de que também aponta para o Ambiente Virtual (`home/vscode/venv/bin/pip`)

### 4. Execute os scripts Python

Progresso: [🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪⚪] 4/12 (33%)

⏳ **~2min**

- Execute o script `main.py` e confirme que não ocorram erros:

    ```shell
    python main.py
    ```

- Execute o script `check.py` e confirme que não ocorram erros:

    ```shell
    python check.py
    ```

    Deve haver algumas linhas OK e algumas FAIL:

    ```shell
    [OK  ]   verify_drop_notes
    [FAIL]   verify_high_ratings - Not all ratings are 90 or higher.
    [FAIL]   verify_one_hot_encoding - The 'Red Wine' column was not one-hot encoded correctly.
    [OK  ]   verify_remove_newlines_carriage_returns
    [FAIL]   verify_ratings_to_int - The 'ratings' column was not converted to integers correctly.
    ```

### 5. Abra arquivos relevantes

Progresso: [🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪⚪] 5/12 (41%)

⏳ **~2min**

O GitHub Copilot se beneficia de ter contexto. Uma maneira de aprimorar o contexto é abrir arquivos relevantes.

- Abra os arquivos `main.py`, `check.py`, `train.csv` e `transformed_train.csv`

## Desenvolvimento

### 1. Veja o quanto você pode aprender sobre o projeto e os dados

Progresso: [🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪⚪] 6/12 (50%) - Metade do caminho!

⏳ **~5min**

- Abra o GitHub Copilot Chat
- Use o agente `@workspace` para perguntar ao Copilot o que os arquivos `main.py` e `check.py` estão fazendo
- Novamente, com o agente `@workspace`, pergunte ao Copilot qual é a natureza dos dados com os quais você vai trabalhar

#### 2. Corrija a função de altas classificações

Progresso: [🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪⚪] 7/12 (58%)

⏳ **~3min**

- Em `main.py` encontre a função `select_high_ratings()`
- Insira seu cursor na assinatura ou corpo da função em algum lugar
- Abra o chat inline com `Ctrl-i` ou `Cmd-i` (no Mac)
- Prefixe seu prompt com o comando de barra `/explain`
- Pergunte por que essa função pode não estar funcionando e implemente possíveis correções
- Regenere o arquivo `transformed_train.csv` executando `python main.py`
- Verifique a correção executando `python check.py` com esta função retornando `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
/explique por que esta função pode não estar funcionando corretamente?
```

##### Saída esperada

```sh
Com base no código fornecido, existem algumas razões potenciais pelas quais a função `select_high_ratings` pode não estar funcionando corretamente:

1. Erro de digitação no nome da coluna: A função verifica se o nome da coluna 'ratings' existe no DataFrame `df.columns`. Se houver um erro de digitação no nome da coluna, como 'rating' em vez de 'ratings', a condição `if 'ratings' in df.columns` não será atendida.

```

</details>

> [!NOTE]
> Sinta-se à vontade para usar o GitHub Copilot Chat para implementar ou corroborar a correção

#### 3. Corrija o problema de codificação one-hot

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪⚪] 8/12 (66%)

⏳ **~3min**

- Selecione a função `drop_and_one_hot_encode_red_wine()` e abra o chat inline (Ctrl-i / Cmd-i)
- Use o comando de barra `/fix` para pedir ao GitHub Copilot que sugira uma possível correção
- Regenere o arquivo `transformed_train.csv` executando `python main.py`
- Verifique a correção executando `python check.py` com esta função retornando `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
Esta função não está fazendo codificação one-hot na coluna variety
```

##### Saída esperada

```python
def drop_and_one_hot_encode_red_wine(df):
    """
    Create a 'Red_Wine' column that is 1 if 'variety' is 'Red Wine' and 0 otherwise.
    Drop the original 'variety' column.
    """
    if 'variety' in df.columns:
        df['Red_Wine'] = df['variety'].apply(lambda x: 1 if x == 'Red Wine' else 0)
        df = df.drop(columns=['variety'])
    return df
```

</details>

#### 4. Corrija a conversão de classificações para int

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪⚪] 9/12 (75%)

⏳ **~3min**

- Se sua verificação `verify_ratings_to_int` já estiver "OK", então o Copilot pode ter corrigido esse problema para você. Caso contrário, continue com as seguintes etapas.
- Selecione a função `convert_ratings_to_int()` e abra o chat inline (Ctrl-i / Cmd-i)
- Use o comando de barra `/explain` para perguntar ao GitHub Copilot por que esta função pode não estar funcionando corretamente
- Identifique o problema e implemente a correção
- Regenere o arquivo `transformed_train.csv` executando `python main.py`
- Verifique a correção executando `python check.py` com esta função retornando `OK`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
Esta função não está convertendo as classificações para números inteiros

##### Saída esperada

```python
def convert_ratings_to_int(df):
    """
    Convert the 'rating' column from float to integer.
    """
    if 'rating' in df.columns:
        df['rating'] = df['rating'].to_int()
    return df
```

</details>

## Teste

Um projeto Python robusto pode se beneficiar de testes. Você adicionará alguns testes unitários e descobrirá mais sobre como executá-los com a ajuda do GitHub Copilot.

Certifique-se de ter o terminal aberto executando a paleta de comandos e digitando `toggle terminal`

### 1. Teste sua CLI

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪⚪] 10/12 (83%)

⏳ **~5min**

- Este projeto tem o executor e framework de teste Pytest pré-instalado, certifique-se de que está disponível executando `pytest --version`
- Execute os testes enquanto estiver no diretório `workshop` usando o seguinte comando: `pytest -v`

A saída deve apresentar uma falha.

#### 2. Corrija o teste com falha

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢⚪] 11/12 (91%)

⏳ **~5min**

- Selecione a saída no terminal e cole-a no GitHub Copilot Chat, prefixando com uma solicitação de correção e uma explicação
- Use a saída do chat para implementar uma correção em `test_main.py`

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
Corrija o teste e explique sua correção:
// Copie e cole a saída do terminal aqui
```

##### Saída esperada

O erro ocorre porque a função drop_notes provavelmente está modificando o DataFrame no local, em vez de retornar um novo DataFrame com a coluna 'notes' removida. Para corrigir o teste, precisamos garantir que a função drop_notes retorne um novo DataFrame sem a coluna 'notes' e então verificar as colunas deste novo DataFrame.

Aqui está a função de teste corrigida:

```python
def test_drop_notes_column_dropped():
    # Crie um DataFrame de exemplo com a coluna 'notes'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'notes': ['note1', 'note2', 'note3']})

    # Chame a função drop_notes e obtenha o resultado
    result = main.drop_notes(df)
    
    # Verifique se a coluna 'notes' no dataframe de resultado foi removida
    columns = result.columns.to_list()
    assert columns == ['A', 'B']
```

Ao armazenar o resultado da função drop_notes em uma nova variável e verificando suas colunas, garantimos que o teste verifica corretamente o comportamento da função.

</details>

#### 3. Adicione testes para a função de codificação one-hot

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) - 🎉 Celebre!

⏳ **~5min**

- Certifique-se de que o `python check.py` tenha todas as saídas OK, caso contrário, essa etapa pode não funcionar.
- Selecione a função `drop_and_one_hot_encode_red_wine` em `main.py`
- Abra o chat inline com `Ctrl-i` / `Cmd-i`
- Use o comando de barra `/tests` para obter sugestões de testes
- Revise a saída, aceite-a e verifique com o comando `pytest -v`. Todos os testes devem estar passando, e você deve ter mais testes do que antes. Às vezes, o Copilot indenta os testes sugeridos incorretamente (aninhando-os dentro de uma função de teste existente), então certifique-se de que os testes estejam corretamente indentados antes de executá-los.

<details>
<summary>Cheatsheet</summary>

##### Prompt

```sh
/tests
```

##### Saída esperada

```python
def test_drop_and_one_hot_encode_red_wine_red_wine_column_created():
    # Cria um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chama a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifique que a coluna 'Red_Wine_Red Wine' está criada
    assert 'Red_Wine_Red Wine' in result.columns

def test_drop_and_one_hot_encode_red_wine_red_wine_column_encoded():
    # Crie um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chame a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifique se a coluna 'Red_Wine_Red Wine' está codificada corretamente
    assert result['Red_Wine_Red Wine'].tolist() == [1, 0, 1]

def test_drop_and_one_hot_encode_red_wine_variety_column_dropped():
    # Crie um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chame a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifique se a coluna 'variety' foi removida
    assert 'variety' not in result.columns

def test_drop_and_one_hot_encode_red_wine_dataframe_unchanged():
    # Crie um DataFrame de exemplo com a coluna 'variety'
    df = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 5, 6], 'variety': ['Red Wine', 'White Wine', 'Red Wine']})

    # Chame a função drop_and_one_hot_encode_red_wine
    result = main.drop_and_one_hot_encode_red_wine(df)

    # Verifique se a forma do DataFrame não foi alterada
    assert result.shape == (3, 3)

    # Verifique se o DataFrame original não foi modificado
    assert 'variety' in df.columns
    assert df.shape == (3, 3)
```

</details>

## Bônus

Existem alguns desafios bônus se você concluiu todas as tarefas e seus scripts estão em bom estado.

### Desafio Bônus 1 - Criar uma ferramenta CLI robusta

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Opcional: [🚀 Turbo Boost! (1/2) 33%]  

- Use o chat do GitHub Copilot com o prefixo `@workspace` para converter o projeto em uma CLI com opções e um menu de ajuda
- Certifique-se de que o prompt especifique sem dependências externas e que deve usar apenas a biblioteca padrão

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace Quero converter este projeto em uma CLI com um menu de ajuda. Me ajude a fazer isso sem usar nenhuma dependência, apenas a biblioteca padrão do Python
```

#### Saída esperada

```python
def main():
    parser = argparse.ArgumentParser(description="DataFrame manipulation CLI")
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("drop_notes", help="Drop the 'notes' column from the DataFrame")
    subparsers.add_parser("select_high_ratings", help="Select rows where the 'rating' column is 90 or higher")
    subparsers.add_parser("drop_and_one_hot_encode_red_wine", help="One-hot encode 'Red Wine' and drop 'variety' column")
    subparsers.add_parser("remove_newlines_carriage_returns", help="Remove newlines and carriage returns from string columns")
    subparsers.add_parser("convert_ratings_to_int", help="Convert the 'rating' column from float to integer")

    args = parser.parse_args()

    # Load your DataFrame here
    df = pd.read_csv('workshop/train.csv')

    if args.command == "drop_notes":
        df = drop_notes(df)
    elif args.command == "select_high_ratings":
        df = select_high_ratings(df)
    elif args.command == "drop_and_one_hot_encode_red_wine":
        df = drop_and_one_hot_encode_red_wine(df)
    elif args.command == "remove_newlines_carriage_returns":
        df = remove_newlines_carriage_returns(df)
    elif args.command == "convert_ratings_to_int":
        df = convert_ratings_to_int(df)
    else:
        parser.print_help()

    # Save the transformed DataFrame
    df.to_csv('workshop/transformed_train.csv', index=False)

if __name__ == "__main__":
    main()
```

</details>

### Desafio Bônus 2 - Documentar seu projeto

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Opcional: [🚀 Turbo Boost! (1/2) 33%]  
Opcional: [🌟 Pontos Extras! (2/2) 66%]  

- Crie uma nova pasta `docs/` e um arquivo chamado `README.md`
- Use o chat do GitHub Copilot com o prefixo `@workspace` para começar a documentar seu projeto usando Markdown em um README.md
- Em seu prompt, peça ajuda para documentar os objetivos do projeto, a natureza dos dados nos arquivos CSV e como a CLI funciona.

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace me ajude a criar um bom arquivo README.md em Markdown para que eu possa documentar isso e ajudar outros a entenderem como funciona e a natureza dos dados
```

#### Saída esperada

```markdown
# CLI de Manipulação de DataFrame

Este projeto fornece uma interface de linha de comando (CLI) para manipular um DataFrame usando várias operações. A CLI é construída usando a biblioteca padrão Python e não requer dependências externas.

## Sumário

- [Instalação](#installation)
- [Uso](#usage)
- [Comandos](#commands)
- [Dados](#data)
- [Contribuindo](#contributing)
- [Licença](#license)

## Instalação

1. Clone o repositório:
    ```sh
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```
    2. Configure um ambiente virtual:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instale os pacotes necessários:
    ```sh
    pip install -r workshop/requirements.txt
    ```

## Uso

Para usar a CLI, navegue até o diretório `workshop` e execute o script `main.py` com o comando desejado.

### Comandos

- `drop_notes`: Remove a coluna 'notes' do DataFrame.
- `select_high_ratings`: Seleciona linhas onde a coluna 'rating' é 90 ou superior.
- `drop_and_one_hot_encode_red_wine`: Realiza codificação one-hot para 'Red Wine' e remove a coluna 'variety'.
- `remove_newlines_carriage_returns`: Remove quebras de linha e retornos de carro das colunas de texto.
- `convert_ratings_to_int`: Converte a coluna 'rating' de float para inteiro.

### Exemplos

1. Remover a coluna 'notes':
    ```sh
    python main.py drop_notes
    ```

2. Selecionar linhas com classificações altas:
    ```sh
    python main.py select_high_ratings
    ```

3. Codificação one-hot para 'Red Wine' e remoção da coluna 'variety':
    ```sh
    python main.py drop_and_one_hot_encode_red_wine
    ```

4. Remover quebras de linha e retornos de carro de colunas de string:
    ```sh
    python main.py remove_newlines_carriage_returns
    ```

5. Converter coluna 'rating' para inteiro:
    ```sh
    python main.py convert_ratings_to_int
    ```

## Dados

Os dados usados neste projeto são armazenados em arquivos CSV localizados no diretório `workshop`. O arquivo principal é `train.csv`, que contém as seguintes colunas:

- `notes`: Notas de texto sobre os dados.
- `ratings`: Classificações numéricas para os dados.
- `variety`: A variedade dos dados (por exemplo, 'Red Wine').

Os dados transformados são salvos em `transformed_train.csv` após a aplicação dos comandos da CLI.

## Contribuindo

Contribuições são bem-vindas! Por favor, siga estes passos para contribuir:

1. Faça um fork do repositório.
2. Crie uma nova branch (`git checkout -b feature-branch`).
3. Faça suas alterações.
4. Commit suas alterações (`git commit -m 'Add new feature'`).
5. Envie para a branch (`git push origin feature-branch`).
6. Abra um pull request.

## Licença

Este projeto está licenciado sob a Licença MIT. Veja o arquivo [LICENSE](../LICENSE) para detalhes.
```

</details>

### Desafio Bônus 3 - Automatizar a transformação de dados

Progresso: [🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢🟢] 12/12 (100%) 🎉  
Opcional: [🚀 Turbo Boost! (1/2) 33%]  
Opcional: [🌟 Pontos Extras! (2/2) 66%]  
Opcional: [🏆 Tripla Ameaça! (2/2) 100%]  

- Crie um novo arquivo chamado `transform-data.yaml` no diretório `.github/workflows/`.
- Use o chat do GitHub Copilot com o prefixo `@workspace` para criar uma GitHub Action que transformará os dados sempre que um push ou pull request for feito no repositório.
- Abra um pull request para testar a ação. Se ocorrerem erros, use o chat do GitHub Copilot para ajudá-lo a corrigi-los.

<details>
<summary>Cheatsheet</summary>

#### Prompt

```shell
@workspace Gere uma GitHub action que transforma os dados em cada push e pull request
```

#### Saída esperada

```markdown
Para criar uma GitHub Action que transformará os dados usando sua CLI, você pode criar um arquivo de workflow no diretório `.github/workflows`. Aqui está um exemplo de um arquivo de workflow GitHub Action chamado `transform-data.yml`:

    ```yaml
    // Workflow omitido, já que este é o bônus final!
    ```

Este workflow irá:

* Disparar em pushes para a branch main e em acionamentos manuais.
* Fazer checkout do repositório.
* Configurar o Python.
* Instalar as dependências necessárias (neste caso, pandas).
* Executar a transformação de dados usando o comando `run_all` de sua CLI.
* Fazer upload dos dados transformados como um artefato.
```

</details>

## Limpeza

### 1. Exclua seu Codespace

⏳ **~1min**

Antes de excluir, se desejar, você pode enviar suas alterações ao seu repositório.

Acesse [https://github.com/codespaces](https://github.com/codespaces) e encontre seu Codespace em execução e exclua-o.

## Recursos adicionais

Se você quiser saber mais sobre o uso do GitHub Copilot, confira estes recursos:

* [Documentação do GitHub Copilot](https://docs.github.com/copilot)
* [Série de vídeos do VS Code: GitHub Copilot](https://www.youtube.com/playlist?list=PLj6YeMhvp2S7rQaCLRrMnzRdkNdKnMVwg)
* [Blog: Melhores práticas para prompts do Copilot](http://blog.pamelafox.org/2023/06/best-practices-for-prompting-github.html)

Confira também o [caminho de aprendizado GitHub Foundations](https://learn.microsoft.com/training/paths/github-foundations/) para mais recursos sobre GitHub e GitHub Copilot.
