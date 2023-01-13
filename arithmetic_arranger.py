def ans(u,l,arp,lenght,ans_visible):

    for idx, i in enumerate(u):
        print(' '* (lenght[idx]-len(i)),i,sep='',end='')
        if idx <= len(lenght)-2:
            print('    ',end='') 
        else: print('')

    for idx, e in enumerate(l):
        #print(e,sep=' ',end='')
        print(arp[idx],' '*(lenght[idx]-len(e)-1),e,sep='',end='')
        if idx <= len(lenght)-2:
            print('    ',end='') 
        else: print('')

    for idx, i in enumerate(lenght):
        print('-'* lenght[idx],end='')
        if idx <= len(lenght)-2:
            print('    ',end='') 
        else: print('')
    
    def oper(u,d,opr):
        if opr=='+':
            return u+d
        elif opr=='-':
            return u-d
        else:
            raise NameError('Error: Operator must be \'+\' or \'-\' ')

    if ans_visible:
        for idx, i in enumerate(lenght):
            ans=oper(int(u[idx]),int(l[idx]),arp[idx])    
            print(' '* (lenght[idx]-len(str(ans))),ans,sep='',end='')
            if idx <= len(lenght)-2:
                print('    ',end='') 
            else: print('')

def arithmetic_arranger(opr,ans_visible=False):
    if len(opr)>5:
        raise  NameError("Too many problems.")
    
    u=[]
    arp=[]
    l=[]
    length=[]
    for o in opr:
        parts=o.split()
        u.append(parts[0])
        arp.append(parts[1])
        l.append(parts[2])
        length.append((max(len(parts[0]),len(parts[2]))+2))
    
    for idx in range(len(u)):
        if len(u[idx])>4 or len(l[idx])>4:
            raise NameError('Error: Numbers cannot be more than four digits.')
        if arp[idx]!='+' and arp[idx]!='-':
            raise NameError('Error: Operator must be \'+\' or \'-\' ')
        try:
            int(u[idx])
            int(l[idx])
        except:
            raise NameError('Error: Numbers must only contain digits.')

