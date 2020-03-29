# read a 5-member ensemble forecast from a .csv file and create a proper tidy dataframe
from EnsPy import enspytools

myfile = enspytools("/Users/georgiosboumis/Desktop/5-memberEnsemble.csv")
mydataframe = myfile.enspyframe()
print(mydataframe)
