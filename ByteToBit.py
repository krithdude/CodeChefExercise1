# cook your dish here
T = int(input("Enter Test Case:"))
N_List = []

for _ in range(T):
    E = int(input("Enter Time:"))
    N_List.append(E)

for N in N_List:
    i=0
    n = 1
    PopulationList = [0, 0, 0]
    while i<N:
            if (i==0):
                PopulationList[0] = PopulationList[0] + n
            i = i + 2
            if (i<N):
                PopulationList[0] = 0
                PopulationList[1] = PopulationList[1] + n
            i = i + 8
            if(i<N):
                PopulationList[1] = 0
                PopulationList[2] = PopulationList[2] + n          
                i = i+16
            if (i<N):
                PopulationList[2] = 0
                n = n*2
                PopulationList[0] = PopulationList[0] + n
    print(*PopulationList, sep = " ")