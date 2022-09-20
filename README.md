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

# Table of content
- **cross-reference-gc**: some mysterious memory leak might because of Python cross-reference issues and its garbage collection mechanism, use weak reference might be a good solution
- **generator**: when we want to iterate over any object(for me especially in dataframe or series), it will be more memeory efficient to use generators instead of converting data into iterables, sometime even necessary to use multi-layer chunk-sized generator.
- **multi-thread, multi-process, ascycI/O **

### Good reference books:
- [Advanced Guide to Python 3 Programming](https://warin.ca/ressources/books/2019_Book_AdvancedGuideToPython3Programm.pdf)
