#!/usr/bin/python
# encoding: utf-8
import random

hiraganaDict = {
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

katakanaDict = { 
'a': u'ア',
'i': u'イ',
'u': u'ウ',
'e': u'エ',
'o': u'オ',
'ka': u'カ',
'ki': u'キ',
'ku': u'ク',
'ke': u'ケ',
'ko': u'コ',
'sa': u'サ',
'shi': u'シ',
'su': u'ス',
'se': u'セ',
'so': u'ソ',
'ta': u'タ',
'chi': u'チ',
'tsu': u'ツ',
'te': u'テ',
'to': u'ト',
'na': u'ナ',
'ni': u'ニ',
'nu': u'ヌ',
'ne': u'ネ',
'no': u'ノ',
'ha': u'ハ',
'hi': u'ヒ',
'fu': u'フ',
'he': u'ヘ',
'ho': u'ホ',
'ma': u'マ',
'mi': u'ミ',
'mu': u'ム',
'me': u'メ',
'mo': u'モ',
'ya': u'ヤ',
'yu': u'ユ',
'yo': u'ヨ',
'ra': u'ラ',
'ri': u'リ',
'ru': u'ル',
're': u'レ',
'ro': u'ロ',
'wa': u'ワ',
'wo': u'ヲ',
'n': u'ン',
}

import argparse

parser = argparse.ArgumentParser(description='Generate some characters.')
parser.add_argument('--hiragana', dest='hiragana', action='store_true', default=False)
parser.add_argument('--katakana', dest='katakana', action='store_true', default=False)
parser.add_argument('--romaji', dest='romaji', action='store_true', default=False)
parser.add_argument('-w','--words', dest='numWords', type=int, default=10)
parser.add_argument('-c','--characters', dest='charactersPerWord', type=int, default=3)

args = parser.parse_args()

if args.hiragana:
    japaneseDict = hiraganaDict
elif args.katakana:
    japaneseDict = katakanaDict
else:
    #Defaulting to hiragana
    japaneseDict = hiraganaDict
    
for j in range (0, args.numWords):
	print j,
	for i in range(0, args.charactersPerWord):
		item = random.choice(list(japaneseDict.keys()))		
		if args.romaji:
			print item,
		else:
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
