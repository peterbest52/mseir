
import win32com.client

xlFile = r"I:\Peter_temp\Mij_data_V2.xlsx"

# create the excel application object
xlapp = win32com.client.Dispatch("Excel.Application")

# make xlapp visible, turn off display alerts
xlapp.Visible = 1
xlapp.DisplayAlerts = False

# open an existing file
workbook = xlapp.Workbooks.Open(xlFile)

# get "Sheet1"
worksheet1 = workbook.Worksheets("Mij")
worksheet2 = workbook.Worksheets("TownID")

# go through all the town ID
for i in range (1,170):

    z2 = 0

# target on each town section
    r1 = (i-1)*169+2
    r2 = (i-1)*169+170

    print r1,r2

# loop in each town section
    for xrow in range (int(r1),int(r2)+1):

# get the value of distance
        dis = worksheet1.Range("F%s" % xrow).Value

# compare distance with the contaiment threshold
        if dis == 0 or dis >140:

            z1 = 0

        elif dis < 140:
            
            pop = worksheet1.Range("G%s" % xrow).Value

            z1 = float(pop/dis)

# calculate accumulative population
        z2 = z2 + z1

    print z2

    for yrow in range (int(r1),int(r2)+1):

        dis1 = worksheet1.Range("F%s" % yrow).Value

        if dis1 == 0 or dis1 >140:

            z3 = 0

            pij = 0

        elif dis1 < 140:

            pop1 = worksheet1.Range("G%s" % yrow).Value

            z3 = float(pop1/dis1)

            print z3

# calculate the probability of transmission from Town i to Town j
            pij = float(z3/z2)

        else:

            pij = 0

        worksheet1.Range("J%s" % yrow).Value = pij


# compare distance with the contaiment threshold
        if dis == 0 or dis >20:

            z1 = 0

        elif dis < 20:
            
            pop = worksheet1.Range("G%s" % xrow).Value

            z1 = float(pop/dis)

# calculate accumulative population
        z2 = z2 + z1

    print z2

    for yrow in range (int(r1),int(r2)+1):

        dis1 = worksheet1.Range("F%s" % yrow).Value

        if dis1 == 0 or dis1 >20:

            z3 = 0

            pij = 0

        elif dis1 < 20:

            pop1 = worksheet1.Range("G%s" % yrow).Value

            z3 = float(pop1/dis1)

            print z3

# calculate the probability of transmission from Town i to Town j
            pij = float(z3/z2)

        else:

            pij = 0

        worksheet1.Range("H%s" % yrow).Value = pij



# compare distance with the contaiment threshold
        if dis == 0 or dis >60:

            z1 = 0

        elif dis < 60:
            
            pop = worksheet1.Range("G%s" % xrow).Value

            z1 = float(pop/dis)

# calculate accumulative population
        z2 = z2 + z1

    print z2

    for yrow in range (int(r1),int(r2)+1):

        dis1 = worksheet1.Range("F%s" % yrow).Value

        if dis1 == 0 or dis1 >60:

            z3 = 0

            pij = 0

        elif dis1 < 60:

            pop1 = worksheet1.Range("G%s" % yrow).Value

            z3 = float(pop1/dis1)

            print z3

# calculate the probability of transmission from Town i to Town j
            pij = float(z3/z2)

        else:

            pij = 0

        worksheet1.Range("I%s" % yrow).Value = pij
