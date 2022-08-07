import matplotlib.pyplot as plt
import pickle
import os

import numpy as np

RUN_NUM=3
outdir='output'
if not os.path.exists(outdir):
    os.makedirs(outdir)

learning_rates=['0.5','1e-2','1e-5']

for learning_rate in learning_rates:
    for i in range(RUN_NUM):
        os.system('python main.py --optimizer sgd --learning_rate '+learning_rate+' --output='+outdir+'/sgd'+learning_rate+"_run"+str(i)+'.pkl')
        os.system('python main.py --optimizer momentumsgd --learning_rate '+learning_rate+' --output='+outdir+'/momentumsgd'+learning_rate+"_run"+str(i)+'.pkl')
        os.system('python main.py --optimizer rmsprop --learning_rate '+learning_rate+' --output='+outdir+'/rmsprop'+learning_rate+"_run"+str(i)+'.pkl')
        os.system('python main.py --optimizer amsgrad --learning_rate '+learning_rate+' --output='+outdir+'/amsgrad'+learning_rate+"_run"+str(i)+'.pkl')

optimizers = ['sgd', 'momentumsgd', 'rmsprop', 'amsgrad']

# Plots the training losses.
for learning_rate in learning_rates:
    for optimizer in optimizers:
        for i in range(RUN_NUM):
            data = pickle.load(open(outdir+'/'+optimizer+learning_rate+"_run"+str(i)+".pkl", "rb"))
            if i == 0:
                loss_sum = np.array(data['train_loss'])
            else:
                loss_sum += np.array(data['train_loss'])
        plt.plot(loss_sum / RUN_NUM, label=optimizer)
    plt.ylabel('Trainig loss')
    plt.xlabel('Epochs')
    plt.legend()
    plt.savefig('loss'+learning_rate+'.pdf')
    plt.show()

# Plots the training accuracies.
for learning_rate in learning_rates:
    for optimizer in optimizers:
        for i in range(RUN_NUM):
            data = pickle.load(open(outdir + '/' + optimizer + learning_rate + "_run" + str(i) + ".pkl", "rb"))
            if i == 0:
                accuracy_sum = np.array(data['train_accuracy'])
            else:
                accuracy_sum += np.array(data['train_accuracy'])
        plt.plot(accuracy_sum / RUN_NUM, label=optimizer)
    plt.ylabel('Trainig accuracy')
    plt.xlabel('Epochs')
    plt.legend()
    plt.savefig('accuracy'+learning_rate+'.pdf')
    plt.show()
