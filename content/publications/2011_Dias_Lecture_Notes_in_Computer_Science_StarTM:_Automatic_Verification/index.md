---
title: "StarTM: Automatic Verification of Snapshot Isolation in Transactional Memory Java Programs"
date: 2011-01-01
publishDate: 2011-01-01
authors: ["Ricardo J Dias", "Dino Distefano", "Joao M Lourenço", "Joao Costa Seco"]
publication_types: ["2"]
abstract: "This paper presents StarTM, an automatic verification tool for transactional memory Java programs executing under relaxed isolation levels. We certify which transactions in a program are safe to execute under Snapshot Isolation without triggering the write-skew anomaly, opening the way to run-time optimizations that may lead to considerable performance enhancements.Our tool builds on a novel shape analysis technique based on Separation Logic to statically approximate the read-and write-sets of a transactional memory Java program. This technique is particularly challenging due to the presence of dynamically allocated memory. We implement our technique and apply our tool to a set of intricate examples. We corroborate known results, certifying some of the examples for safe execution under Snapshot Isolation by proving the absence of write-skew anomalies. In other cases we identify transactions that potentially trigger"
featured: true
publication: "Lecture Notes in Computer Science 2011 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://www.academia.edu/download/30684332/ddls11.pdf'
---
