
class ControladorPrincipal:
    # cabeçalhos substituir pelo enum
    nomes_campos = ['Id', 'Nome Completo', 'Quantidade de Cupons']

    def __init__(self):
        pass

    def gerar_cupons(self, link_arquivo):
        self.validar_arquivo(link_arquivo)
        self.verificar_integridade(link_arquivo)

    def validar_arquivo(self, link_arquivo):  #  Valida se o arquivo está padrão de três colunas e com todas preenchidas
        file = self.__abri_arquivo(link_arquivo)
        erros_encontrados = ''  # Inicia variável de erros

        for line in file:  # varre cada linha do arquivo
            campos = self.__dividir_linha_em_campos(line)
            if len(campos) != 3:  # verifica se possui 3 colunas
                erros_encontrados = 'Linha possui mais que 3 campos.'
            numero_campo = 0  # Incia na primeira posição ID
            for campo in campos:  # varre os campos da linha, id, nome e cupons
                if campo is '':  # verifica se o campo em branco
                    erros_encontrados = self.__montar_mensagem_erro(numero_campo, 'está em branco', erros_encontrados)
                numero_campo += 1  # Qual campo da linha está sendo verificado (ID, nome, Cupons)
            # posica_campo = 0  # recomeça a contagem para uma nova linha
            self.__log_erros(line, erros_encontrados)  # escreve no arquivo de erro os erros encontrados
            erros_encontrados = ''  # Limpa erros da linha anterior
        file.close()

    def verificar_integridade(self, link_arquivo):
        file = self.__abri_arquivo(link_arquivo)
        file_copia = []  # armazena copia das linhas
        dicionario_ids = {}  # dicionario ID com CHAVE e uma COLEÇAO com as LINHAS QUE CONTEM O MESMO ID
        dicionario_nomes = {}  # dicionario ID com NOME e uma COLEÇAO com as LINHAS QUE CONTEM O MESMO ID
        contador_linhas = 2  # Cabeçalho primeira linha, por isso começa no 2, caso tenha linha repetida, a segunda seria desconsiderada usando index

        for line in file:  # faz a leitura dor arquivo original para montar o hash
            campos = self.__dividir_linha_em_campos(line)
            id = campos[0]
            nome = campos[1]
            dicionario_ids = self.__atualizar_dicionario_linhas_repetidas(dicionario_ids, id, contador_linhas)
            dicionario_nomes = self.__atualizar_dicionario_linhas_repetidas(dicionario_nomes, nome, contador_linhas)
            contador_linhas += 1
            file_copia.append(line)  # Guarda uma cópia da linha

        contador_linhas = 2  # reinicia a contagem vai percorrer novamente as linhas
        for line2 in file_copia:  # faz leitura do copia das informações, procura no hash as duplicidades e escreve no log os erros
            campos = self.__dividir_linha_em_campos(line2)
            erros_encontrados = ''
            numero_campo = 0
            for campo in campos:
                linhas_repetidas = 0
                if numero_campo == 0:  # id
                    linhas_repetidas = self.__get_linhas_repetidas_dicionario(dicionario_ids, campo)
                elif numero_campo == 1:  # nome
                    linhas_repetidas = self.__get_linhas_repetidas_dicionario(dicionario_nomes, campo)
                else:  # campo numerico
                    break

                if len(linhas_repetidas) > 1:
                    for numero_linha in linhas_repetidas:
                        if int(numero_linha) != contador_linhas:
                            mensagem = 'já utlizado na linha {}'.format(numero_linha)
                            erros_encontrados = self.__montar_mensagem_erro(numero_campo, mensagem, erros_encontrados)
                numero_campo += 1  # incrementa para vericiar proximo campo ID, Nome, Quantidade cupons
            self.__log_erros(line2, erros_encontrados)
            contador_linhas += 1  # Incrementa para verificar a proxima linha

    def __get_linhas_repetidas_dicionario(self, dicionario,
                                          chave):  # Retornar todas as linhas que contem aquele id, forma de um ARRAY
        return str(dicionario.get(chave)).split(';')

    def __atualizar_dicionario_linhas_repetidas(self, dicionario, chave,
                                                numero_linha):  # diciona o numero da linha no dicionario
        colecao_linhas = dicionario.get(chave)
        if colecao_linhas is None:
            dicionario[chave] = numero_linha
        else:
            dicionario[chave] = '{};{}'.format(colecao_linhas, numero_linha)
        return dicionario

    def __montar_mensagem_erro(self, numero_campo, mensagem_erro, erros_encontrados):
        nome_campo = self.nomes_campos[numero_campo]  # Pega o nome do campo que está em branco
        if erros_encontrados is '':  # Verfica se já possui alguma mensagem de erro anterior
            return '{} {}.'.format(nome_campo,
                                   mensagem_erro)  # Se não possui nenhum erro nesta linha apenas monta mensagem de erro
        else:
            return '{},{} {}'.format(erros_encontrados, nome_campo,
                                     mensagem_erro)  # se a linha possui mais algum erro concatena com anterior

    def __dividir_linha_em_campos(self, linha):
        campos = linha.replace('\n', '').split(';')  # Divide a Linha em partes de acordo com ";"
        return campos

    def __abri_arquivo(self, link_arquivo):
        file = open(link_arquivo, "r", encoding="ISO-8859-1")  # abre o arquivo para leitura
        reader = file.readline()  # leitura do cabeçalho
        self.__limpar_arquivo_erros()  # Limpra o arquivo de erros
        self.__log_erros(reader, 'Erros Encontrados')  # Cria o cabeçaçho do arquivo de erros
        return file

    def __log_erros(self, linha, erros_encontrados):  # faz a escrita no arquivo
        arquivo_erros = open('Erros.csv', "a", encoding="utf8")
        erro = '{}{}{}'.format(linha.replace('\n', ';'), erros_encontrados,
                               '\n')  # formata a mensagem de erro ferente a linha para escrever no log
        arquivo_erros.write(erro)
        arquivo_erros.close()

    def __limpar_arquivo_erros(self):  # limpa arquvo
        arquivo_erros = open('Erros.csv', "w")
        arquivo_erros.close()
