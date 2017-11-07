# -*- coding: utf-8 -*-
"""
created by huash at 2016/6/18 20:14

Given a list of unique words. Find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
Credits:


1. 记录每个单词的下标到字典中
2. 遍历列表，计算当前单词W的逆序词R
3. 如果R在#1的字典中，W+R是回文
4. 如果当前词的前面一部分W[:i]的逆序词R[:i]在字典中，且W的后面部分W[i:]是回文，W+R[:i]是回文
5. 同#4，W[:i]+R是回文的情况

"""
__author__ = 'huash'

import sys
import os
import datetime
import functools
import itertools
import collections
import time

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        res = []
        dic = {}
        for i in range(len(words)):
            dic[words[i]] = i

        for word in words:
            word_rev = word[::-1]
            if word_rev in dic and dic[word_rev] != dic[word]:
                res.append([dic[word_rev], dic[word]])
            for i in range(len(word)):
                temp1 = word[:i][::-1]
                temp2 = word_rev[:i]
                if temp1 in dic and self.isPal(word[i:]):
                    res.append([dic[word], dic[temp1]])
                if temp2 in dic and self.isPal(word_rev[i:]):
                    res.append([dic[temp2], dic[word]])
        return res

    def isPal(self, word):
        left = 0
        right = len(word)-1
        while left < right:
            if word[left] != word[right]:
                return False
            left += 1
            right -= 1
        return True



    def isPalindrome(self, word):

        lw = len(word)
        for i in range(lw // 2):
            if word[i] != word[lw - 1 - i]:
                return False
        return True

    def samePrefix(self, w1, w2):
        if len(w1) > len(w2):
            return self.samePrefix(w2, w1)

        return w1 == w2[:len(w1)]


s = Solution()

print(s.isPalindrome("abcd"))
print(s.isPalindrome("acbvbca"))

print(s.palindromePairs(["abcd", "dcba", "lls", "s", "sssll"]))

t0 = time.clock()
print(s.palindromePairs(["gefbcfh","jjiejgjbb","ch","hhfbigfijd","g","fbheegdbhdiiff","jhabjjhfifejidcb","jdcgbg","aihegfjcbfiiaaihidh","eg","id","aefafdbbfhchf","fhghdjgdbjd","adieahbiaebc","ecebigcffbbjbfhfag","hddbhgaea","bfejhejjiegiihgdjeeg","cffffcggifgjcgfd","ccaa","b","jcefbac","djgehbiebi","ajjgafaidjjg","bcdfcjc","eaghbegj","chhaehhdadd","cjcafbffciabhadaiee","gdeabbbchh","f","aabajhhjdedcea","bidfaifb","chggdhegbciibjgcf","dafhbbchhcchbgeec","eaajabgdeijgfh","fbadhabfcbfg","dhfhdhbfiaiidf","eieagje","fdadhbecfdfgjeifb","ehhijaghjijbbfc","eejjghidbbfgbi","fej","bfejicdf","iifahjafegfaaeecf","cifieehg","hcjhijcch","if","jcdbfggghjfibgdhbf","j","d","jdgedjagebbcgbjbcfbj","cdfccg","bcdae","bg","ghbeeihacdifgdac","aieebghibghfig","febjaiegfaediigccj","igaacjibagjcgegjf","gbacadihj","idgeacdgecdghbhi","jjcjefiedba","i","cciegdigecahjfe","bajhh","fijehibgb","bfcgbaaechf","fgjae","abdgabaadj","hadbib","hgbiebbgi","jgbhgcfbbfhg","jaabgijdfbfhcacbcajj","jgbejcadecaaghic","igbigdbfd","ijch","jcah","ihcefagfcgfcfh","cjag","fdcjhbigbia","jjcjbjebieafdj","daeaciihgfcj","ghbheaghdd","gde","gigff","igddfjefbibb","eddfdbgacbidbb","deigiaajgg","eidjadcbihhebiee","ccbdiaga","ajeb","jadicdbbhjgbihab","cdgfbdjjhcfbbfg","ijgbgbjjceebgifbe","icjbhhe","achgfhhhgbagb","cgia","ggbhebigibcaeabegiia","ddbdbddb","ibfcefh","jiaabicecighhhghjcad","fbidd","eefabbbagbh","bcahhg","fgfajfibaji","jjefji","a","dfbgggg","c","iciajhcbbddgjiej","bdhjffcfhheccfa","adeaahfe","dhfbifj","cfe","fh","cejigibjefcd","bief","gaaadfajdefdicfgb","bfgcdhgaedaaeficcchj","hfcchcca","cbeedffaaia","e","bfcjjegic","aeibffhaejejfhfhi","jidcibgidfcbjfh","gibjgd","cbgdgijcah","jebicbdic","cbgeacjibgidfajig","iedaidgjjaffefb","ehjbedicggfjjd","bdfagbdf","gdiigehbdhabaadg","dafbh","ea","ace","cadabcih","idciabag","cbghh","febbbad","cdcaiidjbdga","jeahghciaiicd","gfifeiabhhdigh","ddjcgfg","cejfaffhdbgh","gd","edcgfjifjjcidje","gdeeabeeh","jgia","eegdefcacidbi","bcdhhcafacg","aiefhaghcbijgd","ghbegceidafcheajfi","eihea","jebigiiecajjddehea","eebaeg","jbddbb","jdjaeaici","fihcaahg","jdcf","faccigchibj","djbcfi","ehjdffcb","agcjaeebciaeacbbgfj","ijjhdbifcfeddfajf","ahfhd","fifidiajjeajbif","hehehfdhhbge","aii","bdicfcgecfe","aaiahdedajgiiaffeg","cffibb","bfibdjad","jhfhddgd","bfceijgbae","bahbbedcfiaga","ad","ccaiefeeabeafe","fgibhjeidcbijcjij","hggbai","aiibeegdjaffifgjj","bed","ecifejda","afabdhcejhj","bbfdjjbedihegjgccce","jbddfjhbdjab","gcee","ija","cjjcgiibdchjgbfb","jfiibachfjdjjfjahheg","jjhgdgha","cfhjefdbie","jfjdjjg","ahbgjcgjedcaeggicd","iajhd","ciadddibi","igdahbedfajafcc","aac","hfhhijbeacjibfbccgfh","daaei","ddbfifb","ichefdafgbjeffc","hjjbec","fggd","hbadedjaab","hjgdadfdccc","eagi","jhadibebjhedfjb","ajeejfaedh","fejdajbjjgjieccjcjhh","iadgfcfbdiafccchhfj","bcfaiiehfcihcfbgbg","ccjagcdjiaeeachh","gbhajbcjajchdibc","aheabh","fbcfcijeggejdcjaddh","fbbaiagecfjihaej","hi","gjiehb","figdce","ghiieciedec","hgeihiic","abbhafgjaijj","biifjgidccge","gi","aaihjajcfchjciif","ggeiajjediiiffdj","iiiaehjcjgehjefdbcb","fgeegeiaeifiegfc","afgjgahfghcfacfjfgdj","jjebaeccicjdbjb","adeejfbbgee","jdjdcje","jbjeigchgd","hbjf","icjgcbhhdaafbhf","cdfh","ie","igbjeejbdjehjh","acj","hebfaeaiiba","gfdaf","ffdgigd","hgjigaabihih","hgeaddei","jaaefhhbb","afbib","jhijcifccae","hafiehc","jhigiaahjh","hbgejdaabgaah","abfgdebbehhdji","eddacc","ibdfeebfdgjbhdc","fjchdefbhadcjdageg","agjddbcjebhgejhd","jdjjbfdeefjddiijie","efjiaijadbdd","biacbffggcijagahchhd","eieacgccebf","efhhh","aejadiahcgffebgeedhi","bbddeaahbaeia","edda","ibfejegidaa","diafdiaejj","cdj","cja","bcgcigajgj","bgbeaaigibfeji","egejhedgf","jijafheidieacj"]))

print("Time Cost: {} s".format(time.clock() - t0))


t0 = time.clock()
print(s.palindromePairs(["f","giihhaafhebggjgb","ddbij","fhdhfigjfbbefdc","cbbfdjgbdcffdfefbf","gegcdibdijfhhe","eaijgddhf","icijchjgffgbhdde","fbdghbcgahjeh","ebaecfgehabedec","fjdchbcfdedgb","eec","efcagidihhhb","abbgchijajdbidfiig","cba","fcgcjadidcdef","fjgchhjjcicdfih","bjeeiecihfha","bgde","cddgaghge","feacbh","bidcggcdajgefeehjg","gheachjddddhgbeg","jaddfhfc","debfbbici","jdaffgdegi","jegdaihhea","bbdhgbegbgdbda","acgdacjcjbhhae","fc","ihiefdadjdfjd","dchdfcadbegeiig","bfeffebadjchefjce","ejhiccefcceed","fgfga","gdeffdcehcgfdd","ghehedchdejgjjg","gbfeccbiidjgjfbibjd","a","bfahedcffjgghidbheej","jagfaegiigbjch","cgjecdac","fdecabedajieeadafdc","ebebcbf","aghacjce","gdiiggcfghabagef","beh","fgebdgefhedgfghhddj","ghfbhcccbggfbhcie","ecbebjeecajieb","ffjhcab","dfbchgbeafe","ecjbjedjddifijibee","cdddd","bjhhib","ebjbeheg","fdaaihejaaf","cgiiaefhahfjebcdicfa","dheibbefdcgfgdgac","bjcgebahfbhe","jhdidghajgcaae","icgddfgihedaa","biggeddigcgh","icjdd","ijieji","hfeegjdibcebagabe","cjdafhfgfejei","if","bcjjc","efchjjigcgjf","efejhdbie","igdaejfcbcacgheb","jffbejgghcehffegdc","jibedfbie","jah","ibiidfejdgdcj","iaeidag","ihihf","efcibiceag","gcieiigfdfdb","ajjjhfhf","cbfbabhgdb","gfgdb","hcdacdfabg","bigjbgifiaej","cigcd","ae","ge","aiihbafjecdea","beefbgiie","cgjgadiccedhc","cjdgcffbidfgeeafff","fhjgfffbba","bccach","eahfdaf","ahjdd","fihg","jbfjebg","cddahfafi","bbgbdaddhi","gdj","jeajeij","heghedag","jjchaicjjgfbg","abjgdiaejfbggi","acdchjidcjgbf","cejiijdjdhdfcee","jigaddhbgicdia","abc","agbjdbgjiehag","hfdigcigg","cgghefgejfhijdibdjg","hccieii","igcaddcchefdd","cgbbghdcihe","fecbhbibi","babjihei","i","d","jh","cifgachjchjbhaccc","bicbbbhhdbhiff","adedehahigage","ggchhigjicfieih","cdjjdcicfdgb","ideifebi","cfigg","cgeggchj","eefghjfgefhj","ddfdggagecjic","hjihgfaeii","ia","heidcecebahjbdfggdga","ecghbb","cejaeccaccdidia","gfehiajh","iffhjcgacb","jj","eaf","iajdhbaegee","aebhibdefdjg","iedhdj","hjjghaigbhabagag","gcgjabbhb","ceafidjdehiag","chadafai","hbedhgbhbjf","cjd","ffghjdedhcicibigi","egiegbjgfgafbfhjc","ihhdceihj","bejcfcchiifbe","fdgdibhfdjfbedhbe","faicaabjhdjhhhjijfc","hje","hiaijbcjidfcbfgcag","faeaifgei","dch","jgbffecigegeeadegj","aidgajdbdbaaa","gijf","ebedacfhedjedi","hbacgaahfdfjgi","fifgigbjgjgghhhd","j","ddjgbbiijjehchdbgbai","biga","bhfgcb","dhjadab","chdaiddifdffahcei","iafgaafifihabbgjj","cjegdheh","ehgdadgei","ehdfc","eacifidabdggjach","hhbhi","fcbbbbah","cegedidaigaci","cag","hegeiahfijhfciefd","dbab","gcgefhfjcgjhjecgddah","cdjgjjcjjicgbeih","ci","ijhjf","fbbgdeiageejdc","be","cjchgdgdgfagjjg","ibgeidbfa","fddggdhbddjaeddgdcfc","gcaggif","fjbgcgcgehbdbe","aicfjeichbeicfhecf","efie","hc","idfadbihjg","aaebdgc","fhjcgd","hhafdff","aabibgbfagajgjb","dghgcbggghgeaeg","fjgediahjigaa","fedgeeibjc","ejfejedc","bhaebiei","abgcbghfiedgehahcdci","bdhedihcbbffc","afhbdjjbd","fi","afdaicafe","jie","beagcaejegffega","aia","hi","jbighfjfcjahjgehe","bc","fadida","ighadgahjdghbb","bcifi","jiihgjheabbghfj","feejabbfgjgdcabdfbca","aedgdhcigb","ieaacbdebebh","dhhbbeeig","hieehbfibafgdhbg","fjfbegiaie","ccfaaigcaihejeijjaje","dadeacjcbfcfhhbij","eeecbheggdfjbecad","fjihfdgghjeae","hiffifdbj","ecidaedbfehehag","adegjjjc","cd","gf","ghfjagihccfcigige","bgf","chjgfeaieicigahh","cjiaddegfg","gdcgdij","dicehgcifif","fiidajechjiiijhbegbh","jefgfbhgdfciedagb","jjjgcbdjicabef","cdfid","edbfiicbefeajiic","ejbibi","cbhbihjeid","cabiiegaciib","gabbcdfijghgijicebj","jehfhhbfgegeg","jghffhffjf","dd","cjfaa","jifj","ibjiaihdcggcieaib","iifbiahhifgbacab","eebijggehcaijg","ejahjbhfchaa","ibibcfcbiec","dgdbgjcgcc","ageaibbdhjbfcbf","bhaedifejehbfibegeca","fejjhhcccccjeehgh","ahibaggjiacadbhefgec","ehigiijgd","ggbaabg","hh","heaajjgjggdigbb","aaejdigg","aiicbhfddcfjjbhhjjeh","ffaifijbhjbag","fahabbfdd","gbfhbhdfhhfjjcgaaj","abjfcge","adcfeecgbjhegi","chdddefcdf","bjhecbej","egib","da","jebagfj","behfe","higbgdiajeeehj","jib","idcghdbea","gdejgdcdihfbacaj","ajhiagcaahbfhadhib","ceejaidajdea","cde","bjfifjghfbc","eifiacecdci","jjafcaihfhej","afcaaibefidajhibag","dehd","hhiaifciaf","badjbageeeihbgcif","bcaeiidbijfhcid","abi","ah","ffefcc","fdieagiiajfafh","hcchdbihjdbec","ihidjiigibjf","edcdbcedacbjce","jbfdecgfbh","dacgadjgd","eejdhcfbdihbijcja","hbbj","gichdddfifgdaddajge","ffbcfbifeh","fjhaaidiifibhhejfidg","aeaehgfcbba","iihjefbjaifbda","adfiaaeajgic","jihdbcgbbiieigf","ecfiac","degf","idchfgeffdjiabgef","jb","eag","cgjadfejgjgc","iabghedbdheg","hiecdcegiecfjiedc","cigbaihic","jeechicij","edceggdjjeaa","ja","gdbdjeibhafgcfhgag","jeicf","jcgaadahjfbjihb","ghhiigfjaacii","ebiadgeh","ighd","jhaj","cfdiheagdihiicffbbh","jfdfc","jbedecaacicgd","fffcabach","e","ccebdc","jhgfghhjaijaabd","fdaidaeig","eeciegigac","hjjjaeiaaficijggdgh","c","babddddaeeffd","afdgbibgicccffgaee","hbhjbifbafhb","edcbhceeigd","hdgbheiadhcbfgj","dhidiiia","jjheg","ecjifcjdaacgdahcdid","ccjbdgbfhjiie","jajej","jjehhbedbfdi","ahffeh","gi","cjaghiejjhfdbgcijc","aibcfajefbihgde","ibjfiihieidfh","djceefcghhejjbd","djfdghagedbfhgid","dbh","hhfjcfghfcabidajaih","gj","eabaejcadggcgi","af","habi","idigfeaacffdhcfih","aaieehjfebihiaadfe","jjiadadfghgceicbbc","jej","fhecjeeibafgbac","icajjhihddfhehgcha","ihecchggh","jfichaagbicfhdcca","hgi","eeecaibagajdachadjcj","fda"]))
print("Time Cost: {} s".format(time.clock() - t0))
