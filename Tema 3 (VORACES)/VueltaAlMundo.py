def function(countries):
    countries.sort()
    currentTime = 0
    visitedCountries = 0
    for country in countries:
        if currentTime <= country[1]:
            currentTime = country[0]
            visitedCountries += 1

    print(visitedCountries)


if __name__ == "__main__":
    n = int(input().strip())

    for _ in range(n):
        p = int(input().strip())

        list = input().strip().split()
        months = []
        for value in list:
            months.append(int(value))

        countries = [[months[i + 1], months[i]] for i in range(0, len(months), 2)]
        function(countries)
