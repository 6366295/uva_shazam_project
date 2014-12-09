'''
    
'''
def match_fingerprints(fingerprints, test_data):
    
    # Vind het nummer in test_data dat het best overeenkomt met de opgegeven fingerprints
    
    n_hits = {}
    
    for filename, cur_test_data in test_data.items():
        total_hits = []
        
        cur_match = (-1, -1)
        
        def next_match(last_match):
            for i in range(last_match[0] + 1, len(fingerprints)):
                p = fingerprints[i]
                for mi in range(last_match[1] + 1, len(cur_test_data)):
                    # Is it mi you're looking for?
                    if p[1] == cur_test_data[mi][1]:
                        return i, mi
              
        cur_match = next_match(cur_match)
        while cur_match != None:
            consecutive_hits = 1
            i1, i2 = cur_match
            found_hit = True
            while found_hit and i2 < len(cur_test_data) - 1:
                p = cur_test_data[i2 + 1][1]
                dt = cur_test_data[i2 + 1][0] - cur_test_data[i2][0]
                t = fingerprints[i1][0] + dt
                found_hit = False
                for i in range(i1 + 1, len(fingerprints)):
                    if t == fingerprints[i][0] and p == fingerprints[i][1]:
                        consecutive_hits += 1
                        i1, i2 = cur_match = i, i2 + 1
                        found_hit = True
                        break
            total_hits.append(consecutive_hits)
            cur_match = next_match(cur_match)
        
        n_hits[filename] = total_hits
    
    return n_hits
    
# fingerprints = [(2, 's'), (4, '2'), (5, 'q')]
# cur_test_data = [[(1, 'a'), (2, 's'), (3, 'q'), (4, '2'), (5, 'q')]]
                
# print match_fingerprints(fingerprints, cur_test_data)