import os
import re

# Caminho do diretório onde estão seus arquivos .pas e .dfm
PROJECT_DIRECTORY = "D:/Desenvolvimento/Delphi/Projetos/05 - Alexandria/ATISolution/App-ERP"

# Função para ler e substituir os tipos nos arquivos
def replace_field_types(file_path):
    # Tenta abrir usando UTF-8
    try:
        with open(file_path, 'r', encoding='utf-8-sig') as file:
            content = file.read()
    except UnicodeDecodeError:
        # Se falhar, tenta com Latin-1
        with open(file_path, 'r', encoding='latin-1') as file:
            content = file.read()

    # Regex para identificar os campos no DFM ou no .pas
    # Substituir TBCDField por TFloatField
    content = re.sub(r'\bTBCDField\b', 'TFloatField', content)
    # Substituir TFMTBCDField por TFloatField
    content = re.sub(r'\bTFMTBCDField\b', 'TFloatField', content)

    # Substituir outros tipos se necessário (exemplo para TCurrencyField, TDateTimeField)
    content = re.sub(r'\bTDateField\b', 'TDatetimeField', content)

    # Escrever o arquivo novamente em UTF-8 para preservar todos os caracteres
    with open(file_path, 'w', encoding='utf-8-sig') as file:
        file.write(content)

# Função para percorrer o diretório e processar os arquivos .dfm e .pas
def process_project_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.dfm') or file.endswith('.pas'):
                file_path = os.path.join(root, file)
                replace_field_types(file_path)
                print(f"Processed: {file_path}")

if __name__ == "__main__":
    # Chamar a função para processar todos os arquivos no diretório do projeto
    process_project_files(PROJECT_DIRECTORY)
