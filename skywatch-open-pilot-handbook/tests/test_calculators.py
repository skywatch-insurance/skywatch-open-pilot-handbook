import importlib.util
import unittest
from pathlib import Path


SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"


def load(name):
    spec = importlib.util.spec_from_file_location(name, SCRIPTS / f"{name}.py")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class CalculatorTests(unittest.TestCase):
    def test_training_budget(self):
        m = load("training_budget")
        result = m.estimate(60, 160, 45, 70, 15, 1000, 1000, 10)
        self.assertEqual(result["aircraft"], 9600)
        self.assertEqual(result["instruction"], 4200)
        self.assertEqual(result["estimated_total"], 17380)

    def test_training_rejects_impossible_dual(self):
        m = load("training_budget")
        with self.assertRaises(ValueError):
            m.estimate(40, 100, 41, 50, 0, 0, 0, 0)

    def test_ownership_cost(self):
        m = load("ownership_cost")
        result = m.estimate(100, 8, 6, 2, 30, 20, 5, 2000, 6000, 2500, 600, 0, 500, 10)
        self.assertEqual(result["fuel"], 4800)
        self.assertEqual(result["estimated_annual_total"], 24310)

    def test_weight_balance(self):
        m = load("weight_balance")
        result = m.calculate([("empty", 1500, 40), ("pilot", 200, 37)], 1800, 35, 47)
        self.assertAlmostEqual(result["total_weight"], 1700)
        self.assertAlmostEqual(result["calculated_cg"], 39.647, places=3)
        self.assertTrue(all(result["user_supplied_boundary_checks"].values()))


if __name__ == "__main__":
    unittest.main()
