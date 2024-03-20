#!/usr/bin/python
# -*- coding: utf-8 -*-

import subprocess
import time


nome_arquivo = "captura_trafego_{0}.pcap".format(time.strftime("%Y%m%d-%H%M%S"))

ip_servico_nome = "192.168.0.2"
porta_servico_nome = "53"


print("Servico de Nome:")
print("IP: {0}, Porta: {1}".format(ip_servico_nome, porta_servico_nome))

print("\nServico Web:")
ip_servico_web = "192.168.0.1"
porta_servico_web = "80"
print("IP: {0}, Porta: {1}".format(ip_servico_web, porta_servico_web))


comando_captura = "tcpdump -i any -w {0}".format(nome_arquivo)
processo_captura = subprocess.Popen(comando_captura, shell=True)


comando_ping = "ping -c 4 {0}".format(ip_servico_nome)  
saida_ping = subprocess.call(comando_ping, shell=True)
if saida_ping == 0:
    print("\nHost online.")
else:
    print("\nHost offline.")


comando_teste_web = "curl -I {0}:{1}".format(ip_servico_web, porta_servico_web)
saida_teste_web = subprocess.call(comando_teste_web, shell=True)
if saida_teste_web == 0:
    print("Servico Web respondendo corretamente.")
else:
    print("Erro ao acessar o Servico Web.")


time.sleep(10) 
processo_captura.terminate()
print("\nCaptura de trafego finalizada. Arquivo: {0}".format(nome_arquivo))
