---
title: "Lazy State Determination: More concurrency for contending linearizable transactions"
date: 2020-01-01
publishDate: 2020-01-01
authors: ["Tiago M Vale", "João Leitão", "Nuno Preguiça", "Rodrigo Rodrigues", "Ricardo J Dias", "João M Lourenço"]
publication_types: ["3"]
abstract: "The concurrency control algorithms in transactional systems limits concurrency to provide strong semantics, which leads to poor performance under high contention. As a consequence, many transactional systems eschew strong semantics to achieve acceptable performance. We show that by leveraging semantic information associated with the transactional programs to increase concurrency, it is possible to significantly improve performance while maintaining linearizability. To this end, we introduce the lazy state determination API to easily expose the semantics of application transactions to the database, and propose new optimistic and pessimistic concurrency control algorithms that leverage this information to safely increase concurrency in the presence of contention. Our evaluation shows that our approach can achieve up to 5x more throughput with 1.5c less latency than standard techniques in the popular TPC-C benchmark."
featured: true
publication: "arXiv 2020 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://arxiv.org/abs/2007.09733'
---
