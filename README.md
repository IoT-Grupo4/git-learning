# Aprendendo Git

----

## Buscando ajuda

O git possui uma documentação bem extensa que vem instalada junto com ele. Para todo comando, haverá uma página de ajuda, a qual pode ser acessada, via terminal da seguinte forma:

	git help [comando]

Caso não especifique nenhum comando, será apresentado uma lista de possíveis comandos e um breve resumo de cada um deles.

-----

## Configurando ambiente

- [Linux](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git)
- [MacOS](https://git-scm.com/download/mac)
- [Windows](https://git-for-windows.github.io/)

----

## Iniciando o trabalho

#### Iniciando um repositório do zero:

	git init
	git remote add <nome do remote> <url da plataforma>

#### Clonando um repositório:

	git clone <url do repositório>

Caso venha a fazer o clone de um repositório privado (o que não deve ser o nosso caso) e não tenha uma chave SSH, será necessário passar seu usuário junto com o link:

	git clone username@host:<url do repositório>

-----

## Adicionando conteúdo



![trees](http://rogerdudler.github.io/git-guide/img/trees.png)

-----

#### Alterando conteúdo local


	git add <nome do(s) arquivo(s) ou diretório(s)>
	git commit [-m <texto do commit>]

#### Sincronizando o conteúdo local com o da nuvem

Baixe as modificações na nuvem e corrija as diferenças

	git pull [-r] [<nome do remote> <nome da branch>]

Suba para a nuvem suas alterações

	git push [<nome do remote> <nome da branch>]

----

## Trabalhando com múltiplas frentes de trabalho

![branchs](http://rogerdudler.github.io/git-guide/img/branches.png)

----

#### Criando uma nova branch

	git branch <nome da nova branch>

#### Trocando de *branch*

	git checkout <nome da branch>

#### Criando uma nova *branch* e trocando para ela

	git checkout -b <nome da nova branch>

----

#### Atualizando a **branch 1** com as modificações da **branch 2**

Vá para a **branch 1**:

	git checkout <branch 1>

Baixe as modificações da **branch 2**:

	git pull [-r] <nome do remote> <branch 2>

----

#### Mesclando a **branch 1** na *branch 2**

Vá para a **branch 2**:

	git checkout <branch 2>

Mescle as branchs:

	git merge <branch 1>


---- 

#### Deletando uma branch

	git branch <-D | -d | --delete> <nome da branch>

----

## No que o git pode ser útil para nós?

----

#### Histórico de modificações

	git log

#### Desfazendo modificações

	git checkout <arquivo(s) ou pasta(s) rastreados que sofreram alterações>

#### Recuperando versões antigas do código

- Utilize `git log` para localizar a versão que deseja restaurar
- Copie ao menos os 7 primeiros dígitos da *hash* do commit desejado
- Mude para a versão desejada com:

	`git checkout <hash do commit>`

----

#### Recuperando versões antigas do código (versão 2)

É possível criar `tags` para um determinado estado do código, com:

	git tag <nome da tag>

Assim, podemos definir estados específicos do código, com **Versão x** ou **Release a.b-c**. De forma análoga, podemos mudar para a versão do código recebeu a *tag* com:

	git checkout <tag>


Imagens de [Roger Dudler](http://rogerdudler.github.io/git-guide/)