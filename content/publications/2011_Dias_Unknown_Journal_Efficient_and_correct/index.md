---
title: "Efficient and correct transactional memory programs combining snapshot isolation and static analysis"
date: 2011-01-01
publishDate: 2011-01-01
authors: ["Ricardo J Dias", "João M Lourenço", "Nuno M Preguiça"]
publication_types: ["2"]
abstract: "The use of the Snapshot Isolation (SI) level in Transactional Memory (TM) eliminates the need of tracking memory read accesses, reducing the run-time overhead and fastening the commit phase. By detecting only write-write conflicts, SI allows many memory transactions to succeed that would otherwise abort if serialized. This higher commit rate comes at the expense of introducing anomalous behaviors by allowing some real conflicting transactions to commit. We aim at improving the performance of TM systems by running programs under SI, while guaranteeing a serializable semantics. This is achieved by static analysis of TM programs using Separation Logic to detect possible anomalies when running under SI. To guarantee correct behavior, the program code can be automatically modified to avoid these anomalies. Our approach can have an important impact on the performance of single multi-core node TM systems, and also of distributed TM systems by considerable reducing the required network traffic."
featured: true
publication: "Unknown Journal 2011 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://www.usenix.org/events/hotpar11/tech/final_files/Dias.pdf'
---
