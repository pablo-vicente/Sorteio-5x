from Controladores.ControladorPrincipal import ControladorPrincipal

controladorPrincipal = ControladorPrincipal()
controladorPrincipal.gerar_cupons('Base.csv')
#controladorPrincipal.gerar_cupons()

#Base.csv
#Erros.csv

#  file = open('Gerar cupons.csv', 'r')
#  reader = file.readline()  # leitura do cabeçalho
#  for line in file:
#      temp = line.split(';')  # Divide a linha em partes, verifica se tem somente 3 campos
#      for titulo_campo in temp:  # varrer cs campos da linha
#          n = temp.index(titulo_campo)
#          print(titulo_campo, n)
