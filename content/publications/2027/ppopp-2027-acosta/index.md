---
title: "deqalloc: the memory-stealing allocator"
date: 2027-01-01
publishDate: 2026-11-06
authors: ["André Costa", "Guy Blelloch", "**João M. Lourenço**", "Zachary Kent"]
publication_types: ["1"]
abstract: "deqalloc is a memory allocator designed for concurrent data structures. Instead of remote freeing, a thread that frees memory drops it into its own work-stealing deque, and other threads take memory from these deques only when they need it, rather than having it pushed to them. The design has three layers: a thread-local pool, a work-stealing deque, and a segment layer."
featured: false
publication: "PPoPP 2027: ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming (to appear)"
---
