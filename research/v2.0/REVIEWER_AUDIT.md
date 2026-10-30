# Independent adversarial research audit — v2.0 (25 October 2026)

**Scope:** New original-chronology n<=14 half-forest theorem; original classical source comparison carried forward from v1.8. **No external peer review has occurred.**

| Claim | Exact supporting evidence | Status |
|---|---|---|
| Single-source tree-entry collector lemma | One-use tree-edge cut proof with one original secret initially confined to a singleton intersection | HUMAN-PROVED, external review pending |
| Cellwise secret coverage across every prefix/suffix intersection | Conservation argument, no source can enter a suffix component after the cut except through its midpoint intersection | HUMAN-PROVED |
| n=13 former residual excluded without local-order enumeration | First-bridge collector filter leaves 9 square-pattern placements; new lemma demands 3 complete collectors in a 5-node tree, impossible | PASS |
| n=14 necessary incidence filter | Exact unquotiented 1287 allocations, 4698 eligible cycle placements, 738 previous survivors, 81 strengthened survivors | PASS |
| n=14 symmetry reduction | S3 x S3 x transpose acts on full (matrix, cyclic row, cyclic column) triple; 81 divide into three orbits of 36,9,36 | PASS |
| n=14 first two orbits excluded | Full connected local order enumeration on 6 participants; 360360 and 3603600 ordered edge choices; 0 collector+coverage solutions | PASS |
| n=14 final orbit excluded | 48 five-node prefix-tree orders, 288 five-node suffix-unicyclic orders, all 13824 pairs fail P1-to-Q2 secret propagation | PASS |
| Independent residual implementation | C++ independently constructs local candidate orders and tests all 13824; matches Python | PASS |
| All 4<=n<=14 | Earlier classical two-contact vertex extension preserves both chronological half cycle ranks, reducing smaller counterexample to n14 | PROVED given n14 finite certificate |
| Full n>=15 | No finite/global proof | OPEN |
| Historical global novelty | Labahn/Krumme originals read and compared, but implicit older corollaries across all literature not ruled out | UNRESOLVED |

## Adversarial objections and answers

**1. Could a forward-only suffix filter falsely exclude a valid ordering? Critical.** The reverse collector conditions are checked by running each candidate suffix sequence **backwards**, then the original chronology is used for the actual information transfer. A false use of forward collector flags was caught in early exploration and corrected before the committed proof. Preserve regression assertions of exactly 288 suffix candidates.

**2. Could local necessary conditions be too strong? Major.** Every demanded complete collector is justified by (a) a singleton destination, (b) the single-source suffix-tree entry lemma, or (c) two singleton sources and the first-bridge cut. Every cell must collectively contain all component secrets at the midpoint or that suffix component can never receive the missing secret. A *real* schedule must satisfy every condition; dropping unrelated contacts is valid because prefix components are disjoint and suffix components are disjoint. Failing a condition proves impossibility; passing does not imply realizability.

**3. Did symmetry omit cyclic-placement distinctions? Major.** The canonicalizer transforms \`(matrix, cyclic row, cyclic column)\` under independent permutations and transpose, and checks the exact multiplicities 36+9+36=81. It does not merely quotient matrices.

**4. Are distinct edges enforced?** Every local enumerator selects a sequence without duplicate internal edges. The decisive pair test separately checks for duplicates between the prefix and suffix local components; all 13824 candidate pairs are actually rejected for information propagation, not edge reuse.

**5. Does computational UNSAT imply a universal n theorem? Fatal if claimed.** No. The finite theorem is for n=14, extended downward via a classical explicit construction. n>=15 remains open. The old 2n-3 temporal clique conjecture is independent.

**6. Does novelty follow from no verbatim statement in Labahn/Krumme? No.** The full papers were inspected in v1.8 and are directly cited; mathematical implication from their stronger classifications and remote literature may remain. Priority is not established, only a defensible narrow contribution description.

## Contribution subtraction / next gate

The 2n-4 minimum, static forest partitions, minimal kernel orders, two-contact participant extension, and existential reorderings are classical prior art. The surviving technical contribution is the **single-source tree-entry collector constraint** and an independently executable, *fixed original chronology* finite half-forest guarantee **through n=14**.

**Decision:** strong research-draft candidate suitable for external mathematician scrutiny. The full finite proof, code, and source-linked audit can be shared. **Do not present it as an externally peer-reviewed or first-ever universal result.**
