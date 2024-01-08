from matplotlib import pyplot as plt

def creat_chart(x,y,file_name):
    figure = plt.figure()
    plt.scatter(x,y,alpha=0.5)
    # plt.savefig("graph.png",dpi=100)
    plt.show()
    # figure.savefig(f"{file_name}.png",dpi=100)
    

# creat_chart([1,4,7,9,6],[2,3,5,2,3],"fghj")