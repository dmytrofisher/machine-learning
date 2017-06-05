import matplotlib.pyplot as plt
import seaborn as sns

def income_by_features(data, features):    
    fig, axis = plt.subplots(ncols = len(features), figsize = (15, 5))

    for i, feature in enumerate(features):
        if (data[feature].dtype == "object"):
            sns.countplot(y = feature, hue="income", data=data, palette="RdBu", ax = axis[i])            
            axis[i].set_xlabel("Number of Records")            
        else:
            sns.boxplot(x = "income", y = feature, data = data, palette = "RdBu", ax = axis[i])
            axis[i].set_title("'{}' Feature Distribution".format(feature), fontsize = 14)            
        axis[i].set_title("'{}' Feature Distribution".format(feature), fontsize = 14)
        axis[i].set_ylabel("")
     
    fig.tight_layout()
    fig.show()