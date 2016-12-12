## python code for rule learning..



import csv

from random import randint

def read_data(filename):
    ruledict = {}

    with open(filename) as csvfile:
        for id, row in enumerate(csvfile):
            ruledict[id] = [x.replace("\n","") for x in row.split(",")]
    return ruledict

def train_rules(rules, iteration):
    if rules == None:
        ruledict = read_data('data/contra.csv')
        max_accuracy = 0
        cbr = {}
        print(len(ruledict), "Rows has this dataframe..")
        for key,value in ruledict.items():
            ruleAccp = 0
            ruleAccn = 0
            trigger = False
            for k,v in ruledict.items():
        
                for id, _ in enumerate(v):
                    try:
                        if value[id] == v[id] or v[id] == "" and value[::-1] == v[::-1]:
                            trigger = True
                        else:
                            trigger = False
                    except:
                        pass
                if trigger == True:
                    ruleAccp += 1
                else:
                    ruleAccn += 1

            current_accuracy = round(ruleAccp/(ruleAccn+ruleAccp),2)
            if  current_accuracy < 1 and current_accuracy > 0.2:
                max_accuracy = current_accuracy
                cbr[key] = value

        print ("{} : Max accuracy: {} for rule count {}".format(iteration,max_accuracy, len(cbr)))
        return cbr
    else:
        cbr = {}
        max_accuracy = 0
        ## v tem primeru pa ze imamo rules, pa preverimo, kako dobri so!
        data= read_data('data/contra.csv')
        for k,v in rules.items():
            trigger = False
            ruleAccn = 0
            ruleAccp = 0
            for a,b in data.items():
                for id, _ in enumerate(v):
                    try:
                        if b[id] == v[id] or v[id] == "" and v[::-1] == b[::-1]:
                            trigger = True
                        else:
                            trigger = False
                    except:
                        pass
                if trigger == True:
                    ruleAccp += 1
                else:
                    ruleAccn += 1
            

            current_accuracy = round(ruleAccp/(ruleAccn+ruleAccp),2)
            if  current_accuracy < 1 and current_accuracy > 0.2:
                max_accuracy = current_accuracy
                cbr[k] = v

        print ("{} : Max accuracy: {} for rule count {}".format(iteration,max_accuracy, len(cbr)))
        return cbr
    
    
def generalize_rules(ruleset, cycles):
    outputrules = {}
    for key, val in ruleset.items():
        if val.count('') < int(len(val))/3:
            for j in range(cycles):
                val[randint(0,(len(val)-1))] = ''
            outputrules[key] = val
    return outputrules


def train_model():
    current_rules = train_rules(None, 1) # to initialize
    current_rs = {}
    minrules = 600
    for k in range(1000):
        current_rules = train_rules(generalize_rules(current_rules,1),k)
        if len(current_rules) < minrules^2:
            current_rs = current_rules
            minrules = len(current_rs)
            print ("Current optimum: ",minrules)
            if minrules < 30:
                break
    print (current_rs)
    return minrules

train_model()
