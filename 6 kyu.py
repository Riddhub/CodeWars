# def high(x):
#     #################### VERSION 3 #######################
#
#     return max(x.split(), key=lambda k: sum(ord(c) - 96 for c in k))


    #################### VERSION 2 #######################
    # x = x.split()
    # l = []
    # for i in list(map(lambda n: list(n), x)):
    #     l.append(sum(list(map(lambda n: ord(n)-96, i))))
    #
    # return x[l.index(max(l))]


    #################### VERSION 1 #######################
    # Code here
    # import string
    # s = (string.ascii_lowercase)
    # a = []
    # a1 = []
    # k = []
    #
    # for i in x.split():
    #     a1.append(str(''.join(i)))
    #     a.append(str(''.join(set(i))))
    # print(a)
    #
    # for i in a1:
    #     r = 0
    #     for j in i:
    #         r += s.index(j)+1
    #     k.append(r)
    # print(k)
    # return a1[(k.index(max(k)))]

# print(high('what time are we climbing up the volcano'))




