#!/usr/bin/python
#-*-coding: utf-8-*-

import subprocess
import time

# Definindo o nome do arquivo de captura
nome_arquivo = "captura_trafego_{0}.pcap".format(time.strftime("%Y%m%d-%H%M%S"))

# a. Informando na tela qual o IP e porta dos serviços de nome e web
print("Servico de Nome:")
nome_host = "exemplo.psi.br"
comando_nome = "nslookup {0}".format(nome_host)
saida_nome = subprocess.check_output(comando_nome, shell=True)
print(saida_nome)

print("\nServico Web:")
ip_servico_web = "192.168.0.1"
porta_servico_web = "80"
print("IP: {0}, Porta: {1}".format(ip_servico_web, porta_servico_web))

# b. Capturando o trafego gerado quando testar se os serviços estão funcionando corretamente
comando_captura = "tcpdump -i any -w {0}".format(nome_arquivo)
processo_captura = subprocess.Popen(comando_captura, shell=True)

# c. Testando se o host está online
comando_ping = "ping -c 4 {0}".format(nome_host)
saida_ping = subprocess.call(comando_ping, shell=True)
if saida_ping == 0:
    print("\nHost online.")
else:
    print("\nHost offline.")

# d. Testando se o serviço está respondendo corretamente
comando_teste_web = "curl -I {0}:{1}".format(ip_servico_web, porta_servico_web)
saida_teste_web = subprocess.call(comando_teste_web, shell=True)
if saida_teste_web == 0:
    print("Servico Web respondendo corretamente.")
else:
    print("Erro ao acessar o Servico Web.")

# e. Terminando a captura de trafego
time.sleep(10)  # Espera 10 segundos para capturar o trafego
processo_captura.terminate()
print("\nCaptura de trafego finalizada. Arquivo: {0}".format(nome_arquivo))
