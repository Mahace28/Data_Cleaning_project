import matplotlib.pyplot as plt
import seaborn as sns

def create_charts(df):

    # Math score distribution
    sns.histplot(df["math score"], bins=20)
    plt.title("Math Score Distribution")
    plt.show()

    # Reading score distribution
    sns.histplot(df["reading score"], bins=20)
    plt.title("Reading Score Distribution")
    plt.show()

    # Gender count
    sns.countplot(x="gender", data=df)
    plt.title("Gender Distribution")
    plt.show()