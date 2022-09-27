<!-- Written with [StackEdit](https://stackedit.io/). -->

# Aplicação em Python para checar a conectividade de URLs

A aplicação apresentada neste repositório foi criada como parte das atividades do programa Lighthouse da Indicium e usou como base o exemplo existente no link a seguir:

https://realpython.com/site-connectivity-checker-python/

Foi seguido o passo a passo do tutorial no link para implementação de uma aplicação em python que receba uma ou mais URLs e cheque se há conectividade

## Características

- Implementada para ser usada em CLI
- Possibilidade de receber uma ou mais URLs no mesmo comando para testar
- Possibilidade de realizar consulta síncrona ou assíncrona
- Possibilidade de receber um arquivo com lista de URLs
- Resultados são salvos em arquivos .csv em cada consulta

## Estrutura de diretórios

```
URL_Checker/
│
├── urlchecker/
│   ├── __init__.py
│   ├── __main__.py
│   ├── checker.py
│   └── cli.py
│
├── results/
│
├── README.md
├── .gitignore.txt
└── requirements.txt

```

## Requisitos

É necessário uma máquina rodando uma versão atualizada do Python.
as bibliotecas necessárias estão listadas no arquivo requirements.txt

## Instruções de uso

para usar o aplicativo, basta seguir as seguintes instruções:
- Clone ou baixe o repositório para a máquina de destino;
- Abra um terminal na pasta URL_Checker
- Execute um dos seguintes comandos:

* para acessar o menu de ajuda da função :
```
python3 -m urlchecker -h
```

* para checar a conectividade de uma ou mais urls :
```
python3 -m urlchecker -u www.exemple.org www.exemple2.com
```

* para checar a conectividade de URLs armazenadas em forma de lista num arquivo :
```
python3 -m urlchecker -f /filepath/file.txt
```

* para checar a conectividade de URLs de forma assíncrona :
```
python3 -m urlchecker -f /filepath/file.txt -a
```

* para salvar o resultado em um arquivo .csv :
```
python3 -m urlchecker -f /filepath/file.txt -s
```
