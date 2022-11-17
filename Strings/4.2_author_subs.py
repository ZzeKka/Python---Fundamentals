def author_replace(str, list):
    for name in list:
        str = str.replace(name,"_")
    return str

phrase = "Ola Jose Gomes cheiras mal do cu como o Joao Maria mas tu Jose Gomes cheiras melhor"
names = ["Jose Gomes","Joao Maria"]

print(author_replace(phrase, names))

