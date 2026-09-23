---
title: "Macrodb: Scaling database engines on multicores"
date: 2013-01-01
publishDate: 2013-01-01
authors: ["João Soares", "**João Lourenço**", "Nuno Preguiça"]
publication_types: ["2"]
abstract: "Multicore processors are available for over a decade, but general purpose database management systems (DBMS) still cannot fully explore the computational resources of these platforms. This paper explores a simple and easy to deploy approach for improving DBMS performance in multicore platforms, by maintaining multiple database engines running in parallel, rather than a single instance, thus circumventing the increase in contention due to load interactions. Unlike previous works, we focus on in-memory DBMS, exploring different design solutions that combine distributed systems and concurrent programming techniques. We show that we are able to improve performance over standalone solutions, without modifying either database or application code, by up to 3 times while minimizing response times."
featured: true
publication: "Lecture Notes in Computer Science 2013 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://link.springer.com/chapter/10.1007/978-3-642-40047-6_61'
---
