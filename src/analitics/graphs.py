import json
import functools

def getLawsByDate(locationsMapJson, decade=""):
    locations = []
    for location in locationsMapJson.keys():
        laws = locationsMapJson.get(location)
        if not decade == "":
            laws = list(filter(isLawInDecade(decade), laws))
        locations.append([location, len(laws)])
    return locations


def getYearByDate(date):
    YYMMDD = date.split('-')
    if len(YYMMDD) == 3:
        return YYMMDD[0]
    else:
        return None


def isInDecade(decade, date):
    return decade[:3] == date[:3]


def isLawInDecade(decade):
    def isInD(law):
        date = law.get('date')
        year = getYearByDate(date)
        if year:
            return isInDecade(decade, year)
        else:
            return False
    return isInD

def getTopK(locations, k):
    locations.sort(key=(lambda location: location[1]), reverse=True)
    return locations[:k]

def getLowK(locations, k):
    locations.sort(key=(lambda location: location[1]))
    return locations[:k]

def makeIsraelStockChartByDecades():
    with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
        locationsMapJson = json.load(json_file)
        locations = getLawsByDate(locationsMapJson)
        israelLaws = locationsMapJson.get("ישראל")

        decadesToLaws = {
            1000: 0,
        }
        for c in range(1900, 2030, 10):
            decadesToLaws.update({c: 0})
        for law in israelLaws:
            date = getYearByDate(law.get("date"))
            dateDecade = date[:3] + "0"
            decadesToLaws[(int(dateDecade))] += 1
        decadesList = list(map(lambda key: [str(key), decadesToLaws.get(key)], decadesToLaws.keys()))
        with open('StockChartByDecades.json', 'w', encoding='UTF-8') as file:
            json.dump(decadesList, file)
        # print(locationsMapJson.min(lambda location: location))


def buildTopTen():
    with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
        locationsMapJson = json.load(json_file)
        locations = getTopK(getLawsByDate(locationsMapJson), 10)

        with open('top10WithIsrael.json', 'w', encoding='UTF-8') as file:
            json.dump(locations, file)

def buildTopTwenteWithoutISrael():
    with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
        locationsMapJson = json.load(json_file)
        locations = getTopK(getLawsByDate(locationsMapJson), 22)
        locations.pop(0)

        with open('TopTwenteWithoutISrael.json', 'w', encoding='UTF-8') as file:
            json.dump(locations, file)


def buildDataForGraph():
    with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
        locationsMapJson = json.load(json_file)
        locations = getTopK(getLawsByDate(locationsMapJson), 10)

        with open('dataGraph.json', 'w', encoding='UTF-8') as file:
            json.dump(locations, file)

def findMax(lst):
    max  = 0
    indx = 0
    for i, element in enumerate(lst):
        if element[1] > max:
            max = element[1]
            indx = i
    return lst[indx]


    # list2 = locations[:]  # make a copy of list1
    # result = []
    # for i in range(k):
    #     result.append(max(list2))  # append largest element to list of results
    #     list2.remove(max(list2))  # remove largest element from old list



# buildDataForGraph()
# makeIsraelStockChartByDecades()
buildTopTwenteWithoutISrael()