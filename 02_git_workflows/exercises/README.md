Git workflow exercises
=======================

The exercises should be worked on in groups of two people.
Start with forking this repository (each one of you), and decide which of the two
forks should act as the "main repository". Note that the exercises
build upon each other, so you need, for instance, exercise 1 to be completed before
you can continue with exercise 2. Each exercise is described in the comments at the top of the respective `.py` file.

Typically, each one of you will have to make one of the already existing tests pass. 
The tests in a file can be run with `pytest`, for instance, with `python3 -m pytest FILENAME.py`.
To run only the test you are working on, use `python3 -m pytest FILE.py -k TESTNAME`.


## Exercise 1

- commit `exercise1.py` into the repository and push it
- make sure both of you have this state of the repository on your local machines
- distribute the two tasks and work on them in parallel:
  - create a branch for your task, giving it an appropriate name
  - commit the solution to your task in a single commit with appropriate name
  - push your commit to the remote repository
  - open a merge request into the main branch
- Together, integrate both tasks via merge requests. The final git history should look like this (but with proper commit messages):
- ```sh
    * merge task B
    | \
    |  * task B
    | /
    * merge task A
    | \
    |  * task A
    | /
    * commit adding `exercise1.py`
    ```


## Exercise 2

- repeat the same procedure as from exercise 1, but this time using the file `exercise2.py`
- as in exercise 1 we want a semi-linear history, which should now continue like this:
- ```sh
    * merge ex2 task B
    | \
    |  * ex2 task B
    | /
    * merge ex2 task A
    | \
    |  * ex2 task A
    | /
    * commit adding `exercise2.py`
    | \
    ...
    ```
- again, proper commit messages and branch names should be used


## Exercise 3

- repeat the procedure from the previous exercises, but this time using the file `exercise3.py`
- we again want a semi-linear history, but this time the entire exercise should be done in one merge request:
- ```sh
    * merge ex3
    | \
    |  * ex3 task B
    |  * ex3 task A
    |  * commit adding `exercise3.py`
    | /
    * merge ex2 task B (from last exercise)
    | \
    ...
    ```
- again, proper commit messages and branch names should be used


## Exercise 4

- in this exercise, we want to achieve yet a different layout of the git history:
- ```sh
    * merge ex4
    | \
    |  * merge ex4 task B
    |  | \
    |  |  * ex4 task B
    |  | /
    |  * merge ex4 task A
    |  | \
    |  |  * ex 4 task A
    |  | /
    |  * commit adding `exercise4.py`
    | /
    * merge ex3 (from last exercise)
    | \
    ...
    ```
