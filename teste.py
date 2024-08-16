def add_json(p1):
    add={"nome":input("nome: "),"Idade":input("idade: "),"Prontuário":input("Prontuário: "),"Portugues nota":input("Nota de portugues: "),"Matemática nota":input("Nota de matematica: "),"Ciencias nota":input("Nota de ciencias: "),"media":0,}
    p1.append(add)
def media_json(p1,id):
    n1=int(p1[id]["Portugues nota"])
    n2=int(p1[id]["Matemática nota"])
    n3=int(p1[id]["Ciencias nota"])
    p1[id]["media"]=(n1+n2+n3)/3
def exibir_json(p1):
    return print(p1)
p1=[{"nome":"Igor","Idade":"20 anos","Prontuário":"SP12345","Portugues nota":6,"Matemática nota":8,"Ciencias nota":10,"media":0,},
    {"nome":"Ana","Idade":"19 anos","Prontuário":"SP45678","Portugues nota":10,"Matemática nota":3,"Ciencias nota":9,"media":0,}]
add_json(p1)
for id in range(len(p1)): 
    media_json(p1,id)
for id in range(len(p1)): 
    print(p1[id])