import os # biblioteca que permite abrir arquivos externos como o google
import pyttsx # biblioteca que transforma texto em áudio

eng = pyttsx.init() # salvando dentro de uma variável aquilo que seria a Engine do pip pyttsx
class Bot():
    
    def recebe(frase):      # def que exclusivamente recebe uma frase do usuario
        frase = input('>>> ')
        frase = frase.lower()   # função que transforma letras maiúsculas em minúsculas
        frase = frase.replace('é','eh')      # função que troca o 'primeiro' argumento pelo 'segundo' dos parênteses
        frase = str(frase)   #função que transforma tudo dentro de "frase" em string
        return frase
             
    def lembrar(lembrar):    # def que aprende ou responde algo que ja sabe
        arquivo = open ('Memoria.txt','a')  # cria o arquivo em txt caso não haja um, que escreve em array
        memoria = open ('Memoria.txt','r')   # abre o arquivo txt em formato de leitura
        lembrar = memoria.read()      # grava dendtro da variavel "lembrar" o comando de leitura
        memoria.seek(0)     # volta o ponto de inserção do teclado para o primeiro bit escrito dentro do arquivo txt, o bit 0
        
        if frase in lembrar:     # caso o usuário tenha dito algo que consta no banco de dados:
            for line in memoria:     # for que roda todas as linhas dentro do arquivo txt
                if frase in line:    # caso "frase" esteja nessa linha:
                    resposta = memoria.readline().replace('\n','')   # salvar a linha de baixo dentro da variável 'resposta'
                    print (resposta)
                    eng.say(resposta)   #eng do pyttsx dizendo a resposta em áudio
                    eng.runAndWait()    #eng do pyttsx rodando e aguardando o fim do áudio para executar outro comando
                    if 'abrir' in line:     # caso o usuario digitar "abrir" 
                       os.startfile(resposta)   #entender que a proxima linha é um URL ou um endereço de algum aplicativo, e executar o app deste endereço
        else:       # caso o usuário tenha dito algo que não consta no banco de dados   # aprender como array
            arquivo.write(frase + "\n") 
            print("aprendido")
            
while True:     #repetição da Titania até ser fechada manualmente
    frase = Bot().recebe()
    resp = Bot().lembrar()
