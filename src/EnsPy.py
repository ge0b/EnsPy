# Copyright (c) 2020 Georgios Boumis
# Distributed under the terms of the BSD 3-Clause License
# SPDX-License-Identifier: BSD-3-Clause
"""A collection of tools for reading, visualizing, and extracting information from ensemble forecasts data."""


import os.path
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime, timedelta
plt.style.use("ggplot")
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

    def enspygraph(self, dataframe):
        issuedate = datetime.strptime(dataframe.iloc[0, 0], '%Y-%m-%d %H')
        issuedate = issuedate - timedelta(hours=int(dataframe.iloc[0, 1]))
        issuedate = "Forecast issue date:" + " " + str(issuedate)
        plotlist = []
        for i in range(len(dataframe.columns) - 2):
            vlist = list(dataframe.iloc[:, i + 2])
            plotlist.append(vlist)
        plotarray = np.array(plotlist)
        plt.plot(dataframe.iloc[:, 1], np.matrix.transpose(
            plotarray), color="cornflowerblue")
        plt.xlabel("Lead time (hours)")
        plt.xticks(dataframe.iloc[:, 1])
        plt.title(issuedate)
        plt.show()

    def enspyprob(self, dataframe, date, threshold):
        row = dataframe.index[dataframe["Forecast valid date"] == date][0]
        i = 0
        for j in range(2, len(dataframe.iloc[row, :])):
            if dataframe.iloc[row, j] < threshold:
                i += 1
        prob = (i + 1 - 1 / 3) / (len(dataframe.iloc[row, :]) - 2 + 1 - 1 / 3)
        prob = (1 - prob) * 100
        print("")
        print(f"Probability of >= {threshold} equals {prob}")
