---
title: "Prevenção de Violações de Atomicidade usando Contratos"
date: 2013-01-01
publishDate: 2013-01-01
authors: ["D Sousa", "Carla Ferreira", "**João M. Lourenço**"]
publication_types: ["1"]
abstract: "A programação concorrente obriga o programador a sincronizar os acessos concorrentes a regiões de memória partilhada, contudo esta abordagem não é suficiente para evitar todas as anomalias que podem ocorrer num cenário concorrente. Executar uma sequência de operações atómicas pode causar violações de atomicidade se existir uma correlação entre essas operações, devendo o programador garantir que toda a sequência de operações é executada atomicamente. Este problema é especialmente comum quando se usam operações de pacotes ou módulos de terceiros, pois o programador pode identificar incorretamente o âmbito das regiões de código que precisam de ser atómicas para garantir o correto comportamento do programa. Para evitar este problema o programador do módulo pode criar um contrato que especifica quais as sequências de operações do módulo que devem ser sempre executadas de forma atómica. Este trabalho apresenta uma análise estática para verificação destes contratos."
featured: true
publication: "INForum 2013 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://docentes.fct.unl.pt/sites/default/files/joao-lourenco/files/inforum2013-sousa.pdf'
---
