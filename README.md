# NetworkPingLogger (Python)
Este projeto consiste em um script de automação desenvolvido em **Python** para monitorar a disponibilidade de dispositivos na rede (hosts) e registrar o histórico de conectividade em um arquivo de log.

## Objetivo
Automatizar o processo de "ping", eliminando a necessidade de testes manuais e fornecendo um registro histórico (log) para análise posterior de quedas de conexão.

## Funcionalidades
- **Detecção Automática de SO:** Identifica se o sistema é Windows ou Linux para executar os parâmetros de comando corretos (Linha: 15, 36).
- **Registro de Log:** Salva automaticamente a data, hora, host e status da conexão em um arquivo `.txt` separado.
- **Formatação de Dados:** Utiliza a biblioteca `datetime` para carimbos de tempo precisos em cada teste.

## Tecnologias Utilizadas
- **Python 3.13.7**
- **Bibliotecas Nativas:**
  - `os`: Para interação com os comandos do sistema operacional.
  - `platform`: Para identificação da arquitetura e sistema.
  - `datetime`: Para manipulação de data e hora.
  - `time`: Para controle de fluxo e delay.

## Como executar:
1. Certifique-se de ter o Python instalado.
2. Clone este repositório:
   - git clone [[https://github.com/OlavoNicolas/NetworkPingLogger](https://github.com/OlavoNicolas/NetworkPingLogger.git))
   - Ative o agendador de tarefas do seu SO para o intervalo de tempo que desejar executar o programa.
