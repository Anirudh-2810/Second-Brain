---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 5
topic: "Data Structures — Stacks, Queues, Linked Lists, Trees, Hash Tables, Tries"
tags: [programming, computer-science, cs50, harvard, data-structures, linked-list, hash-table, binary-search-tree, stack, queue, trie]
last_updated: "2026-08-11"
---

# Week 5 — Data Structures

> **Goal of the week:** meet the **hash table** — the unlock for speller-speed lookups — and the *family* of pointer-built structures that make it possible: stacks, queues, linked lists, binary search trees, and tries. The deepest "abstraction un-hidden" of the course.
> **PSet 5:** *Speller* — the dictionary/hash-table PSET: implement `load`, `hash`, `check`, `size`, `unload` and decide the trade-off between speed and memory.

---

## 1. Why Data Structures Exist — Abstract Data Types (ADTs)

- A **data structure** package = (a) how data is *organized* in memory + (b) the *operations* you can perform.
- C has no built-in lists beyond arrays, so the course builds structures **out of structs + pointers** (Week 4's tools).
- Every structure is a **time↔space trade-off**; there is no free lunch — the hash table buys speed with memory.

---

## 2. Stacks & Queues — Restricted-Use ADTs

| ADT | Rule (insert/remove) | Mental image | Use cases |
|---|---|---|---|
| **Stack** | **LIFO** — Last In, First Out; `push` & `pop` from the same end (top) | a stack of plates | undo; call stack (Week 4 recursion); back-button |
| **Queue** | **FIFO** — First In, First Out; `enqueue` to back, `dequeue` from front | a line of students | print queue; message queues; BFS |

Implemented with arrays (fixed size) or linked lists (dynamic).

---

## 3. Linked Lists — Pointers as Structure

Each **node** holds data + a pointer to the next node; the list grows/shrinks anywhere.

```c
typedef struct node
{
    int number;
    struct node *next;   // self-referential pointer
} node;
```

- **Searching a singly linked list is $O(n)$** — you cannot jump to the middle (no random access). To *insert*, you rebuild the `next` links; to *delete*, you traverse to parent.
- **Array vs linked list** — the week's central contrast:

| | Array | Linked list |
|---|---|---|
| Access by index | $O(1)$ | $O(n)$ |
| Insert/delete in middle | $O(n)$ (shift) | $O(1)$ (rewire pointers) |
| Size | fixed at declaration | grows dynamically |
| Memory | contiguous | scattered (each node + pointer overhead) |

- **Circular** and **doubly linked** lists (both `prev` and `next` pointers) solve traversal edge cases.
- Care with memory: new node = `malloc`, delete node = `free`, and **don't lose the head pointer** while rewiring.

---

## 4. Binary Search Trees (BST) — Recursion Made Tangible

A binary tree where **left < node < right** at every node, plus a `left`/`right` child instead of just `next`:

- Search: compare, descend one side, halving possibilities → **$O(\log n)$** when the tree is balanced.
- Insert: same walk, attach a new leaf.
- **Recursion is the natural implementation** — mirroring Week 3's binary search.

```
          50
        /    \
      30      75
     /  \      \
    20   40    80     → searching for 40: 50 → 30 → 40  (3 steps, was 6 in a list)
```

- **Degenerate tree warning:** feeding nodes in sorted order makes the BST a *linked list* → $O(n)$. Balanced trees (AVL, red–black) fix this — see the AI/ML + systems modules for deeper treatment.

---

## 5. Hash Tables — Speed via Math + Memory

- A **hash table = an array of buckets**, each bucket a linked list.
- **Hash function** maps a *key* (e.g. spelling word) → array index. `hash("carter") = 0, hash("zmalan") = 25 …`
- **Collisions** (two keys → same bucket) are absorbed by chaining — the list grows in that bucket.

```c
node *table[N];   // array of N linked-list heads

unsigned int hash(const char *word)
{
    // simple: sum of first letters / table size
    return (toupper(word[0]) - 'A') % N;
}
```

- **Lookup cost:** hash in $O(1)$ → walk the bucket's small list. Overall **≈ $O(1)$** average, $O(n)$ worst.
- **The trade-off dials:** more buckets (bigger `N`) → fewer collisions → faster lookup, *more RAM*; fewer buckets → slower, leaner. **Speller's whole design exercise is picking this dial** and a good hash.

> **Hash-in-the-wild:** Python dicts, SQL indexes, Bloom filters, and Week 7's database internals all implement hashing.

---

## 6. Tries — Fastest Lookup, Most Memory

- A **trie** (retrieval tree) stores strings as *paths*, one node per possible **letter**, not per word. Every node = an array of 26 child pointers + a "is a word?" flag.

```
(root) --M--> (a,l) -->(a,n) --> t = word?  => "Malan"
```

- Lookup = walk the letters of the word, each step an $O(1)$ array jump ⇒ **$O(\text{length of word})$** — effectively constant, independent of dictionary size. Speller's holy grail.
- **Cost:** a huge amount of memory (every node reserves 26 pointers whether used or not).

---

## 7. The Big Shop Window — Six Structures, One Table

| Structure | Search | Insert | Memory | Use when |
|---|---|---|---|---|
| Array | $O(1)$ index / $O(n)$ value | $O(n)$ shift | tight | fixed-size, indexed |
| Stack | top $O(1)$ | $O(1)$ | low | LIFO processing |
| Queue | front $O(1)$ | $O(1)$ | low | FIFO/buffers |
| Linked list | $O(n)$ | $O(1)$ at head | nodes+pointers | dynamic, no random access |
| BST | $O(\log n)$ balanced | $O(\log n)$ | moderate | ordered data, search/insert |
| Hash table | ≈ $O(1)$ | ≈ $O(1)$ | buckets+chains | fast key lookup (speller) |
| Trie | $O(k)$ (`len`) | $O(k)$ | very high | fixed-alphabet, lookup-dominated |

> **Recurring exam insight:** every structure is a *point on a curve* — you're choosing to spend memory to buy time (hash tables, tries) or to spend time to save memory (linked lists).

---

## 8. Vocabulary to Master

- abstract data type (ADT) · stack/push/pop · queue/enqueue/dequeue · node · singly/doubly linked list · binary search tree · balanced vs degenerate tree · hash table · hash function · collision · chaining · try/trie

## 9. Cross-Links

- [[cs50/week-4-memory]] — every structure above is `malloc` + `free` + pointers in disguise.
- [[cs50/week-3-algorithms]] — BST search *is* binary search re-hosted in a tree.
- [[cs50/week-6-python]] — Python's `list`, `dict`, `set`, `tuple` are these exact structures with no pointer-visible assembly required.
- [[cs50/week-7-sql]] — database indexes are hash tables/B-trees under the hood.
- [[matching-engine-cpp]] · [[quant-toolkit-and-skills]] — hash tables and trees are the substrate of real order books and C++ engines.
- [[cs50/problem-sets]] — PSet 5 (Speller).