sup_a = .45
sup_b = .8
sup_ab = .3

sup_tresh = .2
conf_tresh = .6

''''
1. Confidence{A->B}
'''

conf_ab = sup_ab / sup_a
print 'Confidence {A->B} = ' + str(conf_ab*100) + '%'
conf_ba = sup_ab / sup_b
print 'Confidence {B->A} = ' + str(conf_ba*100) + '%'

''''
2. Lift{A->B}
'''
lift_ab = sup_ab / (sup_a * sup_b)
print 'Lift {A->B} = ' + str(lift_ab*100) + '%'

pa = 0
pb = 0
pab = 0