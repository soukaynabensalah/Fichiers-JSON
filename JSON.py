import json


data = {
    "nom": "Jean",
    "age": 25,
    "ville": "Paris"
}

with open("data.json", "w") as file:
    json.dump(data, json_file, indent=2)

with open("data.json", "r") as file:
    ld = json.load(file)
    print("Contenu du fichier initial :")
    print(ld)


ld["langage"] = "Python"


with open("data.json", "w") as file:
    json.dump(ld, file, indent=2)

with open("data.json", "r") as file:
    md = json.load(file)
    print("\nContenu du fichier après modification :")
    print(md)
