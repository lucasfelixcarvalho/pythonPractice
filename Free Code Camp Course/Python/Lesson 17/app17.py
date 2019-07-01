month_conversions = {
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

print(month_conversions["Jun"])
print(month_conversions.get("Dec"))
print(month_conversions.get("Luv"))
print(month_conversions.get("Luv", "Not a valid key"))
