import math
text = """C UYGHARMZ IUWMPRWIR GAIR YVRMP
MBHMZWMPUM C VMMXWPE YV PYR VCZ
ZMGYQMD VZYG CXCZG YP CPCXKTWPE CPD MBHXYZM
RNM VXYYD YV CDQCPUMD OPYSXMDEM SNWUN MCUN
KMCZ LZWPEI SWRN WR
"""
f = [0]*26
s = 0
for i in text:
    if i!=" "and i!='\n':
        s +=1
        f[ord(i)-ord('A')]+=1

for i in range(26):
    print(chr(ord('A')+i)+':',end = ' ')
    print(f[i])
    print(math.floor(f[i]/s*10000)/100)
    