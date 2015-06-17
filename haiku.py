from spacy.en import English
from spacy.parts_of_speech import ADJ
from random import randint


def generate_haiku():
    # From http://www.101computing.net/haiku-generator-in-python/
    wordList1 = ["Enchanting", "Amazing", "Colourful", "Delightful", "Delicate"]
    wordList2 = ["visions", "distance", "conscience", "process", "chaos"]
    wordList3 = ["superstitious", "contrasting", "graceful", "inviting", "contradicting", "overwhelming"]
    wordList4 = ["true", "dark", "cold", "warm", "great"]
    wordList5 = ["scenery","season", "colours","lights","Spring","Winter","Summer","Autumn"]
    wordList6 = ["undeniable", "beautiful", "irreplaceable", "unbelievable", "irrevocable"]
    wordList7 = ["inspiration", "imagination", "wisdom", "thoughts"]
            
    wordIndex1=randint(0, len(wordList1)-1)
    wordIndex2=randint(0, len(wordList2)-1)
    wordIndex3=randint(0, len(wordList3)-1)
    wordIndex4=randint(0, len(wordList4)-1)
    wordIndex5=randint(0, len(wordList5)-1)
    wordIndex6=randint(0, len(wordList6)-1)
    wordIndex7=randint(0, len(wordList7)-1)

    haiku = wordList1[wordIndex1] + " " + wordList2[wordIndex2] + ",\n" 
    haiku = haiku + wordList3[wordIndex3] + " " + wordList4[wordIndex4] + " " + wordList5[wordIndex5]  + ",\n"
    haiku = haiku + wordList6[wordIndex6] + " " + wordList7[wordIndex7] + "."

    return unicode(haiku)



def bagifier():
    nlp = English()
    probs = [lex.prob for lex in nlp.vocab]
    probs.sort()
    is_adj = lambda tok: tok.pos == ADJ and tok.prob < probs[-1000]
    while 1:
        poem = generate_haiku()
        tokens = nlp(poem)
        adjs = []
        complete = []
        for tok in tokens:
            if is_adj(tok):
                adjs.append(tok.string)
                complete.append("baggy ")
            else:
                complete.append(tok.string)
        if not adjs:
            continue
        return ''.join(complete)

print bagifier()
