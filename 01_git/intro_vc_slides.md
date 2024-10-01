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
</style>

# Introduction to Version Control

---

## Why Do We Need Version Control?

Version control ...

- tracks changes to files and helps people share those changes with each other.
    - Could also be done via email / Google Docs / ..., but not as accurately and efficiently
- was originally developed for software development, but today cornerstone of *reproducible research*

> "If you can't git diff a file format, it's broken."

---

## How Does Version Control Work?

- *master* (or *main*) copy of code in repository, can't edit directly
- Instead: check out a working copy of code, edit, commit changes back
- Repository records complete revision history
    - You can go back in time
    - It's clear who did what when

---

## The Alternative: A Story Told in File Names

<img src="http://phdcomics.com/comics/archive/phd052810s.gif" width=60% style="margin-left:auto; margin-right:auto">

[http://phdcomics.com/comics/archive/phd052810s.gif](http://phdcomics.com/comics/archive/phd052810s.gif)

---

## The Only Standard Today: Git

- There were many version control systems: [Podcast All Things Git: History of VC](https://www.allthingsgit.com/episodes/the_history_of_vc_with_eric_sink.html)
- Today: no longer a fragmented market, there is nearly only Git:
  - [Stackoverflow developer survey 2021](https://insights.stackoverflow.com/survey/2021#technology-most-popular-technologies):
    > "Over 90% of respondents use Git, suggesting that it is a fundamental tool to being a developer."
  - Is this good or bad?

---

## More Facts on Git

Git itself is open-source: GPL license

- source on [GitHub](https://github.com/git/git), contributions are a bit more complicated than a simple PR
- written mainly in C
- started by Linus Torvalds, core maintainer since later 2005: Junio Hamano
