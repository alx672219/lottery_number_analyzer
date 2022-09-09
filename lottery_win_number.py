import matplotlib.pyplot as plt


data = []
each_line = []
each_number = [[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   # first number
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   # second number
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   # third number
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   # fourth number
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   # fifth number
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],   # sixth number
               [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]   # bonus number
counter = 0


with open("lottery_winning_numbers.csv", "r") as file:
    data = file.readlines()
    for each_line in data:
        
        if each_line[-1] == "/n":
            each_line = each_line[:-2]
       
        revised_data = each_line.split(",")

        counter = 0
        for n in revised_data:
            each_number[counter][int(n) - 1] = each_number[counter][int(n) - 1] + 1
            counter += 1
            if counter == 7:
                break


for m in range(45):
    print("%3d" % (m + 1), end = " ")

print()


for m in range(7):
    plt.plot(each_number[m])
    for k in range(0, 45):
        print("%3d" % (each_number[m][k]), end = " ")   # print each_number
    
    print()


plt.legend(range(1,8))
plt.show()