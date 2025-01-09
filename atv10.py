frases = []
frase1 = input('Digite uma frase: ').split()
frases.append(frase1)
for i,frase in enumerate (frases):
    resul = len(frase)
    print('tem {} palavras nessa frase'.format(resul))
