<h1 align=center>Instalando o Pyenv</h1>

<p align="justify">Este breve tutorial aborda a instalação do Pyenv para gerenciamento 
mais eficiente de diferentes versões Python. Aborda também o básico no uso de Ambientes Virtuais</p>

<b>Projeto Pyenv:</b>

https://github.com/pyenv/pyenv

<b>Projeto cefpython3:</b>

https://github.com/cztomczak/cefpython

Muitas vezes precisamos trabalhar com multiplas versões python e bibliotecas, que tal buscar
uma forma organizada de realizar essa tarefa?
Visite o site dos projetos acima e leia a documentação com atenção.

Começaremos com a instalação do <b>curl</b> e <b>git</b>. No meu caso como estou usando o <b>Debian 12.0.5</b> 

```bash
$ sudo apt install curl git
```

Agora execute no seu terminal com o usuário comum <b>(nada de usar conta ROOT ou SUDO)</b>:

```bash
$ curl https://pyenv.run | bash
```

Ao final da instalação seré exibida uma saída solicitando que você edite seu bashrc.
Por precaução efetue o backup do mesmo antes de qualquer alteração.

```bash
$ cp ~/.bashrc ~/.bashrc.backup
```

```bash
$ nano ~/.bashrc
```

Adicione ao final do arquivo:
```
export PYENV_ROOT="$HOME/.pyenv"
[[ -d $PYENV_ROOT/bin ]] && export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```
Para efetivar as alterações abra e feche seu terminal ou execute:

```bash
$ source ~/.bashrc
```

<b>Pronto a partir daqui você já pode usar o pyenv!</b>

Começe listando as versões do Python disponíveis para instalação:

Execute no terminal:

```bash
$ pyenv install -l
```

Você verá uma lista de versões disponíveis

<b>Antes de instalar uma nova versão do Python você precisa de algumas dependências:</b>

```bash
$ sudo apt install build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev \
libncursesw5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev
```

Vamos instalar a versão do Python 3.7.17:

```bash
$ pyenv install 3.7.17
```

Agora aguarde um pouco <b>(tenha um pouco de paciência, será feito o download e build da versão escolhida, isso pode demorar um pouco)</b>

<b>Se tudo deu certo ao final você obterá uma saída de algo como:</b>

``
Installed Python-3.7.17 to /home/leonardo/.pyenv/versions/3.7.17
``

Vamos organizar um pouco as coisas, começe criando uma pasta "estudo-pyenv-virtenv"
eu já estou no terminal então faço:

```bash
$ mkdir estudo-pyenv-virtenv
```

Depois:

```bash
$ cd estudo-pyenv-virtenv
```

Agora vamos ver as versões de Python que podemos utilizar, para isso digite:

```bash
$ pyenv versions
```

No meu caso já tenho mais de uma versão instalada:

```
* system (set by /home/leonardo/.pyenv/version) 
  3.7.17
  3.12.2
```

Agora vamos setar a versão que desejamos usar localmente com:

```bash
$ pyenv local 3.7.17
```

Como curiosidade execute:

```bash
$ ls -a   (Para exibir arquivos ocultos)
```
Repare que foi criado um arquivo "python-version"

vamos ver o que há nesse arquivo:

```bash
$ cat .python-version
```

A saída será a versão do Python que você definiu com o pyenv local.

Execute dentro da pasta que criamos (estudo-pyenv-virtenv) :

```bash
$ pyenv versions
```

Agora sua saída será:

```
system
  
* 3.7.17 (set by /home/leonardo/estudo-pyenv/.python-version)
  
3.12.2
``` 

Repare que o <b>*(asterisco)</b> moveu para a versão que você selecionou.

Aqui o pyenv básicamente te passa a seguinte informação:

Você tem 3 versões do python instaladas<p> 
( a nativa do sistema, 3.7 e 3.12).<p>
<b>Atualemente o que você executar nesse local usuará a versão 3.7.</b>

Vamos agora criar um ambiente virtual e executar um código simples de exempo usando a biblioteca
cefpython3.

<h2 align=center>Criando Ambientes Virtuais</h2>

Crie um novo ambiente virtual dentro da pasta estudo-python

```bash
$ python -m venv amb-virtual
```

Vamos ativar esse ambiente virtual recém criado:

```bash
$ source amb-virtual/bin/activate
```

Repare que o shell mudou agora ele fica assim:

``(amb-virtual) leonardo@localhost:~/estudo-pyenv$``

Isso indica que você já está usando um ambiente virtual

Vamos aproveitar para atualizar o pip

Execute:

```bash
$ pip install --upgrade pip
```

Agora vamos instalar a biblioteca:

```bash
$ pip install cefpython3==66.0
```

Agora copie o arquivo <b>teste-cefpython3.py</b> para dentro da pasta estudo-pyenv.

Vamos rodar esse exemplo para testar se deu tudo certo

Execute:

```bash
$ python teste-cefpython3.py
```

Se tudo foi feito corretamente você terá uma saída semelhante em seu terminal:

```
teste-cefpython3.py] CEF Python 66.0
[teste-cefpython3.py] Chromium 66.0.3359.181
[teste-cefpython3.py] CEF 3.3359.1774.gd49d25f
[teste-cefpython3.py] Python 3.7.17 64bit

DevTools listening on ws://127.0.0.1:61995/devtools/browser/2e57b811-2ca1-4997-902d-7e81d1fa63de
```
Será também aberta uma tela do chromium com o DuckDuckGo aberto e título da janela "Ola Mundo!" conforme imagem abaixo

![Tela cefpython3](/tela_cefpython3.png)

Este tutorial foi elaborado por <b>Leonardo Bruno</b><p>
Seu uso e reprodução é livre com a referência ao repositório original.<p>
Encontrou algum erro? Quer sugerir alguma alteração?<p>
<b>202301011744@alunos.estacio.br</b>
