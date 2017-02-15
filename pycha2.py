inputt = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
alfabet = "abcdefghijklmnopqrstuvwxyz"
alfabetlist = list(alfabet)
inputlist = list(inputt)
result = []


for i in range(len(inputlist)):
	if inputlist[i]==' ':
		result.append(' ')
	else:
		for n in range(len(alfabetlist)):
			try:
				if inputlist[i] == alfabetlist[n]:
					result.extend(alfabetlist[n+2])
			except IndexError:
				result.extend(alfabetlist[n-len(alfabetlist)+2])

print("".join(result))
