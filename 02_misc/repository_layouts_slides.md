---
type: slide
slideOptions:
  transition: slide
  width: 1400
  height: 900
  margin: 0.1
---

<style>
  .reveal strong {
    font-weight: bold;
    color: orange;
  }
  .reveal p {
    text-align: left;
  }
  .reveal section h1 {
    color: orange;
  }
  .reveal section h2 {
    color: orange;
  }
  .reveal pre code {
    font-family: 'Ubuntu Mono';
    color: orange;
  }
  .reveal section img {
    background:none;
    border:none;
    box-shadow:none;
  }
</style>

# Repository layouts

---

## Motivation

- Repositories contain source code, documentation, CI/CD config files, test files, author lists, etc.
- You want to divide the project structure to simplify CD workflows and packaging.

---

## Python src layout

```
mypackage/
├── docs/
│   ├── conf.py
│   └── index.rst
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── main.py
├── tests/
│   └── integration_test.py
├── CHANGELOG.md
├── LICENSE.md
├── README.md
└── pyproject.toml
```

---

## Pitchfork layout

```
myapp/
├── docs/
│   ├── Doxyfile
│   └── main.dox
├── include/
│   └── myapp/
│       └── api.h
├── src/
│   ├── core.h
│   └── core.c
├── tests/
│   └── unit_test.c
├── CHANGELOG.md
├── LICENSE.md
└── README.md
```

---

## Further Reading

- [Pitchfork](https://github.com/vector-of-bool/pitchfork)
- Python Packaging User Guide's [src layout vs flat layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
