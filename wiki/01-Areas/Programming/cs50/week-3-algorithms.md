---
module: "programming"
course: "CS50x — Introduction to Computer Science"
week: 3
topic: "Searching, Sorting, Running Time (Big-O), Recursion & Phonebook Algorithms"
tags: [programming, computer-science, cs50, harvard, algorithms, searching, sorting, big-o, recursion, complexity, merge-sort]
last_updated: "2026-08-11"
---

# Week 3 — Algorithms

> **Goal of the week:** measure *how fast* code runs (big-$O$/$\Omega$/$\Theta$), implement searching and sorting, see `O(n \log n)$` emerge from merge sort, and meet **recursion**.
> **PSet 3:** *Plurality* (simple voting), *Runoff* (ranked-choice vote elimination), *Tideman* (Condorcet method + cycle detection).

---

## 1. Searching — The Phone-Book Setup Revisited

- **Linear search**: scan from the first element to the last. Works on sorted *or* unsorted data. Worst case = look at every element.

```c
bool search(int value, int values[], int n)   // returns true if found
{
    for (int i = 0; i < n; i++)
        if (values[i] == value)
            return true;
    return false;
}
```

- **Binary search**: only on a **sorted** list. Compare the target to the *middle*; throw away half each time.

```c
bool binary_search(int value, int values[], int lo, int hi)
{
    if (lo > hi) return false;
    int mid = (lo + hi) / 2;
    if (values[mid] == value) return true;
    if (values[mid] < value)  return binary_search(value, values, mid + 1, hi);
    return binary_search(value, values, lo, mid - 1);
}
```

> The identical "compare to middle, halve, recurse" logic shows up again as **binary search trees** (Week 5) and as database **indexes** (Week 7). Learn it once.

---

## 2. Running Time — Big-$O$, $\Omega$, $\Theta$

| Notation | Meaning | Example |
|---|---|---|
| $O(\cdot)$ | **upper bound** — worst case, "at most this many steps" | $O(n)$, $O(n^2)$, $O(\log n)$, $O(n \log n)$, $O(1)$ |
| $\Omega(\cdot)$ | **lower bound** — best case, "at least this many steps" | $\Omega(1)$ (search on lucky first element) |
| $\Theta(\cdot)$ | **tight bound** — both, same order; true only when worst == best | $\Theta(n)$ for linear search, $\Theta(n \log n)$ for merge sort |

**Common running times, ascending:**

```
O(1) < O(log n) < O(n) < O(n log n) < O(n²) < O(2ⁿ)
```

- **Drop constants & lower-order terms**: $O(n/2) \to O(n)$; $O(3n^2+2n) \to O(n^2)$ — big-$O$ describes *growth*, not exact counts.
- "n" = input size. $O(\log n)$ with $n = 16$ is just 4 steps; $O(n)$ is 16. The *difference compounds* as $n$ grows.

---

## 3. Sorting — The Comparison Bowl

### Selection sort (find the minimum, swap to front)
- Each pass scans the remaining list for the smallest and swaps it into position.
- Steps: always about $n/2$ comparisons per pass → **$\Theta(n^2)$** regardless of input.

### Bubble sort (swap adjacent pairs until sorted)
- Repeatedly swap out-of-order neighbours; after pass $k$, the $k$-th largest is "bubbled" to the end.
- **$O(n^2)$** worst; **$\Omega(n)$** best (an already-sorted list — detect no swaps and stop early).

### Insertion sort (grow a sorted prefix, insert each new element where it belongs)
- **$O(n^2)$** worst (reverse-sorted input), **$\Omega(n)$** best (already sorted). Practical winner on small/near-sorted data.

### Merge sort (divide, sort halves, conquer — the "intelligent" sort)
```c
void merge_sort(int arr[], int lo, int hi)
{
    if (lo >= hi) return;                    // base case: 1 element
    int mid = (lo + hi) / 2;
    merge_sort(arr, lo, mid);
    merge_sort(arr, mid + 1, hi);
    merge(arr, lo, mid, hi);                 // combine two sorted halves
}
```
- Splitting is $O(\log n)$ deep; each of the $\log_2 n$ levels merges the whole array in $O(n)$.
- **Merge sort is $\Theta(n \log n)$** in *all* cases — far better than $O(n^2)$ for large $n$ (trades speed for extra memory while merging).

| Sort | Best | Worst | In-place? | Notes |
|---|---|---|---|---|
| Selection | $\Theta(n^2)$ | $\Theta(n^2)$ | yes | simple, consistent |
| Bubble | $\Omega(n)$ | $O(n^2)$ | yes | early-exit trick |
| Insertion | $\Omega(n)$ | $O(n^2)$ | yes | great on tiny/near-sorted data |
| Merge | $\Theta(n \log n)$ | $\Theta(n \log n)$ | **no** (needs extra array) | the asymptotic winner |

> **Fundamental lower bound:** any *comparison-based* sort needs at least $\Omega(n \log n)$ comparisons worst-case — you cannot sort a general list faster than $O(n \log n)$ by comparing elements.

---

## 4. Recursion — A Function Calling Itself

- Recursion = a function whose body calls itself, each time closer to a **base case**.
- **You need (1) a base case** (stop condition, returns directly) **and (2) progress toward it** — otherwise infinite recursion → **Stack Overflow**.
- The classic: countdown / cumulative sum.

```c
int sum(int n)            // 1 + 2 + … + n
{
    if (n <= 1)           // base case
        return 1;
    return n + sum(n - 1); // recurse
}
```
$sum(3) = 3 + sum(2) = 3 + 2 + sum(1) = 3+2+1 = 6$

- **Why it works:** calls stack up (LIFO); each waits for its deeper call; unwinding computes answers bottom-up. The **call stack** discipline reappears properly in [[cs50/week-4-memory]].
- Malan's favourite visualization: **recursive Mario** — `draw(int h)` recurses down to height 1, drawing each row on the way back up (`draw(h-1); for h: #`), which prints the pyramid base-first. The "recursive graphics" shortcut — *trade iteration for a well-specified smaller self-call*.

**Recursion vs iteration:** any loop can be written recursively and vice versa; recursion expresses divide-and-conquer (merge sort, binary search, trees) far more cleanly.

---

## 5. The Week in One Diagram

```mermaid
flowchart TB
    S[Searching] --> LS[Linear search O(n)]
    S --> BS[Binary search O(log n) on sorted data]
    RT[Running time O/Omega/Theta] --- S
    SO[Sorting] --> SEL[Selection Theta(n²)]
    SO --> BUB[Bubble O(n²)/Omega(n)]
    SO --> INS[Insertion O(n²)/Omega(n)]
    SO --> MS[Merge Theta(n log n) ← recursion]
    MS --> R[Recursion: base case + progress]
    BS --> R
    SO --> RT
```

**The design lesson:** speed costs *preconditions* (sorted data) or *memory* (merge array); "faster" is always a trade-off to reason about — the mindset of [[math-for-programming]] and quant work.

---

## 6. Vocabulary to Master

- linear search · binary search · big-$O$ / Ω / Θ · lower bound · selection/bubble/insertion/merge sort · recursion · base case · stack overflow / call stack · in-place · comparison sort

## 7. Cross-Links

- [[cs50/week-2-arrays]] — arrays and string-compare are the raw material being searched/sorted.
- [[cs50/week-4-memory]] — recursion's call stack & recursion-in-memory live here.
- [[cs50/week-5-data-structures]] — binary search's "halve" becomes the *BST*; hash tables sort-of fearlessly.
- [[cs50/week-6-python]] — every algorithm gets re-implemented in Python, same complexity.
- [[programming-cs-fundamentals]] — segments 17–18 (searching + recursion) are this week's trailer.
- [[cs50/problem-sets]] — Plurality/Runoff/Tideman: voting algorithms chosen to force careful loop/index reasoning.