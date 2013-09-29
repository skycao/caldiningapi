"""Write into from Soup Demo to file"""
def write(DC):
    ofile = csv.writer(open('test.csv', "wb"))
    ofile.writerow = (["name","vegan","calories","totalfat","satfat","transfat","cholesterol","sodium","totalcarbs","dietfib","sugar","protein","vitc","calcium","iron"])
    for x in DC.list:
        row = []
        row.append(x.name.toString())
        row.append(x.veg.toString())
        for y in x.nutfacts:
            row.append(y.toString()):
        ofile.writerow(row)
    ofile.close()