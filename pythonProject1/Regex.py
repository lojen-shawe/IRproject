import re
from dateutil.parser import parse
import enchant

class Regex:
    list = ["[\w\.-]+@[\w\.-]+[.in|.com|.uk]","\s(\d{2}\:\d{2}\s?(?:AM|PM|am|pm))",
            "https?:\/\/w{0,3}\w*?\.\w{2,3}\S*","www\.\w*?\.\w{2,3}\S*","\w*?\.\w{2,3}[\/\?]\S*","\w*?\.\w{2,3}"]
    dash_List="(\w+[_\-.]\w+[_\-.]\w+[_\-.]\w+)|(\w+[_\-.]\w+[_\-.]\w+)|(\w+[_\-.]\w+)"
    Date_1 = "(([12]\d|30|31|0?[1-9])[/.-](0?[1-9]|1[0-2])[/.-](\d{4}|\d{2}))"
    Date_2 = "((0?[1-9]|1[0-2])[/.-]([12]\d|30|31|0?[1-9])[/.-](\d{4}|\d{2}))"
    Date_3 = "((\d{4}|\d{2})[/.-](0?[1-9]|1[0-2])[/.-]([12]\d|30|31|0?[1-9]))"
    Date_4 = "((January|February|Mars|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Jun|Jul|Agu|Sept|Sep|Oct|Nov|Dec) ([12]\d|30|31|0?[1-9]),? (\d{4}|\d{2}))"
    Date_5 = "(([12]\d|30|31|0?[1-9]) (January|February|Mars|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Jun|Jul|Agu|Sept|Sep|Oct|Nov|Dec),? (\d{4}|\d{2}))"
    Date_6 = "((\d{4}|\d{2}) ,?(January|February|Mars|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Jun|Jul|Agu|Sept|Sep|Oct|Nov|Dec) ([12]\d|30|31|0?[1-9]))"
    Date_7="(January|February|Mars|April|May|June|July|August|September|October|November|December|Jan|Feb|Mar|Jun|Jul|Agu|Sept|Sep|Oct|Nov|Dec) .? ([12]\d|30|31|0?[1-9]) "
    All_REGEX = "(" + Date_1 + "|" + Date_2 + "|" + Date_3 + "|" + \
                        Date_4 + "|" + Date_5 + "|" + Date_6 + "|" + Date_7 + ")"

    def __init__(self):
	    self.result = [] 

    def is_date(string, fuzzy=False):
        try:
            parse(string,fuzzy=fuzzy)
            return True
        except ValueError:
            return False

    def Convert(string):
        if Regex.is_date(string):
            return parse(string).strftime("%d-%m-%Y")

    def check(self,string):
        ok=1
        while (ok==1):
            ok=0
            if (string.find("U.S") != -1):
                string=string.replace("U.S","")
                self.result.append('UNITED STATES')
                ok=1
            if (string.find("U_S") != -1):
                string=string.replace("U_S","")
                self.result.append('UNITED STATES')
                ok=1
            if (string.find("U-S") != -1):
                string=string.replace("U-S","")
                self.result.append('UNITED STATES')
                ok=1
            if (string.find("U.N") != -1):
                string=string.replace("U.N","")
                self.result.append('UNITED NATIONS')
                ok=1
            if (string.find("U_N") != -1):
                string = string.replace("U_N", "")
                self.result.append('UNITED NATIONS')
                ok = 1
            if (string.find("U-N") != -1):
                string=string.replace("U-N","")
                self.result.append('UNITED NATIONS')
                ok=1
            if (string.find("UNITED STATES") != -1):
                string=string.replace("UNITED STATES","")
                self.result.append('UNITED STATES')
                ok=1
            if (string.find("UNITED NATIONS") != -1):
                string=string.replace("UNITED NATIONS","")
                self.result.append('UNITED NATIONS')
                ok=1
            if (string.find("VIET NAM") != -1):
                string=string.replace("VIET NAM","")
                self.result.append('VIET NAM')
                ok=1
            if (string.find("VIETNAM") != -1):
                string = string.replace("VIETNAM", "")
                self.result.append('VIET NAM')
                ok=1
        return string

    def compile_string(self,string): 
        old_string=string
        for i in self.list:
            match1=re.findall(i,string)
            self.result.extend(match1)
            for ma in match1:
                string=string.replace(ma,'')


        regex_all = re.compile(self.All_REGEX, re.IGNORECASE)
        tokens = regex_all.findall(string)

        for token in tokens:
            if token!='':
               string = string.replace(token[0],Regex.Convert(token[0]))
               string=string.replace(Regex.Convert(token[0]),'')
               self.result.append(Regex.Convert(token[0]))

        string=self.check(string)
        string=self.dealWithDash(string)
        return string


    def dealWithDash(self,string):
        match1 = re.findall(self.dash_List, string)
        d = enchant.Dict("en_US")
        for ma in match1:
            str_without_space=""
            str_with_space=""
            strs=[]
            for i in ma:
                if i!='':
                    string=string.replace(i,'')
                    strs=re.split('[\.\-\_]',i)
            for i in strs:
                if (d.check(i) and len(i)>1 and i.upper()!='EL' and i.upper()!='AL'):
                    self.result.append(i.upper())
                elif not i.isnumeric():
                    str_without_space+=i
                else:
                    if len(i)>1:
                        self.result.append(i.upper().split('\.\-\_'))
                    elif not i.isnumeric():
                        str_without_space+=i

                str_with_space += i+" "

            self.result.append(str_with_space.upper())
            if str_without_space!="":
                self.result.append(str_without_space.upper())

        return string
