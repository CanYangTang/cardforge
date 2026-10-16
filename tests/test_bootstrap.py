import subprocess
import sys
import unittest
from pathlib import Path


PROJECT_ROOT = Path(__file__).parents[1]


class BootstrapTest(unittest.TestCase):
    def test_module_starts_successfully(self) -> None:
        result = subprocess.run(
            [sys.executable, "-m", "app"],
            cwd=PROJECT_ROOT,
            capture_output=True,
            text=True,
            check=False,
        )

        self.assertEqual(result.returncode, 0)
        self.assertIn("CardForge is ready", result.stdout)


if __name__ == "__main__":
    unittest.main()

