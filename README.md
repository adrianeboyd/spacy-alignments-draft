<a href="https://explosion.ai"><img src="https://explosion.ai/assets/img/logo.svg" width="125" height="125" align="right" /></a>

# spacy-tokenizations: Align tokenizations for spaCy + transformers

A spaCy package for Yohei Tamura's Rust [tokenizations
library](https://github.com/tamuhey/tokenizations/) and [Python
bindings](https://github.com/tamuhey/tokenizations/tree/master/python).

## Installation

```
pip install -U pip setuptools wheel
pip install spacy-tokenizations
```

If no binary wheel is available for your platform, you will need to [install
Rust](https://www.rust-lang.org/tools/install) in order to build
`spacy-tokenizations` from source.

## spacy-tokenizations vs. pytokenizations

The `spacy_tokenizations` module is a drop-in replacement for `tokenizations`:

```python
import spacy_tokenizations as tokenizations
a2b, b2a = tokenizations.get_alignments(["å", "BC"], ["abc"])
assert a2b == [[0], [0]]
assert b2a == [[0, 1]]
```

The only difference between this package and the original
[`pytokenizations`](https://pypi.org/project/pytokenizations/) is that it
switches the build system to `setuptools-rust` to make it easier for us at
Explosion to build binary and source packages for a wider range of platforms.
