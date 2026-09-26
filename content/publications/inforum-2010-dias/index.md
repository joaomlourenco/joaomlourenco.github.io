---
title: "Snapshot Isolation Anomalies Detection in Software Transactional Memory"
date: 2010-01-01
publishDate: 2010-01-01
authors: ["Ricardo J. Dias", "João Seco", "**João M. Lourenço**"]
publication_types: ["1"]
abstract: "Some performance issues of transactional memory are caused by unnecessary abort situations where non serializable and yet non conflicting transactions are scheduled to execute concurrently. Smartly relaxing the isolation properties of transactions may overcome these issues and attain considerable performance improvements. However, it is known that relaxing isolation restrictions may lead to runtime anomalies. In some situations, like database management systems, developers may choose that compromise, hence avoiding anomalies explicitly. Memory transactions protect the state of the program, therefore execution anomalies may have more severe consequences in the semantics of programs. So, the compromise between a relaxed isolation strategy and enforcing the necessary program correctness is harder to setup. The solution we devise is to statically analyse programs to detect the kind of anomalies that emerge under snapshot isolation. Our approach allows a compiler to either warn the developer about the possible snapshot isolation anomalies in a given program, or possibly inform automatic correctness strategies to ensure Serializability."
featured: true
publication: "INForum 2010 - Atas do 2º Simpósio de Informática 31-42"
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'http://inforum.org.pt/INForum2010/papers/ciencia-e-engenharia-de-software/Paper053.pdf'
---
