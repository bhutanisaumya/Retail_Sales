Predictive and Forecasting Sales Revenue Model
==============================
**Overview**
This project focuses on developing robust machine learning models to accurately predict and forecast sales revenue for an American retailer.

**Model 1: Predictive Sales Revenue Model** 
A predictive model using LightGBM to provide accurate sales revenue predictions for an item at a specific store on any given date. LightGBM is chosen for its efficiency and speed, making it suitable for large, complex, high-dimensional data.

**Model 2: Forecasting Sales Revenue Model** 
A forecasting model using SARIMA to predict revenue for the next 7 days from any given date. SARIMA is chosen for its effectiveness in addressing the seasonality present in the dataset.

Project Organization
------------

    ├── LICENSE
    ├── Makefile           <- Makefile with commands like `make data` or `make train`
    ├── README.md          <- The top-level README for developers using this project.
    ├── data
    │   ├── external       <- Data from third party sources.
    │   ├── interim        <- Intermediate data that has been transformed.
    │   ├── processed      <- The final, canonical data sets for modeling.
    │   └── raw            <- The original, immutable data dump.
    │
    ├── docs               <- A default Sphinx project; see sphinx-doc.org for details
    │
    ├── models             <- Trained and serialized models, model predictions, or model summaries
    │
    ├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
    │                         the creator's initials, and a short `-` delimited description, e.g.
    │                         `1.0-jqp-initial-data-exploration`.
    │
    ├── references         <- Data dictionaries, manuals, and all other explanatory materials.
    │
    ├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
    │   └── figures        <- Generated graphics and figures to be used in reporting
    │
    ├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
    │                         generated with `pip freeze > requirements.txt`
    │
    ├── setup.py           <- makes project pip installable (pip install -e .) so src can be imported
    ├── src                <- Source code for use in this project.
    │   ├── __init__.py    <- Makes src a Python module
    │   │
    │   ├── data           <- Scripts to download or generate data
    │   │   └── make_dataset.py
    │   │
    │   ├── features       <- Scripts to turn raw data into features for modeling
    │   │   └── build_features.py
    │   │
    │   ├── models         <- Scripts to train models and then use trained models to make
    │   │   │                 predictions
    │   │   ├── predict_model.py
    │   │   └── train_model.py
    │   │
    │   └── visualization  <- Scripts to create exploratory and results oriented visualizations
    │       └── visualize.py
    │
    └── tox.ini            <- tox file with settings for running tox; see tox.readthedocs.io


**Initializing and Pushing to a Remote Repository**
--------------------------------------------------------

1. git init: Initializes a new Git repository in the current directory.

2. git remote add origin git@github.com:bhutanisaumya/Adv_MLA_AT2.git: Sets up a remote repository named "origin" with the provided URL.

3. git add .: Stages all the changes in the current directory for the next commit.

4. git commit -m "first commit": Commits the staged changes with a descriptive commit message.

5. git push --set-upstream origin main: Pushes the committed changes to the remote repository's "main" branch, setting it as the upstream branch for future pushes.



**Steps to access the Project**
--------------------------------

1. Clone the Repository: Using the git clone command, copy the project files from the online Git repository to your local computer.

2. Access the Reository: Open the cmd prompt on your local machine, then go to the directory containing the cloned project.

3. Create a virtual setting: To prevent problems with other projects, it is recommended to a separate environment for the project's dependencies.

4. Install Requirements: Using the pip install command, install the necessary libraries.

5. Execute the Code: Use the notebooks provided in the repository to run the code.



<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
