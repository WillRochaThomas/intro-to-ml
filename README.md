This repository includes a Dockerfile that comes with python3 installed.
The container it starts will automatically run any code in `app.py`. A couple of example usages of machine learning algorithms are provided in this repo, to run them:

    cp fileIWant.py app.py
    docker build -t learn && docker run --rm --name learn

(replace `fileIWant.py` with the real name of the file you want to run e.g. dt.py)
