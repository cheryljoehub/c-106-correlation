import csv
import numpy as np

def getDataSource(data_path):
    marks = []
    days = []
    with open (data_path) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            marks.append(float(row["Marks In Percentage"]))
            days.append(float(row["Days Present"]))
    return{"x":marks,"y":days}
def findCorr(datasource):
    Corr = np.corrcoef(datasource["x"],datasource["y"])
    print("CorrValue",Corr[0,1])
def setup():
    data_path = "Student Marks vs Days Present.csv"
    datasource = getDataSource(data_path)
    findCorr(datasource)
setup()
            