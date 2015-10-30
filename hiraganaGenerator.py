#!/usr/bin/python
# encoding: utf-8
import random

japaneseDict = {
'a': u'あ',
'i': u'い',
'u': u'う',
'e': u'え',
'o': u'お',
'ka': u'か',
'ki': u'き',
'ku': u'く',
'ke': u'け',
'ko': u'こ',
'sa': u'さ',
'shi': u'し',
'su': u'す',
'se': u'せ',
'so': u'そ',
'ta': u'た',
'chi': u'ち',
'tsu': u'つ',
'te': u'て',
'to': u'と',
'na': u'な',
'ni': u'に',
'nu': u'ぬ',
'ne': u'ね',
'no': u'の',
'ha': u'は',
'hi': u'ひ',
'fu': u'ふ',
'he': u'へ',
'ho': u'ほ',
'ma': u'ま',
'mi': u'み',
'mu': u'む',
'me': u'め',
'mo': u'も',
'ya': u'や',
'yu': u'ゆ',
'yo': u'よ',
'ra': u'ら',
'ri': u'り',
'ru': u'る',
're': u'れ',
'ro': u'ろ',
'wa': u'わ',
'wo': u'を',
'n': u'ん',
}

lengthOfOutput = 3
numberOfDesiredSamples = 10

printRomanji = False
printHiragana = True

for j in range (0, numberOfDesiredSamples):
	print j,
	for i in range(0, lengthOfOutput):
		item = random.choice(list(japaneseDict.keys()))		
		if printRomanji:
			print item,
		if printHiragana:
			print japaneseDict[item],
	print 



# inShuffle = True
# outShuffle = True
# if inShuffle:
# 	random.shuffle(allHiragana)

# for word1 in allHiragana:
# 	for word2 in allHiragana:
# 		if (word2 is word1):
# 			continue
# 		for word3 in allHiragana:
# 			if (word3 is word2) or (word3 is word1):
# 				continue
# 			outputList.append(word1+word2+word3)


# if outShuffle:
# 	random.shuffle(outputList)

# for word in outputList:
# 	print word
	#pass

#print len(outputList)
#print len(allHiragana)**3
# 9 words and 7 words = 16
# 16^3 if we allow dups
# 16 pick 3
#wow... two lessons is already 3360 words.
#wtf? how did i get hekekota and kekonte in here? thats 4 characters..
# missed a , between 'ke' and 'ko so they became 'keko'
