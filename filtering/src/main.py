import csv
from loader import load_data as load
from loader import load_win_rate
from generalModel import Model
import psutil
import time
from datetime import date

#config
config = { 
    'dataset':"../data/filtered-dataset-no-header.csv",
    'win_rate_file': '../data/win_rate.txt',
    'team_dictionary': '../data/team_dict.txt',
    'num_recs': 1,
    'num_requests': 100,
    'save_results': False,
    'results_location': 'results/real'
}

def main():
    run_experiment(config["num_requests"], config['results_location'])

def run_experiment(num_requests, location):
    #load the data
    data = load(config["dataset"], config['team_dictionary']) 
    win_rate = load_win_rate(config["win_rate_file"])

    #instantiate the filtering model object
    model = Model(data, win_rate, config['num_recs'])

    #example input
    blue_team = ['121', '24', '18']
    red_team = ['11', '26']
    
    results = []
    recs = []
    for i in range(num_requests):
        print(f'iter: {i}')
        res, blue, red = make_prediction(model, blue_team, red_team, model.predict)
        results.append(res)
        recs.append(combine_recs(blue, red))
        print(res)
    if config['save_results']:
        save_results(results, recs, location)

#print out the recommendations to std out
def combine_recs(blue, red):
    res = []
    for b, r in zip(blue.keys(),red.keys()):
        res.append(list(b) + list(r))
        print(list(b) + list(r))
    return res

#make a recommendation and return the latency, and the memory usage
def make_prediction(model, blue_team, red_team, prediction_function):
    start_time = time.time()
    blue, red = prediction_function(blue_team, red_team)
    finish_time = time.time()
    peak_memory_usage = psutil.Process().memory_info().rss / 1000000
    print('Blue recommendations:')
    print(blue)
    print('Red recommendations:')
    print(red)
    return [finish_time - start_time, peak_memory_usage], blue, red

#save results, if necessary
def save_results(results, recs, location):
    today = date.today().strftime('%d-%m-%Y')
    curr_time = time.time()
    average_time = 0
    average_mem = 0
    with open(f'{location}/results-{today}-{curr_time}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in results:
            writer.writerow(row)
            average_time += row[0]
            average_mem += row[1]
    f.close()

    with open(f'{location}/recs-{today}-{curr_time}.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        for row in recs:
            for rec in row:
                writer.writerow(rec)
    f.close()

    average_time /= len(results)
    average_mem /= len(results)
    print(f'Average time: {average_time}')
    print(f'Average peak memory usage: {average_mem}')

if __name__ =='__main__':
    main()