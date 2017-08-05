def calculateAllocation(a, b, c):
    person = b
    amount = [0 for x in range(len(b))]
    for p in person:
        indices = [i for i, x in enumerate(c[1]) if x == p]
        inList = list(map(lambda x:a[x],indices))
        tempAmount = [int(i) for i in list(map(lambda x:c[0][x],indices))]
        number_of_people = [sum(x) for x in inList]
        tempAmount =  [x/y for x, y in zip(tempAmount, number_of_people)]
        for i in range(len(inList)):
            for j in range(len(person)):
                if person.index(p) == j: amount[j] += tempAmount[i] * (number_of_people[i]-inList[i][j])
                elif inList[i][j] == 1: amount[j] -= tempAmount[i]
    return settlements(person, amount)

def settlements(people, amount):
    statement = ""
    while True:
        payer = amount.index(min(amount))
        payee = amount.index(max(amount))
        transfer = min(abs(min(amount)),max(amount))
        if transfer == 0.0:
            break
        statement += people[payer] + " should pay " + people[payee] + " an amount of " + str(transfer) + "\n"
        amount[payer] = amount[payer] + transfer
        amount[payee] = amount[payee] - transfer
    return statement
