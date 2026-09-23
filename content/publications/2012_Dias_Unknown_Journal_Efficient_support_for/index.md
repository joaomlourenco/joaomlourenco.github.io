---
title: "Efficient support for in-place metadata in transactional memory"
date: 2012-01-01
publishDate: 2012-01-01
authors: ["Ricardo J Dias", "Tiago M Vale", "João M Lourenço"]
publication_types: ["2"]
abstract: "Implementations of Software Transactional Memory (STM) algorithms associate metadata with the memory locations accessed during a transaction’s lifetime. This metadata may be stored either in-place, by wrapping every memory cell in a container that includes the memory cell itself and the corresponding metadata; or out-place (also called external), by resorting to a mapping function that associates the memory cell address with an external table entry containing the corresponding metadata. The implementation techniques for these two approaches are very different and each STM framework is usually biased towards one of them, only allowing the efficient implementation of STM algorithms following that approach, hence inhibiting the fair comparison with STM algorithms falling into the other. In this paper we introduce a technique to implement in-place metadata that does not wrap memory cells, thus overcoming …"
featured: true
publication: "Lecture Notes in Computer Science 2012 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://link.springer.com/chapter/10.1007/978-3-642-32820-6_59'
---
