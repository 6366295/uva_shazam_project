from database import create_database
from database import read_database
from database import analyze

from match import match_fingerprints

from sys import argv

def rate(results):
    return
    
def print_scores(results, consecutive_scale_factor=1):
    rate = lambda r: sum(map(lambda m: pow(m, consecutive_scale_factor), r))
    results = map(lambda t: (t[0], rate(t[1])), results.items())
    # max_score = max(map(lambda t: t[1], results))
    # results = map(lambda t: (t[0], 10.0*t[1]/max_score), results)
    results = sorted(results, key=lambda tup: tup[1], reverse=True)
    
    for filename, score in results:
        print filename + ':', score

if __name__=="__main__":
    # create_database()
    database = read_database()
    
    data = analyze(argv[1])
    results = match_fingerprints(data, database)
    print_scores(results)
    
    
    
    
