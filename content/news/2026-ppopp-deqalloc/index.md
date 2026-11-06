---
title: "deqalloc accepted at PPoPP 2027"
date: 2026-11-06
---

Our paper "deqalloc: the memory-stealing allocator" has been accepted at PPoPP 2027 (ACM SIGPLAN Symposium on Principles and Practice of Parallel Programming).

deqalloc is a memory allocator designed for concurrent data structures. Allocators usually return freed memory to the thread that allocated it ("remote freeing"). deqalloc does the opposite: a thread that frees a block simply drops it into its own work-stealing deque, and other threads take memory from these deques only when they need it, instead of having it pushed to them. The design has three layers: a thread-local pool, a work-stealing deque, and a segment layer.

The paper is by André Costa (Carnegie Mellon University and NOVA LINCS | NOVA University Lisbon), Guy Blelloch (Carnegie Mellon University), João Manuel dos Santos Lourenço (NOVA LINCS | NOVA University Lisbon), and Zachary Kent (Carnegie Mellon University). André is my PhD student in the Portugal–CMU PhD program, co-advised with Guy.
