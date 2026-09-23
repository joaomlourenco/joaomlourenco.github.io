---
title: "Snapshot isolation anomalies detection in software transactional memory"
date: 2010-01-01
publishDate: 2010-01-01
authors: ["Ricardo J Dias", "João Seco", "João M Lourenço"]
publication_types: ["2"]
abstract: "Some performance issues of transactional memory are caused by unnecessary abort situations where non serializable and yet non conflicting transactions are scheduled to execute concurrently. Smartly relaxing the isolation properties of transactions may overcome these issues and attain considerable performance improvements. However, it is known that relaxing isolation restrictions may lead to runtime anomalies. In some situations, like database management systems, developers may choose that compromise, hence avoiding anomalies explicitly. Memory transactions protect the state of the program, therefore execution anomalies may have more severe consequences in the semantics of programs. So, the compromise between a relaxed isolation strategy and enforcing the necessary program correctness is harder to setup. The solution we devise is to statically analyse programs to detect the kind of anomalies that emerge under snapshot isolation. Our approach allows a compiler to either warn the developer about the possible snapshot isolation anomalies in a given program, or possibly inform automatic correctness strategies to ensure Serializability."
featured: true
publication: "Proceedings of InForum 2010 2010 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://docentes.fct.unl.pt/sites/default/files/joao-lourenco/files/paper.pdf'
---
