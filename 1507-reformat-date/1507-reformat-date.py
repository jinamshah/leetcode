import re
from datetime import datetime as D
class Solution:
    def reformatDate(self, date: str) -> str:
        # values = date.split(" ")
        # months = {
        #     "Jan": "01", 
        #     "Feb": "02",
        #     "Mar": "03",
        #     "Apr": "04",
        #     "May": "05",
        #     "Jun": "06",
        #     "Jul": "07",
        #     "Aug": "08",
        #     "Sep": "09",
        #     "Oct": "10",
        #     "Nov": "11",
        #     "Dec": "12"
        # }
        # year = values[2]
        # month = months[values[1]]
        # # print(values)
        # date = re.sub(r"th|rd|nd|st", "", values[0])
        # if len(date) == 1:
        #     date = "0"+date
        # return f"{year}-{month}-{date}"
        return D.strptime(re.sub('rd|nd|th|st|','',date),'%d %b %Y').strftime('%Y-%m-%d')