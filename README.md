# Course material for RSE 102

## What is this?

This is course material for a one-week graduate school block course, which is regularly given at the University of Stuttgart. The block course emerged from material of the two master lectures [Simulation Software Engineering](https://simulation-software-engineering.github.io) and [Sustainable Development of Simulation Software](https://gitlab.com/sustainable-simulation-software/course-material) in an effort to teach better research software engineering skills to PhD students.

**Why 102?** We do not start from scratch, but assume a certain pre-knowledge from participants -- knowledge typically taught in Software Carpentry Workshops: Unix shell, Git basics, and Python. We want to build on these fundamentals and study methods and tools used to ensure good (research) software engineering:

- Git workflows
- Containerization
- Testing and continuous integration
- Building and packaging
- Software design principles

Skills in these areas are crucial for developing or contributing to quality-assured software in collaborative environments and are very useful in today’s research landscape.

## Courses

- We typically give the course just before the lecture period in winter term.
- Next course will be **October 7-11, 2024** with the *reflection day* on **December 10, 2024**. Registration via [Campus](
https://campus.uni-stuttgart.de/cusonline/ee/ui/ca2/app/desktop/#/pl/ui/$ctx/wbLv.wbShowLVDetail?$ctx=design=ca2;header=max&pSpracheNr=1&pStpSpNr=403777) or (if you not a student and cannot access) via mail to [benjamin.uekermann@ipvs.uni-stuttgart.de](mailto:benjamin.uekermann@ipvs.uni-stuttgart.de). Limited seats, first come first serve.
- The first course ran from Tuesday, October 4 to Friday October 7, 2022, with the *reflection day* on December 6, 2022.
- There was no course in 2023. Instead, we organized a week-long summer school on [Research Software Engineering with Julia: Basics, Visualization, and Statistics](https://www.simtech.uni-stuttgart.de/events/simtech-summer-school/SuSch_2/)

## Timetable and content

### Day 1: Orga and Git

- 10:30-12:30: Orga and student presentations
- 14:00-15:30: Recap of Git basic, Git workflows
- 16:00-17:30: Exercise on Git workflows

### Day 2: Python packaging and testing

- 09:00-10:30: Introduction to packaging and packaging for Python
- 11:00-12:30: Exercise on packaging for Python
- 14:00-15:30: Introduction to testing and testing for Python
- 16:00-17:30: Exercise on testing for Python

### Day 3: Containerization and automation

- 09:00-10:30: Introduction to containerization and Docker
- 11:00-12:30: Exercise: build and run your research code in a Docker container
- 14:00-15:30: Introduction to automation and GitHub Actions 
- 16:00-17:30: Exercise on GitHub Actions

### Day 4: Software design

- 09:00-10:30: Clean code
- 11:00-12:30: Exercise on clean code
- 14:00-15:30: Design principles and patterns
- 16:00-17:30: Exercise on design principles and patterns

### Day 5: Misc and wrap up

- 09:00-10:30: Technical writing, versioning, licenses, and more
- 11:00-12:30: Finish all your exercises or start applying things on your project

### Reflection day

How did you apply the newly learned skills in your work? Which problems did you face?
Each participant should prepare a 5-10 minutes presentation. There is enough time for in-depth discussions.

## Credits

- The Simulation Software Engineering lecture was originally developed by [Ishaan Desai](https://github.com/IshaanDesai), [Alexander Jaust](https://github.com/ajaust), and [Benjamin Uekermann](https://github.com/uekerman). [Many students](https://github.com/Simulation-Software-Engineering/Lecture-Material/graphs/contributors) helped improving the content.
- The Sustainable Development of Simulation Software was originally developed by [Dennis Gläser](https://github.com/dglaeser) and [Bernd Flemisch](https://github.com/berndflemisch).
- Since then, also Matthias Braun, [Gerasimos Chourdakis](https://github.com/MakisH), and Stefan Meggendorfer have been contributing to the material. 

In several parts of the material, we use content from

> Irving, Hertweck, Johnston, Ostblom, Wickham, and Wilson: [Research Software Engineering with Python](https://merely-useful.tech/py-rse), 2021,

a book, which we also recommend to recap Git/Bash/Python basics.
