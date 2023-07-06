## Developer and deployment guide of ship rental http server

# How to install
1. unzip the zip file and see folder structure
   ![](resources\folder-structure.JPG)
2. There are 2 folders `resources` and `src`:
   1. `src` is the folder contains code and unit test
   2. `resources` is the folder contains question pdf and some jpg picture
3. open cmd and navigate to your target folder, in this case: `C:\repos\qrt-test`
   1. Assume that you have already installed python 3.10 in your computer, install python virtual environment: `python -m venv myvenv`
   2. Activate python virtual environment:
      1. In windows: `myvenv\Scripts\activate`
      2. In linux: `source myvenv/bin/activate`
         ![](resources\cmd-pyvenv.JPG)
   3. Run server: `python src\startup.py`
      ![](resources\startup.JPG)

# How to play with the server
1. Please pre-install some API platform, such as postman so that you can easily edit your request. [postman download](https://www.postman.com/downloads/)
2. Edit your request in postman, in this case do `GET`, so you can see ``Hello QRT! This is Ruicheng.``
   ![](resources\hello.JPG)
3. Edit your request in postman, in this case do `POST` and input your contract information in json
   ![](resources\optimization-result.JPG)


## CI pipeline:
- Run `mypy --src` to do static code analysis
- In `src\test` folder, there are some simple unit tests that you can run to make sure the algo works fine

## TODO:
1. database service
2. pre-commit code reformat
3. add git if more development needs to be done
