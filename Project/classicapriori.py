# Based on script by github user nalinaksh 
# Adapted by Lisa Tostrams (august 2017)
# Adapted by Rodi Scheele (janauri 2018)
from __future__ import print_function

import itertools

def classic_apriori(filename, support, confidence, maxr):
    # L1 = All frequent 1 itemsets > Support
    # D = All transactions
    L1, D, transactions = frequent_1_itemsets(filename, support)
    L = freq_itemsets(L1, support, D)
    return 0

def frequent_1_itemsets(filename, support):
    print("test")
    C1 = {} #item, it's transactions
    """total number of transactions contained in the file"""
    transactions = 0 #total number of transactions to calculate support
    D = [] # List of all transactions
    T = [] # list of transactions with item occurence
    with open(filename, "r") as f:
        for line in f:
            T = []
            for word in line.split(','):
                word = word.rstrip()
                T.append(word)
                if word not in C1.keys():
                    C1[word] = [transactions]
                else:
                    C1[word].append(transactions)

            transactions += 1
            D.append(T)

    L1=[] #C1 with low support items removed
    for key in C1.keys():
        if round(100.0 * len(C1[key]) / transactions, 2) >= support:
            sup = round(100.0 * len(C1[key]) / transactions, 2)
            transaction = (key, C1[key], sup)
            L1.append(transaction)

    L1.sort(key=lambda s:s[2],reverse=True)

    print("---------------TOP 10 FREQUENT 1-ITEMSET-------------------------")
    for i in range(0,10):
        print('Item ID=' + str(L1[i][0]) + ' Supp=' + str(L1[i][2]))
    print("-----------------------------------------------------------------")

    return (L1, D, transactions)

def freq_itemsets(L1, support, D):
    k = 2
    Lk_1 = []
    Lk = []
    L = []
    L.append(L1)
    count = 0
    transactions = 0
    support = 10
    for item in L1:
        Lk_1.append([item[0]])
    while Lk_1 != []:
        Ck = []
        Lk = []
        Ck = apriori_gen(Lk_1, k - 1)
        for c in Ck:
            count = 0
            transactions = 0
            s = set(c)
            for T in D:
                transactions += 1
                t = set(T)
                if s.issubset(t) == True:
                    count += 1
            if count >= support:
                c.sort()
                Lk.append((c, ('sup=', count, 2)))
        Lk_1 = []
        if (len(Lk) > 0):
            print("-------TOP 10 (or less) FREQUENT %d-ITEMSET------------------------" % k)
            print(*['set= {{ {} }},  {} {}'.format(', '.join(item[0]), item[1][0], item[1][1]) for item in
                    sorted(Lk, key=lambda item: item[1][1], reverse=True)][:10], sep='\n')
            print("------------------------------------------------------------------")
        for l in Lk:
            Lk_1.append(l[0])
        k += 1
        if Lk != []:
            L.append(Lk)

    return L

def apriori_gen(Lk_1, k):
    length = k
    Ck = []
    for list1 in Lk_1:
        for list2 in Lk_1:
            count = 0
            c = []
            if list1 != list2:
                while count < length-1:
                    if list1[count] != list2[count]:
                        break
                    else:
                        count += 1
                else:
                    if list1[length-1] < list2[length-1]:
                        for item in list1:
                            c.append(item)
                        c.append(list2[length-1])
                        if not has_infrequent_subset(c, Lk_1, k):
                            Ck.append(c)
                            c = []
    return Ck

def has_infrequent_subset(c, Lk_1, k):
    list = []
    list = set(itertools.combinations(c,k))
    for item in list:
        s = []
        for l in item:
            s.append(l)
        s.sort()
        if s not in Lk_1:
            return True
    return False

def generate_association_rules(D, L, confidence, maxr):
    s = []
    r = []
    length = 0
    count = 1
    inc1 = 0
    inc2 = 0
    num = 1
    m = []
    print("---------------------ASSOCIATION RULES------------------")
    print("--------------------------------------------------------")
    RULES = []
    for list in L:  # for each group of K size frequent itemsets e.g. all size 3 frequent itemssets
        for l in list:  # for each frequent itemset e.g. {a,b,c}
            l = l[0]
            length = len(l)
            count = 0
            while count < length:  # compute at all length <count> subsets of that itemset e.g. for count =2 {a,b} {a,c} {b,c}
                s = []
                r = set(itertools.combinations(l, count))
                count += 1
                for item in r:  # for each length <count> subset of the frequent itemset e.g. {a,b}
                    inc1 = 0
                    inc2 = 0
                    s = []
                    m = []
                    for i in item:
                        s.append(i)
                    for T in D:
                        if set(s).issubset(
                                set(T)) == True:  # count how often that subset occurs e.g. {a,b} occurs 9 times
                            inc1 += 1
                        if set(l).issubset(set(
                                T)) == True:  # count how often the frequent itemset occurs e.g. {a,b,c} occurs 5 times
                            inc2 += 1
                    if 100.0 * inc2 / inc1 >= confidence:  # compute confidence of {a,b} => {c} == #{a,b,c}/#{a,b} %
                        for index in l:
                            if index not in s:
                                m.append(index)
                        RULES.append((num, s, m, 100.0 * inc2 / len(D), 100.0 * inc2 / inc1))  # add rule

                        num += 1
    if (maxr < 1):
        maxr = len(RULES)
    print(*["Rule #{}: {{ {} }} ==> {{ {} }}, sup= {:.2f}, conf= {:.2f}".format(r[0], ', '.join(r[1]), ', '.join(r[2]),
                                                                                r[3], r[4]) for r in
            sorted(RULES, key=lambda r: r[4], reverse=True)][:maxr], sep='\n\n')
    print("--------------------------------------------------------")
