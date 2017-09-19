import matplotlib.pyplot as plt

def plot_history(history):
    fig, (axis1, axis2) = plt.subplots(ncols = 2, figsize = (10, 4))

    # Model accuracy
    axis1.plot(history.history["acc"])
    axis1.plot(history.history["val_acc"])
    axis1.set_title("Model accuracy")
    axis1.set_xlabel("Epoch")
    axis1.set_ylabel("Acuracy")
    axis1.legend(['train', 'test'], loc='lower right')
    
    # Model loss
    axis2.plot(history.history["loss"])
    axis2.plot(history.history["val_loss"])
    axis2.set_title("Model loss")
    axis2.set_xlabel("Epoch")
    axis2.set_ylabel("Loss")
    axis2.legend(['train', 'test'], loc='upper right')
    
    fig.tight_layout()
