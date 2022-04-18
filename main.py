from graph import Graph

def checkInput(input, max = 20, min = 1): 
    return (input < min or input > max) 

def resString(list):
    res_str = "  |  "
    for i in range(len(list)):
        if(i < 9):
            res_str += f'{i + 1}  '
        else:
            res_str += f'{i + 1} '
    res_str += '\n'
    for i, obj in enumerate(list):
        if(i < 9):
            res_str += f'{i + 1} | {obj.getResString()}\n'
        else:
            res_str += f'{i + 1}| {obj.getResString()}\n'
    return(res_str)

def main():
    max = int(input('Unesite broj cvorova:\n>>>'))
    while(checkInput(max)):
        max = int(input('->Greska u unosu!\n>>>'))

    list = [] # list of class instances
    #template_arr = [[0 for x in range(max)] for y in range(max)] # creating a MAX x MAX array
    for i in range(max):
        c = int(input(f'Unesite broj grana [{i + 1}] cvora\n>>>')) # c -> cvor
        while(checkInput(c, max, 0)):
            c = int(input(f'->Greska!\nUnesite broj grana [{i + 1}] cvora\n>>>')) 
        list.append(Graph(c, i, [], max))
        for j in range(c):
            if(c == max):
                for k in range(max):
                    list[i].addNode(k)
                break
            n = int(input(f'Unesite {j + 1}. cvor:\n>>>')) # g -> grana
            while(checkInput(n, max) or list[i].elemInConnected(n)):
                n = int(input(f'->Greska!\nUnesite {j + 1}. cvor:\n>>>'))
            list[i].addNode(n)
    res = resString(list)
    print(res)
     
main()