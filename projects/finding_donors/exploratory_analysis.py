import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix

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


def confusion_matrices(X, y, classifiers):
    fig, axis = plt.subplots(ncols = len(classifiers), figsize = (15, 5))
    
    for i, model in enumerate(classifiers):
        cm = confusion_matrix(y.values, model.predict(X))        
        sns.heatmap(cm, annot=True, cmap='Blues', xticklabels=['no', 'yes'], yticklabels=['no', 'yes'], fmt="d", ax = axis[i])
        axis[i].set_ylabel('True label')
        axis[i].set_xlabel('Predicted label')
        axis[i].set_title('Confusion matrix for: {}'.format(model.__class__.__name__));
     
    fig.tight_layout()
    fig.show()