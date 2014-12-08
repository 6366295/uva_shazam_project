import hashlib

'''
    Calculates fingerprints from a set of spectrogram maxima.
    Makes pairs of maxima consisting of each maximum and the next `num_pairs` in time.
    Expects `maxima` as a list of (t, f) tuples.
    Returns fingerprints as a list of (t, p) tuples.
'''
def generate_fingerprints(maxima, num_pairs=5):
    maxima = sorted(maxima, key=lambda tup: tup[0])
    fingerprints = []
    
    for index in range(len(maxima)):
        t1, f1 = maxima[index]
        for offset in range(1, num_pairs + 1):
            if index + offset < len(maxima):
                t2, f2 = maxima[index + offset]
                
                # invoeren max/min dt?
                dt = t2 - t1
                p = hashlib.sha1('{0} {1} {2}'.format(f1, f2, dt)).hexdigest()
                
                #print (t1, f1), (t2, f2)
                fingerprints.append((t1, p))
    
    return fingerprints
