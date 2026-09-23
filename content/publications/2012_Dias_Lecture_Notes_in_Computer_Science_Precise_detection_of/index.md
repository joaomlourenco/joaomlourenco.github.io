---
title: "Precise detection of atomicity violations"
date: 2012-01-01
publishDate: 2012-01-01
authors: ["Ricardo J Dias", "Vasco Pessanha", "João M Lourenço"]
publication_types: ["2"]
abstract: "Concurrent programs that are free of unsynchronized accesses to shared data may still exhibit unpredictable concurrency errors, called atomicity violations, which include both high-level data races and stale-value errors. Atomicity violations occur when programmers make wrong assumptions about the atomicity scope of a code block, incorrectly splitting it in two or more atomic blocks and allowing them to be interleaved with other atomic blocks. In this paper we propose a novel static analysis algorithm that works on a dependency graph of program variables and detects both high-level data races and stale-value errors. The algorithm was implemented for a Java Bytecode analyzer and its effectiveness was evaluated with well known faulty programs. The results obtained show that our algorithm performs better than previous approaches, achieving higher precision for small and medium sized programs, making it a …"
featured: true
publication: "Lecture Notes in Computer Science 2012 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://link.springer.com/chapter/10.1007/978-3-642-39611-3_8'
---
