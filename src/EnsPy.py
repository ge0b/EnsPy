# Copyright (c) 2020 Georgios Boumis
# Distributed under the terms of the BSD 3-Clause License
# SPDX-License-Identifier: BSD-3-Clause
"""A collection of tools for reading, visualizing, and extracting information from ensemble forecasts data."""


import os.path
import pandas as pd
pd.set_option('mode.chained_assignment', None)


class enspytools:
    def __init__(self, path):
        self.path = path
        extensions = {"1": ".csv"}
        extension = os.path.splitext(path)[1]
        if extension not in extensions.values():
            raise ValueError("File currently not supported!")
        for key, value in extensions.items():
            if value == extension:
                self.key = key
        return

    def enspyframe(self):
        if self.key == "1":
            dataframe = pd.read_csv(self.path, header=None)
        nomembers = len(dataframe.columns) - 2
        colnames = ["Forecast valid date", "Lead time (hours)"]
        mname = "Member"
        for i in range(nomembers):
            mname = mname + " " + str(i + 1)
            colnames.append(mname)
            mname = "Member"
        dataframe.columns = colnames
        dataframe[dataframe.columns[0]
                  ] = dataframe[dataframe.columns[0]].apply(str)
        for i in range(len(dataframe)):
            a = dataframe[dataframe.columns[0]][i][0:4] + "-"
            b = dataframe[dataframe.columns[0]][i][4:6] + "-"
            c = dataframe[dataframe.columns[0]][i][6:8] + " "
            d = dataframe[dataframe.columns[0]][i][-2:]
            dataframe[dataframe.columns[0]][i] = a + b + c + d
        return dataframe