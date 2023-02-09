import requests
from  zipfile import ZipFile
import os
#import pandas as pd
import csv
import string


caminho_arquivo = 'D://Arquivos//'
caminho_api_download = 'https://api.worldbank.org/v2/en/indicator/NY.GDP.MKTP.KD.ZG?downloadformat=csv'

def baixar_arquivo(url, endereco):
    resposta = requests.get(url, stream=True)  # baixar um partes e vai salvando no disco
    if resposta.status_code == requests.codes.OK:
        with open(endereco,'wb') as novo_arquivo:
            for parte in resposta.iter_content(chunk_size=256):
                novo_arquivo.write(parte)

        print('Downloing finalizado: Salvo em: {}'.format(endereco))
    else:
        resposta.raise_for_status()

def descompactar_arquivo(caminho_arquivo):
    with ZipFile(caminho_arquivo+ str('arquivo.zip'),'r') as zip_object:
        zip_object.extractall(path=caminho_arquivo)
   #print(zip_object.namelist())

def deleta_arquivo_zip(caminho_arquivo):
    dir = os.listdir(caminho_arquivo)
    #print(dir)
    for file in dir:
        print(file)
        if file == 'arquivo.zip':
            os.remove(caminho_arquivo+file)

def trata_linhas(caminho_arquivo):
    dir = os.listdir(caminho_arquivo)
    dir.remove('APROCESSAR')
    dir.remove('PROCESSADOS')
    for file in dir:
        with open(caminho_arquivo+file, newline='',encoding='utf-8') as in_file:
            filtered = (line.replace('\n', '') for line in in_file)  #trata a quebra de linha
            with open(caminho_arquivo+str('new_')+file, 'w', newline='',encoding='utf-8') as out_file:
                writer = csv.writer(out_file, delimiter=';', lineterminator='\n')
                for row in csv.reader(filtered):
                    if any(field.strip() for field in row): #retira as linhas em branco
                        if 'Data Source' not in row[0] and 'Last Update' not in row[0]:
                            row2 = row[:-1] 
                            writer.writerow(row2)
if __name__ == '__main__':
    baixar_arquivo(caminho_api_download,caminho_arquivo + str('arquivo.zip'))
    descompactar_arquivo(caminho_arquivo)
    deleta_arquivo_zip(caminho_arquivo)
    trata_linhas(caminho_arquivo)