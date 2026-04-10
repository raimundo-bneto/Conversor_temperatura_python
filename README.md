# Conversor de Temperaturas

Este é um projeto em Python que realiza conversões de temperatura a partir de um valor em Celsius para as escalas Fahrenheit ou Kelvin. O programa funciona via terminal e permite ao usuário realizar múltiplas conversões com validação de entrada.

## Funcionalidades

- Conversão de Celsius para Fahrenheit
- Conversão de Celsius para Kelvin
- Validação da opção escolhida pelo usuário (F ou K)
- Possibilidade de realizar várias conversões sem reiniciar o programa
- Interação via terminal

## Estrutura do Código

O programa é dividido em funções para melhor organização e reutilização.

### Função: celsius_para_fahrenheit(celsius)

Responsável por converter um valor de temperatura em Celsius para Fahrenheit.

Fórmula utilizada:
F = (C × 9/5) + 32

### Função: celsius_para_kelvin(celsius)

Responsável por converter um valor de temperatura em Celsius para Kelvin.

Fórmula utilizada:
K = C + 273.15

## Fluxo do Programa

1. O programa inicia exibindo o título
2. O usuário informa a temperatura em Celsius
3. O sistema calcula os valores em Fahrenheit e Kelvin
4. O usuário escolhe qual conversão deseja visualizar (F ou K)
5. Caso a opção seja inválida, o sistema solicita novamente
6. O resultado é exibido na tela
7. O usuário pode decidir se deseja realizar outra conversão

## Tecnologias utilizadas

- Python

## Como executar

1. Tenha o Python instalado
2. Execute o arquivo no terminal com o comando:
python temperatura.py
3. Siga as instruções exibidas pelo programa

## Observações

Este projeto foi desenvolvido com foco em praticar conceitos fundamentais de programação, como funções, estruturas de repetição, condicionais e entrada/saída de dados.

## Possíveis melhorias futuras

- Permitir conversões entre outras escalas
- Criar interface gráfica
- Melhorar tratamento de erros
- Organizar o código em módulos
