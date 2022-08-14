#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 14 13:25:43 2022

@author: lucas
"""

from tensorflow import keras
from tensorflow.keras import regularizers

#### Builds a neural net with specified number of layers and neurons for binary classification

def build_net(layer_size, l, act_func, out_act, loss_metric, perf_metrics):
    model = keras.Sequential()
    model.add(keras.layers.Dense(units=layer_size[0], activation=act_func, input_shape=(nfeat,), kernel_regularizer=regularizers.l2(l)))
    for i in range(1,len(layer_size)):
        model.add(keras.layers.Dense(units=layer_size[i], activation=act_func, kernel_regularizer=regularizers.l2(l)))
    model.add(keras.layers.Dense(units=1, activation=out_act))
    opt = keras.optimizers.Adam()
    model.compile(optimizer=opt,loss=loss_metric, metrics=perf_metrics)

    return(model)

layer_size = [10,20,10]  ### number of neurons in each layer, 
l = 0.01 ### l2 regularizer lambda value
act_func = "relu"
out_act = "sigmoid" ### output activation
nfeat=1316 ## number of features
loss_metric = "binary_crossentropy"  ### loss metric
perf_metrics = "accuracy" ## performance metric

m1 = build_net(layer_size, l, act_func, out_act, loss_metric, perf_metrics)

