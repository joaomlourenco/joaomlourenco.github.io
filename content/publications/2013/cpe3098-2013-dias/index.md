---
title: "Efficient Support for In-place Metadata in Java Software Transactional Memory"
date: 2013-12-01
publishDate: 2013-12-01
authors: ["Ricardo J. Dias", "Tiago M. Vale", "**João M. Lourenço**"]
publication_types: ["2"]
abstract: "Software transactional memory (STM) algorithms associate metadata with the memory locations accessed during a transaction's lifetime. This metadata may be stored in an external table by resorting to a mapping function that associates the address of a memory cell with the table entry containing the corresponding metadata (out‐place or external strategy). Alternatively, the metadata may be stored adjacent to the associated memory cell by wrapping the cell and metadata together (in‐place strategy). The implementation techniques to support these two approaches are very different and each STM framework is usually biased towards one of them, only allowing the efficient implementation of STM algorithms which suit one of the approaches and inhibiting a fair comparison with STM algorithms suiting the other. In this paper, we introduce a technique to implement in‐place metadata that does not wrap memory cells …"
featured: true
publication: "Concurrency and Computation: Practice and Experience 25 (17) 2394-2411"
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'http://dx.doi.org/10.1002/cpe.3098'
---
