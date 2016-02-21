def getfactors(agrv):
    if not isinstance(agrv, int):
        print 'invalid number!'
    if agrv in (0,1):
        print agrv
    else:
        res=[]
        