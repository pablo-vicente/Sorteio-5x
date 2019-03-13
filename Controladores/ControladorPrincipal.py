class ControladorPrincipal:

    def __init__(self, tabela_participantes = ['Id', 'Nome Completo', 'Quantidade de Cupons']):
        pass

    def gerarCupons(self):


        file = open('Gerar cupons.csv', 'r')
        reader = file.readline()  # leitura do cabeçalho
        contadorDeLinhas = 1  # quantidades de linhas lidas do arquivo
        errosEncontrados = ''  # Inicia variável de erros
        for line in file:
            contadorDeLinhas += +1  # Adiciona uma linha ao contador
            temp = line.split(';')  # Leitura de cada linha
            if len(temp) != 3:  # verifica se possui 3 colunas
                errosEncontrados = errosEncontrados + "LINHA " + str(contadorDeLinhas) + ": Possui mais de 4 (quatro) colunas. Verifique se as colunas ao lado estão em branco. \n"
            if temp[0] is "":  #Verifica se campo ID está em branco
                errosEncontrados = errosEncontrados + "LINHA " + str(contadorDeLinhas) + ": Campo " + tabela_participantes + " está em branco.\n"

        return errosEncontrados

    def __mensage_erro(self, erros_encontrados, contador_linhas, campo):
        erros_encontrados = '{} Linha {}: Campo {} está em branco.\n'.format(erros_encontrados,str(contador_linhas), '')



