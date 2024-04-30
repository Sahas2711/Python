import numpy as np
arr = np.loadtxt('/content/sample_data/Untitled spreadsheet - Sheet1.csv', delimiter=',',dtype=str,skiprows=1)
print(arr)

SIC = []
EDS = []
EGR = []
PHY = []
EEE = []

for i in arr:
  SIC.append(int(i[1]))
  EDS.append(int(i[1]))
  EGR.append(int(i[1]))
  PHY.append(int(i[1]))
  EEE.append(int(i[1]))


print(SIC)
print(EDS)
print(EGR)
print(PHY)
print(EEE)