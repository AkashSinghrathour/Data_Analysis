
def read_data(number):
    column_data = []
    with open('D:\DJANGO\matplotlib\project\Details.csv',"r") as dta:     
        for line in dta.readlines()[0:6]:
            d = line.strip().split(",")
            column_data.append(d[number])
    return column_data

 