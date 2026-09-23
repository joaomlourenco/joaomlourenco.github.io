---
title: "Detection of transactional memory anomalies using static analysis"
date: 2010-01-01
publishDate: 2010-01-01
authors: ["Bruno Teixeira", "**João Lourenço**", "Eitan Farchi", "Ricardo Dias", "Diogo Sousa"]
publication_types: ["2"]
abstract: "Transactional Memory allows programmers to reduce the number of synchronization errors introduced in concurrent programs, but does not ensures its complete elimination. This paper proposes a pattern matching based approach to the static detection of atomicity violation, based on a path-sensitive symbolic execution method to model four anomalies that may affect Transactional Memory programs. The proposed technique may be used to to bring to programmer's attention pairs of transactions that the programmer has mis-specified, and should have been combined into a single transaction. The algorithm first traverses the AST tree, removing all the non-transactional blocks and generating a trace tree in the path sensitive manner for each thread. The trace tree is a Trie like data structure, where each path from root to a leaf is a list of transactions. For each pair of threads, erroneous patterns involving two …"
featured: true
publication: "Proceedings of the 8th Workshop on Parallel and Distributed Systems: Testing, Analysis, and Debugging 2010 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://dl.acm.org/doi/abs/10.1145/1866210.1866213'
---
