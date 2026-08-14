# Guia de organização e continuidade

Este documento é o manual de manutenção do repositório. Seu objetivo é manter os próximos mundos organizados sem apagar a personalidade das soluções nem transformar exercícios de aprendizagem em código artificialmente “perfeito”.

## Regra central

Organização e autoria são coisas diferentes:

- nomes de pastas, documentação e validações devem ser consistentes;
- lógica, comentários, escolhas de implementação e evolução do autor devem ser preservados;
- uma solução antiga só deve ser refatorada quando o objetivo for explicitamente estudar refatoração;
- nesse caso, mantenha a original e crie uma versão identificada.

## Estrutura de cada mundo

```text
python/mundo_NN_nome_do_mundo/
├── README.md
├── aulas/
│   └── aula_NN/
│       └── nome_descritivo.py
└── exercicios/
    ├── exercicio_NNN.py
    └── exercicio_NNN/
        ├── main.py
        └── demais_modulos.py
```

Use uma pasta para o exercício somente quando ele tiver vários módulos, dados próprios ou outros recursos. Um exercício contido em um único programa deve continuar como um único arquivo.

## Convenção de nomes

Use sempre:

- letras minúsculas;
- palavras separadas por `_`;
- nomes sem espaços, acentos ou caracteres especiais;
- dois dígitos para mundos e aulas: `mundo_04`, `aula_01`;
- três dígitos para a sequência antiga de exercícios: `exercicio_115.py`;
- a numeração oficial do curso dentro de cada mundo, inclusive quando ela reiniciar.

Exemplos adequados:

```text
aulas/aula_04/objetos_como_variaveis.py
exercicios/exercicio_016.py
exercicios/exercicio_021/main.py
```

Evite nomes genéricos quando houver mais de um arquivo na mesma aula, como `main2.py`, `teste.py` ou `novo.py`. Prefira dizer o que o arquivo demonstra: `listas_aninhadas.py`, `metodos_de_classe.py` ou `validacao_de_entrada.py`.

## Mundo 4

O Mundo 4 possui sua própria sequência oficial de desafios, começando no desafio 016. Portanto, o número do arquivo é interpretado dentro do diretório do mundo:

```text
python/mundo_04_orientacao_a_objetos/exercicios/exercicio_016.py
```

Isso não conflita com o exercício 016 do Mundo 1 porque os mundos são contextos diferentes. Não invente uma numeração global para “corrigir” a numeração do curso.

Para cada nova aula:

1. Crie `aulas/aula_NN/`.
2. Use nomes descritivos para os exemplos.
3. Separe exemplos somente quando explorarem ideias diferentes.
4. Atualize o README do Mundo 4 se um novo assunto importante for iniciado.

Para cada novo exercício:

1. Crie `exercicios/exercicio_NNN.py` se houver apenas um arquivo.
2. Use `exercicios/exercicio_NNN/` se houver classes, módulos ou recursos separados.
3. Registre título, tema e link em `docs/INDICE_EXERCICIOS.md`.
4. Execute `python3 scripts/validar_repositorio.py` antes do commit.

## Cabeçalho recomendado

O cabeçalho é recomendado para arquivos novos, mas não deve ser inserido retroativamente à força nas soluções antigas:

```python
"""Exercício 016 — Funcionário.

Conceitos praticados: classes, atributos e métodos.
"""
```

Depois do cabeçalho, escreva a solução com seu próprio estilo. O objetivo é identificar o aprendizado, não padronizar sua voz.

## Versões alternativas

Quando quiser preservar abordagens diferentes, use:

```text
exercicio_023.py
exercicio_023_v2.py
```

No arquivo mais recente, explique em uma frase o motivo da nova versão. Exemplos: uso de uma estrutura aprendida depois, simplificação da lógica ou correção de uma limitação. Não use nomes como `final`, `final_agora`, `certo` ou `novo`.

## Arquivos de apoio e dados

- Recursos exclusivos de um exercício ficam dentro da pasta desse exercício.
- Arquivos gerados durante a execução não devem ser versionados, salvo quando forem exemplos necessários.
- Dados de exemplo versionados devem ter conteúdo fictício e não conter informações pessoais.
- Segredos, senhas, tokens e arquivos de ambiente nunca devem ser adicionados ao Git.

## Commits

Faça commits pequenos, com verbo no presente e assunto específico:

```text
Adiciona exemplos da aula 04 do Mundo 4
Resolve exercício 016 sobre funcionários
Documenta herança e abstração
Corrige validação do exercício 028
```

Evite mensagens vagas como `Atualização`, `Coisas novas`, `Final` ou somente o número da aula.

## Checklist antes de publicar

- [ ] O arquivo está no mundo e na categoria corretos.
- [ ] O nome segue a convenção.
- [ ] O exercício possui título ou contexto suficiente.
- [ ] Uma nova versão não apagou a solução anterior relevante.
- [ ] Nenhum dado pessoal ou segredo foi incluído.
- [ ] O índice e o README do mundo foram atualizados quando necessário.
- [ ] `python3 scripts/validar_repositorio.py` terminou com sucesso.

## Decisões históricas preservadas

Os Mundos 1 a 3 contêm nomes internos como `main.py`, `dic.py` e `teste.py`, além de versões `_v2`. Eles documentam a forma como o conteúdo foi estudado e, por isso, não foram reescritos. A padronização estrutural foi aplicada ao redor dessas soluções; a convenção mais descritiva passa a valer para arquivos novos.

## Referências da organização

A convenção foi formulada após comparar repositórios públicos do mesmo conteúdo e a estrutura oficial do curso:

- o repositório [Curso-Python-Gustavo-Guanabara](https://github.com/divertimentos/Curso-Python-Gustavo-Guanabara) demonstrou a utilidade de separar os mundos e manter uma lista navegável com os títulos;
- a coleção pública do tópico [curso-em-video-python](https://github.com/topics/curso-em-video-python?l=python) mostrou que a divisão por mundos é reconhecível para outros estudantes, mas que muitos projetos perdem consistência nos nomes internos;
- a página oficial do [Mundo 04 — Orientação a Objetos](https://www.estudonauta.com/curso/linguagem-python-3-mundo-04-orientacao-a-objetos/) confirmou o escopo e a numeração própria dos novos desafios.

Este repositório combina essas ideias com uma convenção própria: mundo, categoria, número normalizado, índice por assunto e preservação explícita das etapas históricas.
