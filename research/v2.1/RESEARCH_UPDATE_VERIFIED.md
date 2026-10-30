# v2.1 n=15 finite verification: reconstructed evidence and soundness audit

Date: 26 October 2026. This is a **new reconstruction**, not a copy of lost executable files. The previous MANUSCRIPT_DRAFT_UNVERIFIED.md and REVIEWER_DRAFT_UNVERIFIED.md are historical drafts, not sources of executable proof.

## Exact bounded statement

In a shortest successful undirected telephone-gossip sequence of 26 **distinct** contacts on 15 vertices, with the original order split after 13 contacts, at least one chronological half induces a forest. With the previously certified v2.0 results and the classical two-contact extension, the finite assertion holds for 4 <= n <= 15. This is a bounded computer-assisted theorem, not a universal theorem for all n and not the temporal-clique 2n-3 conjecture.

## Exhaustive reduction

The prior component-intersection and rectangular-grid lemmas confine hypothetical both-cyclic n15 schedules to three prefix and three suffix components. Each half has one unicyclic component and two trees. Every prefix component meets every suffix component. The nine positive intersection sizes sum to 15: exactly 3,003 allocations.

The verified collector and first-bridge constraints enumerate 13,680 eligible placements, reduce to 4,662 and then 945 stronger-filter survivors. Cycle-row and cycle-column positions are part of the equivalence relation; full row/column relabeling and reversal give exactly 20 orbits. The old multiset algorithm and the independent stars-and-bars positive-composition algorithm agree on all n13/n14/n15 counts **and the entire orbit multiplicity map**.

## Exact temporal-information profile semantics

For prefix row P and intersection X=P intersect Q, for every subset S of X, B(S) means that the union of the midpoint knowledge of S covers all original P secrets. Run each suffix component Q's calls backward with one distinct token per Q vertex. For suffix destination v let A_v be the entries whose reversed token sets contain v. Original-order suffix propagation delivers every P secret to every v exactly when B(A_v) is true for every v, equivalently to the subset-bitmask check (B & D) == D, with D marking the A_v requirements.

Separate components in each half use disjoint participants, so component-local orders commute. A global schedule induces a feasible selection of one prefix profile for each of the three rows and one reversed-suffix profile for each of the three columns, satisfying all nine compatibility cells.

**A deliberate relaxation:** the profile CSP does not disallow reuse of an unordered contact edge across the two halves. Removing this restriction can only enlarge the feasible set, so a genuinely UNSAT relaxed CSP excludes the original distinct-contact problem. A SAT relaxed CSP would not be a valid witness.

## Exact and optimistic domains

For a local component on m vertices, the C++ oracle enumerates distinct internal calls: m-1 for a tree and m for a unicyclic component. It checks connectedness, per-cell union coverage and mandatory complete collectors. For m=7, caching the complete (used-edge set, secret-knowledge vector) merges only histories with identical future successors.

A tree's complete collectors must lie among the endpoints of its last contact. For a unicyclic m-contact component, no vertex can know all m secrets after at most m-2 contacts (its contact graph is disconnected), so all final collectors must lie among endpoints of the final two contacts. The implementation's duplicate-endpoint counting is deliberately optimistic, so this pruning cannot exclude a real collector set.

For large seven- and eight-vertex trees the oracle uses an **overapproximation**: remove the final contact edge xy, splitting the prior tree into sides A and C. Give x and y all secrets, and each other vertex all secrets of its own side. Every real tree chronology is dominated by an enumerated optimistic profile. Union coverage and collector conditions are monotone under this extra knowledge. Therefore UNSAT with such profiles is sound.

## Executed results

The freshly reconstructed verifier finds 20/20 UNSAT orbits covering all 945 survivors, partitioned as follows:

| Exclusion type | Orbits |
| --- | ---: |
| Exact empty local component domain | 6 |
| Global incompatible exact component profiles | 10 |
| Global incompatible profiles with optimistic large-tree relaxation | 4 |
| **Total** | **20** |

This is a **different classification** from the lost draft's unverified 7/10/3 report. Two of the six locally impossible orbits also use optimistic domains for unrelated components; their actual obstructions are exact empty local domains.

The demanding seven-vertex unicyclic local pattern with group sizes (2,2,3) and collector demands (2,2,0) is exhausted in the C++ implementation: 28,950,444 node visits, 26,384,430 terminal visits and zero locally admissible states. These are C++ exploration counts from the original implementation; Stage 3 now provides a second independent seven-vertex implementation with different raw chronology counts and exactly matching complete B/D domains. See STAGE3_ADVERSARIAL_AUDIT.md.

The Python checker separately evaluates **all 20 CSP compatibility questions** from the exported local-domain sets, with a different domain-filtering/selection algorithm. Independent Python local chronology enumeration matches C++ on four small component types. An independent semantic checker passes 3,200 randomized direct-gossip versus backward-token-profile tests and 240 randomized optimistic-tree dominance tests.

**Independence boundary updated by Stage 3:** The second C++ disjoint-set/two-phase oracle, which performs no history-state memoization, has now independently enumerated **all 33 exact component types**, including both seven-vertex cyclic cases. Its complete B/D profile sets agree exactly with the primary implementation. The independent Python global checker then reconfirms **20/20** UNSAT using those independently generated exact domains. Large-tree optimistic domains remain shared with the primary generator, supported by a mathematical dominance proof and separate falsification checks. No proof assistant or external referee is claimed. See [Stage 3 adversarial audit](STAGE3_ADVERSARIAL_AUDIT.md).

## Reproduction and machine-readable evidence

From the repository root, run:

    python3 research/v2.1/prove_n15.py

This compiles profile_oracle.cpp with C++17, independently re-enumerates all structural n13-n15 grids, executes every n15 component and compatibility test, compares all twenty recomputed records with N15_CERTIFICATE.json, executes the independent local-domain checks and temporal semantics tests. A crash, timeout, profile-SAT result or mismatched evidence causes failure.

GitHub Actions workflow: .github/workflows/research-v21.yml. Successful source-and-certificate executions after the independent grid checker was added:
- Push: https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40346862524
- PR: https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40346871327

The earlier failed CI at run 40346095006 detected a Python tuple/list difference when comparing in-memory matrices with JSON arrays. That representation mismatch was fixed; the full mathematical search and differential tests had already passed in that run. It was **not** counted as successful CI.

## Boundaries

The unbounded half-forest question (n >= 16), the separate fixed-timestamp temporal-clique 2n-3 conjecture, and global historical priority versus Labahn (1995), Krumme (1996) and other classical gossip-kernel results remain unresolved. The PR remains **draft and unmerged**. A complete externally refereed proof or historical originality certification is not claimed.


## Stage 3 addendum — independent exact component and adversarial pruning audit (26 Oct 2026)

The former single-C++-oracle independence limitation has been **closed for all exact component domains**. A separately written enumerator uses incremental union-find/cycle-rank and explicit final-two-contact search, does not memoize contact history states, and reproduces all **33** complete B/D domain pairs. A separate exhaustive Python suite tests 360,360 n=6 candidate tree orders and the tree/unicyclic n=3..5 spaces against the last-contact collector and optimistic bound, plus 8,272 K4 forward/reverse reachability equivalences. All passed in [Stage 3 push CI](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356861884) and [PR CI](https://github.com/SaridakisStamatisChristos/2nquestion/actions/runs/40356872700). The detailed evidence and residual limits are in [STAGE3_ADVERSARIAL_AUDIT.md](STAGE3_ADVERSARIAL_AUDIT.md). **No formal proof assistant, universal n-theorem, or originality claim is implied.**
