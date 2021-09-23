FILE_NAME = "DATA.txt"

def pievienot(rindina):
    f = open(FILE_NAME, "a")
    f.write(rindina + "\n")
    f.close()