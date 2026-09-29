# 🧮 Calculadora de Área do Círculo

Uma calculadora de área de círculos desenvolvida em **Python**, executada diretamente pelo terminal através de uma interface de linha de comando (CLI).

O programa permite calcular a área de um círculo informando seu **raio** ou **diâmetro**, além de permitir definir a quantidade de casas decimais do resultado.

## 🚀 Funcionalidades

* 📐 Cálculo da área através do raio
* ⭕ Cálculo da área através do diâmetro
* 🔢 Definição da precisão do resultado
* ✅ Validação dos valores informados
* ⚠️ Tratamento de argumentos inválidos
* 💻 Execução pelo terminal
* 🐍 Utilização apenas da biblioteca padrão do Python

## 🛠️ Tecnologias

* Python 3
* `argparse`
* `math`

Nenhuma biblioteca externa é necessária.

## 📥 Instalação

Clone o repositório:

```bash
git clone https://github.com/pascalramos175/001.py.git
```

Entre na pasta:

```bash
cd 001.py
```

Execute o programa:

```bash
python main.py
```

> Dependendo do nome do arquivo Python no repositório, substitua `main.py` pelo nome correto do arquivo.

## 💻 Utilização

O programa exige que seja informado **um raio ou um diâmetro**.

### 📐 Utilizando o raio

```bash
python main.py --raio 5
```

Ou utilizando a forma abreviada:

```bash
python main.py -r 5
```

Saída:

```text
A área do círculo com raio 5.0 é: 78.54
```

### ⭕ Utilizando o diâmetro

```bash
python main.py --diametro 10
```

Ou:

```bash
python main.py -d 10
```

Saída:

```text
A área do círculo com diâmetro 10.0 é: 78.54
```

## 🔢 Definindo a precisão

Por padrão, o resultado possui **2 casas decimais**.

É possível alterar essa quantidade utilizando `-p` ou `--precisao`.

Exemplo:

```bash
python main.py -r 5 -p 4
```

Saída:

```text
A área do círculo com raio 5.0 é: 78.5398
```

Também é possível utilizar precisão zero:

```bash
python main.py -r 5 -p 0
```

Saída:

```text
A área do círculo com raio 5.0 é: 79
```

## 📋 Argumentos

| Argumento          | Descrição                             | Obrigatório |
| ------------------ | ------------------------------------- | :---------: |
| `-r`, `--raio`     | Define o raio do círculo              |     Sim*    |
| `-d`, `--diametro` | Define o diâmetro do círculo          |     Sim*    |
| `-p`, `--precisao` | Define a quantidade de casas decimais |     Não     |

* É necessário informar **raio ou diâmetro**, mas não os dois.

### Ajuda

Para visualizar todos os argumentos disponíveis:

```bash
python main.py --help
```

## 📐 Fórmula

A área de um círculo é calculada através da fórmula:

```text
A = π × r²
```

Quando o usuário informa o diâmetro, o programa primeiro encontra o raio:

```text
r = d / 2
```

Depois, utiliza o raio para calcular a área.

### Exemplo

Para um círculo com raio `5`:

```text
A = π × 5²
A = π × 25
A ≈ 78.54
```

## ⚠️ Validações

O programa verifica se os valores fornecidos são válidos.

Valores negativos ou iguais a zero são rejeitados.

Exemplo:

```bash
python main.py -r -5
```

Resultado:

```text
error: O raio deve ser um número maior que zero.
```

A precisão também não pode ser negativa:

```bash
python main.py -r 5 -p -2
```

Resultado:

```text
error: A precisão não pode ser um número negativo.
```

## 📂 Estrutura

```text
001.py/
│
├── main.py
└── README.md
```

## 🎯 Objetivo

Este projeto foi desenvolvido como um exercício prático para estudar conceitos fundamentais de **Python** e desenvolvimento de aplicações de linha de comando.

Entre os conceitos utilizados estão:

* Funções
* Argumentos de linha de comando
* Validação de dados
* Estruturas condicionais
* Formatação de strings
* Módulos da biblioteca padrão
* `argparse`
* Operações matemáticas

## 👨‍💻 Autor

**Pascal Ramos**

GitHub: [@pascalramos175](https://github.com/pascalramos175)

---

⭐ Se você gostou do projeto, considere deixar uma estrela no repositório!
