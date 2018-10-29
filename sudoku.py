from satispy import Variable, Cnf
from satispy.solver import Minisat

solver = Minisat()

file = open('testes.txt')

x = [[[0 for k in range(4)] for j in range(4)] for i in range(4)] 

for i in range(4):
    for j in range(4):
        for k in range(4):
            x[i][j][k] = Variable('x_'+str(i)+str(j)+'_'+str(k))

sudoku = file.readline()

n = 1

while sudoku != '':

########################################################################################
########################################################################################
## Escreva aqui o código gerador da formula CNF que representa o Sudoku codificado na ##
## variavel 'sudoku'. Nao se esqueca que o codigo deve estar no escopo do 'while'     ##
## acima e deve guardar a formula CNF na variavel 'cnf'.                              ##
########################################################################################
########################################################################################

    cnf = Cnf()

    quad1=[[0,0],[0,1],[1,0],[1,1]]
    quad2=[[0,2],[0,3],[1,2],[1,3]]
    quad3=[[2,0],[2,1],[3,0],[3,1]]
    quad4=[[2,2],[2,3],[3,2],[3,3]]
    
    sudoku = sudoku.split(';')
    l=len(sudoku) 
    for i in range(l):
        if sudoku[i] != []:
            sudoku[i]=sudoku[i].split(' ')
    
    

    for i in range(l-1):
        for j in range(4):
            if j == sudoku[i][2]:
                cnf &= (x[sudoku[i][0]][sudoku[i][1]][sudoku[i][2]])
    #only one number for each square
    for i in range(4):
        for j in range(4):
            cnf &= (x[i][j][0] | x[i][j][1] | x[i][j][2] | x[i][j][3]) & (-x[i][j][2] | -x[i][j][3]) & (-x[i][j][0] | -x[i][j][1])  & (-x[i][j][1] | -x[i][j][3]) & (-x[i][j][1] | -x[i][j][2]) & (-x[i][j][0] | -x[i][j][3]) & (-x[i][j][0] | -x[i][j][2])
        
    #only one number for each line
    for i in range(4):
        for k in range(4):
            cnf &= (x[i][0][k] | x[i][1][k] | x[i][2][k] | x[i][3][k]) & (-x[i][2][k] | -x[i][3][k]) & (-x[i][0][k] | -x[i][1][k])  & (-x[i][1][k] | -x[i][3][k]) & (-x[i][1][k] | -x[i][2][k]) & (-x[i][0][k] | -x[i][3][k]) & (-x[i][0][k] | -x[i][2][k])
        
    #only one number for each column
    for j in range(4):
        for k in range(4):
            cnf &= (x[0][j][k] | x[1][j][k] | x[2][j][k] | x[3][j][k]) & (-x[2][j][k] | -x[3][j][k]) & (-x[0][j][k] | -x[1][j][k])  & (-x[1][j][k] | -x[3][j][k]) & (-x[1][j][k] | -x[2][j][k]) & (-x[0][j][k] | -x[3][j][k]) & (-x[0][j][k] | -x[2][j][k])

    #only one number for each quadrant
    for i in range(4):
        for j in range(4):
            if ([i,j] in quad1) or ([i,j] in quad2) or ([i,j] in quad3) or ([i,j] in quad4):
                for k in range(4):
                    cnf &= (x[i][j][0] | x[i][j][1] | x[i][j][2] | x[i][j][3]) & (-x[i][j][2] | -x[i][j][3]) & (-x[i][j][0] | -x[i][j][1])  & (-x[i][j][1] | -x[i][j][3]) & (-x[i][j][1] | -x[i][j][2]) & (-x[i][j][0] | -x[i][j][3]) & (-x[i][j][0] | -x[i][j][2])
 
########################################################################################
########################################################################################
## Fim do código gerador da formula CNF.                                              ##
########################################################################################
########################################################################################

    sol = [[0 for j in range(4)] for i in range(4)]

    solution = solver.solve(cnf)

    if solution.success:
        print("Solution %d:\n" % n)
            for i in range(4):
                for j in range(4):
                    for k in range(4):
                        if solution[x[i][j][k]]:
                            sol[i][j] = k

        print("%d %d | %d %d" % (sol[0][0], sol[0][1], sol[0][2], sol[0][3]))
        print("%d %d | %d %d" % (sol[1][0], sol[1][1], sol[1][2], sol[1][3]))
        print("---------")
        print("%d %d | %d %d" % (sol[2][0], sol[2][1], sol[2][2], sol[2][3]))
        print("%d %d | %d %d\n" % (sol[3][0], sol[3][1], sol[3][2], sol[3][3]))

    else:
        print("There is no solution.\n")

    n+=1

    sudoku = file.readline()

file.close()
