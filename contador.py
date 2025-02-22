import os

# Nome do arquivo onde a contagem será salva
arquivo = "contador.txt"

# Se o arquivo já existir, carregamos o valor salvo
if os.path.exists(arquivo):
    with open(arquivo, "r") as f:
        contador = int(f.read())
else:
    contador = 0

print("Contador de cliques. Pressione Enter para contar (Ctrl+C para sair).")

while True:
    input()
    contador += 1
    print(f"Cliques: {contador}")

    # Salvar a contagem no arquivo
    with open(arquivo, "w") as f:
        f.write(str(contador))
