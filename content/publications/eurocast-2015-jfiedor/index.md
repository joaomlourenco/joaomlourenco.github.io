---
title: "Dynamic Validation of Contracts in Concurrent Code"
date: 2015-02-01
publishDate: 2015-02-01
authors: ["Jan Fiedor", "Zdenek Letko", "**João M. Lourenço**", "Tomas Vojnar"]
publication_types: ["1"]
abstract: "Multi-threaded programs allow one to achieve better performance by doing a lot of work in parallel using multiple threads. Such parallel programs often contain code blocks that a thread must execute atomically, i.e., with no interference from the other threads of the program. Failing to execute these code blocks atomically leads to errors known as atomicity violations. However, frequently it not obvious to tell when a piece of code should be executed atomically, especially when that piece of code contains calls to some third-party library functions, about which the programmer has little or no knowledge at all. One solution to this problem is to associate a contract with such a library, telling the programmer how the library functions should be used, and then check whether the contract is indeed respected. For contract validation, static approaches have been proposed, with known limitations on precision and scalability. In …"
featured: true
publication: "Proceedings of the Fifteenth International Conference on Computer Aided Systems Theory (EUROCAST'15)"
---
