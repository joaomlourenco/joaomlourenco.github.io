---
title: "Verification of Snapshot Isolation in Transactional Memory Java Programs"
date: 2012-06-01
publishDate: 2012-06-01
authors: ["Ricardo J. Dias", "Dino Distefano", "João Costa Seco", "**João M. Lourenço**"]
publication_types: ["6"]
abstract: "This paper presents an automatic verification technique for transactional memory Java programs executing under snapshot isolation level. We certify which transactions in a program are safe to execute under snapshot isolation without triggering the write-skew anomaly, opening the way to run-time optimizations that may lead to considerable performance enhancements.Our work builds on a novel deep-heap analysis technique based on separation logic to statically approximate the read- and write-sets of a transactional memory Java program.We implement our technique and apply our tool to a set of micro benchmarks and also to one benchmark of the STAMP package. We corroborate known results, certifying some of the examples for safe execution under snapshot isolation by proving the absence of write-skew anomalies. In other cases our analysis has identified transactions that potentially trigger previously …"
featured: true
publication: "ECOOP 2012 – Object-Oriented Programming 7313 640-664"
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'http://dx.doi.org/10.1007/978-3-642-31057-7_28'
---
