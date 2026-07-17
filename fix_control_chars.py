import os

def main():
    print("Iniciando correção de caracteres de controle (travessões, aspas, etc)...")
    
    # Gera o mapeamento de caracteres de controle Latin-1 (U+0080 a U+009F)
    # para os caracteres correspondentes corretos da tabela Windows-1252 (CP1252)
    cp1252_translation = {}
    for i in range(0x80, 0xA0):
        try:
            control_char_code = i
            correct_char = bytes([i]).decode('cp1252')
            if chr(control_char_code) != correct_char:
                cp1252_translation[control_char_code] = correct_char
        except UnicodeDecodeError:
            pass

    ignored_dirs = {'.git', '.github', 'node_modules', 'bootstrap', 'fonts'}
    fixed_count = 0
    total_files = 0

    for root, dirs, files in os.walk('.'):
        dirs[:] = [d for d in dirs if d not in ignored_dirs]
        for file in files:
            if file.endswith('.html'):
                total_files += 1
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    
                    # Verifica se o arquivo tem algum caractere de controle na faixa problemática
                    has_broken = any(chr(code) in content for code in cp1252_translation.keys())
                    
                    if has_broken:
                        # Corrige traduzindo os caracteres de controle para os corretos
                        fixed_content = content.translate(cp1252_translation)
                        with open(file_path, 'w', encoding='utf-8', newline='') as f:
                            f.write(fixed_content)
                        fixed_count += 1
                        print(f"[CORRIGIDO] {file_path}")
                except Exception as e:
                    print(f"[ERRO] Falha ao processar {file_path}: {e}")

    print(f"\nCorreção concluída!")
    print(f"Total de arquivos HTML verificados: {total_files}")
    print(f"Arquivos corrigidos: {fixed_count}")

if __name__ == '__main__':
    main()
