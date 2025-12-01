def classifyProduce(colorScore, sizeScore, freshDay):
    if (sizeScore < 0 or sizeScore > 10) or \
    (freshDay < 0 or freshDay > 30) or \
    (colorScore < 0 or colorScore > 10) :
        return "Invalid Input"
    if colorScore >= 5:
        if sizeScore >= 7:
            if freshDay <= 10:
                return "Good"
            return "Average"
        else:
            if freshDay <= 10:
                return "Average"
            return "Bad"
    else:
        if sizeScore >= 7:
            if freshDay <= 10:
                return "Average"
            return "Bad"
        return "Bad"