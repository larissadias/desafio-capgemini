# 2ª Parte Desafio Capgemini (2021)
## Sistema de Gerenciamento de Anúncios

O Sistema de Gerenciamento de Anúncios permite a gestão de anúncios e o rastreio dos resultados de uma campanha nas redes sociais. O sistema permite o cadastro de anúncios recebendo como entrada os seguintes dados: nome do anúncio, cliente, data de início da campanha, data de término da campanha e o investimento diário em reais. A partir do cadastro, é possível gerar o relatório de cada um dos anúncios cadastrados contendo métricas importantes da campanha como o valor total investido e a quantidade máxima de visualizações, cliques e compartilhamentos que o anuncio obteve. O código do Sistema foi desenvolvido na linguagem [Python](https://www.python.org/downloads/) e o pacote [tkinter](https://docs.python.org/pt-br/3/library/tkinter.html#) foi usado para desenvolver sua interface gráfica, já que por ser nativo do Python não são necessárias instalações adicionais. Além disso, para criação e gerenciamento do banco de dados do sistema foi utilizado o [SQLite](https://www.sqlite.org/index.html).

### Estrutura do Código
- `gerenciamento_de_anuncios.py`: é o arquivo principal do sistema de gerenciamento, sendo responsável por interligar a interface gráfica e o banco de dados.
- `interface.py`: é o arquivo que realiza a importação da biblioteca tkinter e define a interface gráfica do sistema.
- `bancodedados.py`: é o arquivo responsável pela persistência de dados utilizando o SQLite. Nele é desenvolvido o CRUD (as quatro operações básicas de armazenamento persistente: Create, Read, Update e Delete), e também é criado o bando de dados em si chamado `anuncios.db`.

### Ferramentas Utilizadas

- [Python](https://www.python.org/downloads/) (v3.8.5)
- [tkinter](https://docs.python.org/pt-br/3/library/tkinter.html#) (v8.6)
- [SQLite](https://www.sqlite.org/index.html) (v3.33.0)
- Testado no sistema operacional :penguin:[Ubuntu](https://ubuntu.com/download) 20.04.2

## Instalação das Dependências no Linux

Primeiramente, verifique se já tem o Python instalado, se você usa GNU/Linux, provavelmente já possui alguma versão do Python instalada por padrão. Para conferir, digite no terminal:
```bash
python --version
```
Se a saída do comando acima for `-bash: python: command not found`, que significa que o Python ainda não está instalado, ou se a saída do comando for que você tem instalado apenas o Python2, execute no terminal o seguinte comando que irá instalar o Python3 e o seu  gerenciador de pacotes `pip`. 
```bash
sudo apt-get install python3 python3-pip
```
Os módulos Tkinter e SQLite3 normalmente não precisam de instalações adicionais, pois são incluídos por padrão na biblioteca do Python3. Porém, se por alguma razão a sua versão do Python3 não conter esses módulos, eles podem ser instalados com os comandos abaixo.
```bash
sudo apt-get install -y python3-tk
sudo apt install sqlite3
```
Para verificar a instalação dos módulos, os comandos abaixo podem ser executados no terminal e a saída deve ser a versão de cada um dos módulos instalados.
```bash
python3 -m tkinter
sqlite3 –version
```

### Instruções de Execução
O download do código do Sistema de Gerenciamento de Anúncios pode ser feito de duas maneiras, clicando no botão `code` da interface do repositório no Github e depois em `download ZIP` ou através do terminal usando o seguinte comando do [git](https://git-scm.com/):
```bash
git clone https://github.com/larissadias/desafio-capgemini.git
```

Para executar o sistema pelo terminal apenas é preciso mudar para o diretório em seu computador que contém os 3 arquivos de source do sistema e então executar o seguinte comando dentro do diretório:
```bash
python3 gerenciamento_de_anuncios.py
```
![alt text](https://github.com/larissadias/desafio-capgemini/blob/c3065100ec78b19a853201b83f0ecf3b824348d0/parte-2/doc/compilar.gif)


### Instruções de Utilização
Para cadastrar um novo anúncio no sistema de gerenciamento é preciso primeiro que você preencha os seguintes campos de informação sobre o anúncio: nome do anúncio, cliente, data de ínício da campanha, data de término da campanha e o valor em reais investido por dia. Depois dos campos preenchidos, clique no botão `Cadastrar anúncio` e as informações do anúncio serão persistidas no banco de dados. Atente-se, por favor, aos campos referentes às datas(data de ínício e data de término), pois eles necessitam ser preenchidos no formado `dias-mês-ano`, separados por um hífen `-`, como no exemplo abaixo:

![alt text](https://github.com/larissadias/desafio-capgemini/blob/c3065100ec78b19a853201b83f0ecf3b824348d0/parte-2/doc/cadastrar.gif)


Se for necessário atualizar alguma informação de um anúncio já cadastrado no banco de dados do sistema, é necessário apenas que você selecione o anúncio a ser atualizado clicando na linha correpondente a ele na interface gráfica do sistema, mudar a informação do campo desejado e por fim clicar no botão `Atualizar cadastro do anúncio selecinado` e as mudanças realizadas serão salvas no banco de dados. 

![alt text](https://github.com/larissadias/desafio-capgemini/blob/c3065100ec78b19a853201b83f0ecf3b824348d0/parte-2/doc/atualizar.gif)


Para gerar o relatório contendo as projeções dos resultados de uma campanha, selecione clicando com o mouse no anúncio desejado e então clique no botão `Gerar relatório do anúncio`. Uma nova janela se abrirá contendo o relatório do anúncio com as seguintes informacões: nome do anúncio, nome do cliente, valor total investido na campanha e as projeções das quantidades máximas de visualizações, cliques e compartilhamentos que o anúncio obteve. 

![alt text](https://github.com/larissadias/desafio-capgemini/blob/c3065100ec78b19a853201b83f0ecf3b824348d0/parte-2/doc/relatorio.gif)


Se você deseja visualizar todos os anúncios cadastrados no banco de dados do sistema, basta clicar no botão `Ver todos os anúncios cadastrados`.

![alt text](https://github.com/larissadias/desafio-capgemini/blob/c3065100ec78b19a853201b83f0ecf3b824348d0/parte-2/doc/ver_todos.gif)


Para deletar um dos anúncios cadastrados no banco de dados do sistema, primeiro selecione o anúncio a ser deletado clicando nele com o mouse e então clique no botão `Deletar anúncio selecionado`.
![alt text](https://github.com/larissadias/desafio-capgemini/blob/c3065100ec78b19a853201b83f0ecf3b824348d0/parte-2/doc/deletar.gif)


Ana Larissa Dias - larissa.engcomp@gmail.com
