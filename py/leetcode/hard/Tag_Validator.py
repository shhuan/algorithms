# -*- coding: utf-8 -*-
"""

Given a string representing a code snippet, you need to implement a tag validator to parse the code and return whether it is valid. A code snippet is valid if all the following rules hold:

The code must be wrapped in a valid closed tag. Otherwise, the code is invalid.
A closed tag (not necessarily valid) has exactly the following format : <TAG_NAME>TAG_CONTENT</TAG_NAME>. Among them, <TAG_NAME> is the start tag, and </TAG_NAME> is the end tag. The TAG_NAME in start and end tags should be the same. A closed tag is valid if and only if the TAG_NAME and TAG_CONTENT are valid.
A valid TAG_NAME only contain upper-case letters, and has length in range [1,9]. Otherwise, the TAG_NAME is invalid.
A valid TAG_CONTENT may contain other valid closed tags, cdata and any characters (see note1) EXCEPT unmatched <, unmatched start and end tag, and unmatched or closed tags with invalid TAG_NAME. Otherwise, the TAG_CONTENT is invalid.
A start tag is unmatched if no end tag exists with the same TAG_NAME, and vice versa. However, you also need to consider the issue of unbalanced when tags are nested.
A < is unmatched if you cannot find a subsequent >. And when you find a < or </, all the subsequent characters until the next > should be parsed as TAG_NAME (not necessarily valid).
The cdata has the following format : <![CDATA[CDATA_CONTENT]]>. The range of CDATA_CONTENT is defined as the characters between <![CDATA[ and the first subsequent ]]>.
CDATA_CONTENT may contain any characters. The function of cdata is to forbid the validator to parse CDATA_CONTENT, so even it has some characters that can be parsed as tag (no matter valid or invalid), you should treat it as regular characters.
Valid Code Examples:
Input: "<DIV>This is the first line <![CDATA[<div>]]></DIV>"

Output: True

Explanation:

The code is wrapped in a closed tag : <DIV> and </DIV>.

The TAG_NAME is valid, the TAG_CONTENT consists of some characters and cdata.

Although CDATA_CONTENT has unmatched start tag with invalid TAG_NAME, it should be considered as plain text, not parsed as tag.

So TAG_CONTENT is valid, and then the code is valid. Thus return true.


Input: "<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"

Output: True

Explanation:

We first separate the code into : start_tag|tag_content|end_tag.

start_tag -> "<DIV>"

end_tag -> "</DIV>"

tag_content could also be separated into : text1|cdata|text2.

text1 -> ">>  ![cdata[]] "

cdata -> "<![CDATA[<div>]>]]>", where the CDATA_CONTENT is "<div>]>"

text2 -> "]]>>]"


The reason why start_tag is NOT "<DIV>>>" is because of the rule 6.
The reason why cdata is NOT "<![CDATA[<div>]>]]>]]>" is because of the rule 7.
Invalid Code Examples:
Input: "<A>  <B> </A>   </B>"
Output: False
Explanation: Unbalanced. If "<A>" is closed, then "<B>" must be unmatched, and vice versa.

Input: "<DIV>  div tag is not closed  <DIV>"
Output: False

Input: "<DIV>  unmatched <  </DIV>"
Output: False

Input: "<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"
Output: False

Input: "<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"
Output: False

Input: "<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"
Output: False
Note:
For simplicity, you could assume the input code (including the any characters mentioned above) only contain letters, digits, '<','>','/','!','[',']' and ' '.
"""

import re

class Solution(object):
    def isValid(self, code):
        """
        :type code: str
        :rtype: bool
        """

        def dfs(codestr, inner):
            # print(codestr)
            if not codestr:
                return True if inner else False

            parts = re.split("<!\[CDATA\[.*?\]\]>", codestr)
            if len(parts) > 1:
                if not parts[0] or not parts[-1]:
                    return False
                return dfs(''.join(parts), inner)
            start = 0
            N = len(codestr)
            while start < N:
                if codestr[start] == ' ':
                    start += 1
                else:
                    break

            if start == N:
                return True

            if codestr[start] != '<':
                if not inner:
                    return False
                for i in range(start, N):
                    if codestr[i] == '<':
                        return dfs(codestr[i:], 1)

                return True

            else:
                if start >= N - 1:
                    return False

                # <TAG_NAME>...</TAG_NAME>
                end = start + 1
                while end < N:
                    if codestr[end] != '>':
                        if not (ord('A') <= ord(codestr[end]) <= ord('Z')):
                            return False
                    else:
                        if end - start == 1:
                            return False
                        break
                    if end - start > 9:
                        return False
                    end += 1

                if end == N:
                    return False

                if not inner:
                    # find right most close tag
                    rstart = N - 1
                    while rstart > end and codestr[rstart] == ' ':
                        rstart -= 1

                    if rstart == end:
                        return False
                    if codestr[rstart] != '>':
                        return False

                    rend = rstart - 2
                    while rend > end and codestr[rend: rend + 2] != '</':
                        rend -= 1

                    if rend <= end:
                        return False

                    if codestr[rend + 2: rstart] != codestr[start + 1:end]:
                        return False
                else:
                    startTag = codestr[start:end]
                    closeTag = '</' + startTag[1:]

                    startTagIndex = [(x.start(), 0) for x in re.finditer(startTag, codestr)]
                    closeTagIndex =  [(x.start(), 1) for x in re.finditer(closeTag, codestr)]

                    if len(closeTagIndex) < len(startTagIndex):
                        return False

                    c = 0
                    tagIndex = list(sorted(startTagIndex + closeTagIndex))
                    for ti in tagIndex:
                        if ti[1] == 1:
                            c -= 1
                            if c == 0:
                                return dfs(codestr[end+1: ti[0]], 1) and dfs(codestr[ti[0]+len(closeTag):], 1)
                        else:
                            c += 1
                    return False

                return dfs(codestr[end + 1:rend], 1)

        return dfs(code, 0)


s = Solution()
print(s.isValid("<DIV>This is the first line <![CDATA[<div> <![cdata]> [[]]</div>   ]]>  <DIV> <A>  <![CDATA[<b>]]>  </A>  <A> <C></C></A></DIV>    </DIV>"))
print(s.isValid("<![CDATA[ABC]]><TAG>sometext</TAG>"))
print(s.isValid("<![CDATA[<div>]]>"))
print(s.isValid("<A><A>456</A>  <A> 123  !!  <![CDATA[<![cdata]>]]>  123 </A>   <A><![CDATA[</A>]]>  </A>  <A>123</A></A>"))
print(s.isValid("<A><A>456</A>  <A> 123  !!  <![CDATA[]]>  123 </A>   <A>123</A></A>"))
print(s.isValid("<![CDATA[wahaha]]]><![CDATA[]> wahaha]]>"))
print(s.isValid("<DIV>This is the first line <![CDATA[<div>]]></DIV>"))
print(s.isValid("<DIV>>>  ![cdata[]] <![CDATA[<div>]>]]>]]>>]</DIV>"))
print(s.isValid("<A>  <B> </A>   </B>"))
print(s.isValid("<DIV>  unmatched <  </DIV>"))
print(s.isValid("<DIV>  div tag is not closed  <DIV>"))
print(s.isValid("<DIV> unmatched tags with invalid tag name  </1234567890> and <CDATA[[]]>  </DIV>"))
print(s.isValid("<DIV> closed tags with invalid tag name  <b>123</b> </DIV>"))
print(s.isValid("<DIV>  unmatched start tag <B>  and unmatched end tag </C>  </DIV>"))
print(s.isValid("dee<ST>cdd </ST>  "))
print(s.isValid(''))