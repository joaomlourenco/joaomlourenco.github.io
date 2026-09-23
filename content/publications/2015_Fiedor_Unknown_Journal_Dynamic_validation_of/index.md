---
title: "Dynamic validation of contracts in concurrent code"
date: 2015-01-01
publishDate: 2015-01-01
authors: ["Jan Fiedor", "Zdeněk Letko", "**João Lourenço**", "Tomáš Vojnar"]
publication_types: ["2"]
abstract: "Multi-threaded programs allow one to achieve better performance by doing a lot of work in parallel using multiple threads. Such parallel programs often contain code blocks that a thread must execute atomically, i.e., with no interference from the other threads of the program. Failing to execute these code blocks atomically leads to errors known as atomicity violations. However, frequently it not obvious to tell when a piece of code should be executed atomically, especially when that piece of code contains calls to some third-party library functions, about which the programmer has little or no knowledge at all. One solution to this problem is to associate a contract with such a library, telling the programmer how the library functions should be used, and then check whether the contract is indeed respected. For contract validation, static approaches have been proposed, with known limitations on precision and scalability. In …"
featured: true
publication: "Lecture Notes in Computer Science 2015 "
links:
  - icon_pack: fas
    icon: scroll
    name: Link
    url: 'https://link.springer.com/chapter/10.1007/978-3-319-27340-2_69'
---
