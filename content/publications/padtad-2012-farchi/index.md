---
title: "Using Program Closures to Make an Application Programming Interface (Api) Implementation Thread Safe"
date: 2012-07-01
publishDate: 2012-07-01
authors: ["Eitan Farchi", "Itai Segall", "**João M. Lourenço**", "Diogo G. Sousa"]
publication_types: ["1"]
abstract: " Consider a set of methods implementing an Application Programming Interface (API) of a given library or program module that is to be used in a multithreaded setting. If those methods were not originally designed to be thread safe, races and deadlocks are expected to happen. This work introduces the novel concept of program closure and describes how it can be applied in a methodology used to make the library or module implementation thread safe, by identifying the high level data races introduced by interleaving the parallel execution of methods from the API. High-level data races result from the misspecification of the scope of an atomic block, by wrongly splitting it into two or more atomic blocks sharing a data dependency.  Roughly speaking, the closure of a program P, clos(P), is obtained by incrementally adding new threads to P in such a way that enables the identification of the potential high level data …"
featured: true
publication: "Proceedings of the 2012 Workshop on Parallel and Distributed Systems: Testing, Analysis, and Debugging 18-24"
---
