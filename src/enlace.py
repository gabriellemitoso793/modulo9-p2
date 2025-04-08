import sys

def calcular_bits_paridade(m):
    #calcula a quantidade de bits de paridade necessários para o tamanho de mensagem
    r = 0
    while (2**r) < (m + r + 1):
        r += 1
    return r

def gerar_hamming(bits):
    #gera o código de Hamming para o conjunto de bits
    m = len(bits)
    r = calcular_bits_paridade(m)
    hamming = ['0'] * (m + r)
    
    j = 0
    for i in range(1, len(hamming) + 1):
        if i & (i - 1) == 0:
            continue
        hamming[i - 1] = bits[j]
        j += 1
    
    for i in range(r):
        pos = 2**i - 1
        valor = 0
        for j in range(1, len(hamming) + 1):
            if j & (pos + 1):
                valor ^= int(hamming[j - 1])
        hamming[pos] = str(valor)
    
    return ''.join(hamming)

def verificar_hamming(bits):
    #verifica e corrige o código de Hamming
    n = len(bits)
    r = calcular_bits_paridade(n - calcular_bits_paridade(n))
    erro = 0
    
    for i in range(r):
        pos = 2**i - 1
        valor = 0
        for j in range(1, n + 1):
            if j & (pos + 1):
                valor ^= int(bits[j - 1])
        if valor:
            erro += pos + 1
    
    if erro:
        bits = list(bits)
        bits[erro - 1] = '1' if bits[erro - 1] == '0' else '0'
        bits = ''.join(bits)
    
    return bits, erro

def extrair_payload(bits):
    #remove os bits de paridade do código de Hamming
    r = calcular_bits_paridade(len(bits))
    mensagem = []
    for i in range(len(bits)):
        if (i + 1) & i:
            mensagem.append(bits[i])
    return ''.join(mensagem)

def remetente():
    #função do remetente que lê da entrada padrão e envia o frame via stdout
    mensagem = sys.stdin.read().strip()
    
    if not mensagem:
        sys.stderr.write("Erro: Nenhuma mensagem recebida.\n")
        sys.exit(1)
    
    header = '1010'  #header de sincronização
    terminador = '0101'  #terminador de sincronização
    hamming = gerar_hamming(mensagem)  #aplicando Hamming ao payload
    frame = header + hamming + terminador  #construção do frame
    
    sys.stdout.write(frame + "\n")  #envia o frame pela saída padrão

def destinatario():
    #função do destinatário que lê da entrada padrão e processa o frame 
    frame = sys.stdin.read().strip()
    
    if not frame:
        sys.stderr.write("Erro: Nenhum frame recebido.\n")
        sys.exit(1)

    if not frame.startswith('1010') or not frame.endswith('0101'):
        sys.stderr.write("Erro: Frame inválido\n")
        return
    
    dados = frame[4:-4]  #removendo cabeçalho e terminador
    corrigido, erro = verificar_hamming(dados)  #verificação e correção de erros
    payload = extrair_payload(corrigido)  #extraindo o payload
    
    if erro:
        sys.stdout.write(f"Erro corrigido na posição {erro}. Mensagem decodificada: {payload}\n")
    else:
        sys.stdout.write(f"Mensagem decodificada: {payload}\n")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.stderr.write("Uso correto: python src/enlace.py [remetente|destinatario]\n")
        sys.exit(1)
    
    if sys.argv[1] == "remetente":
        remetente()
    elif sys.argv[1] == "destinatario":
        destinatario()
    else:
        sys.stderr.write("Erro: Argumento inválido. Use 'remetente' ou 'destinatario'.\n")
        sys.exit(1)
