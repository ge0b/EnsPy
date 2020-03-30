# example of reading an ensemble forecast from a .csv file and creating a proper tidy dataframe and a graph
from EnsPy import enspytools

myfile = enspytools("/Users/georgiosboumis/Desktop/5-memberEnsemble.csv")
mydataframe = myfile.enspyframe()
myfile.enspygraph(mydataframe)
