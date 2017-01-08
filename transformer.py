def es(str,i,k):
    x = ord(str[i])
    x += k
    if x > 90:
        x = (x % 90) + 64
    elif x < 65:
        x = 91 - (65 - x)
    c = chr(x)
    newstr = str[:i] + c + str[i+1:]
    return newstr
def er(str,i):
    x = str[-i:]
    newstr =str[0:len(str) - i]
    newstr = x + newstr
    return newstr
def ed(word,pos,rep):
    return word[:pos] + rep * word[pos] + word[pos + 1:]
def et(str,g,i,j):
    if len(str)%2 == 0:
        part = len(str)//g
    else:
        part = (len(str) + 1)// g
    strs = []
    for x in range(0, len(str), part):
        strs.append(str[x:x+part])
    strs[i],strs[j] = strs[j],strs[i]
    str = ""
    for x in strs:
        str = str + x
    return str
def dr(str,i):
    x = str[i:]
    newstr = str[0:i]
    newstr = x + newstr
    return newstr
def dd(word,pos,rep):
    return word[:pos+1] + word[pos + rep:]
def dt(str,g,i,j):
    str = rev(str)
    if len(str)%2 == 0:
        part = len(str)//g
    else:
        part = (len(str) + 1)// g
    strs = []
    for x in range(0, len(str), part):
        strs.append(str[x:x+part])
    strs[-i-1],strs[-j-1] = strs[-j-1],strs[-i-1]
    str = ""
    for x in strs:
        str = str + x
    str = rev(str)
    return str

def rev(str):
    return (str[::-1])
def add(l,f):
    for i in l:
        f.write(i)
        f.write('\n')
def filecheck(file,perm):
    try:
        f = open(file,perm)
        return f
    except FileNotFoundError:
        print("File",file,"does not exist...")
        exit()
def main():
    mfile = input("Enter the file name with the messages: ")
    mf = filecheck(mfile, 'r+')
    tfile = input("Enter the file name with the transformations: ")
    tf = filecheck(tfile,'r')
    lines = []
    eord = input("Should the messages be encrypted or decrypted(e/d): ")
    if eord == 'e':
        for wrd, tr in zip(mf, tf):
            tr = tr.split(";")
            for trlist in tr:
                wrd = wrd.strip()
                trs = trlist[1:].split(",")
                if trlist[0] == 'S':
                    if len(trs) == 1:
                        trs.insert(0,1)
                    wrd = es(wrd,int(trs[0]),int(trs[1]))
                elif trlist[0] == 'R':
                    if trs[0] == '':
                        trs[0] = 1
                    wrd = er(wrd,int(trs[0]))
                elif trlist[0] == 'D':
                    if len(trs) == 1:
                        trs.append(2)
                    wrd = ed(wrd,int(trs[0]),int(trs[1]))
                elif trlist[0] == 'T':
                    if '(' not in trs[0]:
                        trs.insert(0,len(wrd))
                    else:
                        x = trs[0].split(")")
                        x[0] = x[0].split("(")[1]
                        trs.insert(0,x[0])
                        trs[1] = x[1]
                    wrd = et(wrd,int(trs[0]),int(trs[1]),int(trs[2]))
                elif trlist[0] == 'E':
                    wrd = rev(wrd)
                else:
                    print("Unknown Symbol '" + trlist[0] + "' Found....Quiting")
                    return
            lines.append(wrd)
    elif eord == 'd':
        for wrd, tr in zip(mf, tf):
            tr = tr.split(";")
            tr.reverse()
            for trlist in tr:
                wrd = wrd.strip()
                trs = trlist[1:].split(",")
                if trlist[0] == 'S':
                    if len(trs) == 1:
                        trs.insert(0, 1)
                    wrd = es(wrd, int(trs[0]), -int(trs[1]))
                elif trlist[0] == 'R':
                    if trs[0] == '':
                        trs[0] = 1
                    wrd = dr(wrd,int(trs[0]))
                elif trlist[0] == 'D':
                    if len(trs) == 1:
                        trs.append(2)
                    wrd = dd(wrd,int(trs[0]),int(trs[1]))
                elif trlist[0] == 'T':
                    if '(' not in trs[0]:
                        trs.insert(0,len(wrd))
                    else:
                        x = trs[0].split(")")
                        x[0] = x[0].split("(")[1]
                        trs.insert(0,x[0])
                        trs[1] = x[1]
                    wrd = dt(wrd, int(trs[0]), int(trs[1]), int(trs[2]))
                elif trlist[0] == 'E':
                    wrd = rev(wrd)
                else:
                    print("Unknown Symbol '" + trlist[0] + "' Found....Quiting")
                    return
            lines.append(wrd)
    else:
        print("Please enter only lowercase e or d...")
        return
    mf.seek(0)
    mf.truncate()
    add(lines,mf)
    mf.close()
    tf.close()

if __name__ == '__main__':
    main()