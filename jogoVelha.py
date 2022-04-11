import os
import random
from Colorama   import Fore, Back, Style

jogarNovamente="s"
jogadas=0
quemJoga=2
maxJogadas=9
vit="n"
velha=[
    [" "," "," "],
    [" "," "," "],
    [" "," "," "]  
]

def tela():
    global velha
    global jogadas
    os.system("cls")
    print("    0   1   2")
    print("0:  " + velha[0][0] + "  " + velha [0][1]+ "   "velha [0][2])
    print("   -----------")
    print("1:  " + velha[1][0] + " / " + velha [1][1]+ "  / "velha [1][2])
    print("   -----------")
    print("2:  " + velha[2][0] + " / " + velha [2][1]+ "  / "velha [2][2])
    print("Jogadas: " + Fore.GREEN + str(jogadas) + Fore.RESET)
    
    def jogador joga():
        global jogador
        global quemJoga
        global vit
        global maxJogadas
        if quemJoga==2 and jogadas<maxJogadas:
            l=int(imput("Linha..: "))
            c=int("Coluna... "))
            while velha[1][c]!=" ":
                l=int(imput("Linha..: "))
                c=int("Coluna... "))
        try:
                velha[1] [c]= "x"
                quemJoga=1
                jogadas+=1
        except:
            print("Linha e ou coluna invalida")
            #vit="n"
            
def cpuJoga():
    global jogador
    global quemJoga
    global vit
    global maxJogadas
    if quemJoga==1 and jogadas<maxJogadas:
        l=random.randrange(0,3)
        c=random.randrange(0,3)
        while velha [1][c]!= " ":
            l=random.randrange(0,3)
            c=random.randrange(0,3)
        velha[1][c]="0"
        jogadas+=1
        quemJoga=2
            
            
        
        
while True:
    tela()
    jogo Joga()
    cpuJoga()
    #vv()
    
    
    
    
    
    




 
      

