import subprocess

def runBardStep(domain='tests/door-domain-sc.pddl',
                problem='tests/door-problem-notense.pddl',
                ip = None):
    if ip == None:
        subprocess.call(['java', '-jar', 'BardStep1.0.jar',
                        '-d', domain,
                        '-p', problem])
    else:
        subprocess.call(['java', '-jar', 'BardStep1.0.jar',
                        '-d', domain,
                        '-p', problem,
                        '-ip', ip])

#set this to run without printing somehow.
runBardStep()

#fetch world state and convert it to WG

#fetch next options

#fetch executed steps
