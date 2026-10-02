---
title: "Pot: Deterministic Transactional Execution"
date: 2016-12-01
publishDate: 2016-12-01
authors: ["Tiago M. Vale", "João A. Silva", "Ricardo J. Dias", "**João M. Lourenço**"]
publication_types: ["2"]
abstract: "This article presents Pot, a system that leverages the concept of preordered transactions to achieve deterministic multithreaded execution of programs that use Transactional Memory. Preordered transactions eliminate the root cause of nondeterminism in transactional execution: they provide the illusion of executing in a deterministic serial order, unlike traditional transactions that appear to execute in a nondeterministic order that can change from execution to execution. Pot uses a new concurrency control protocol that exploits the serialization order to distinguish between fast and speculative transaction execution modes in order to mitigate the overhead of imposing a deterministic order. We build two Pot prototypes: one using STM and another using off-the-shelf HTM. To the best of our knowledge, Pot enables deterministic execution of programs using off-the-shelf HTM for the first time. An experimental evaluation …"
featured: true
publication: "ACM Transactions on Architecture and Code Optimization 13 (4) 1–24"
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'http://dx.doi.org/10.1145/3017993'
---
