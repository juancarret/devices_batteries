import json
import pandas as pd
import pathlib

def json_to_csv(file_name):
    if pathlib.Path(file_name).exists():
        with open(file_name, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)

        df = pd.json_normalize(data, errors='ignore')

        df.to_csv('devices.csv', index=False)
        print('Ordenes .csv creada exitosamente!')
    else:
        print(f'El archivo {file_name} no existe.')


def main():
    file_name = 'devices.json'
    json_to_csv(file_name)

if __name__ == '__main__':
    main()