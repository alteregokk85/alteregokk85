import configparser
import json
import os

# Konfigurationsdatei lesen
config = configparser.ConfigParser()
config.read('Settings.config')
input_folder_path = config['input_folder']['path']

# Überprüfen, ob der Ordner existiert
if not os.path.exists(input_folder_path):
    raise Exception(f"Der Ordner {input_folder_path} existiert nicht.")

# JSON-Dateien einlesen und als Dictionarys speichern
fhir_dictionaries = []
for file_name in os.listdir(input_folder_path):
    if file_name.endswith('.json'):
        file_path = os.path.join(input_folder_path, file_name)
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            fhir_dictionaries.append(data)

# Ergebnisse ausgeben (Beispiel)
for i, fhir_dict in enumerate(fhir_dictionaries):
    print(f"Datei {i}: {fhir_dict}\n")
