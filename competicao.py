import random

################################################################################ listas auxiliares para ramdomizacao
lista_nomes = ["Miguel","Sophia","Davi","Alice","Arthur","Julia","Pedro","Isabella","Gabriel","Manuela","Bernardo","Laura",
"Lucas","Luiza","Matheus","Valentina","Rafael","Giovanna","Heitor","Maria Eduarda","Enzo","Helena","Guilherme",
"Beatriz","Nicolas","Maria Luiza","Lorenzo","Lara","Gustavo","Mariana","Felipe","Nicole",'Samuel',"Rafaela",
"João Pedro","Heloísa","Daniel","Isadora","Vitor","Lívia","Leonardo","Maria Clara","Henrique","Ana Clara"
"Theo","Lorena","Murilo","Gabriela","Eduardo","Yasmin","João","Clara","Vinícius","Letícia"]

lista_torneios = ["Primeiro torneio de","Copa nacional de","II Campeonato de","Copa Fluxo de","Campeonato de","Torneio oficial de"
                    ,"Copa Nacional de","II Copa mundial de","Competição nacional de","Primeiro campeonato de","Torneio mundial de"
                    ,"Campeonato mundial de","Liga nacional de","Liga mundial de","Liga anual de"]

lista_artes_marciais = ["kung fu","caratê","judô","aikido","krav magá","jiu-jitsu","muay thai","taekwondo","boxe","ninjutsu",
                                                                                                    "capoeira","esgrima","mma"]

lista_faixas = ["faixa livre","branca","cinza","amarela","laranja","verde","azul","roxa","marrom","preta","vermelha"]

lista_pesos = [[40,45],[45,55],[55,60],[60,70],[70,80],[80,90],[90,100],[100,120]]

################################################################################ Classes

####### Classe Lutador
#
# nome : indica o nome do lutador, tipo: string
#   ex: nome = "Torneio da FLUXO"
#
# idade: indica a idade do lutador, tipo: int
#   ex: idade = 25
#
# peso: indica o peso do lutador, tipo: int
#   ex: peso = 80
#
# forca: indica uma pontuacao de 0 a 100 para a forca do lutador, tipo: int (0 < forca < 100)
#   ex: forca = 100
#
# faixa: indica a faixa do lutador, tipo : string
#   ex: faixa = "branca"
#
# arte_marcial : indica a arte marcial do lutador, tipo: string
#   ex: arte_marcial = "jiu-jítsu"
#
# pontuacao_pessoal : valor estimado a partir de seus atributos e usado pra definir o vencedor em batalhas
class Lutador:
    def __init__(self, nome, idade, peso, forca, faixa, arte_marcial):
        if ((isinstance(nome,str)) and 
            (isinstance(idade,int)) and 
            (isinstance(peso,int)) and 
            (isinstance(forca,int)) and (forca <= 100) and (forca >= 0) and 
            (isinstance(faixa,str)) and
            (isinstance(arte_marcial,str))) :
            
            self.nome = nome
            self.idade = idade
            self.peso = peso
            self.forca = forca
            self.faixa = faixa
            self.arte_marcial = arte_marcial
                       
        else:
            print("Existe algum tipo de atributo inválido")
    
    def __str__(self):
        return f"Lutador nome: {self.nome} idade:{self.idade}  peso:{self.peso} força:{self.forca} faixa:{self.faixa} arte_marcial:{self.arte_marcial}"       
             
    def setNome(self,nome):
        if (isinstance(nome,str)):
            self.nome = nome
        else:
            print("Tipo inválido para o nome do lutador")

    def setIdade(self,idade):
        if (isinstance(idade,int)):
            self.idade = idade
        else: 
            print("Tipo inválido para a idade do lutador")

    def setPeso(self,peso):
        if (isinstance(peso,int)):
            self.peso = peso
        else: 
            print("Tipo inválido para o peso do lutador")
    
    def setForca(self,forca):
        if (isinstance(forca,int)) and (forca <= 100) and (forca > 0):
            self.forca = forca
        else: 
            print("Tipo inválido para a força do lutador")

    def setFaixa(self,faixa):
        if (isinstance(faixa,str)):
            self.faixa = faixa
        else: 
            print("Tipo inválido para a faixa do lutador")

    def setArteMarcial(self,arte_marcial):
        if (isinstance(arte_marcial,str)):
            self.arte_marcial = arte_marcial
        else:
            print("Tipo inválido para a arte marcial do lutador")

    def setPontuacaoPessoal(self):
        self.pontuacao_pessoal = calcular_pontuacao_pessoal(self) 
    


####### Classe Torneio
#
# nome : indica o nome do torneio, tipo: string
#   ex: nome = "Torneio da FLUXO"
#
# arte_marcial : indica a arte marcial da categoria, tipo: string
#   ex: arte_marcial = "jiu-jítsu"
#
# faixas : indica as faixas disponíveis para luta, tipo: lista de strings
#   ex: faixas = ["branca", "azul", "marrom", "livre"]
#
# pesos : indica os pesos disponíneis, tipo: lista de listas de 2 elementos inteiros (peso mín e máx)
#   ex: pesos = [[70,80],[80, 90], [90, 100]]
#
# competicoes_internas : indica todas as subdivisoes de competicoes que podem acontecer no torneio
#                        São as combinacoes entre faixas e intervalos de peso
class Torneio:
    def __init__(self, nome, arte_marcial, faixas, pesos):
        if ((isinstance(nome,str)) and 
            (isinstance(arte_marcial,str)) and
            (isinstance(faixas,list)) and (all(isinstance(i, str) for i in faixas)) and   # comentário sobre a verificação 
            ((isinstance(pesos,list)) and (all(isinstance(i,list) for i in pesos)) and    # dos pesos em setPesos
            (all(len(i) == 2  for i in pesos)) and (all( all(isinstance(j,int) for j in i) for i in pesos)))):
            
            self.nome = nome
            self.arte_marcial = arte_marcial
            self.faixas = faixas
            self.pesos = pesos
        else:
            print("Existe algum tipo de atributo inválido")

    def __str__(self):
        return f"Torneio nome:{self.nome} arte_marcial:{self.arte_marcial} faixas:{self.faixas} pesos:{self.pesos}"

    def setNome(self,nome):
        if (isinstance(nome,str)):
            self.nome = nome
        else:
            print("Tipo inválido para o nome do torneio")

    def setArteMarcial(self,arte_marcial):
        if (isinstance(arte_marcial,str)):
            self.arte_marcial = arte_marcial
        else:
            print("Tipo inválido para a arte marcial do torneio")

    def setFaixas(self,faixas):
        #checa se "faixas" é uma lista e se todos os seus elementos são strings
        if (isinstance(faixas,list)) and (all(isinstance(i, str) for i in faixas)):
            self.faixas = faixas
        else:
            print("Tipo inválido para as faixas do torneio")

    def setPesos(self,pesos):   
        #verifica se é uma lista                            
        if ((isinstance(pesos,list)) and 
            #verifica se os items da lista são listas                 
            (all(isinstance(i,list) for i in pesos)) and 
            #verifica se todas as listas possuem exatamente 2 elementos
            (all(len(i) == 2  for i in pesos)) and
            #verifica se a lista possui exatamente 2 elementos
            (all( all(isinstance(j,int) for j in i) for i in pesos))):
            
            self.pesos = pesos

        else:
            print("Tipo inválido para os pesos do torneio")

    def setCompeticoesInternas(self):
        self.competicoes_internas = []
        for faixa in self.faixas :
            for lista_pesos in self.pesos:
                peso_min = lista_pesos[0]
                peso_max = lista_pesos[1]
                self.competicoes_internas.append(CompeticaoInterna(faixa,peso_min,peso_max))


####### Classe Competicao Interna
# Esta classe serve para dividir o torneio em competicoes internas que envolvem uma faixa especifica e um intervalo de peso especifico
# 
# faixa: indica a faixa usada na competicao
# peso_min: peso mínimo pra competir
# peso_max: peso máximo para competir
# competidores: lista com os objetos de cada competidor, tipo: lista de objetos da classe Competidor 
class CompeticaoInterna:
    def __init__(self,faixa,peso_min,peso_max):
        if ((isinstance(faixa,str)) and 
            (isinstance(peso_min,int)) and (peso_min >= 0) and
            (isinstance(peso_min,int)) and (peso_min >= 0)):
            
            self.faixa = faixa
            self.peso_min = peso_min
            self.peso_max = peso_max
            self.competidores = [] 

    def __str__(self):
        return f"Competicao interna - faixa:{self.faixa} peso_min:{self.peso_min} peso_max:{self.peso_max}"

    def setFaixa(self,faixa):
        if (isinstance(faixa,str)):
            self.faixa = faixa
        else:
            print("Tipo inválido para a faixa da competição interna")

    def setPesoMin(self,peso_min):
        if((isinstance(peso_min,int)) and (peso_min >= 0)):
            self.peso_min = peso_min
        else:
            print("Tipo inválido para o peso mínimo da competição interna")
    
    def setPesoMax(self,peso_max):
        if((isinstance(peso_max,int)) and (peso_max >= 0)):
            self.peso_max = peso_max
        else:
            print("Tipo inválido para o peso máximo da competição interna")

    def setCompetidor(self,competidor):
        if (isinstance(competidor,Competidor)):
            self.competidores.append(competidor)
        else:
            print("Tipo inválido para o novo competidor na competição interna")
    

####### Classe Competidor
# Esta classe serve para definir as pontuacoes de um lutador em uma competicao especifica. Para cada competicao que o lutador for participar
# ele devera ter um objeto dessa classe no objeto da classe competicao
# 
# lutador: objeto do tipo Lutador contendo todos os atributos do competidor
# vitorias: numero de batalhas ganhas
# derrotas: numero de batalhas perdidas
class Competidor:    
    def __init__(self,lutador):
        if (isinstance(lutador, Lutador)):
            self.lutador = lutador
            self.vitorias = 0
            self.derrotas = 0

    def __str__(self):
        return f"Competidor:{self.lutador.nome} vitorias:{self.vitorias} derrotas:{self.derrotas}"
    
    def novaVitoria(self):
        self.vitorias += 1
    
    def novaDerrota(self):
        self.derrotas += 1
    
            

################################################################################ Funcoes

####### Recebe um inteiro positivo como input do usuário e testa a entrada  
def receber_int_pos_ou_nulo_como_input(texto_do_input):
    while True:
        try:
            entrada = int(input(texto_do_input))
            if(entrada < 0):
                print("Entrada inválida, digite novamente!")
            else:
                break
        except :
            print("Entrada inválida, digite novamente!")
    return entrada 


####### mostra as opcoes do menu principal na tela e recebe a escolha do usuario
def menu_principal():
    print("\n|------------------------------------------------|")
    print("|               MENU PRINCIPAL                   |")
    print("|------------------------------------------------|")
    print("| 1 - MENU DE TORNEIO                            |")
    print("|------------------------------------------------|")
    print("| 2 - MENU DE LUTADOR                            |")
    print("|------------------------------------------------|")
    print("| 3 - TORNEIO ALEATÓRIO COM LUTADORES ALEATÓRIOS |")
    print("|------------------------------------------------|")
    print("| 4 - SAIR DO PROGRAMA                           |")
    print("|------------------------------------------------|\n")
    
    escolha = input("Digite o número da opção desejada: ")

    while (escolha not in ('1','2','3','4')):
        escolha = input("Erro - Opção inválida.   Digite novamente: ")
           
    return escolha
 

####### mostra as opcoes do menu de lutador na tela e recebe a escolha do usuario
def menu_lutador():
    print("\n|------------------------------------------------|")
    print("|               MENU DE LUTADOR                  |")
    print("|------------------------------------------------|")
    print("| 1 - Cadastrar lutador                          |")
    print("|------------------------------------------------|")
    print("| 2 - Cadastrar lutador aleatório                |")
    print("|------------------------------------------------|")
    print("| 3 - Ver lutadores                              |")
    print("|------------------------------------------------|")
    print("| 4 - Ver detalhes de um lutador                 |")    
    print("|------------------------------------------------|")
    print("| 5 - Voltar ao menu principal                   |")
    print("|------------------------------------------------|\n")
    
    escolha = input("Digite o número da opção desejada: ")

    while (escolha not in ('1','2','3','4','5')):
        escolha = input("Erro - Opção inválida.   Digite novamente: ")
                            
    return escolha


####### mostra as opcoes do menu de torneio na tela e recebe a escolha do usuario
def menu_torneio():
    print("\n|------------------------------------------------|")
    print("|                MENU DE TORNEIO                 |")
    print("|------------------------------------------------|")
    print("| 1 - Criar torneio                              |")
    print("|------------------------------------------------|")
    print("| 2 - Criar torneio aleatório                    |")
    print("|------------------------------------------------|")
    print("| 3 - Inscrever lutador                          |")
    print("|------------------------------------------------|")
    print("| 4 - Ver torneios existentes                    |")
    print("|------------------------------------------------|")
    print("| 5 - Ver ranking de um torneio                  |")
    print("|------------------------------------------------|")
    print("| 6 - Ver lutadores inscritos em torneio         |")
    print("|------------------------------------------------|")
    print("| 7 - Realizar luta                              |")
    print("|------------------------------------------------|")
    print("| 8 - Voltar ao menu principal                   |")
    print("|------------------------------------------------|\n")
    
    escolha = input("Digite o número da opção desejada: ")

    while (escolha not in ('1','2','3','4','5','6','7','8')):
        escolha = input("Erro - Opção inválida.   Digite novamente: ")
                            
    return escolha


####### Mostra na tela um aviso de que o programa será fechado
def fechar_programa():
    
    print("\n|------------------------------------------------|")
    print("|                Fim do programa                 |")
    print("|------------------------------------------------|\n")


####### Funcao cria um objeto da classe torneio a partir de inputs do usuario
def criar_torneio():
    #inicializacao de um torneio com atributos vazios
    torneio_aux = Torneio("","",[],[])
    print("\n|------------------------------------------------|")
    print("|                  Novo Torneio                  |")
    print("|------------------------------------------------|\n")
    
    #nome
    torneio_aux.setNome(input("Digite o nome do torneio: "))

    #arte marcial
    #é garantido que a letra seja minuscula para possiveis comparacoes futuras ocorrerem normalmente
    torneio_aux.setArteMarcial((input("Digite a arte marcial a ser disputada: ")).lower())

    #faixas
    lista_aux = []
    resposta_aux = ""
    while (resposta_aux not in ("S","s","Sim","SIM","sim","N","n","NÃO","não","Não","NAO","Nao","nao")):
        resposta_aux = input("Deseja incluir a opção de faixa livre? (S/N) :  ")
        if (resposta_aux in ("S","s","Sim","SIM","sim")):
            lista_aux.append("faixa livre")
            numero_faixas = receber_int_pos_ou_nulo_como_input("Digite o número de faixas que o torneio terá além da faixa livre :  ")
        elif (resposta_aux in ("N","n","NÃO","não","Não","NAO","Nao","nao")):
            numero_faixas = receber_int_pos_ou_nulo_como_input("Digite o número de faixas que o torneio terá :  ")
        else:
            
            print("Resposta inválida, digite novamente. ----------------")
    for i in range(0,numero_faixas,1):
         #é garantido que a letra seja minuscula para possiveis comparacoes futuras ocorrerem normalmente
        lista_aux.append((input(f"Digite o nome da faixa {i+1}:  ")).lower())
    torneio_aux.setFaixas(lista_aux)

    #pesos
    lista_aux = []
    numero_faixas = receber_int_pos_ou_nulo_como_input("Digite o número de faixas de peso que a competição terá:  ")
    for i in range(0,numero_faixas,1):        
        print(f"|------------   Faixa de Peso {i+1}  ----------------|")
        min = receber_int_pos_ou_nulo_como_input("Peso Mínimo:  ")
        max = receber_int_pos_ou_nulo_como_input("Peso Máximo:  ")
        lista_aux.append([min,max])
    torneio_aux.setPesos(lista_aux)

    #competicoes_internas
    torneio_aux.setCompeticoesInternas()

    print("\n\n          Torneio cadastrado com sucesso")
    mostrar_torneio(torneio_aux)
    return torneio_aux


####### Funcao recebe um objeto da classe torneio e o mostra na tela
def mostrar_torneio(torneio):
    print("|------------------------------------------------|")
    print(f"   nome do torneio: {torneio.nome}")   
    print("|------------------------------------------------|")    
    print(f"   arte marcial : {torneio.arte_marcial}")
    print("|------------------------------------------------|") 
    print("   faixas:") 
    for faixa in torneio.faixas:
        print(f"           {faixa}")
    print("|------------------------------------------------|") 
    print("   faixas de peso:")
    for pesos in torneio.pesos:
        print(f"                   de {pesos[0]}kg a {pesos[1]}kg ")
    print("|------------------------------------------------|\n\n")
    print("   Competições ativas :")
    mostrar_competicoes_com_lutadores_inscritos(torneio)


####### cria torneio aleatorio usando numeros gerados aleatorios e as listas auxiliares de atributos possiveis
def criar_torneio_aleatorio():
    #inicializacao de um torneio com atributos vazios
    torneio_aux = Torneio("","",[],[])

    # arte_marcial
    index_aux = random.randint( 0 , len(lista_artes_marciais)-1 )
    arte_marcial = lista_artes_marciais[index_aux]
    torneio_aux.setArteMarcial(arte_marcial)

    #nome
    index_aux = random.randint(0,len(lista_torneios)-1)
    torneio_aux.setNome(f"{lista_torneios[index_aux]} {arte_marcial}"  )

    #faixas
    lista_aux = []
    num_faixas = random.randint(1,len(lista_faixas)-1)   
    for i in range (0,num_faixas,1):
        index_aux = random.randint(0,len(lista_faixas)-1)
        if (lista_faixas[index_aux] not in lista_aux):
            lista_aux.append(lista_faixas[index_aux])
    torneio_aux.setFaixas(lista_aux)

    #pesos
    lista_aux = []
    num_pesos = random.randint(1,len(lista_pesos)-1)
    for i in range (0,num_pesos):
        index_aux = random.randint(0,len(lista_pesos)-1)
        if (lista_pesos[index_aux] not in lista_aux):
            lista_aux.append(lista_pesos[index_aux])
    torneio_aux.setPesos(lista_aux)

    #competicoes_internas
    torneio_aux.setCompeticoesInternas()

    return torneio_aux


####### lista todos os torneios na tela
def ver_torneios(torneios):
    if (len(torneios) > 0 ):
        print("\n\n|------------------------------------------------|")
        print("|              Torneios Cadastrados              |")
        print("|------------------------------------------------|")
        for torneio in torneios:
            mostrar_torneio(torneios[torneio])
        print("\n\n")
    else:
        print("Ainda não existem torneios cadastrados.")
    
####### Funcao cria um objeto da classe lutador a partir de inputs do usuario
def criar_lutador():
    #inicializacao de um lutador com atributos vazios
    lutador_aux = Lutador("",0,0,0,"","")
    print("\n|------------------------------------------------|")
    print("|                  Novo Lutador                  |")
    print("|------------------------------------------------|\n")
    
    #nome
    nome = input("Digite o nome do lutador:  ")
    # o nome nao pode ser zero pois eh a opcao que retorna ao menu na funcao ver_lutadores()
    if ( nome != "0"):
        lutador_aux.setNome(nome)
    else:
        print("O nome do lutador não pode ser \"0\", tente novamente.")

    #idade
    lutador_aux.setIdade(receber_int_pos_ou_nulo_como_input("Digite a idade do lutador:  "))

    #peso
    lutador_aux.setPeso(receber_int_pos_ou_nulo_como_input("Digite o peso do lutador:   "))

    #forca
    ok = False
    while (ok == False):
        forca = receber_int_pos_ou_nulo_como_input("Digite a força do lutador:   ")
        if (forca > 100) :
            print("A pontuação de força deve valer no máximo até 100. Digite novamente")
        else:
            ok = True
    lutador_aux.setForca(forca)
    
    #faixa 
    #eh garantido que a letra seja minuscula para possiveis comparacoes futuras ocorrerem normalmente
    lutador_aux.setFaixa((input("Digite a faixa do lutador:  ")).lower())

    #arte_marcial
    #eh garantido que a letra seja minuscula para possiveis comparacoes futuras ocorrerem normalmente
    lutador_aux.setArteMarcial((input("Digite a arte marcial a ser disputada pelo lutador:  ")).lower())

    #pontuacao_pessoal
    lutador_aux.setPontuacaoPessoal()

    print("\n\n          Lutador cadastrado com sucesso")
    mostrar_lutador(lutador_aux)
    return lutador_aux


####### Funcao recebe um objeto da classe lutador e o mostra na tela
def mostrar_lutador(lutador):
    print("|------------------------------------------------|")
    print(f"   nome do lutador: {lutador.nome}")   
    print("|------------------------------------------------|")  
    print(f"   idade do lutador: {lutador.idade} anos")   
    print("|------------------------------------------------|")
    print(f"   peso do lutador: {lutador.peso} kg")   
    print("|------------------------------------------------|") 
    print(f"   força do lutador: {lutador.forca}")   
    print("|------------------------------------------------|")  
    print(f"   faixa do lutador: {lutador.faixa}")   
    print("|------------------------------------------------|")    
    print(f"   arte marcial do lutador: {lutador.arte_marcial}")
    print("|------------------------------------------------|") 
    print(f"   pontuacao pessoal do lutador: {lutador.pontuacao_pessoal}")
    print("|------------------------------------------------|") 

####### Cria lutador aleatorio usando numeros gerados aleatorios e as listas auxiliares de atributos possiveis
def criar_lutador_aleatorio():
    #inicializacao de um lutador com atributos vazios
    lutador_aux = Lutador("",0,0,0,"","")

    #nome
    index_aux = random.randint( 0 , len(lista_nomes)-1 ) 
    lutador_aux.setNome(lista_nomes[index_aux])

    #idade
    index_aux = random.randint(0,55)
    lutador_aux.setIdade(index_aux)

    #peso
    index_aux = random.randint(40,120)
    lutador_aux.setPeso(index_aux)

    #forca
    # 4*index_aux com (0 < index_aux < 25) torna os indices de forca mais realistas 
    index_aux = random.randint(1,25)
    lutador_aux.setForca(4*index_aux)

    #faixa
    index_aux = random.randint( 0 , len(lista_faixas)-1 )
    lutador_aux.setFaixa(lista_faixas[index_aux])

    #arte_marcial
    index_aux = random.randint( 0 , len(lista_artes_marciais)-1 )
    lutador_aux.setArteMarcial(lista_artes_marciais[index_aux])

    #pontuacao_pessoal
    lutador_aux.setPontuacaoPessoal()

    return lutador_aux 


####### mostra a lista com todos os lutadores cadastrados no sistema
def ver_lutadores(lutadores):
    if (len(lutadores) > 0 ):
        print("\n\n|------------------------------------------------|")
        print("|             Lutadores Cadastrados              |")
        print("|------------------------------------------------|")
        for lutador in lutadores:
            print(f"    {lutador}")
            print("|------------------------------------------------|")
        print("\n\n")
    else:
        print("Ainda não existem lutadores cadastrados.")


####### seleciona um lutador, pelo input do usuario, para exibir seus detalhes 
def ver_detalhes_lutador(lutadores):
    if (len(lutadores) > 0 ):
        ver_lutadores(lutadores)
        ok = False
        while (ok == False):
            escolha = input("Digite o nome do lutador desejado ou \"0\"  para retornar ao menu:  ")
            if (escolha != "0" ):
                if(escolha not in lutadores):
                    print("Nome do lutador inválido, digite novamente.")
                else:
                    ok = True
                    mostrar_lutador(lutadores[escolha])
                    print("\n\n")
            else:
                ok = True
    

####### Funca para estimar a pontuacao pessoal de um lutador a partir de seus atributos
def calcular_pontuacao_pessoal(lutador):
    pontos = 0

    # forca - peso 2
    # a forca soma sua representacao com peso 2 na pontuacao
    pontos += 2 * lutador.forca

    # idade - peso 2
    # para a idade, vamos considerar o apice de um lutador aos 34 anos. Sua influencia na pontuacao
    # ocorre de uma forma que ela vai aumentando ate chegar em 34, e a partir de 35 passa a decair.
    # pontuacao(35) = pontuacao(33)  ,  pontuacao(36) = pontuacao(32) e assim sucessivamente 
    # a partir de 68 anos a idade nao influencia mais na pontuacao
    if (lutador.idade <35):
        pontos += 2 * lutador.idade
    elif(lutador.idade > 35) and (lutador.idade <= 68):
        pontos += 2 * (68-lutador.idade)

    # peso(kg)
    # vamos definir faixas de peso com pontuacao semelhante
    # se peso<40 ou peso>125 ele nao tem influencia na pontuacao
    if (lutador.peso >= 40) and  (lutador.peso < 50) :
        pontos += 15
    elif (lutador.peso >= 50) and  (lutador.peso < 60) :
        pontos += 25
    elif (lutador.peso >= 60) and  (lutador.peso < 70) :
        pontos += 35
    elif (lutador.peso >= 70) and  (lutador.peso < 75) :
        pontos += 45
    elif (lutador.peso >= 75) and  (lutador.peso < 80) :
        pontos += 55
    elif (lutador.peso >= 85) and  (lutador.peso < 90) :
        pontos += 65
    elif (lutador.peso >= 90) and  (lutador.peso < 95) :
        pontos += 55
    elif (lutador.peso >= 95) and  (lutador.peso < 100) :
        pontos += 45
    elif (lutador.peso >= 100) and  (lutador.peso < 110) :
        pontos += 35
    elif (lutador.peso >= 110) and  (lutador.peso < 125) :
        pontos += 25

    # faixa
    #tambem vamos dividir em intervalos
    if (lutador.faixa == "branca") :
        pontos += 15 
    elif (lutador.faixa == "branca") :
        pontos += 25 
    elif (lutador.faixa == "cinza") :
        pontos += 35 
    elif (lutador.faixa == "amarela") :
        pontos += 45 
    elif (lutador.faixa == "laranja") :
        pontos += 55 
    elif (lutador.faixa == "verde") :
        pontos += 65 
    elif (lutador.faixa == "azul") :
        pontos += 75 
    elif (lutador.faixa == "roxa") :
        pontos += 85 
    elif (lutador.faixa == "marrom") :
        pontos += 95 
    elif (lutador.faixa == "preta") :
        pontos += 105 
    elif (lutador.faixa == "vermelha") :
        pontos += 120

    return pontos


####### Funcao usada para inscrever um lutador em um torneio
def inscrever_lutador_torneio(lutador,torneio):
    peso_min = 0
    peso_max = 0
    # verifica se existe faixa disponivel nesse torneio para o lutador
    if ("faixa livre" not in torneio.faixas) and (lutador.faixa not in torneio.faixas):
        print("|------------------------------------------------|")
        print("Não há competição disponível para a faixa desse lutador")
        print("|------------------------------------------------|\n")
        return None
    
    # verifica se existe faixa de peso disponivel nesse torneio para o lutador
    for lista_pesos in torneio.pesos:
        if (lutador.peso >= lista_pesos[0]) and (lutador.peso <= lista_pesos[1]):
            peso_min = lista_pesos[0]
            peso_max = lista_pesos[1]

    if (peso_min == 0) and (peso_max==0):
        print("|------------------------------------------------|")
        print("Não há competição disponível para o peso desse lutador")
        print("|------------------------------------------------|\n")
        return None
    
    # insere o lutador na competicao de faixa livre em sua faixa de peso
    competidor = Competidor(lutador)  
    if("faixa livre" in torneio.faixas):
        for competicao in torneio.competicoes_internas:
            if (competicao.faixa == "faixa livre") and (competicao.peso_min == peso_min) and (competicao.peso_max == peso_max):
                competicao.setCompetidor(competidor)

    # insere o lutador na competicao da sua respectiva faixa e em sua faixa de peso       
    if(lutador.faixa in torneio.faixas):
        for competicao in torneio.competicoes_internas:
            if (competicao.faixa == lutador.faixa) and (competicao.peso_min == peso_min) and (competicao.peso_max == peso_max):
                competicao.setCompetidor(competidor)


####### lista na tela todas as competicoes de um torneio que possuem algum lutador inscrito e quantos lutadores sao
def mostrar_competicoes_com_lutadores_inscritos(torneio):
    print("\n\n|------------------------------------------------|")
    for competicao in torneio.competicoes_internas:
        if len(competicao.competidores) > 0 : 
            print("\n\n|------------------------------------------------|")
            print(f"Competição da faixa {competicao.faixa} entre {competicao.peso_min}kg e {competicao.peso_max}kg com {len(competicao.competidores)} lutadores.")
            print("\n\n|------------------------------------------------|")


####### Funcao para receber e analisar os inputs do usuario a fim de inscrever um lutador em um torneio
def inscrever_lutador_usuario(lutadores,torneios):
    if (len(lutadores) > 0 ) and (len(torneios) > 0):
        ver_lutadores(lutadores)
        ok = False
        while (ok == False):
            nome_lutador = input("Digite o nome do lutador desejado ou \"0\"  para retornar ao menu:  ")
            if (nome_lutador != "0" ):
                if(nome_lutador not in lutadores):
                    print("Nome do lutador inválido, digite novamente.")
                else:
                    ok = True
            else:
                return None
        
        ok = False
        while (ok == False):
            nome_torneio = input("Digite o nome do torneio desejado ou \"0\"  para retornar ao menu:  ")
            if (nome_torneio != "0" ):
                if(nome_torneio not in torneios):
                    print("Nome do torneio inválido, digite novamente.")
                else:
                    ok = True
            else:
                return None
        inscrever_lutador_torneio(lutadores[nome_lutador],torneios[nome_torneio])
    else:
        print("Não há lutador para ser inscrito ou torneio para realizar a inscrição")
    

####### Funcao para listar na tela todos os campeonatos em andamento e seus respectivos lutadores
def ver_lutadores_inscritos_torneio(torneios):
    ok = False
    while (ok == False):
            nome_torneio = input("Digite o nome do torneio desejado ou \"0\"  para retornar ao menu:  ")
            if (nome_torneio != "0" ):
                if(nome_torneio not in torneios):   
                    print("Nome do torneio inválido, digite novamente.")
                else:
                    ok = True
            else:
                return None
    for competicao in torneios[nome_torneio].competicoes_internas:
        if len(competicao.competidores) > 0 : 
            print("\n\n|------------------------------------------------|")
            print(f"   Competição de {torneios[nome_torneio].arte_marcial} para a faixa {competicao.faixa} e pesos de {competicao.peso_min}kg a {competicao.peso_max}kg.")
            print("\n    competidores :")
            for competidor in competicao.competidores:
                print(f"     {competidor}")
            print("\n\n|------------------------------------------------|")

####### Recebe 2 competidores para uma batalha e seleciona o vencedor e o perdedor
def realizar_luta(competidor1,competidor2):
    print("\n\n|------------------------------------------------|")
    print(f" Batalha entre {competidor1.lutador.nome} e {competidor2.lutador.nome}")
    print("|------------------------------------------------|")

    if(competidor1.pontuacao_pessoal) > (competidor2.pontuacao_pessoal):
        competidor1.novaVitoria()
        competidor2.novaDerrota()
        print(f" Vencedor = {competidor1.lutador.nome}")
        print(f" Perdedor = {competidor2.lutador.nome}")

    if(competidor2.pontuacao_pessoal) > (competidor1.pontuacao_pessoal):
        competidor2.novaVitoria()
        competidor1.novaDerrota()
        print(f" Vencedor = {competidor2.lutador.nome}")
        print(f" Perdedor = {competidor1.lutador.nome}")

    if(competidor1.pontuacao_pessoal) == (competidor2.pontuacao_pessoal):
        num_do_vencedor = random.randint(0,1)
        if (num_do_vencedor == 0):
            competidor1.novaVitoria()
            competidor2.novaDerrota()
            print(f" Vencedor = {competidor1.lutador.nome}")
            print(f" Perdedor = {competidor2.lutador.nome}")
            
        else:
            competidor2.novaVitoria()
            competidor1.novaDerrota()
            print(f" Vencedor = {competidor2.lutador.nome}")
            print(f" Perdedor = {competidor1.lutador.nome}")
#
#def vizualizar_ranking(competicao):
#    for competidor in competicao.competidores:






################################################################################ Main
dados = { 
    "torneios":{},
    "lutadores":{}
}

def main():
    sair_do_programa = False
    
    while (sair_do_programa == False):

        escolha_menu_principal = menu_principal()

        # OPCAO 1 ESCOLHIDA -> MENU DE TORNEIO
        if (escolha_menu_principal == '1'):
            voltar_ao_menu_principal = False

            while (voltar_ao_menu_principal == False) :
                escolha_menu_torneio = menu_torneio()

                # opcao 1 -> cadastrar torneio
                if (escolha_menu_torneio == '1'):
                    torneio_aux = criar_torneio()
                    dados["torneios"][torneio_aux.nome] = torneio_aux

                # opcao 2 -> cadastrar torneio torneio aleatório  
                if (escolha_menu_torneio == '2'):
                    torneio_aux = criar_torneio_aleatorio()
                    dados["torneios"][torneio_aux.nome] = torneio_aux
                    print("\n\n          Torneio cadastrado com sucesso")
                    mostrar_torneio(torneio_aux)
                    print("\n\n")

                 # opcao 3 -> inscrever jogador
                if (escolha_menu_torneio == '3'):
                    inscrever_lutador_usuario(dados['lutadores'],dados['torneios'])

                # opcao 4 -> ver torneios   
                if (escolha_menu_torneio == '4'):
                    ver_torneios(dados['torneios'])

                # opcao 5 -> ver ranking
                if (escolha_menu_torneio == '5'):
                    print("Função não implementada")

                # opcao 6 -> ver lutadores inscritos em um torneio    
                if (escolha_menu_torneio == '6'):
                    ver_lutadores_inscritos_torneio(dados['torneios'])

                # opcao 7 -> realizar luta
                if (escolha_menu_torneio == '7'):
                    print("Função não implementada")
                # opcao 8 -> voltar ao menu principal
                if (escolha_menu_torneio == '8'):
                    voltar_ao_menu_principal = True

        # OPCAO 2 ESCOLHIDA -> MENU DE LUTADOR
        if (escolha_menu_principal == '2'):
            voltar_ao_menu_principal = False

            while (voltar_ao_menu_principal == False) :
                escolha_menu_lutador = menu_lutador()

                # opcao 1 -> cadastrar lutador
                if (escolha_menu_lutador == '1'):
                    lutador_aux = criar_lutador()
                    dados["lutadores"][lutador_aux.nome] = lutador_aux

                # opcao 2 -> cadastrar lutador aleatorio
                if (escolha_menu_lutador == '2'):
                    lutador_aux = criar_lutador_aleatorio()
                    dados["lutadores"][lutador_aux.nome] = lutador_aux
                    print("\n\n          Lutador cadastrado com sucesso")
                    mostrar_lutador(lutador_aux)
                    print("\n\n")
                    
                # opcao 3 -> ver lutadores
                if (escolha_menu_lutador == '3'):
                    ver_lutadores(dados['lutadores'])

                # opcao 4 -> ver detalhes de um lutador
                if (escolha_menu_lutador == '4'):
                    ver_detalhes_lutador(dados['lutadores'])
                    
                # opcao 5 -> voltar ao menu principal
                if (escolha_menu_lutador == '5'):
                    voltar_ao_menu_principal = True


        # OPÇÃO 3 ESCOLHIDA -> TORNEIO ALEATÓRIO
        if (escolha_menu_principal == '3'):
            torneio_aux = criar_torneio_aleatorio()
            dados["torneios"][torneio_aux.nome] = torneio_aux
            num_lutadores = random.randint(15,50)
            for i in range(0,num_lutadores,1):
                lutador_aux = criar_lutador_aleatorio()
                dados["lutadores"][lutador_aux.nome] = lutador_aux
                inscrever_lutador_torneio(dados["lutadores"][lutador_aux.nome],dados["torneios"][torneio_aux.nome])


        # OPCAO 4 ESCOLHIDA -> SAIR DO PROGRAMA
        if (escolha_menu_principal == '4'):
            sair_do_programa = True

    fechar_programa()

if __name__ == "__main__":
    main()
