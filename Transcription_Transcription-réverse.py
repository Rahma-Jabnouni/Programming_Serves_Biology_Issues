def verification_seq(sequence,sequence_entre):
    x=[65,67,71,84]
    if (choix==2):
        x[-1]=85
    for base in range (len(sequence)):
        if ((ord(sequence[base]) in x)== True):
            sequence_entre=sequence_entre+sequence[base]
        else:
            print("La base n°",(base+1),"est invalide! Veuillé la corriger")
            base_corrige=input("Corrigez: ")
            while not ((ord(base_corrige) in x)== True):
                base_corrige=input("Corrigez: ")
            sequence_entre=sequence_entre+base_corrige
    return sequence_entre

#Trouver l'ARN à partir d'un brin d'ADN
def transcription_ADN_ARN(sequence_entre,sequence_sortie,bases_ARN,bases_ADN):
    for base in range(len(sequence_entre)):
        sequence_sortie=sequence_sortie+bases_ARN[(bases_ADN.index(sequence_entre[base]))]
    return sequence_sortie

#Trouver les deux brins d'ADN à partir de l'ARN
def transcription_ARN_ADN(sequence_entre,sequence_sortie,bases_ARN,bases_ADN):
    for base in range(len(sequence_entre)):
        sequence_sortie=sequence_sortie+bases_ADN[bases_ARN.index(sequence_entre[base])]
    sequence_sortie=sequence_sortie+chr(10)+' '
    bases_brin2=['A','T','C','G']
    for i in range ((len(sequence_sortie)-2)):
        sequence_sortie=sequence_sortie+bases_brin2[bases_ADN.index(sequence_sortie[i])]
    return sequence_sortie

#Saisie du choix
print("Bienvenue")
print("Choisissez quelle opération à effectuer:")
print("(Tapez le numéro saisie devant l'opération souhaité)")
print("1:Transcription de l'ADN en ARN")
print("2:Transcription réverse polymérase de l'ARN en ADN")
choix=int(input("Donnez votre choix ici: "))
affch=["ADN","ARN"]
aff="Donner la séquence d'"+affch[choix-1]+": "
while not (type(choix)==int):
    print("Il faut écrire un nombre!!")
while not ((choix==1) or (choix==2)):
    choix=int(input("Choix erroné! Essayez une autre fois: "))
sequence=input(aff)
sequence_entre=''
sequence_entre=verification_seq(sequence,sequence_entre)
bases_ARN=['A','U','C','G']
bases_ADN=['T','A','G','C']
operations=[transcription_ADN_ARN,transcription_ARN_ADN]
sequence_sortie=''
sequence_sortie=operations[(choix-1)](sequence_entre,sequence_sortie,bases_ARN,bases_ADN)
print("La séquence d'",affch[choix//2],"résultat est:",chr(10),sequence_sortie)