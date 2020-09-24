

syntaxlist = [['pass','block'],['in','out'],['log'],['quick'],['egress','vmx0'],['inet','inet6'],['tcp','udp','icmp','icmp6','http','https'],['from'],['to'],['port'],['flags S/SA'],['no state','keep state','modulate state','synproxy state']]


with open('pfrule.txt','r') as f:
    for line in f:
        rule = line.split()
        rulelen = len(rule)
        for s in range(len(rule)):
            for rulecount in range(len(syntaxlist)):
                if rulecount == 7:
                    
                    print("source ip is", rule[s])
                    rulecount += 1
                    break
                for listitem in range(len(syntaxlist[rulecount])):
                    if rule[s] == syntaxlist[rulecount][listitem]:
                        print(rule[s])
        print("\n")

