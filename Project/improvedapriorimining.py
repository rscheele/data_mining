# Based on script by github user nalinaksh 
# Adapted by Lisa Tostrams (august 2017)
# Adapted by Rodi Scheele (janauri 2018)
from __future__ import print_function

import itertools

"""generate_association_rules function to mine and print all the association rules with given min support and confidence value"""
def generate_association_rules(filename, support, confidence, maxr):
    """1) Compute frequent 1-itemset"""
    # L1 = All frequent 1 itemsets > Support
    # D = All transactions
    L1, D, support, confidence, maxr = frequent_1_itemsets(filename, support, confidence, maxr)

    return 0

''' 1) Frequent 1 itemsets '''
def frequent_1_itemsets(filename, support, confidence, maxr):
    print("test")
    C1 = {}
    """total number of transactions contained in the file"""
    transactions = 0.0
    D = []
    T = []
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

    """Compute frequent 1-itemset"""
    L1 = []
    for key in C1.keys():
        print(key +":"+ str(C1[key]) )
        if (100 * len(C1[key]) / transactions) >= support:
            L1.append(([key], ('sup=', round(100.0 * len(C1[key]) / transactions, 2))))

    print("---------------TOP 10 FREQUENT 1-ITEMSET-------------------------")
    print(*['set= {{ {} }},  {} {}'.format(item[0][0], item[1][0], item[1][1]) for item in
            sorted(L1, key=lambda item: item[1][1], reverse=True)][:10], sep='\n')
    print("-----------------------------------------------------------------")

    return (L1, D, support, confidence, maxr)


