# Focused n=16 prior-art addendum — Labahn–Pietsch

**26 October 2026.** This audit addresses a high-collision title that was surfaced by exact-title search, rather than asserting novelty from its absence.

## Identified historical source

Roger Labahn and Christian Pietsch, *Characterizing Minimum Gossip Graphs on 16 Vertices*. Institutional [University of Bonn working-paper register](https://www.or.uni-bonn.de/publications.de.html), **Report No. 91707**. This title is also referenced explicitly as a Bonn 1991 preprint in Labahn, *Some minimum gossip graphs*, Networks 23 (1993), 333–341, DOI [10.1002/net.3230230416](https://doi.org/10.1002/net.3230230416). A [full-text manuscript facsimile](https://www.researchgate.net/publication/2297002_Characterizing_Minimum_Gossip_Graphs_on_16_Vertices) is available via ResearchGate, with the manuscript itself dated **October 12, 1993**, "submitted to Networks." Public metadata disagrees about the precise report/manuscript year; **do not manufacture one unified publication date or a journal article DOI**.

## Actual problem solved by the preprint

Its introduction defines T(G) as the **number of parallel rounds** and T_n as the minimum possible round count. A graph G is a "minimum gossip graph" there when T(G)=T_n and its **number of links** is minimum among graphs achieving this fastest possible dissemination. The source studies powers of two, n=2^k, and for n=16 has minimum round count **four**. It states that every round of a minimum-time scheme must consist of eight disjoint calls, so a corresponding four-round scheme has **32 pairwise-call occurrences**.

Our model instead fixes **exactly 2n-4=28 sequential calls** (the minimum *number of calls* for n=16), without optimizing parallel rounds, and asks whether its first or last **14 original chronological calls** induce a forest. The two problems overlap in gossip semantics but have **different objectives and extremal budgets**.

## Novelty implication

- **Verified older work:** construction/classification of **fastest-round 16-vertex gossip graphs** and their edge/coloring structures.
- **Not established from that source:** the universal original-half-forest property for *every 28-call successful distinct-contact chronology*.
- **Not claimed:** that this different-title overlap cannot supply reusable proof ingredients or a hidden corollary after deeper analysis. The complete literature novelty gate remains **UNRESOLVED**, especially relative to Labahn's separate 1995 minimum-*call* kernel classification and Krumme's 1996 reordering theorem.

**Conclusion:** This is an important, close-titled historical source that must be cited and model-disambiguated, but it is **not direct theorem-level priority evidence** for the n16 original-14/14 half-forest result under the definitions visible in its abstract and opening manuscript. The mathematical finite result remains unchanged. PR #1 stays draft/unmerged.
