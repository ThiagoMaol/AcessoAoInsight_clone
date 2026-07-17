with open('familiarizando-se_com_suttas.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Vamos achar a linha que contem "Cânone em Pali"
for idx, line in enumerate(lines):
    if "Cânone em Pali" in line:
        print(f"Linha {idx+1}: {line.strip()}")
        # Imprimir o unicode de cada caractere ao redor do travessao
        # Procurar o indice do caractere apos "Pali "
        pali_idx = line.find("Pali")
        if pali_idx != -1:
            snippet = line[pali_idx:pali_idx+15]
            print(f"Trecho: {snippet!r}")
            for char in snippet:
                print(f"  Caractere: {char!r} | Unicode: U+{ord(char):04X}")
