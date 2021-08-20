import pandas as pd

file = "Project_File (2) (2).xlsx"
xlsx = pd.ExcelFile(file)


dataFrame = xlsx.parse(
    usecols=[0,1,2,3,4,5,6,7,8,9,10,11,12,],
    names=["", "Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", "Viet Nam", "Myanmar", "Japan",
            "Hong Kong", "China", "Taiwan", "Korea,Republic Of"]
)
print(dataFrame)

# split year
yr = dataFrame.iloc[:, 0].str.split(' ', n=2, expand=True)

print(yr)

# assigning year to a column
yr = dataFrame.assign(Year=yr[1])
print(yr)

# print asia 2008-2017 range
yrRange = dataFrame[(yr['Year'] >= str(2008)) & (yr['Year'] <= str(2017))]
print(yrRange)

# printing without years and months ,, replacing na
asiaCountries = dataFrame[["Brunei Darussalam", "Indonesia", "Malaysia", "Philippines", "Thailand", "Viet Nam", "Myanmar", "Japan",
            "Hong Kong", "China", "Taiwan", "Korea,Republic Of"]]

asiaCountries = asiaCountries.replace(',', '', regex=True)
asiaCountries = asiaCountries.replace('na', '0', regex=True)
print(asiaCountries)

# calculate 10 years range
asiaCountries = asiaCountries.astype(int)
totalSum = asiaCountries.sum()
print(totalSum)

# put to ascending orders
ascending = totalSum.sort_values(ascending=False)
print(ascending)

# printing top 3 countries
top3Countries = ascending.head(3)
print(top3Countries)

# sort the values ascending in order
ascending = totalSum.sort_values(ascending=False)
print("The number of visitors from all Asia Countries in ascending order:" + '\n' + str(ascending))

# Top 3 Countries with the most Visitors
Top3 = ascending.head(3)
print("The number of visitors from Top 3 Countries in ascending order:" + '\n' + str(Top3))

# total sum of visitors for top 3 countries
topSum = top3Countries.sum()
print("Total number of visitors for top 3 countries in Asia: ", topSum)
# mean visitor numbers from Top3 Countries
average = top3Countries.mean()
print("Mean of top 3 highest visitors Country in Asia: ", round(average, 1))

# median visitor numbers from Top 3 Countries
median = top3Countries.median()
print("Median of top 3 countries of highest visitor: ", median)

import matplotlib.pyplot as plt

#top 3 countries with the most visitors chart
chart = top3Countries.sort_values(ascending=False)
plt.xlabel('Countries', fontsize=10)
plt.ylabel('No. of Visitors', fontsize=10)
plt.title('Top 3 Countries in Asia visitors from 2008-2017')
plt.bar(chart.index, chart.values/1000)
plt.show()

# Visitor numbers from all asia Countries
VisitorNo = totalSum.sort_values(ascending=False)
print(VisitorNo)

plt.xlabel('Countries', fontsize=10)
plt.ylabel('No of Visitors', fontsize=8)
plt.title('All Countries in Asia from 2008 to 2017')
plt.bar(VisitorNo.index, VisitorNo.values/1000)
plt.show()

#unit testing
class Testing:
    def add(no1, no2, no3):
        result = no1 + no2 + no3
        return result

    def mean(no2):
        result = sum(no2) / len(no2)
        return result

    #asdfghjkl