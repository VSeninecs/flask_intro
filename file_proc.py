FILE_NAME = "DATA.txt"

def pievienot(rindina):
    f = open(FILE_NAME, "a", encoding="utf-8")
    for rinda in rindina:
        f.write(rinda + "`")
    f.write('\n')
    f.close()

def lasit():
    f = open(FILE_NAME, "r", encoding="utf-8")
    rindinas = f.readlines()
    return rindinas
    f.close()
