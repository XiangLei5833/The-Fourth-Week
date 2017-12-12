#!/usr/bin/env python
# -*- coding:utf-8 -*-

import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0

    try:
        new_file = pd.read_json(file)
        new_dataframe = new_file[new_file['user_id']==user_id].reindex(
               columns=['user_id', 'minutes'])
    except ValueError:
        return 0

    times = new_dataframe.shape[0]
    minutes = new_dataframe['minutes'].sum()
    
    return times, minutes
