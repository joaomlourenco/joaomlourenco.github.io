---
title: "A hardware approach for detecting, exposing and tolerating high level atomicity violations"
date: 2016-01-01
publishDate: 2016-01-01
authors: ["Lois Orosa", "JM Lourenço"]
publication_types: ["2"]
abstract: "Multicores are the main trend in computer architecture to gain performance without exponentially increasing the power consumption. However, to take advantage of these new architectures we need parallel programs. Parallel programming is challenging mainly because the programmer has to reason about many threads accessing data concurrently, and the data access interleavings are not deterministic, hence unpredictable.Locks are the most used mechanism to synchronize the accesses to shared memory. Using coarse-grain locks enforces the serialization of large code blocks and hinders performance, and using fine grain locks is a tedious and error prone process for the programmer that frequently ends up in deadlocks and other concurrency related errors. An alternative to locks is transactional memory, an abstraction for defining atomic blocks that may be executed speculatively, making good use of the available cores and solving some of the problems associated with locks. In this paper we address a solution for detecting and tolerating one of the most typical concurrency bugs: atomicity violations. More specifically, we address High-Level Atomicity Violations (HLAV). High-level atomicity violations result from the misspecification of the scope of an atomic block, by splitting it in two or more atomic blocks which may be interleaved with other atomic blocks. Figure 1 shows an example of this type of atomicity violation. The intuitive idea behind HLAV is that if two shared data items (eg, memory locations) were both accessed inside an atomic block, they are interrelated and probably the programmer intention is that there shall be no interleavings …"
featured: true
publication: "Proceedings of the 24th Euromicro Int’l conference on parallel, distributed, and network-based processing (PDP’16). IEEE Computer Society 2016 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://www.academia.edu/download/112644062/orosa.pdf'
---
