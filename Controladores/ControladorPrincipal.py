class ControladorPrincipal:
    tabela_participantes = ['Id', 'Nome Completo', 'Quantidade de Cupons']
    def __init__(self):

        pass

    def validar_arquivo(self):
        file = open('Base.csv', "r", encoding="ISO-8859-1")
        reader = file.readline()  # leitura do cabeçalho
        self.limpar_arquivo_erros()
        self.log_erros(reader.replace('\n', ';Erros Encontrados\n'))  # Cria o cabeçaçho do arquivo de erros
        erros_encontrados = ''  # Inicia variável de erros
        for line in file:
            temp = line.replace('\n','').split(';')  # Divide a Linha em partes
            if len(temp) != 3:  # verifica se possui 3 colunas
                erros_encontrados = 'Linha possui mais que 3 campos.'
            posicao = 0  # Incia na primeira posição ID
            for titulo_campo in temp:  # varrer cs campos da linha
                if titulo_campo is '':  # verifica se cada campos em branco
                    campo = self.tabela_participantes[posicao]  # Pega o nome do campo que está em branco
                    # Verfica se já possui alguma mensagem de erro anterior
                    if erros_encontrados is '':
                        erros_encontrados = '{} está em branco.'.format(campo)  # Tem as três colunas e algum campo em branco
                    else:
                        erros_encontrados = '{},{} está em branco'.format(erros_encontrados, campo)
                posicao += 1
            posicao =0
            erro = '{}{}{}'.format(line.replace('\n', ';'), erros_encontrados, '\n')
            erros_encontrados = ''  # Limpa erros da linha anterior
            self.log_erros(erro)

    def log_erros(self, erros_encontrados):
        arquivo_erros = open('Erros.csv', "a", encoding="utf8")
        arquivo_erros.write(erros_encontrados)
        arquivo_erros.close()

    def limpar_arquivo_erros(self):
        arquivo_erros = open('Erros.csv', "w")
        arquivo_erros.close()

    def gerar_cupons(self):
        pass