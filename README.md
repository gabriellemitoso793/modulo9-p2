# Implementação da camada de enlace

Este projeto implementa uma **camada de enlace** utilizando um protocolo próprio, incluindo cabeçalhos, terminadores e código de Hamming para correção de erros. 

## Funcionalidades
**Remetente:**
- Lê uma sequência de bits da entrada padrão.
- Adiciona cabeçalho e terminador para sincronização.
- Aplica código de Hamming para correção de erros.
- Envia o frame via `stdout`.

**Destinatário:**
- Lê um frame da entrada padrão.
- Sincroniza a leitura com base no cabeçalho e terminador.
- Verifica e corrige erros de 1 bit usando Hamming.
- Exibe a mensagem decodificada.

## Estrutura do Projeto
```sh
modulo9-p2/
│── src/
│   ├── __init__.py       
│   ├── enlace.py         
│   ├── cli.py            
│── main.py               
│── README.md             
```
## Como Executar

**Testar o remetente:**
```bash
echo "01101001" | python src/enlace.py remetente
```
Saída esperada:
```bash
1010110110011011010101
```

**Testar o destinatário:**
```bash
echo "1010110110011011010101" | python src/enlace.py destinatario
```
Saída esperada:
```bash
Mensagem decodificada: 01101001
```

**Comunicação entre remetente e destinatário:**
```bash
echo "01101001" | python src/enlace.py remetente | python src/enlace.py destinatario
```

Saída esperada:
```bash
Mensagem decodificada: 01101001
```