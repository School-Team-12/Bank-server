def ag(bday, today):
    a = bday.split("/")
    if int(a[1]) > today.month:
        age = today.year-int(a[2])-1
    else:
        age = today.year-int(a[2])
    return(age)


def deposit(nesteddict):
    n = int(input("Enter the account no"))
    dep = int(input("The amount to be deposited is:"))
    for i in nesteddict:
        if i["accno"] == n:
            i["balance"] = i["balance"]+dep
            print(i)


def withdraw(nesteddict):
    n = int(input("Enter the account no"))
    wit = int(input("The amount to be withdrawn is:"))
    for i in nesteddict:
        if i["accno"] == n:
            if i["balance"] == 0:
                print("No bank balance")
            elif i["balance"] < wit:
                print("Bounced")
            else:
                i["balance"] = i["balance"]-wit
                i["withdrawal"] = i["withdrawal"]+wit
            print(i)


def transaction(nesteddict, k):
    c = ["amt transacted", "From acc no", "To accc no"]
    n = int(input("Enter the user's account no"))
    m = int(input("Enter tha acc no where money is to be transferred:"))
    tamt = int(input("Enter the amount to be transferred"))
    d = [tamt, n, m]
    for i in nesteddict:
        if i["accno"] == n:
            if i["balance"] == 0:
                print("No bank balance")
            elif i["balance"] < tamt:
                print("Bounced")
            else:
                i["balance"] = i["balance"]-tamt
                i["transaction"] = i["transaction"]+tamt
                print(tamt, "is the amt transferred from", n, "to", m)
                print(i)
    for i in nesteddict:
        if i["accno"] == m:
            i["balance"] = i["balance"]+tamt
            print(i)
    k = k.append(dict(zip(c, d)))
    return (k)


def alltransaction(nesteddict, k):
    n = int(input("Enter the user's account no"))
    for i in nesteddict:
        if i["accno"] == n:
            print(i)
    for z in k:
        if z["From acc no"] == n:
            print(z)


n = int(input("Enter the number of users"))
keys = ["name", "contact no", "sex", "age", "occupation", "address",
        "accno", "card_no", "balance", "withdrawal", "transaction"]
dwt = [0, 0, 0]
k = []
nesteddict = []
for i in range(n):
    values = []
    nam = input("Enter the name")
    values.append(nam)
    contact = int(input("Enter the contact no"))
    if len(str(contact)) == 10:
        values.append(contact)
    else:
        print("Invalid input")
        continue
    sex = input("Enter your sex(F/M/T)")
    if sex == "F" or sex == "M" or sex == "T":
        values.append(sex)
    else:
        print("Invalid input")
        continue
    bday = input("Enter your date of birth in dd/mm/yyyy format")
    from datetime import date
    today = date.today()
    agee = ag(bday, today)
    values.append(agee)
    occu = input("Enter your occupation")
    values.append(occu)
    addr1 = input("Enter the house number with street name")
    addr2 = input("Enter the municipality and city")
    addr3 = input("Enter the state, postal code and country")
    addr = [addr1, addr2, addr3]
    values.append(addr)
    import random
    acc = random.randint(1000001, 1000000000)
    card = random.randint(1, 1000000)
    values.append(acc)
    values.append(card)
    values.extend(dwt)
    nesteddict.append(dict(zip(keys, values)))
print(nesteddict)
i = 9
while i > 0:
    print("Enter 1 to see  bank balance")
    print("Enter 2 to see amount withdrawn ")
    print("Enter 3 to see amount transacted")
    print("Enter 4 to see all transaction details")
    print("Entrr 5 to exit")
    d = int(input("Give your choice-"))
    if d == 1:
        deposit(nesteddict)
    if d == 2:
        withdraw(nesteddict)
    if d == 3:
        transaction(nesteddict, k)
    if d == 4:
        alltransaction(nesteddict, k)
    if d == 5:
        break
print("Thank you")
