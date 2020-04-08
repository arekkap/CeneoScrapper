#import bibliotek
import os
import pandas as pd

#wyświetlenie zawartości
print(os.listdir("./opinions"))

#wczytanie ID produktu
product_id = input("Podaj kod produktu: ")

opinions = pd.read_json("opinions/"+product_id+".json")
opinions = opinions.set_index("opinion_id")
print(opinions)