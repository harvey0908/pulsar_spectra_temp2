import json

with open("Johnston_2006_raw.txt", "r") as raw_file:
    lines = raw_file.readlines()

pulsar_dict = {}
for row in lines:
    row = row.replace(" ± ", "±").split()
    print(row)
    pulsar = row[0].replace("–", "-").replace("−", "-")
    if pulsar == "J1327-6222":
        continue
    flux = float(row[4].split("(")[0])

    pulsar_dict[pulsar] = {"Frequency MHz":[8400],
                           "Flux Density mJy":[flux],
                           # Text doesn't mention uncertainty so assuming 50%
                           "Flux Density error mJy":[flux*0.5]}

with open("Johnston_2006.json", "w") as cat_file:
    cat_file.write(json.dumps(pulsar_dict))
print(pulsar_dict)