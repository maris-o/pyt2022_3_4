cerealsFile = open('cereals.csv')

lowestCerealRating = 100.0
averageCerealRating = 0.0
averageCerealRatingSum = 0.0
highestCerealRating = 0.0
count = 0

for lines in cerealsFile: 
    count += 1
    if count != 1:
        ratingPlacment = lines.rfind (',')
        ratingNumber = float (lines [ratingPlacment + 1 :])
        averageCerealRatingSum =(averageCerealRatingSum+ratingNumber)

        if ratingNumber > highestCerealRating:
            highestCerealRating = ratingNumber
            cerealNamePalcment = lines.find (',')
            highesCerealName = lines [ :cerealNamePalcment]
        
        elif ratingNumber < lowestCerealRating:
            lowestCerealRating = ratingNumber
            cerealNamePalcment = lines.find (',')
            lowestCerealName = lines [ :cerealNamePalcment]
        
        else:
            continue 
    
    else:
        continue

averageCerealRating = str (averageCerealRatingSum/count)
highestCerealRating = str (highestCerealRating)
lowestCerealRating = str (lowestCerealRating)
    
print("The lowest cereals rating value: " + lowestCerealRating +  ". Cereals name: " + lowestCerealName)
print("The average cereals rating value: " + averageCerealRating)
print("The highest cereals rating value: "+ highestCerealRating +  ". Cereals name: " + highesCerealName)
