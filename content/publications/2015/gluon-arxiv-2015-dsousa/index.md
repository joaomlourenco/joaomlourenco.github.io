---
title: "Preventing Atomicity Violations with Contracts"
date: 2015-01-01
publishDate: 2015-01-01
authors: ["Diogo G. Sousa", "Ricardo J. Dias", "Carla Ferreira", "**João M. Lourenço**"]
publication_types: ["3"]
abstract: "Concurrent programming is a difficult and error-prone task because the programmer must reason about multiple threads of execution and their possible interleavings. A concurrent program must synchronize the concurrent accesses to shared memory regions, but this is not enough to prevent all anomalies that can arise in a concurrent setting. The programmer can misidentify the scope of the regions of code that need to be atomic, resulting in atomicity violations and failing to ensure the correct behavior of the program. Executing a sequence of atomic operations may lead to incorrect results when these operations are co-related. In this case, the programmer may be required to enforce the sequential execution of those operations as a whole to avoid atomicity violations. This situation is specially common when the developer makes use of services from third-party packages or modules."
featured: true
publication: ""
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://arxiv.org/abs/1505.02951'
---
