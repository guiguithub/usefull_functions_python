import os

#check si fichier existe le crée s'il n'existe pas et retourne le fichier
def checkfileExists(filename,modeIfExists):
    if os.path.exists(filename):
        f = file(filename, modeIfExists)
    else: #if doesn't exists create file
        f = file(filename, "w+")
    return f
