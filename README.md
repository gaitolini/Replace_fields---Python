# 🚀 Projeto de Substituição Automática de Tipos de Campos (Delphi)

## 🎯 Objetivo do Projeto
Este projeto foi criado para **automatizar a substituição de tipos de campos** em arquivos `.dfm` e `.pas` de um projeto Delphi. O objetivo principal é lidar com uma situação em que mais de 2200 campos foram mapeados incorretamente pelo FireDAC após alterações no banco de dados. Em vez de fazer ajustes manuais, que seriam muito demorados e sujeitos a erros, este script em **Python** permite **modificar automaticamente** os tipos de campos, garantindo que eles sejam corrigidos para evitar erros de execução e compilação.

### 🛠️ Necessidade
Durante a alteração do banco de dados, os campos `Decimal` e `Numeric` do SQL Server acabaram sendo mapeados como `TBCDField` e `TFMTBCDField` no Delphi, mas, para um funcionamento correto e padronização no código, eles precisam ser `TFloatField` ou outro tipo apropriado (por exemplo, `TDateTimeField` para campos de data). De forma manual, é necessário abrir cada `TFDQuery`, deletar os campos no editor e recriá-los, o que é extremamente ineficiente. Assim, este script foi desenvolvido para acelerar esse processo e reduzir o risco de erros.

## 🖥️ Tecnologias Utilizadas
Este projeto foi desenvolvido em **Python**, utilizando as seguintes bibliotecas:

- **os**: Para percorrer as pastas do projeto e localizar os arquivos `.dfm` e `.pas`.
- **re** (Regular Expressions): Para buscar e substituir tipos de campos nos arquivos, garantindo que apenas as ocorrências corretas sejam modificadas.

### ⚙️ Principais Funcionalidades
- **🔄 Substituição Automática de Tipos de Campo**: O script localiza todos os campos que são do tipo `TBCDField` e `TFMTBCDField` e os substitui por `TFloatField`. Também inclui a substituição de `TDateField` por `TDateTimeField`.
- **🛡️ Manutenção da Codificação Correta**: O script cuida da leitura e escrita dos arquivos usando `utf-8-sig` ou `latin-1`, garantindo que caracteres especiais e acentos sejam preservados corretamente.

## 📋 Como Utilizar
1. **Clone o repositório** na sua máquina local.
2. **Edite o caminho do projeto** para que o `PROJECT_DIRECTORY` aponte para o diretório onde estão seus arquivos `.dfm` e `.pas`.
3. **Execute o script** usando Python:
   ```sh
   python replace_fields.py
   ```
4. O script percorrerá todas as pastas e processará os arquivos, informando quais arquivos foram modificados.

## 🤖 Como o ChatGPT Ajudou
Este código foi desenvolvido com a assistência do **ChatGPT** da OpenAI. O ChatGPT ajudou na criação da estrutura do script, sugerindo as bibliotecas mais apropriadas, a lógica para percorrer os diretórios e o uso de expressões regulares para substituir corretamente os tipos de campos nos arquivos `.dfm` e `.pas`. 

Além disso, o ChatGPT ajudou a resolver problemas de codificação que surgiram ao manipular arquivos contendo caracteres especiais, garantindo que todo o conteúdo fosse preservado de forma correta. 🎉

## 🔚 Considerações Finais
Este script foi criado para ser uma solução eficiente para um problema que, manualmente, demandaria um grande esforço e tempo. Usar Python permite a flexibilidade de adaptar rapidamente o script para atender a outras necessidades semelhantes. Caso encontre problemas ou deseje fazer ajustes, sinta-se à vontade para modificar o código conforme as especificações do seu projeto.

Se precisar de mais ajuda ou orientação, estou aqui para apoiar! 😊

- LinkedIn: [Anderson Gaitolini](https://www.linkedin.com/in/andersongaitolini/)
- WhatsApp: [Entre em contato](https://wa.me/qr/CFND4RGOJHHUN1)
<div align="center">
  <img src="https://github.com/user-attachments/assets/a019d3e6-5a04-4124-b42b-b5824d1f92d5" alt="image" width="300"/>
</div>
