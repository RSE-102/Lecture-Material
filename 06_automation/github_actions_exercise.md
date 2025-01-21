# Automating Workflows with GitHub Actions

In this exercise, we create automated workflows and pipelines based on GitHub Actions. We are again working with our beloved diffusion Python code.

## Preparations

- Create a new repository named "rse102-github-actions-exercise" in your own account/namespace on GitHub (with an empty README file) and clone the repository afterwards.
  - **Note**: We cannot work with forks here because GitHub Actions may not work in pull requests without explicit approval of the owner of the target repository. It is also easier to add badges (see below) to the `README.md` if the repository is under your control.
- Add the contents of the [automation exercise repository](https://github.com/RSE-102/automation-exercise) to your own repository. You can do this by copying the files into your own repository, adding, and committing them to Git. Afterwards push the changes to GitHub and verify that your repository contains the same files as the `automation-exercise` repository.
  - **Note**: If you use another way of adding the data to your repository, e.g., by defining a new remote, make sure that the `origin` remote points to your own repository.

## Task descriptions

The CI workflow should be triggered by `push` events and should have three jobs:

1. Name: `style_check`. Check the code style of the Python files in the repository using [`black`](https://github.com/psf/black). This check should fail if `black` finds any file to reformat.
2. Name: `test`. Run tests while also collecting coverage information via `pytest` and the `coverage` package. The coverage information (stored in the file `.coverage`) has to be stored and handed over to the next step.
    - The intermediate coverage information (`.coverage`) should be kept for one day. This is the minimum amount of time an artifact must be stored.
    - Adding a `.gitignore` file helps to not accidentally commit the temporary coverage files.
3. Name: `coverage_report`. Create a coverage report (`coverage report`) in the terminal and afterwards also convert the coverage information into XML format (`coverage xml`). For this you have to reuse the coverage information (i.e. `.coverage`) from the previous step.
    - Running `coverage report` allows us to inspect the coverage directly in the workflow's output. Saving the XML file allows us to analyze the coverage in more detail with other tools if needed.
    - The resulting file `coverage.xml` should be kept for 14 days.

Once the workflow runs successfully, add a [GitHub workflow status badge](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/adding-a-workflow-status-badge) for your workflow to the `README.md`. Label this badge with "RSE 102 CI/CD".
