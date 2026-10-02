---
title: "FLeeC: A Fast Lock-Free Application Cache"
date: 2023-09-01
publishDate: 2023-09-01
authors: ["André J. Costa", "Nuno M. Preguiça", "**João M. Lourenço**"]
publication_types: ["1"]
abstract: "Access to data in applications that make use of external storage systems (eg, Databases) can be a major performance bottleneck. A common solution is to first query a cache application to reduce data access overhead. These cache applications leverage fast main memory access rates and the parallelism capabilities of hardware to provide high performance. To this end, a cache application needs a concurrency control mechanism to maintain correctness under conflicting concurrent accesses, of which mutual-exclusion locks (blocking concurrency control) are the most common mechanism used. Blocking concurrency control strategies fail to provide a high level of performance when under medium to high contention, as the pessimistic nature of blocking concurrency can not completely avoid needlessly synchronizing operations that do not conflict. Conversely, non-blocking (or lock-free) concurrency control …"
featured: true
publication: "Atas do 14º INForum — Simpósio de Informática, 2023"
---
