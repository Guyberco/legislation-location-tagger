import json
import functools

def getLawsByDate(locationsMapJson, century=""):
    locations = []
    for location in locationsMapJson.keys():
        laws = locationsMapJson.get(location)
        if not century == "":
            laws = list(filter(isLawInCentury(century), laws))
        locations.append([location, len(laws)])
    return locations


def getYearByDate(date):
    YYMMDD = date.split('-')
    if len(YYMMDD) == 3:
        return YYMMDD[0]
    else:
        return None


def isInCentury(century, date):
    return century[:3] == date[:3]


def isLawInCentury(century):
    def isInC(law):
        date = law.get('date')
        year = getYearByDate(date)
        if year:
            return isInCentury(century, year)
        else:
            return False
    return isInC

def getTopK(locations, k):
    locations.sort(key=(lambda location: location[1]), reverse=True)
    return locations[:k]

def getLowK(locations, k):
    locations.sort(key=(lambda location: location[1]))
    return locations[:k]

def makeIsraelStockChartByCenturies():
    with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
        locationsMapJson = json.load(json_file)
        locations = getLawsByDate(locationsMapJson)
        israelLaws = locationsMapJson.get("ישראל")

        centuriesToLaws = {
            1000: 0,
        }
        for c in range(1900, 2030, 10):
            centuriesToLaws.update({c: 0})
        for law in israelLaws:
            date = getYearByDate(law.get("date"))
            dateCentury = date[:3] + "0"
            centuriesToLaws[(int(dateCentury))] += 1
        centuriesList = list(map(lambda key: [str(key), centuriesToLaws.get(key)], centuriesToLaws.keys()))
        with open('StockChartByCenturies.json', 'w', encoding='UTF-8') as file:
            json.dump(centuriesList, file)
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
        locations = getTopK(getLawsByDate(locationsMapJson), 21)
        locations.pop(0)

        with open('TopTwenteWithoutISrael.json', 'w', encoding='UTF-8') as file:
            json.dump(locations, file)


def buildDataForGraph():
    with open('locationsMap.json', 'r', encoding='UTF-8') as json_file:
        locationsMapJson = json.load(json_file)
        locations = getTopK(getLawsByDate(locationsMapJson), 21)

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



buildDataForGraph()
# makeIsraelStockChartByCenturies()
buildTopTwenteWithoutISrael()