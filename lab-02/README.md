# Exercício 1.1 em duplas

#### Participantes: Vinícius Borges da Silva e Eduardo Vanildo da Silva

### Importante!

Ambos da dupla executaram as 2 funções, tanto enviar quanto receber, para fins de organização do conteúdo no nosso material, por isso o documento está se referindo de forma genérica como "outro colega da dupla".

## Parte 1

### Passos

Primeiro é importante separarmos todas as partes, ficando desta forma:

1. Baixar PDF
1. Gerar chave simétrica de 256 bits
1. Cifrar PDF com essa chave
1. Enviar arquivo para o outro colega da dupla
1. O colega deve usar a chave simétrica
1. O colega deve verificar se o hash dos arquivos batem


### O que fizemos

Depois de baixar o PDF enviado pelo professor colocamos ele dentro da pasta chamada "exercicio1.1", e geramos uma chave simétrica de 256 bits (32 bytes).

```
openssl rand -base64 32 > chave.txt
```
Geramos uma chave simétrica e enviamos ela para um arquivo chamado "chave.txt", e agora precisamos cifrar o PDF com esta chave.

```
openssl enc -aes-256-cbc -in seg-criptografia.pdf -out arquivo.cifrado -iter 1000 -pass file:chave.txt
```

Está sendo declarado o arquivo a ser cifrado em `-in seg-criptografia.pdf` e o arquivo final em `-out arquivo.cifrado` e passando o arquivo que contém a chave em `pass file:chave.txt`.

Agora para enviar os arquivos nós utilizamos o WhatsApp que possui criptografia de ponta a ponta, garantindo integrida e confidencialidade para nossos arquivos. Para isso criamos uma pasta "envio" e compactamos ela em ".zip".

Adicionamos esse arquivo recebido na pasta "recebido", a partir dessa pasta, descompactamos o arquivo "envio.zip" e desciframos usando a chave simétrica da seguinte forma:

```
openssl enc -d -aes-256-cbc -in arquivo.cifrado -out slides.pdf -iter 1000 -pass file:chave.txt
```

Com o `-d` estamos descifrando o `arquivo.cifrado` e queremos que o arquivo destino seja `slides.pdf`, utilizando a `chave.txt`.

Para verificarmos o hash, utilizamos o comando `md5sum *` desta maneira podemos verificar se `slides.pdf` e `seg-criptografia.pdf` possuem o mesmo hash, garantindo que o conteúdo não se perdeu no caminho.

## Parte 2