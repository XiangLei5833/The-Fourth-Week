#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def datafigure(file):

    minutes = 0

    try:
        new_file = pd.read_json(file)
        new_dataframe = new_file.loc[:, ['user_id', 'minutes']]    # 这个可要可不要，我只是为了加深一下印象
    except ValueError:
        return 0
    
    minutes = new_dataframe[['user_id','minutes']].groupby('user_id').sum()

    fig = plt.figure()    # 可不要，依据下面运行
    ax = fig.add_subplot(1,1,1)    # ax = minutes.plot()
    ax.set_title("StudyData")
    ax.set_xlabel("User ID")
    ax.set_ylabel("Study Time")
    ax.plot(minutes)    # plt.show()

    fig.show()     # 可不要，依据上面运行
