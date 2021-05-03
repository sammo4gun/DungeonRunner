import subprocess
from shutil import copyfile
from WStoWG import getWG

WORLD_NAME = "door"

def runBardStep(problem='tests/door-problem.pddl',
                ip = None,
                domain='tests/door-domain.pddl',
                output = 'log/door-current.pddl'):
    if ip == None:
        subprocess.call(['java', '-jar', 'BardStep1.0.jar',
                        '-d', domain,
                        '-p', problem,
                        '-o', output])
    else:
        print('y')
        subprocess.call(['java', '-jar', 'BardStep1.0.jar',
                        '-d', domain,
                        '-p', problem,
                        '-ip', ip,
                        '-o', output])

def initialSetup():
    copyfile(   'tests/' + WORLD_NAME + '-problem.pddl',
                'log/' + WORLD_NAME + '-current.pddl')

def getRecentWorldState():
    getWG(  'log/' + WORLD_NAME + '-current.pddl',
            'tests/' + WORLD_NAME + '-domain.pddl')

def setBardStep():
    runBardStep('log/' + WORLD_NAME + '-current.pddl',
                None,
                'tests/' + WORLD_NAME + '-domain.pddl',
                'log/' + WORLD_NAME + '-current.pddl')

def takeAction(action):
    runBardStep('log/' + WORLD_NAME + '-current.pddl',
                action,
                'tests/' + WORLD_NAME + '-domain.pddl',
                'log/' + WORLD_NAME + '-current.pddl')

initialSetup()
getRecentWorldState()
while True:
    action = input("Take step?")
    if action == '':
        setBardStep()
        getRecentWorldState()
    elif action == 'q':
        break
    else:
        takeAction(action)
        getRecentWorldState()

#fetch world state and convert it to WG

#fetch next options

#fetch executed steps
