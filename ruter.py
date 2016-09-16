import json, subprocess, sys

west_lines = ["Vestli via Storo", "Sognsvann", "Ringen via Storo"]
east_lines = ["Bergkrystallen via Majorstuen","Vestli via Majorstuen","Ringen via Majorstuen", "Sognsvann via Tøyen", "Vestli"]
working_lines = None

if len(sys.argv) < 2:
    print ("USAGE: python ruter.py StopName [--W --E]")
    exit(-1)

#Get data for requested stop
data = None
stop = sys.argv[1]
if stop == "Forskningsparken":
      data = subprocess.check_output(["bash","-c","curl -s 'https://ruter.no/reiseplanlegger/Stoppested/(3010370)Forskningsparken%20%5bT-bane%5d%20(Oslo)/Avganger/'"])
elif stop == "Blindern":
    data = subprocess.check_output(["bash","-c","curl -s 'https://ruter.no/reiseplanlegger/Stoppested/(3010360)Blindern%20%5bT-bane%5d%20(Oslo)/Avganger/'"])
elif stop == "Storo":
    data = subprocess.check_output(["bash","-c","curl -s 'https://ruter.no/reiseplanlegger/Stoppested/(3012120)Storo%20%5bT-bane%5d%20(Oslo)/Avganger/'"])
else:
    print ("Unknown stop!")
    exit(-1)

working_lines = west_lines + east_lines
#Find out which lines should be printed
for arg in sys.argv[1:]:
    if arg == "--W":
        working_lines = west_lines
    elif arg == "--E":
        working_lines = east_lines

data = str(data)
#Extract the JSON part of the data
data = data[data.find('angular.fromJson(')+17:]
data = data[0:data.find(");")-1]


data = json.loads(data)


for dep in data["platforms"]:
    for line in dep["lines"]:
        if line["destination"] in working_lines:
            print (line["destination"] + " : " +line["departures"][0]["departureTime"])
