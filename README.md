# my-advanced-python
This repo mainly contains some interesting/advanced topics about Python3 in my work/life

# How to config environment
### tips: strongly encourage users to use pycharm as IDE

- Download anaconda from official web
- Open new project in pycharm and navigate to *Project -> Python Interpreter* and choose a conda interpreter
- Open pycharm integrated terminal and run following lines
  - Open terminal and key in `conda --version` to make sure conda works
  - `conda install mamba -c conda-forge`
  - `mamba env update --file environment.yml`
  - `mamba env update --file environment-dev.yml`
- FYI, find conda guide:
  - https://conda.io/projects/conda/en/latest/user-guide/getting-started.html
