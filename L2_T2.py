date = "12.04.2017"
date_list = date.split(".")
day = {"01": "First", "02": "Second", "03": "Third", "04": "Fourth",
       "05": "Fifth", "06": "Sixth", "07": "Seventh", "08": "Eighth",
       "09": "Ninth", "10": "Tenth", "11": "Eleventh", "12": "Twelfth",
       "13": "Thirteenth", "14": "Fourteenth", "15": "Fifteenth", "16": "Sixteenth",
       "17": "Seventeenth", "18": "Eighteenth", "19": "Nineteenth", "20": "Twentieth",
       "21": "Twenty first", "22": "Twenty second", "23": "Twenty third",
       "24": "Twenty fourth", "25": "Twenty fifth", "26": "Twenty sixth",
       "27": "Twenty seventh", "28": "Twenty eight", "29": "Twenty ninth",
       "30": "Thirtieth", "31": "Thirty first"}
month = {"01": "January", "02": "February", "03": "March",
         "04": "April", "05": "May", "06": "June",
         "07": "July", "08": "August", "09": "September",
         "10": "October", "11": "November", "12": "December"}
day_number = date_list[0]
month_number = date_list[1]
print(f"{day.setdefault(day_number)} of {month.setdefault(month_number)} of year {date_list[2]}")
