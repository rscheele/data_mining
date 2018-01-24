from __future__ import print_function

import itertools

def improved_apriori(filename, support, confidence, maxr):
    # L1 = All frequent 1 itemsets > Support
    # D = All transactions
    L1, D, transactions = frequent_1_itemsets(filename, support)
    L = freq_itemsets(L1, support)
    return 0

def frequent_1_itemsets(filename, support):
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

def freq_itemsets(L1, support):
    k = 2
    support = 10
    Lk = []
    L = []

    while True:
        Ck = list(itertools.combinations(L1, k))
        L1 = []
        for i in range(0, len(Ck)):
            transactionlist = []
            idList = []
            s = 0
            for j in range(0, len(Ck[i])):
                idList.append(Ck[i][j][0])
                transactionlist.append(Ck[i][j][1])
            s = len(set(transactionlist[0]).intersection(*transactionlist[1:]))
            if (s >= support):
                Lk.append((idList,s))
                for m in range(0, len(Ck[i])):
                    if Ck[i][m] not in L1:
                        L1.append(Ck[i][m])
        L.append(Lk)
        Lk = []
        if L1 == []:
            break
        k += 1

    p = 2
    for i in range(0,len(L)-1):
        L[i].sort(key=lambda s:s[1],reverse=True)
        if len(L[i]) > 10:
            k = 10
        else:
            k = len(L[i])
        print("---------------TOP 10 FREQUENT %d-ITEMSET-------------------------" % p)
        for j in range(0,k):
            print('Item ID=' + str(L[i][j][0]) + ' Supp=' + str(L[i][j][1]))
        print("-----------------------------------------------------------------")
        p+=1
    return Lk_all
