# Complete the function below.


def getUmbrellas(n, p):
    numberofpeoplereturn = 999999
    returnumbreallanumber = -1
    flag = 0
    rangenumber = len(p)
    newp = sorted(p, reverse=True)
    print(newp)
    for i in range(rangenumber):
        if newp is None:
            return -1
        if n/newp[i] > 0:

            numberofpeople = int(n/newp[i])*newp[i]
            newpeople = n - numberofpeople
            print(newpeople)
            if newpeople < 0:
                return -1
            else:
                if newpeople == 0:
                    print(int(n/newp[i]))
                    return(int(n/newp[i]))
                    break
                else:
                    print(n/newp[i])
                    if n/newp[i] < 1:
                        return -1
                    else:
                        newp.pop(0)
                        if newp is None:
                            return -1
                        else:
                            getUmbrellas(newpeople, newp)
        else:
            if n/newp[i] == 0:
                return 1

    return returnumbreallanumber
