#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import json
import pandas as pd

def analysis(file, user_id):
    times = 0
    minutes = 0
    try:
        with open(file, 'r') as file_dict:
            new_file = json.loads(file_dict.read())

        df = pd.DataFrame(new_file)
    except ValueError:
        return 0

    times = df[df['user_id'] == user_id].shape[0]
    minutes = df[df['user_id'] == user_id]['minutes'].sum()

    return times, minutes
