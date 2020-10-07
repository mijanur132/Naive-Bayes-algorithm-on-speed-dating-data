import pandas as pd

def training_test_split():
    df = pd.read_csv("dating-binned.csv")
    testSet = df.sample(random_state=47,frac=0.2)
    trainSet=df.copy().drop(testSet.index)
    trainSet.reset_index(drop = True, inplace = True)
    testSet.reset_index(drop = True, inplace = True)
    trainSet.to_csv("trainingSet.csv", index = False)
    testSet.to_csv("testSet.csv", index = False)

if __name__ == "__main__":
   training_test_split()

