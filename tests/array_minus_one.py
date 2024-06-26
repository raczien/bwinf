
def weight_balance(arr):
    counter = 0
    for i in range(len(arr)):
        temp = arr.copy()
        temp[i] *= -1
        for k in range(len(arr)):
            temp[k] *= -1
            print(temp)
            counter += 1
            print()
    print(counter)



def test(arr):
    c = 0
    for i, k in weight_balance(len(arr)):

        temp = arr.copy()
        temp[i] *= -1
        temp[k] *= -1
        print(temp)
        c += 1
    print(c)



if __name__ == '__main__':
    x = [10, 10, 50, 80, 80, 100, 130, 160, 170, 250, 300]
    weight_balance(x)
    #test(x)

'''
            Gesucht: 30
            habe: [10, 10, 50, 80, 80, 100, 130, 160, 170, 250]
            Ich will:                                                   -1 ANZAHL: 1
            [-10, 10, 50, 80, 80, 100, 130, 160, 170, 250]              arr[0] -1
            [10, -10, 50, 80, 80, 100, 130, 160, 170, 250]              arr[1]
            [10, 10, -50, 80, 80, 100, 130, 160, 170, 250]              arr[2]
            .
            .
            --> also immer einen weiter und EIN element *(-1)           
            
            Dann:                                                       -1 ANZAHL: 2
            [-10, -10, 50, 80, 80, 100, 130, 160, 170, 250]             arr[0] FIX && arr[0+i]
            [-10, 10, -50, 80, 80, 100, 130, 160, 170, 250]             
            [-10, 10, 50, -80, 80, 100, 130, 160, 170, 250]             
            [-10, 10, 50, 80, -80, 100, 130, 160, 170, 250]             
            [-10, 10, 50, 80, 80, -100, 130, 160, 170, 250]             
            ....
            dann einen index weiter start
            [10, -10, -50, 80, 80, 100, 130, 160, 170, 250]
            [10, -10, 50, -80, 80, 100, 130, 160, 170, 250]
            [10, -10, 50, 80, -80, 100, 130, 160, 170, 250]
            
            '''
