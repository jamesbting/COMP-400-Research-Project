# League of Legends Real-Time Champion Prediction using Filtering

For a useful recommendation using collaborative filtering, the input must be a subset of the recommendation

In the model implemented for this project, on startup, each combination of teams is recorded in a hash map, mapping to the win-rate of that combination. For the similarity calculation, the model searches the datasets for all possible combinations that could result from the provided team. 

For the prediction calculation, the combinations that satisfied the subset condition were sorted by win rate. Then the algorithm returns the top k combinations with the highest win rate, where k is the number of recommendations requested by the user. 

## Pre-requisites

- Python 3.9.2
- pip 21.0.1

The following Python modules are required as well

- psutil

By running the following command ```pip install psutil```. 

## Setting up the program 

After downloading the repository, and installing all the modules, ensure that the file locations in the config dictionary located in main.py are correct. Select the number of recommendation and experiments.

### Loading the data

The program will load the data into memory for usage to start the model. Loading by team combination will mean that the program will load a dictionary mapping the combinations to the win rate of each combination. 

## Running the program

To run the program, navigate to the directory containing the entire program, and then run the following command: ```python src/main.py```

## Results

Recommendations for each experiment are printed to STDOUT

The results are stored in the results folder by default. Running the program with the option to save data will generate 2 files: results.csv and recs.csv, stamped with the date and the time. 

For results.csv: Each row will represent one experiment, with 2 numbers. The first number is the time to run the experiment, and the second one is the peak memory usage in megabytes. 

For recs.csv: Each row will represent one experiment, with 10 integers. It is the recommendation of the algorithm for that experiement.