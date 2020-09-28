syntaxlist = [['pass','block'],['in','out'],['log'],['quick'],['egress','vmx0'],['inet','inet6'],['tcp','udp','icmp','icmp6','http','https'],['from'],['to'],['port'],['flags S/SA'],['no state','keep state','modulate state','synproxy state']]


with open('pfrule.txt','r') as f:
    for line in f:
        rules = line.split()
        rulelen = len(rules)
        macrohost = ""
        isList = False
        filteredRules = []
        for rule in rules:
            if rule == "{":
                isList = True
            elif str(rule) == "}":
                isList = False
                if rule[0] == "$":
                    macrohost += rule
            else:
                macrohost += rule
            if not isList:
                filteredRules.append(macrohost)
            for rulecount in range(len(syntaxlist)):
                if rulecount == 7:
                    print("source ip is", rule[rule])
                    rulecount += 1
                for listitem in range(len(syntaxlist[rulecount])):
                    if rules[rule] == syntaxlist[rulecount][listitem]:
                        print(rules[rule])
    print("\n")
