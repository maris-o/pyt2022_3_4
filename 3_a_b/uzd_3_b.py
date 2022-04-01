import re
cerealsFile = open('cereals.csv')

lowestCerealRating = 100.0
averageCerealRating = 0.0
averageCerealRatingSum = 0.0
highestCerealRating = 0.0
count = 0

for lines in cerealsFile: 
    count += 1                                                              #aprēķina rindu skaitu

    if count != 1:                                                          #tiek izlaista pirmā rinda                    
        reRatingNumber = re.findall ('[,](\d\d.\d{4,6})', lines)            #tiek izgriezta retinga vērtība 
        ratingNumber = float(reRatingNumber[0])                             #reting vērtība tiek pārveidota uz Float
        averageCerealRatingSum =(averageCerealRatingSum+ratingNumber)       #tiek aprēķināta rating kopējā vērtība
            
        if ratingNumber > highestCerealRating:                              #tiek salīdzināts vai rating vērtība ir lielāka nekā maksimālā rating vērtība
            highestCerealRating = ratingNumber                              #ja izpildās, tad rating vērtība tiek saglabāta, kā maksimālā rating vērtība
            reHighesCerealName = re.findall (r'^[^,]+', lines)              #tiek izgriezts nosaukums
            highesCerealName = str (reHighesCerealName[0])                  #nosaukums tiek pārveidots uz String
            
        elif ratingNumber < lowestCerealRating:                             #tiek salīdzināts vai rating vērtība ir mazāka nekā minimālā rating vērtība
            lowestCerealRating = ratingNumber                               #ja izpildās, tad rating vērtība tiek saglabāta, kā minimālā rating vērtība
            reLowestCerealName = re.findall (r'^[^,]+', lines)              #tiek izgriezts nosaukums
            lowestCerealName = str (reLowestCerealName[0])                  #nosaukums tiek pārveidots uz String
        
        else:
            continue 
    else:
        continue

averageCerealRating = str (averageCerealRatingSum/count)                    #tiek aprēķināta vidējā vērtība un pārvērsta uz String
highestCerealRating = str (highestCerealRating)
lowestCerealRating = str (lowestCerealRating)
    
print("The lowest cereals rating value: " + lowestCerealRating +  ". Cereals name: " + lowestCerealName)        #izdrukā minimālo retinga vērtību un nosaukumu
print("The average cereals rating value: " + averageCerealRating)                                               #izdrukā vidējo retinga vērtību
print("The highest cereals rating value: "+ highestCerealRating +  ". Cereals name: " + highesCerealName)       #izdrukā maksimālo retinga vērtību un nosaukumu