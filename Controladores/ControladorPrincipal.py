from Entidades.Pessoa import *


class ControladorPrincipal:
    # cabeçalhos substituir pelo enum
    nomes_campos = ['Id', 'Nome Completo', 'Quantidade de Cupons']

    def __init__(self):

        pass

    def gerar_cupons(self, link_arquivo):
        validade = self.validar_arquivo(link_arquivo)
        self.verificar_integridade(link_arquivo)

    def validar_arquivo(self, link_arquivo):  #  Valida se o arquivo está padrão de três colunas e com todas preenchidas
        file = self.__abri_arquivo(link_arquivo)
        erros_encontrados = ''  # Inicia variável de erros

        for line in file:  # varre cada linha do arquivo
            campos = self.__dividir_linha_em_campos(line)
            if len(campos) != 3:  # verifica se possui 3 colunas
                erros_encontrados = 'Linha possui mais que 3 campos.'
            posica_campo = 0  # Incia na primeira posição ID
            
            for campo in campos:  # varre os campos da linha, id, nome e cupons
                if campo is '':  # verifica se o campo em branco
                    nome_campo = self.nomes_campos[posica_campo]  # Pega o nome do campo que está em branco
                    if erros_encontrados is '':  # Verfica se já possui alguma mensagem de erro anterior
                        erros_encontrados = '{} está em branco.'.format(nome_campo)   # Se não possui nenhum erro nesta linha apenas monta mensagem de erro
                    else:
                        erros_encontrados = '{},{} está em branco'.format(erros_encontrados, nome_campo)  # se a linha possui mais algum erro concatena com anterior
                posica_campo += 1  # Qual campo da linha está sendo verificado (ID, nome, Cupons)
            posica_campo =0  # Após verificar todos o campos da linha recomeça a contagem para uma nova linha
            erro = '{}{}{}'.format(line.replace('\n', ';'), erros_encontrados, '\n')  # formata a mensagem de erro ferente a linha
            erros_encontrados = ''  # Limpa erros da linha anterior  # limpa a mensagem de erro paar começar  a verificar uma nova linha
            self.__log_erros(erro)  # escreve o arquivo de erro os erros encontrados
        if erros_encontrados is '':
            return True
        else:
            return False

    def verificar_integridade(self, link_arquivo):
        file = self.__abri_arquivo(link_arquivo)

        dicionario_ids = {}  # dicionario ID com CHAVE e uma COLEÇAO com as LINHAS QUE CONTEM O MESMO ID
        dicionario_nomes = {}  # dicionario ID com NOME e uma COLEÇAO com as LINHAS QUE CONTEM O MESMO ID
        dicionario_cupons_not_number = {}  # Armazena valres como TRUE e ALFANUMERICOS como false
        contador_linhas = 2  # Cabeçalho primeira linha, por isso começa no 2

        for line in file:
            campos = self.__dividir_linha_em_campos(line)
            idP = campos[0]
            nomeP = campos[1]

            dicionario_ids = self.__atualizar_dicionario_linhas_repetidas(dicionario_ids, idP, contador_linhas)
            dicionario_nomes = self.__atualizar_dicionario_linhas_repetidas(dicionario_nomes, nomeP, contador_linhas)

            contador_linhas += 1

        for id, linhas in dicionario_ids.items():
            print(id, linhas)

        for id, linhas in dicionario_nomes.items():
            print(id, linhas)

    def __atualizar_dicionario_linhas_repetidas(self, dicionario, chave,
                                                numero_linha):  # diciona o numero da linha no dicionario
        colecao_linhas = dicionario.get(chave)
        if colecao_linhas is None:
            dicionario[chave] = numero_linha
        else:
            dicionario[chave] = '{},{}'.format(colecao_linhas, numero_linha)
        return dicionario

    def __dividir_linha_em_campos(self, linha):
        campos = linha.replace('\n', '').split(';')  # Divide a Linha em partes de acordo com ";"
        return campos

    def __abri_arquivo(self, link_arquivo):
        file = open(link_arquivo, "r", encoding="ISO-8859-1")  # abre o arquivo para leitura
        reader = file.readline()  # leitura do cabeçalho
        self.__limpar_arquivo_erros()  # Limpra o arquivo de erros
        self.__log_erros(reader.replace('\n', ';Erros Encontrados\n'))  # Cria o cabeçaçho do arquivo de erros
        return file

    def __log_erros(self, erros_encontrados):  # faz a escrita no arquivo
        arquivo_erros = open('Erros.csv', "a", encoding="utf8")
        arquivo_erros.write(erros_encontrados)
        arquivo_erros.close()

    def __limpar_arquivo_erros(self):  # limpa arquvo
        arquivo_erros = open('Erros.csv', "w")
        arquivo_erros.close()
