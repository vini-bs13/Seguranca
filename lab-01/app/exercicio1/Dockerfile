# FROM ubuntu:latest - É ruim para manter ativo, logo que ele atualiza constantemente

FROM ubuntu:26.04


# LTS 2 anos - sempre em Abril
# 6 meses - abril ou outubro


WORKDIR /app

RUN apt-get update && \
   apt-get install -y figlet nyancat toilet && \
   rm -rf /var/lib/apt/lists/*

# RUN apt-get update - É boa prática usar o menor número de comandos possíveis, o modelo acima é melhor
# RUN apt-get install -y figlet nyancat


COPY mensagem.txt /app/exercicio1


# CMD [ "nyancat" ]
CMD ["toilet", "-f", "smmono9", "SEGURANCA", "--filter", "gay"]
