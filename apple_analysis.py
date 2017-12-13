#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd

def quarter_volume():
    data = pd.read_csv('apple.csv', header=0)

    datetime_index = pd.to_datetime(list(data.Date))
    volume_list = list(data.Volume)
    volume_series = pd.Series(volume_list, index=datetime_index)
    volume_resample = volume_series.resample('Q').sum()
    volume_sort = volume_resample.sort_values()
    second_volume = volume_sort.iloc[-2]

    return second_volume

if __name__ == '__main__':
    a = quarter_volume()
    print(a)

