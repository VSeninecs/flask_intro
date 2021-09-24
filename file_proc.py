FILE_NAME = "DATA.txt"

def pievienot(rindina):
    f = open(FILE_NAME, "a", encoding="utf-8")
    for rinda in rindina:
        f.write(rinda + "\n")

    f.write("Ziņas beigas" + "\n")
    f.close()

def lasīt():
    with open(FILE_NAME, r, encoding="uth-8") as f:
        rindinas = f.readlines()
