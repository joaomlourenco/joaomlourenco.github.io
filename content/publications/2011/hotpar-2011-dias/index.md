---
title: "Efficient and Correct Transactional Memory Programs Combining Snapshot Isolation and Static Analysis"
date: 2011-05-01
publishDate: 2011-05-01
authors: ["Ricardo J. Dias", "**João M. Lourenço**", "Nuno Preguiça"]
publication_types: ["1"]
abstract: "The use of the Snapshot Isolation (SI) level in Transactional Memory (TM) eliminates the need of tracking memory read accesses, reducing the run-time overhead and fastening the commit phase. By detecting only write-write conflicts, SI allows many memory transactions to succeed that would otherwise abort if serialized. This higher commit rate comes at the expense of introducing anomalous behaviors by allowing some real conflicting transactions to commit. We aim at improving the performance of TM systems by running programs under SI, while guaranteeing a serializable semantics. This is achieved by static analysis of TM programs using Separation Logic to detect possible anomalies when running under SI. To guarantee correct behavior, the program code can be automatically modified to avoid these anomalies. Our approach can have an important impact on the performance of single multi-core node TM systems, and also of distributed TM systems by considerable reducing the required network traffic."
featured: true
publication: "Proceedings of the 3rd USENIX Conference on Hot Topics in Parallelism (HotPar'11)"
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'http://static.usenix.org/events/hotpar11/tech/final_files/Dias.pdf'
---
