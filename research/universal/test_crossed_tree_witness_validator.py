"""Adversarial checks for exact crossed-tree witness validation.

No valid crossed-tree example is assumed to exist. Positive tests exercise
individual chronological trees; negative tests mutate separate hypotheses.
"""
import unittest
from crossed_tree_witness_validator import replay, verify

class TestWitnessValidator(unittest.TestCase):
    def test_chronological_not_static_connectivity(self):
        t={"vertices":[0,1,2,3],"calls":[[0,1],[2,3],[1,2]]}
        v,e,k=replay(t)
        self.assertEqual(k["0"],3)
        self.assertEqual(k["3"],12)
        self.assertEqual(k["1"],15)
        self.assertEqual(k["2"],15)

    def test_reject_repeated_edge(self):
        with self.assertRaises(AssertionError):
            replay({"vertices":[0,1,2],"calls":[[0,1],[1,0]]})

    def test_reject_disconnected_cycle(self):
        with self.assertRaises(AssertionError):
            replay({"vertices":[0,1,2,3],"calls":[[0,1],[1,2],[2,0]]})

    def test_reject_nonterminal_full_roots(self):
        t={"vertices":[0,1,2,3],"calls":[[0,1],[2,3],[1,2]]}
        with self.assertRaises(AssertionError):
            verify({"T":t,"U":t})

    def test_reject_insufficient_coverage_even_with_outside_final_roots(self):
        t={"vertices":["a","b","r","s"],"calls":[["a","r"],["b","s"],["r","s"]]}
        u={"vertices":["a","b","p","q"],"calls":[["a","p"],["b","q"],["p","q"]]}
        # Both original last edges have endpoints OUTSIDE X={a,b}.
        # The reason for rejection is genuinely insufficient X coverage.
        with self.assertRaisesRegex(AssertionError, "double coverage"):
            verify({"T":t,"U":u})

if __name__=="__main__":
    unittest.main()
