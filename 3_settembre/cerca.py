import os
print()

def CercaStringaInNomefile(sFile: str, sStringa: str):

    #mettiamo tutto minuscolo

    sFile = sFile.lower()
    sStringa = sStringa.lower()

    #usiamo sFile.Lower.find() che torna -1 se la parola non c'è e la pos altrimenti
    #torniamo true oppure false

    if sStringa in sFile:

        return True
    
    else:

        return False
    
def CercaStringaInTextfile(sFile: str, sStringa: str):

    check = -1

    with open(sFile, "r") as file1:

        sRiga = file1.readline()

        while(len(sRiga)>0):

            check = sRiga.lower().find(sStringa.lower())

            if(check >= 0):

                return True
            
            sRiga = file1.readline()

            
def CercaStringaInPDFfile(sFile, sStringa):
    return False
    
def CercaStringaInContenutofile(sPathFile, sStringa):
    
    sOutFileName, sOutFileExt = os.path.splitext(sPathFile)
    check: bool = False

    if sOutFileExt.lower() == ".txt":
        check = CercaStringaInTextfile(sPathFile, sStringa)

    elif sOutFileExt.lower() == ".pdf":

        check = CercaStringaInPDFfile(sPathFile, sStringa)

    return check


sRoot = input("Inserisci directory in cui cercare ")
sParola = input("Inserisci parola da cercare ")
sOutDir = input("Inserisci directory di output ")

print()

iNumFileTrovati: int = 0

for root, dirs, files in os.walk(sRoot):

    print()

    print(f"Sto guardando {root} che contiene {len(dirs)} subdir e {len(files)} files")

    for file in files:

        print(f"Devo vedere se {file} contiene {sParola}")
        check: bool = (CercaStringaInNomefile(file, sParola))

        if check:

            iNumFileTrovati += 1

        else:

            sFilePathCompleto: str = os.path.join(root, file)

            check = CercaStringaInContenutofile(sFilePathCompleto, sParola)

            if check:

                iNumFileTrovati += 1

    
    print(f"Ho trovato {iNumFileTrovati} files")