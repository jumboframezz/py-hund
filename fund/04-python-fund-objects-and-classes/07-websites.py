'''
Websites

You have been tasked to create an ordered database of websites. For the task you will need to create a class Website, which will have a Host, a Domain and Queries.

The Host and the Domain are simple strings.
The Queries, is Collections of strings.

You will be given several input lines in the following format:

{host} | {domain} | {query1,query2. . .}

Note: There will always be a host and a domain, but there might NOT be ANY queries.
The input sequence ends, when you receive the command “end”. Then you must print all websites in the following format:
https://www.{host}.{domain}/query?=[{query1]&[{query2}]&[query3]. . .
In case there are NO queries, just print:
https://www.{host}.{domain}

Examples

Input                                       Output
softuni | bg | user,course,homework         https://www.softuni.bg/query?=[user]&[course]&[homework]
judge.softuni | bg | contest,bg             https://www.judge.softuni.bg/query?=[contest]&[bg]
google | bg | search,query                  https://www.google.bg/query?=[search]&[query]
zamunda | net                               https://www.zamunda.net
end

softuni | bg | user,course,homework
judge.softuni | bg | contest,bg
google | bg | search,query
zamunda | net
end
'''


class Website:
    def __init__(self, line):
        fields = list(line.split(" | "))
        self.host = fields[0]
        self.domain = fields[1]
        self.queries = []
        self.numq = 0
        if len(fields) >= 3:
            queries = list(fields[2].split(","))
            for i in queries:
                self.queries.append(i)
        self.numq = len(self.queries)

    def display(self):
        qstr = ""
        print(f"https://www.{self.host}.{self.domain}", end="")
        if self.numq == 0:
                print()
        else:
            print("/query?=", end="")
            for i in range(0, self.numq):
                qstr += f"[{self.queries[i]}]&"
            print (qstr.strip("&"))

in_line = input()
websites=[]
while in_line != "end":
    websites.append(Website(in_line))
    in_line = input()

for i in websites:
        i.display()




