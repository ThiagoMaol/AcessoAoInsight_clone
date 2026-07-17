import os
import re

def convert_file(file_path):
    try:
        # 1. Ler o arquivo em modo binário
        with open(file_path, 'rb') as f:
            raw_data = f.read()
        
        # 2. Verificar se o arquivo já está em UTF-8 válido
        try:
            decoded_content = raw_data.decode('utf-8')
            # Se decodificou com sucesso em UTF-8 e não possui o caractere de substituição U+FFFD (),
            # ou se possui mas o charset já é utf-8, podemos assumir que já está em UTF-8.
            is_utf8 = True
        except UnicodeDecodeError:
            # Se falhou, o arquivo contém sequências inválidas de UTF-8 (provavelmente Latin-1/ISO-8859-1)
            is_utf8 = False
        
        if not is_utf8:
            # Decodificar usando ISO-8859-1 (Latin-1) para recuperar os acentos originais
            content = raw_data.decode('latin1')
            print(f"[CONVERTENDO] {file_path} (ISO-8859-1 -> UTF-8)")
        else:
            content = decoded_content
            # Se já está em UTF-8 mas ainda contém a tag apontando para ISO-8859-1, precisamos atualizar a tag
            if re.search(r'charset=["\']?iso-8859-1["\']?', content, re.IGNORECASE):
                print(f"[ATUALIZANDO TAG] {file_path} (Apenas corrigindo tag de charset)")
            else:
                # Já está tudo certo com o arquivo
                return False

        # 3. Atualizar a declaração de charset no HTML
        # Substitui charset=ISO-8859-1 ou charset="ISO-8859-1" por charset="utf-8"
        new_content = re.sub(
            r'charset=["\']?iso-8859-1["\']?', 
            'charset="utf-8"', 
            content, 
            flags=re.IGNORECASE
        )
        
        # Também corrige a tag http-equiv que mistura X-UA-Compatible com charset se necessário
        # Exemplo: <meta http-equiv="X-UA-Compatible" content="IE=edge" charset="ISO-8859-1">
        # Poderíamos simplificar para: <meta charset="utf-8">
        # Mas para preservar a estrutura, apenas mudar o charset já é suficiente e seguro.

        # 4. Salvar o arquivo de volta codificado em UTF-8
        with open(file_path, 'w', encoding='utf-8', newline='') as f:
            f.write(new_content)
        
        return True

    except Exception as e:
        print(f"[ERRO] Falha ao processar {file_path}: {e}")
        return False

def main():
    print("Iniciando conversão de arquivos HTML para UTF-8...")
    
    # Pastas e arquivos a serem ignorados
    ignored_dirs = {'.git', '.github', 'node_modules', 'bootstrap', 'fonts'}
    
    converted_count = 0
    total_html_files = 0
    
    for root, dirs, files in os.walk('.'):
        # Filtrar diretórios para não entrar nos ignorados
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        
        for file in files:
            if file.endswith('.html'):
                total_html_files += 1
                file_path = os.path.join(root, file)
                if convert_file(file_path):
                    converted_count += 1
                    
    print(f"\nConcluído! Total de arquivos HTML encontrados: {total_html_files}")
    print(f"Arquivos convertidos/atualizados: {converted_count}")

if __name__ == '__main__':
    main()
