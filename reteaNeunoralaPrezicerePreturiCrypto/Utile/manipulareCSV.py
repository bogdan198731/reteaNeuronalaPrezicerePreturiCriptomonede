import pandas as pd

import csv


def openWriteCsv(numeCSV, el):
    print("openWriteCsv")
    # with open(numeCSV, 'w', newline='') as f:
    with open(numeCSV, 'w' ) as f:
        writer = csv.writer(f)
        for row in el:
            print("row = " + str(row))
            writer.writerow(row)
    f.close()

def citireCSV(numeCSV):
    print("citireCSV")
    k = []
    with open(numeCSV, newline='') as f:
        reader = csv.reader(f)
        for read in reader:
            if len(read) > 0:
                k.append(read)
        f.close()
        # df = pd.read_csv(numeCSV)
    return k

def citireCsvPanda(numeCSV):
    df = pd.read_csv(numeCSV)
    return df

def scriereCSV(df, numeCSV):
    print("scriereCSV")
    df.to_csv(numeCSV)

def modificareCSV(numeCSV):
    df = pd.read_csv(numeCSV)
    print(" df = " + str(df))
    df.rename(columns= {0:' date' , 1:'test'})
    print(" df = " + str(df))
    scriereCSV(df,numeCSV)

# modificareCSV("Prediction/ADA-USD.csv")

def scriereCSV(numeFisier, data):
    with open(numeFisier+'.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)