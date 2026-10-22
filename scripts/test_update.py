import unittest
from update import formula


class FormulaTest(unittest.TestCase):
    def sums(self):
        return "\n".join(f'{"a" * 64}  switchpack-{platform}-{arch}.tar.gz' for platform in ["darwin", "linux"] for arch in ["arm64", "x64"])

    def test_four_platforms(self):
        result = formula("v0.1.0", self.sums())
        self.assertEqual(result.count('sha256 "'), 4)
        self.assertIn('version "0.1.0"', result)
        self.assertIn('depends_on "libmtp"', result)

    def test_rejects_incomplete_or_untrusted_metadata(self):
        for tag, checksums in [("v1;injection", self.sums()), ("v0.1.0", ""), ("v0.1.0", self.sums() + "\n" + self.sums()), ("v0.1.0", self.sums().replace("a" * 64, "invalid"))]:
            with self.assertRaises(ValueError):
                formula(tag, checksums)


if __name__ == "__main__":
    unittest.main()
