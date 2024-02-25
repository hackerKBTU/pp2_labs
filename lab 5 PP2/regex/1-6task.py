#1task
import re
pattern1 = re.compile(r"ab*")
print(pattern1.search("abdjla abdhla"))

pattern2 = re.compile(r"ab{2,3}")
print(pattern2.search("dkeodkeokeabbbllprlpabbbbbbb"))

pattern3 = re.compile(r"[a-z]+\_")
print(pattern3.findall("jodjoedjo_ ekdpe48_ kdoedkeoL_ oibai_"))

pattern4 = re.compile(r"[A-Z]{1}+[a-z]+")
print(pattern4.findall("Messi are Is The Best worst"))

pattern5 = re.compile(r"a.+b\Z")
print(pattern5.search("dkrodkrajfrb ldprldpr phphphAkcofb"))


pattern6 = re.compile(r"[ ,.]")
print(pattern6.sub(":", "okdoekdoem,edkoek.d,eo oed.,"))



