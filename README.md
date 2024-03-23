# Este breve tutorial aborda a instalação do Pyenv e criação de Ambientes Virtuais.
# Foi elaborado por Leonardo Bruno.
# Está disponível nesse repositório um código de exemplo para testar o ambiente criado.
# Para mais informações visite o github dos criadores dos projetos:
# 
# Projeto Pyenv
# https://github.com/pyenv/pyenv
#
# Projeto cefpython3
# https://github.com/cztomczak/cefpython

# Instalando o Pyenv

E se você precisar usar diversas versões do Python em diferentes projetos?
Como manter as diversas instalações Python organizadas e acessíveis de maneira fácil?

Dê uma olhada no projeto:

https://github.com/pyenv/pyenv

Leia a documentação do projeto, observe os requisitos e vamos por a mão na massa para efetuar a instalação:

Primeiramente instale o curl e git. No meu caso como estou usando o Debian 12.0.5 
basta efetuar

sudo apt install curl git

Agora execute no seu terminal com o usuário comum (nada de usar conta ROOT ou SUDO):

curl https://pyenv.run | bash

O comando exibirá uma saída solicitando que você edite seu bashrc.

para facilitar execute abaixo (se desejar pode editar manualmente também):

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init -)"' >> ~/.bashrc

Para efetivar as alterações abra e feche seu terminal ou execute:

source ~/.bashrc

Pronto a partir daqui você já pode usar o pyenv:

Começe listando as versões do Python disponíveis para instalação:

Execute no terminal:

pyenv install -l

Você verá uma lista de versões disponíveis

(Para evitar a rolagem da tela use  "pyenv install -l | more" )

# Antes de instalar uma nova versão do Python você precisa de algumas dependências:

sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev

Vamos instalar a versão do Python 3.7.17

pyenv install 3.7.17

Agora aguarde um pouco (tenha um pouco de paciência, será feito o download e build da versão escolhida)

Se tudo deu certo ao final você obterá uma saída de algo como:

"Installed Python-3.7.17 to /home/leonardo/.pyenv/versions/3.7.17"

Vamos organizar um pouco as coisas, começe criando uma pasta "estudo-pyenv"

eu já estou no terminal então faço:

mkdir estudo-pyenv

Depois:

cd estudo-pyenv

Agora vamos ver as versões de Python que podemos utilizar, para isso digite:

pyenv versions

No meu caso já tenho mais de uma versão instalada:

eonardo@localhost:~/estudo-pyenv$ pyenv versions
* system (set by /home/leonardo/.pyenv/version)
  3.7.17
  3.12.2
leonardo@localhost:~/estudo-pyenv$

Agora vamos setar a versão que desejamos usar localmente com

pyenv local 3.7.17

Como curiosidade execute:

ls -a   (Para exibir arquivos ocultos)
Repare que foi criado um arquivo "python-version"

vamos ver o que há nesse arquivo:

cat .python-version

A saída será a versão do Python que você definiu com o pyenv local.

Execute dentro da pasta que criamos (estudo-pyenv) :

pyenv versions

Agora sua saída será:

leonardo@localhost:~/estudo-pyenv$ pyenv versions
  system
* 3.7.17 (set by /home/leonardo/estudo-pyenv/.python-version)
  3.12.2
leonardo@localhost:~/estudo-pyenv$ 

Repare que o *(Asterisco) moveu para a versão que você selecionou.

Aqui o pyenv básicamente te passa a seguinte informação:

Você tem 3 versões do python instaladas ( a nativa do sistema, 3.7 e 3.12). 
Atualemnte o que você executar nesse local usuará a versão 3.7.

Vamos agora criar um ambiente virtual e executar um código simples de exempo usando a biblioteca
cefpython3.

# Crie um novo ambiente virtual dentro da pasta estudo-python

python -m venv amb-virtual

Vamos ativar esse ambiente virtual recém criado:

source amb-virtual/bin/activate

Repare que o shell mudou agora ele fica assim:

"(amb-virtual) leonardo@localhost:~/estudo-pyenv$"

Isso indica que você já está usando um ambiente virtual

Vamos aproveitar para atualizar o pip

Execute:

pip install --upgrade pip

Agora vamos instalar a biblioteca:

pip install cefpython3==66.0

Agora copie o arquivo teste-cefpython3.py para dentro da pasta estudo-pyenv.

Vamos rodar esse exemplo para testar se deu tudo certo

# Execute:

python teste-cefpython3.py

Se tudo foi feito corretamente você terá uma saída semelhante em seu terminal:

teste-cefpython3.py] CEF Python 66.0
[teste-cefpython3.py] Chromium 66.0.3359.181
[teste-cefpython3.py] CEF 3.3359.1774.gd49d25f
[teste-cefpython3.py] Python 3.7.17 64bit

DevTools listening on ws://127.0.0.1:61995/devtools/browser/2e57b811-2ca1-4997-902d-7e81d1fa63de

Será também aberta uma tela chromium com o google aberto e título da janela "Ola Mundo!"



















