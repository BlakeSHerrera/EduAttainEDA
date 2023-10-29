path = r'N:\datathon\Data\2017-18-crdc-data\2017-18 Public-Use Files\Data\LEA\CRDC\CSV'
with open(path + r'\LEA Characteristics.csv') as fp:
    data = fp.read()
with open(path + r'\LEA Characteristics (fixed).csv', 'w') as fp:
    fp.write(data.replace('\n",', '",'))
