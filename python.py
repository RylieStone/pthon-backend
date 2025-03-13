from math import *
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sep": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December"
}

def monthConv(month):
    return monthConversion.get(month, "Not a valid key")
print(monthConv(input("put in the first three letters of a month of your pick: ")))
