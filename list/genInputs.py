from os import listdir
from os.path import isfile, join

path2dir = "./parts"

if __name__ == "__main__":
#     for f in listdir(path2dir):
#         print(join(path2dir,f))
#         if isfile(join(path2dir,f)):
#             print(f)

    myFiles = [f for f in listdir(path2dir) if isfile(join(path2dir, f))]

    myFiles.sort()
    myFiles = [join(path2dir,f) for f in myFiles]

    with open("./assets/files/inputs.tex", "w") as fopt:
        for f in myFiles:
            fopt.write("\\input{" + f + "}")
            print("\\input{" + f + "}")
