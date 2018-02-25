# Complete the function below.


def getUmbrellas(n, p):
    numberofpeoplereturn = 999999
    returnumbreallanumber = -1
    flag = 0
    rangenumber = len(p)
    for i in range(rangenumber):
        if n % p[i] == 0:
            numberofpeople = int(n/p[i])

            flag = 1
            # print('Value of p'+str(i) + ' is ' + str(p[i]) + ' and Mod is ' + str(n%p[i]) +' numberofpeople='+str(numberofpeople))
        if flag == 1:
            print('Returnvalue ' + str(numberofpeoplereturn) + ' Normal value '+str(numberofpeople))
            if numberofpeoplereturn > numberofpeople:
                numberofpeoplereturn = numberofpeople
                returnumbreallanumber = int(n/p[i])
    return returnumbreallanumber
