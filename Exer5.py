num = input("Digite um número:")

string = ""

tamanho =  len(num)
tamanho = tamanho -1

while tamanho >= 0:
    string = string + num[tamanho]
    tamanho -= 1

print(f"Este é o número invertido: {string}")