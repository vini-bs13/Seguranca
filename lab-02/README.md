# Exercício 1.1 em duplas

#### Participantes: Vinícius Borges da Silva e Eduardo Vanildo da Silva

### Importante!

Ambos da dupla executaram as 2 funções, tanto enviar quanto receber, para fins de organização do conteúdo no nosso material, por isso o documento está se referindo de forma genérica como "outro colega da dupla".

Na parte 2, na organização dos arquivos possivelmente não ficou claro a separação das chaves públicas e privadas, esclarecendo:

A pessoa 1 (que enviou os arquivos) possui uma chave privada e uma chave pública, para gerar a assinatura digital ela utilizou a sua chave privada e para cifrar utilizou a chave pública da pessoa 2 (que recebeu os arquivos).
Na verificação/decifração, a pessoa 2 utilizou a sua chave privada para decifrar o conteúdo do arquivo cifrado, para confirmar a integridade (conteúdo não foi alterado no caminho), e para confirmar a assinatura digital, a pessoa 2 utilizou a chave pública da pessoa 1, assegurando que quem enviou o arquivo foi realmente a pessoa 1.

## Parte 1

### Passos

Primeiro é importante separarmos todas as partes, ficando desta forma:

1. Baixar PDF
1. Gerar chave simétrica de 256 bits
1. Cifrar PDF com essa chave
1. Enviar arquivo para o outro colega da dupla
1. O colega deve usar a chave simétrica para decifrar
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

Adicionamos esse arquivo recebido na pasta "recebido", a partir dessa pasta, descompactamos o arquivo "envio.zip" e deciframos usando a chave simétrica da seguinte forma:

```
openssl enc -d -aes-256-cbc -in arquivo.cifrado -out slides.pdf -iter 1000 -pass file:chave.txt
```

Com o `-d` estamos decifrando o `arquivo.cifrado` e queremos que o arquivo destino seja `slides.pdf`, utilizando a `chave.txt`.

Para verificarmos o hash, utilizamos o comando `md5sum *` desta maneira podemos verificar se `slides.pdf` e `seg-criptografia.pdf` possuem o mesmo hash, garantindo que o conteúdo não se perdeu no caminho.

## Parte 2

### Passos

Seguindo a mesma lógica da primeira parte:

1. Baixar PDF
1. Gerar chave simétrica
1. Gerar chave pública/privada de criptografia
1. Assinar PDF com chave privada
1. Cifrar PDF com a chave simétrica
1. Cifrar chave simétrica com a chave pública
1. Enviar arquivo para o outro colega da dupla
1. O colega deve decifrar a chave simétrica com a privada
1. O colega deve decifrar a chave simétrica
1. O colega precisa verificar a integridade
1. O colega necessita confirmar se a assinatura digital é valida

### O que fizemos

O primeiro comando gera uma chave privada RSA de 2048 bits.

```
openssl genrsa -out chave.priv 2048
```

O segundo comando utiliza a chave privada para gerar a chave pública. A chave pública foi compartilhada via WhatsApp, como no exercício anterior.

```
openssl rsa -in chave.priv -pubout -out chave.pub
```

Utilizando a chave simétrica gerada no exercício anterior, foi realizada a cifragem dos slides.

```
openssl enc -aes-256-cbc -in seg-criptografia.pdf -out arquivo.cifrado -iter 1000 -pass file:chave.txt
```

Ciframos a chave simétrica utilizando a chave pública. Dessa forma, somente quem possui a chave privada poderá recuperar a chave simétrica.

```
openssl pkeyutl -encrypt -pubin -inkey chave.pub -in chave.txt -out chave.cifrada
```

Geramos uma assinatura digital do PDF utilizando a chave privada. A assinatura será utilizada para verificar a integridade e autenticidade dos slides da aula.

```
openssl dgst -sha256 -sign chave.priv -out assinatura.sig seg-criptografia.pdf
```

O colega utiliza a chave privada para decifrar `chave.cifrada` e recuperar a chave simétrica original.

```
openssl pkeyutl -decrypt -inkey chave.priv -in chave.cifrada -out chave.txt
```

Utilizamos a chave simétrica decrifrada para decifrar o arquivo `arquivo.cifrado`, gerando novamente o PDF original.

```
openssl enc -d -aes-256-cbc -in arquivo.cifrado -out slides.pdf -iter 1000 -pass file:chave.txt
```

Para verificar se o arquivo decifrado é igual ao arquivo original, comparamos o hash dos dois arquivos. Os valores foram iguais!

```
md5sum slides.pdf
md5sum seg-criptografia.pdf
```

Utilizamos a chave pública para verificar a assinatura digital. A assinatura é válida quando o conteúdo do arquivo não foi alterado e foi assinado pela chave privada correta.

```
openssl dgst -sha256 -verify chave.pub -signature assinatura.sig slides.pdf
```

A verificação da assinatura foi realizada com sucesso, conforme o retorno:

```
Verified OK
```