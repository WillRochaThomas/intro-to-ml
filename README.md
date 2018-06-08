# Intro to machine learning with scikit-learn

This repository includes a Dockerfile for building a container with python3 installed.
The container it starts will automatically run any code in `app.py`. A couple of example usages of machine learning algorithms are provided in this repo, to run them:

    cp decision-tree-example.py app.py
    docker build . -t learn && docker run --rm --name learn

(replace `decision-tree-example.py` with the real name of the file you want to run if it's not that e.g. kmeans-example.py)

I've included some example code showing use of a decision tree (used for classification tasks) and kmeans clustering (used for clustering tasks).


