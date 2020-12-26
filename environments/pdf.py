from reportlab.pdfgen import canvas
import random
import string
import sys

tipoletras    = ['A','B','C','D','E','F']
tiponumeros   = ['0','1','2','3','4','5','6','7','8','9']
tiposerie     = ['1','2','3']
nenhum        = ['','','','','','','','','']

questoes      = [1,2,3,4,5,6,8,9,10,11,13,14]
qtdques       = [5,5,5,5,5,5,5,4,2,3,5,5,4,4,4,5,5,5,5,5,5,5,5,4,3,5,5,5,5,5,5,5,5,5,5,5,4,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,4,4,4,4,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,5,6,6,6,6,5,5,5,5,5,4,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,4,4,4,4,3,3,3,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4]

questoescur   = [7,10]
espacocur     = [3,7]

questoesdes   = [12,15]
espacodes     = [20,60]

raiocabe      = 2.5
distancur     = 6
inicio        = 235
raio          = 2.5 
tamf          = 4
distangab     = 5 

distangab+= raio

escola        = sys.argv[1]
disciplina    = sys.argv[2]
prof          = sys.argv[3]

def desenhaPerimetro(canvas,posx1,posy1,posx2,posy2):
    canvas.setLineWidth(mm2p(1))
    retanguloMM(canvas,posx1,posy1,posx2,posy2)


    
def desenhaBolas(canvas,posx1,posy1,qtd,r,tipo):
    n=0
    while(n<qtd):
        circuloMM(canvas,posx1+r,posy1,r)
        canvas.setFontSize(mm2p(r*2)*0.95)
        desenharTexto(canvas,posx1+r/3,posy1-2*r/3,tipo[n])
        posx1+=2*r+1
        n+=1

def desenhaBolasPre(canvas,posx1,posy1,qtd,r):
    n=0
    while(n<qtd):
        circuloMMPre(canvas,posx1+r,posy1,r)
        posx1+=2*r+1
        n+=1
       
def criaQuesCur(canvas,ques,espaco,posy,tam,tamfo,posyipag):
    posx=10
    num=len(ques)
    n1=0
    canvas.setFontSize(mm2p(tamfo))
    while(n1<num):
        n=ques[n1]
        posy+=-10
        if(posy<espaco[n1]*tam):
            novaPag(canvas,raiocabe,tamf)
            posy=posyipag
        if(n<10):
            desenharTexto(canvas,posx-2*p2mm(tamfo)/5,posy-mm2p(tamfo)/10,str(n)+'-') 
        else:
            desenharTexto(canvas,posx-3*p2mm(tamfo)/5,posy-mm2p(tamfo)/10,str(n)+'-') 
        n2=1
        while(n2<=espaco[n1]):
            
            canvas.setLineWidth(0.5)
            canvas.rect(mm2p(posx+3*mm2p(tamfo)/5),mm2p(posy),mm2p(183),0.0001)
            n2+=1
            posy+=-tam
        print("Cur",n,posx-5,posy,205,posy+espaco[n1]*tam+10)
        ##desenhaPerimetro(canvas,posx-5,posy,200,espaco[n1]*tam+10)
        teste(canvas,posx-5,posy,205,posy+espaco[n1]*tam+10)
        n1+=1
        
    m=posy
    return m
        
def criaQuesDes(canvas,ques,espaco,posy,tamfo,posyipag):
    posx=10
    num=len(ques)
    n1=0
    canvas.setFontSize(mm2p(tamfo))
    while(n1<num):
        n=ques[n1]
        posy+=-10
        if(posy<espaco[n1]):
            novaPag(canvas,raiocabe,tamf)
            posy=posyipag
        if(n<10):
            desenharTexto(canvas,posx-2*p2mm(tamfo)/5,posy-mm2p(tamfo)/10,str(n)+'-') 
        else:
            desenharTexto(canvas,posx-3*p2mm(tamfo)/5,posy-mm2p(tamfo)/10,str(n)+'-') 
        
        canvas.setLineWidth(0.5)
        desenhaPerimetro(canvas,posx+3*mm2p(tamfo)/5,posy-espaco[n1],
             190-3*mm2p(tamfo)/5,espaco[n1])
        posy+=-espaco[n1]
        
        print("Des",n,posx-5,posy-5,205,posy+espaco[n1]+5)
        ##desenhaPerimetro(canvas,posx-5,posy-5,200,espaco[n1]+10)
        teste(canvas,posx-5,posy-5,205,posy+espaco[n1]+5)
        n1+=1
        
def criaGab(canvas,livre,questoes,qtdques,tamfo,posyi,posyipag,dis,r):
    num = len(questoes)
    j=0
    maior=0
    while(j<num):
        d=qtdques[j]
        if(d>maior):
            maior=d
        j+=1
    npa=int((inicio+dis/2)/dis)-1
    if((inicio+dis/2)%dis>0):
        npa+=1
    npa=npa*3
    if(num>npa):
        num1=num
        num=npa
        pecasx=int((inicio+dis/2)/dis)
        pecasy=int(npa/pecasx)
        print(num,npa,pecasx,pecasy)
    else:
        num1=num
        pecasx=int(livre/dis)
        pecasy=int(num/pecasx)
    if(num%pecasx>0 and pecasy<=2):
        pecasy+=1
    if(pecasy==3):
        posx=210/6-((maior*(r*2+1)-1)-3*mm2p(tamfo)/5)/2
    elif(pecasy==2):
        posx=210/4-((maior*(r*2+1)-1)-3*mm2p(tamfo)/5)/2
    else:
        posx=210/2-((maior*(r*2+1)-1)-3*mm2p(tamfo)/5)/2
    posy=posyi
    n1=0
    pp=0
    pq=0
    pi=0
    pa=int(num/pecasy)        
    if(num-pa*pecasy>0):
        pp=1
        if(num-pa*pecasy>1):
            pq=1      
    a=0
    while(n1<num1):
        n=questoes[n1]
        canvas.setFontSize(mm2p(tamfo))
        if(n<10):
            desenharTexto(canvas,posx-2*mm2p(tamfo)/5,posy-mm2p(tamfo)/10,str(n)+'-') 
        else:
            desenharTexto(canvas,posx-3*mm2p(tamfo)/5,posy-mm2p(tamfo)/10,str(n)+'-') 
        desenhaBolas(canvas,posx,posy,qtdques[n1],r,tipoletras)
        
        print("Gab",n,qtdques[n1],r,posx-0.5,posy-r-0.5,posx-0.5+qtdques[n1]*(1+2*r),posy-r-0.5+r*2+1)
        ##desenhaPerimetro(canvas,posx-0.5,posy-r-0.5,qtdques[n1]*(1+2*r),r*2+1)
        teste(canvas,posx-0.5,posy-r-0.5,posx-0.5+qtdques[n1]*(1+2*r),posy-r-0.5+r*2+1)
        
        posy+=-dis
        if(n1+1==pa+pi+pp):
            if(a!=1):
                posy=posyi
            else:
                posy=posyipag
            posx+=210/pecasy
        if(n1+1==2*pa+pi+pq+pp):
            if(a!=1):
                posy=posyi
            else:
                posy=posyipag
            posx+=210/pecasy
        n1+=1
        if(n1==npa):
            a=1
            novaPag(canvas,raiocabe,tamf)
            posx=(210/6-((maior*(r*2+1)-1)-3*mm2p(tamfo)/5)/2)
            posy=posyipag
            pp=0
            pq=0
            pa=int((num1-npa)/pecasy)
            if((num1-npa)-pa*pecasy>0):
                pp=1
                if((num1-npa)-pa*pecasy>1):
                    pq=1 
            pi=npa
    if(num1>npa):        
        m=int(posyipag-((pa+pp)*dis-dis/2))
    else: 
        m=int(posyi-((pa+pp)*dis-dis/2))
    return m
            
def circuloMM(canvas,centroX,centroY,r):
    canvas.setLineWidth(mm2p(0.2))
    canvas.circle(mm2p(centroX), mm2p(centroY), mm2p(r))
    
def circuloMMPre(canvas,centroX,centroY,r):
    canvas.setLineWidth(mm2p(r))
    canvas.circle(mm2p(centroX), mm2p(centroY), mm2p(r/2))

def teste(canvas,posx,posy,posx1,posy1):
    ##desenhaPerimetro(canvas,posx,posy,posx1-posx,posy1-posy)
    return 0
def retanguloMM(canvas,posx1,posy1,posx2,posy2):
    canvas.setLineWidth(2)
    canvas.rect(mm2p(posx1),mm2p(posy1),mm2p(posx2),mm2p(posy2))
  
def mm2p(milimetros):
    return milimetros / 0.352777

def p2mm(pixels):
    return pixels*0.352777

def desenharTexto(canvas,x,y,texto):
    canvas.drawString(mm2p(x),mm2p(y),texto)

def retangulo(canvas,tam,posx,posy,posx1,posy1):
    canvas.setLineWidth(mm2p(tam))
    canvas.rect(mm2p(posx),mm2p(posy),mm2p(posx1)-mm2p(posx),mm2p(posy1)-mm2p(posy))

def desenhaBorda(canvas):
    retangulo(canvas,4,5,290,7,292)
    #retangulo(canvas,1,20,277,35,275)
    
    retangulo(canvas,4,203,290,205,292)
    #retangulo(canvas,1,188,262,190,277)
    
    retangulo(canvas,4,5,5,7,7)
    #retangulo(canvas,1,20,22,35,20)
    
    retangulo(canvas,4,203,5,205,7)
    #retangulo(canvas,1,188,20,190,35)

def novaPag(canvas,r,tam):
    
    canvas.showPage()
    
    desenhaBorda(canvas)
    desenhaPerimetro(canvas,10,264,190,23)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,280,"Pág:")
    desenhaBolasPre(canvas,130+8*mm2p(tam)/5,280+mm2p(tamf)/10,canvas.getPageNumber(),r)
    
    print("Pag",canvas.getPageNumber(),r,130+8*mm2p(tam)/5-0.5,280+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+canvas.getPageNumber()*(1+2*r),280+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,280+mm2p(tam)/10-r-0.5,canvas.getPageNumber()*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,280+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+canvas.getPageNumber()*(1+2*r),280+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,274,"Turma:")
    desenhaBolas(canvas,130+8*mm2p(tam)/5,274+mm2p(tam)/10,4,r,tipoletras)
    
    print("Tur",4,r,130+8*mm2p(tam)/5-0.5,274+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+4*(1+2*r),274+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,274+mm2p(tam)/10-r-0.5,4*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,274+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+4*(1+2*r),274+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,268,"Série:")
    desenhaBolas(canvas,130+8*mm2p(tam)/5,268+mm2p(tam)/10,3,r,tiposerie)
    
    print("Ser",3,r,130+8*mm2p(tam)/5-0.5,268+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+3*(1+2*r),268+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,268+mm2p(tam)/10-r-0.5,3*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,268+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+3*(1+2*r),268+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,12,280,"Número:")  
    
    desenhaBolas(canvas,12+7*mm2p(tam)/5,281,10,2.5,tiponumeros)
    desenhaBolas(canvas,12+7*mm2p(tam)/5,275,10,2.5,tiponumeros)
    
    print("Num1",10,r,12+7*mm2p(tam)/5-0.5,281-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),281-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,12+7*mm2p(tam)/5-0.5,281-r-0.5,10*(1+2*r),r*2+1)
    teste(canvas,12+7*mm2p(tam)/5-0.5,281-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),281-r-0.5+r*2+1)
    print("Num2",10,r,12+7*mm2p(tam)/5-0.5,275-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),275-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,12+7*mm2p(tam)/5-0.5,275-r-0.5,10*(1+2*r),r*2+1)
    teste(canvas,12+7*mm2p(tam)/5-0.5,275-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),275-r-0.5+r*2+1)

def cabePrinci(canvas,tam,esc,dis,pro,r):
    
    desenhaPerimetro(canvas,10,247,190,40)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,12,280,"Escola: "+esc)
    desenharTexto(canvas,12,274,"Disciplina: "+dis)
    desenharTexto(canvas,12,268,"Prof.: "+pro)
    desenharTexto(canvas,12,262,"Aluno: ________________________________")
    desenharTexto(canvas,12,256,"Número: ")    
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,280,"Pág:")
    desenhaBolasPre(canvas,130+8*mm2p(tam)/5,280+mm2p(tam)/10,canvas.getPageNumber(),r)
    
    print("Pag",canvas.getPageNumber(),r,130+8*mm2p(tam)/5-0.5,280+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+canvas.getPageNumber()*(1+2*r),280+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,280+mm2p(tam)/10-r-0.5,canvas.getPageNumber()*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,280+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+canvas.getPageNumber()*(1+2*r),280+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,274,"Tinta:")
    desenhaBolas(canvas,130+8*mm2p(tam)/5,274+mm2p(tam)/10,1,r,nenhum)
    
    print("Tin",1,r,130+8*mm2p(tam)/5-0.5,274+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+1*(1+2*r),274+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,274+mm2p(tam)/10-r-0.5,1*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,274+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+1*(1+2*r),274+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,268,"Revisão:")
    desenhaBolas(canvas,130+8*mm2p(tam)/5,268+mm2p(tam)/10,1,r,nenhum)
    
    print("Rev",1,r,130+8*mm2p(tam)/5-0.5,268+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+1*(1+2*r),268+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,268+mm2p(tam)/10-r-0.5,1*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,268+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+1*(1+2*r),268+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,262,"Turma:")
    desenhaBolas(canvas,130+8*mm2p(tam)/5,262+mm2p(tam)/10,4,r,tipoletras)
    
    print("Tur",4,r,130+8*mm2p(tam)/5-0.5,262+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+4*(1+2*r),262+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,262+mm2p(tam)/10-r-0.5,4*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,262+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+4*(1+2*r),262+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    desenharTexto(canvas,130,256,"Série:")
    desenhaBolas(canvas,130+8*mm2p(tam)/5,256+mm2p(tam)/10,3,r,tiposerie)
    
    print("Ser",3,r,130+8*mm2p(tam)/5-0.5,256+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+3*(1+2*r),256+mm2p(tam)/10-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,130+8*mm2p(tam)/5-0.5,256+mm2p(tam)/10-r-0.5,3*(1+2*r),r*2+1)
    teste(canvas,130+8*mm2p(tam)/5-0.5,256+mm2p(tam)/10-r-0.5,130+8*mm2p(tam)/5-0.5+3*(1+2*r),256+mm2p(tam)/10-r-0.5+r*2+1)
    
    canvas.setFontSize(mm2p(tam))
    
    desenhaBolas(canvas,12+7*mm2p(tam)/5,257,10,r,tiponumeros)
    desenhaBolas(canvas,12+7*mm2p(tam)/5,251,10,r,tiponumeros)
    
    print("Num1",10,r,12+7*mm2p(tam)/5-0.5,257-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),257-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,12+7*mm2p(tam)/5-0.5,257-r-0.5,10*(1+2*r),r*2+1)
    teste(canvas,12+7*mm2p(tam)/5-0.5,257-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),257-r-0.5+r*2+1)
    print("Num2",10,r,12+7*mm2p(tam)/5-0.5,251-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),251-r-0.5+r*2+1)
    ##desenhaPerimetro(canvas,12+7*mm2p(tam)/5-0.5,251-r-0.5,10*(1+2*r),r*2+1)
    teste(canvas,12+7*mm2p(tam)/5-0.5,251-r-0.5,12+7*mm2p(tam)/5-0.5+10*(1+2*r),251-r-0.5+r*2+1)
    
def criarPdf(arquivo,escola,disciplina,prof,raiocabe,questoes,qtdques,questoesdes,espacodes,distancur,inicio,raio,tamf,distangab,espacocur,questoescur):
    cnv = canvas.Canvas(arquivo)
    
    desenhaBorda(cnv)
    
    cabePrinci(cnv,tamf,escola,disciplina,prof,raiocabe)

    espacominob = int(len(questoes)/3*distangab)
    if(len(questoes)%3>0):
        espacominob+=1
    if(espacominob%distangab>0):
        espacominob+=distangab-espacominob%distangab
    soma = 0
    for i in espacocur:
        soma+=i
    espacomincur = len(questoescur)*10+soma*distancur
    
    soma = 0
    for i in espacodes:
        soma+=i
    espacomindes = len(questoesdes)*10+soma
    
    espacolivre=inicio+distangab/2-espacomincur-espacomindes-10
    if(espacolivre<espacominob):
        espacolivre=espacominob

    novoy = criaGab(cnv,espacolivre,questoes,qtdques,tamf,inicio,252,distangab,raio)
    novoy = criaQuesCur(cnv,questoescur,espacocur,novoy,distancur,tamf,252)
    criaQuesDes(cnv,questoesdes,espacodes,novoy,tamf,252)
    cnv.save()

def criarPdfRand(numero):
    j=0
    while(j<numero):
        questoes=[]
        qtdques=[]
        questoescur=[]
        espacocur=[]
        questoesdes=[]
        espacodes=[]

        nq=random.randrange(1, 30)
        n=0
        while(n<nq):
          questoes.append(n)
          qtdques.append(random.randrange(1,6))
          n+=1
       
        nqc=random.randrange(1, 5)
        n=0
        while(n<nqc):
            questoescur.append(n)
            espacocur.append(random.randrange(1,4))
            n+=1
        nqd=random.randrange(1,4)
        n=0
        while(n<nqd):
            questoesdes.append(n)
            espacodes.append(random.randrange(1,20))
            n+=1
        
        arquivo=str(j)+".pdf"
        escola=""
        disciplina=""
        prof=""
        nqe=random.randrange(5, 20)
        n=0
        while(n<nqe):
            escola+=random.choice(string.ascii_uppercase)
            n+=1
        disciplina=""
        nqdi=random.randrange(5, 20)
        n=0
        while(n<nqdi):
            disciplina+=random.choice(string.ascii_uppercase)
            n+=1
        prof=""
        nqp=random.randrange(5, 20)
        n=0
        while(n<nqp):
            prof+=random.choice(string.ascii_uppercase)
            n+=1
        
        criarPdf(arquivo,escola,disciplina,prof,raiocabe,questoes,qtdques,questoesdes,espacodes,distancur,inicio,raio,tamf,distangab,espacocur,questoescur)
        j+=1
    
    
    
    

criarPdf("./public/pdf/gab.pdf",escola,disciplina,prof,raiocabe,questoes,qtdques,questoesdes,espacodes,distancur,inicio,raio,tamf,distangab,espacocur,questoescur)

 