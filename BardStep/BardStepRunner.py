import subprocess
import os
from pathlib import Path
from shutil import copyfile
from WStoWG import getWG

WORLD_NAME = "door"

def runBardStep(problem,ip,domain,output,exoutput,optoutput):
    if ip == None:
        subprocess.call(['java', '-jar', 'BardStep1.1.jar',
                        '-d', domain,
                        '-p', problem,
                        '-o', output,
                        '-eo', exoutput,
                        '-oo', optoutput,
                        '-np'])
    else:
        subprocess.call(['java', '-jar', 'BardStep1.1.jar',
                        '-d', domain,
                        '-p', problem,
                        '-ip', ip,
                        '-o', output,
                        '-eo', exoutput,
                        '-oo', optoutput,
                        '-np'])

def checkForEnding():
    if Path('log/'+ WORLD_NAME + '-executed.txt').is_file():
        f = open('log/'+ WORLD_NAME + '-executed.txt')
        for line in f:
            if line == "Story Over":
                return True
    return False

def initialSetup():
    if Path('log/' + WORLD_NAME + '-current.pddl').is_file():
        os.remove('log/' + WORLD_NAME + '-current.pddl')
    if Path('log/'+ WORLD_NAME + '-executed.txt').is_file():
        os.remove('log/'+ WORLD_NAME + '-executed.txt')
    if Path('log/'+ WORLD_NAME + '-executed.txt').is_file():
        os.remove('log/'+ WORLD_NAME + '-executed.txt')
    copyfile(   'tests/' + WORLD_NAME + '-problem.pddl',
                'log/' + WORLD_NAME + '-current.pddl')

def getRecentWorldState():
    getWG(  'log/' + WORLD_NAME + '-current.pddl',
            'tests/' + WORLD_NAME + '-domain.pddl')

def setBardStep():
    runBardStep('log/' + WORLD_NAME + '-current.pddl',
                None,
                'tests/' + WORLD_NAME + '-domain.pddl',
                'log/' + WORLD_NAME + '-current.pddl',
                'log/' + WORLD_NAME + '-executed.txt',
                'log/' + WORLD_NAME + '-options.txt')

def takeAction(action):
    runBardStep('log/' + WORLD_NAME + '-current.pddl',
                action,
                'tests/' + WORLD_NAME + '-domain.pddl',
                'log/' + WORLD_NAME + '-current.pddl',
                'log/' + WORLD_NAME + '-executed.txt',
                'log/' + WORLD_NAME + '-options.txt')

def getExecuted():
    ls = []
    if Path('log/'+ WORLD_NAME + '-executed.txt').is_file():
        f = open('log/'+ WORLD_NAME + '-executed.txt')
        for line in f:
            line = line.strip()
            if not line.startswith('(Final Bardiche Story'):
                line = line.replace('(:steps ', '')
                ls.append(line)
    return ls

def getOptions():
    ls = []
    if Path('log/'+ WORLD_NAME + '-options.txt').is_file():
        f = open('log/'+ WORLD_NAME + '-options.txt')
        for line in f:
            ls.append(line[4:-2])
    return ls

initialSetup()
setBardStep()
getRecentWorldState()
for e in getExecuted():
    print(e)
while not checkForEnding():
    print("o = show possible options")
    print("q = stop the game")
    while True:
        action = input("Take step? Put in your input:\n")
        if action == '':
            setBardStep()
            getRecentWorldState()
            for e in getExecuted():
                print(e)
            break
        elif action == 'q':
            break
        elif action == 'o':
            for e in getOptions():
                print(e)
            print('\n')
        else:
            takeAction(action)
            getRecentWorldState()
            for e in getExecuted():
                print(e)
            break
print("\nStory over.")
