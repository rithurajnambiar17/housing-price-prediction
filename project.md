## Project: Predicting Boston Housing Prices

## Project Overview
In this project, you will apply basic machine learning concepts on data collected for housing prices in the California area to predict the selling price of a new home. You will first explore the data to obtain important features and descriptive statistics about the dataset. Next, you will properly split the data into testing and training subsets, and determine a suitable performance metric for this problem. You will then analyze performance graphs for a learning algorithm with varying parameters and training set sizes. This will enable you to pick the optimal model that best generalizes for unseen data. Finally, you will test this optimal model on a new sample and compare the predicted selling price to your statistics.

## Project Highlights
This project is designed to get you acquainted to working with datasets in Python and applying basic machine learning techniques using NumPy and Scikit-Learn. Before being expected to use many of the available algorithms in the sklearn library, it will be helpful to first practice analyzing and interpreting the performance of your model.

Things you will learn by completing this project:

- How to use NumPy to investigate the latent features of a dataset.
- How to use scikit-learn library for various manipulations and ML model training and validation.
- How to deploy ML model using Flask

## Software and Libraries
This project uses the following software and Python libraries:

- [Python](https://www.python.org/download/releases/3.0/)
- [NumPy](http://www.numpy.org/)
- [pandas](http://pandas.pydata.org/)
- [scikit-learn](http://scikit-learn.org/stable/)
- [matplotlib](http://matplotlib.org/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/)

You will also need to have software installed to run and execute a [Jupyter Notebook](http://ipython.org/notebook.html).

If you do not have Python installed yet, it is highly recommended that you install the [Anaconda](http://continuum.io/downloads) distribution of Python, which already has the above packages and more included. 

## Starting the Project

This project contains three files:

- `housing-price-prediction.ipynb`: This is the main file where you will be performing your work on the project.
- `housing.csv`: The project dataset. You'll load this data in the notebook.
- `app.py`: This Python script is used to create a deployment project for our ML model.
- `my_model.pkl`: This [Pickle](https://docs.python.org/3/library/pickle.html) is created at the end of our project using [joblib](https://pypi.org/project/joblib/) to save our model for further use in deployment

In the Terminal or Command Prompt, navigate to the folder containing the project files, and then use the command `jupyter notebook housing-price-prediction.ipynb` to open up a browser window or tab to work with your notebook. Alternatively, you can use the command `jupyter notebook` or `ipython notebook` and navigate to the notebook file in the browser window that opens. Follow the instructions in the notebook and answer each question presented to successfully complete the project. A **README** file has also been provided with the project files which may contain additional necessary information or instruction for the project. 
