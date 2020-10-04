'''
<ul>
  <li>
    <a href="http://softuni.bg">SoftUni</a>
 </li>
</ul>
end

<ul><li><ahref="http://softuni.bg">SoftUni</a></li></ul>
end
re.sub(pattern, repl, string, max=0)
This method replaces all occurrences of the RE pattern in string with repl, substituting all occurrences
unless max provided. This method returns modified string.
'''

import re
line = []
#pattern = r"(?P<trail>^\s+|)(?P<begin_tag>\<a)\s?(?P<URL>\w+\=\"\w+\:\/\/\w+\.\w+\")\>(?P<text>\w+)(?P<close_tag>\<\/a\>)"
pattern = r"(?P<URL><a\s?href=)"
in_data = input()
processed_line=""
while in_data != "end":

    processed_line = re.sub(pattern,"[URL href=",in_data)
    processed_line = re.sub(r"\"\>","\"]",processed_line)
    processed_line = re.sub(r"\</a\>","[/URL]",processed_line)
    line.append(processed_line)
    in_data = input()

for i in line:
    print(i)