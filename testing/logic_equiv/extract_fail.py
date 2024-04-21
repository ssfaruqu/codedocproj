import json
import re 

fail_ratios = []

def getFailRatios():
    return fail_ratios

# Extract the fail ratios of logical equivalence tests from its corresponding result file
results = []
with open('result.json', 'r') as f:
    for line in f:
        print(line)
        results.append(json.loads(line))

# only need JSON objects with hypothesis stats key
results = [x for x in results if '_hypothesis_stats' in x]

for r in results:
    print(r['nodeid'])
    print(r['_hypothesis_stats'])

    # get total number of passing tests
    passing = re.findall('[0-9]*[0-9]*[0-9] passing', r['_hypothesis_stats'])
    passing = [re.findall('[0-9]*[0-9]*[0-9]', x)[0] for x in passing]
    passing = [int(x) for x in passing]
    passing = sum(passing)

    # get total number of failing tests
    failing = re.findall('[0-9]*[0-9]*[0-9] failing', r['_hypothesis_stats'])
    failing = [re.findall('[0-9]*[0-9]*[0-9]', x)[0] for x in failing]
    failing = [int(x) for x in failing]
    failing = sum(failing)

    print(passing, failing)
    fail_ratios.append(failing/(passing+failing))
    print(fail_ratios)

