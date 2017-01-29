tut
===

Tut is a tool that makes python project management easier.

[Overview][#overview]
[Contributing][#contributing]

##Overview

Instead of worrying about which set of tools you're using on your project, tut
abstracts them away. Whether your project uses git, pipenv, docker, pytest and
python 3.6, or mercurial, requirements.txt, virtualenv and nose on python 2.7, a
you would create a project with `tut new <folder>`, run your tests with `tut
test`, and install and manage your dependencies with `tut install <dep>` or `tut
update <dep>`. 


##Contributing

To contribute to tut, here's what you do:

1. Install python3
2. Fork this repo
3. Clone your repo locally (`git clone https://github.com/<you>/tut`)
4. Install pipenv (`pip3 install pipenv`)
5. Initialize the environment (`pipenv init`)
6. Install other deps (`pipenv update`)
7. Branch (`git checkout -b <my_feature>`)
8. Make your changes
9. Test your changes
10. Submit a pull request
