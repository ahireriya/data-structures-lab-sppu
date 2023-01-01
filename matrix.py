def main():
    r1=int(input("enter row for 1st matrix"))
    c1=int(input("enter col for 1st matrix"))
    r2=int(input("enter row for 2st matrix "))
    c2=int(input("enter col for 2st matrix"))
    
    mat1=[]
    mat2=[]
    add = []
    sub = []
    multi = []
    tran1 = []
    tran2 = []

    read(r1,c1,mat1)
    display(r1,c1,mat1,"Matrix 1")

    read(r2,c2,mat2)
    display(r2,c2,mat2,"Matrix 2")

    addition(mat1,mat2,r1,c1,r2,c2,add)
    subtract(mat1,mat2,r1,c1,r2,c2,sub)
    multiply(mat1,mat2,r1,c1,r2,c2,multi)
    
    
    transpose(mat1,r1,c1,tran1)
    transpose(mat2,r2,c2,tran2)

    display(c1,r1,tran1,"Transpose of Matrix 1")
    display(c2,r2,tran2,"Transpose of Matrix 2")
    
    
def read(r,c,mat)   :
    for i in range(r):
        a=[]
        for j in range (c):
            num=int(input("enter a number"))
            a.append(num)
        mat.append(a)


def display(r,c,mat,str):
    print(str)
    for i in range(r):
        for j in range (c):
            print(mat[i][j],end=" ")
        print()   

def put_zeros(r,c,mat):
    a = []
    for i in range(r):
        a=[]
        for j in range(c):
            a.append(0)
        mat.append(a)


def addition(mat1,mat2,r1,c1,r2,c2,res):
    if((r1 == r2) and (c1 == c2)):
        put_zeros(r1,c1,res)
        for i in range(r1):
            for j in range (c1):
                res[i][j]=mat1[i][j]+mat2[i][j]
        display(r1,c1,res,"Addition")
    else:
        print("Matrix Addition not possible")


def subtract(mat1,mat2,r1,c1,r2,c2,res):
    if((r1 == r2) and (c1 == c2)):
        put_zeros(r1,c1,res)
        for i in range(r1):
            for j in range (c1):
                res[i][j]=mat1[i][j]-mat2[i][j]  
        display(r1,c1,res,"Subtraction")
    else:
        print("Matrix Subtraction not possible")


def multiply(mat1,mat2,r1,c1,r2,c2,res):
    if (r2==c1):
        put_zeros(r1,c2,res)
        for i in range(r1):
            for j in range(c2):
                for k in range(r2):
                    res[i][j] += mat1[i][k] * mat2[k][j]
        display(r1,c2,res,"Multiplication")
    else:
        print("Matrix Multiplication not possible")


def transpose(mat,r,c,res):
    put_zeros(c,r,res)
    for i in range(0,c):
            for j in range(0,r):
                res[i][j]=mat[j][i]

    

main()    
