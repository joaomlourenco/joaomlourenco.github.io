---
title: "Unifying Memory and Database Transactions"
date: 2009-01-01
publishDate: 2009-01-01
authors: ["Ricardo J. Dias", "**João M. Lourenço**"]
publication_types: ["1"]
abstract: "Software Transactional Memory is a concurrency control technique gaining increasing popularity, as it provides high-level concurrency control constructs and eases the development of highly multi-threaded applications. But this easiness comes at the expense of restricting the operations that can be executed within a memory transaction, and operations such as terminal and file I/O are either not allowed or incur in serious performance penalties. Database I/O is another example of operations that usually are not allowed within a memory transaction. This paper proposes to combine memory and database transactions in a single unified model, benefiting from the ACID properties of the database transactions and from the speed of main memory data processing. The new unified model covers, without differentiating, both memory and database operations. Thus, the users are allowed to freely intertwine memory and …"
featured: true
publication: "Proceedings of the 15th International Euro-Par Conference on Parallel Processing 349-360"
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'http://dx.doi.org/10.1007/978-3-642-03869-3_35'
---
