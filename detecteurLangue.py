#!/usr/bin/python/
# -*- coding:utf-8 -*-

import codecs, unicodedata, os, requests, re
from collections import defaultdict
from bs4 import BeautifulSoup 

#--------------FONCTIONS-OUVERTURE-FICHIER-------------------

def ouvrirFichier(fichier):
    texte = codecs.open(fichier, "r", "utf-8").read()
    return texte

#--------------ENDfonctions-ouverture-fichier-------------------


#--------------DECLARATIONS-------------------

#les fichiers de ressource de langue sont tirés de wikipédia, les langues ont été choisies en fonction de la quantité d'articles écris en cette langue sur wikipédia (+ de 60 000 articles)
nomLangues = {
	"ar": u"Arabe", 
	"az": u"Azéri", 
	"be": u"Biélorusse", 
	"bg": u"Bulgare",
	"br": u"Breton", 
	"ca": u"Catalan", 
	"ce": u"Tchétchène", 
	"ceb": u"Cebuano", 
	"cs": u"Tchèque",
	"cy": u"Gallois", 
	"da": u"Danois", 
	"de": u"Allemand", 
	"dv": u"Maldivien",
	"en": u"Anglais", 
	"el": u"Grec", 
	"eo": u"Esperanto", 
	"es": u"Espagnol", 
	"et": u"Estonien", 
	"eu": u"Basque", 
	"fa": u"Persan", 
	"fi": u"Finnois", 
	"fr": u"Français", 
	"gl": u"Galicien", 
	"hi": u"Hindi", 
	"hu": u"Hongrois", 
	"hr": u"Croate", 
	"hy": u"Arménien", 
	"it": u"Italien", 
	"ja": u"Japonais", 
	"ka": u"Géorgien", 
	"kk": u"Kazakh", 
	"ko": u"Coréen", 
	"la": u"Latin", 
	"lt": u"Lituanien", 
	"mg": u"Malgache", 
	"min": u"Minangkabau", 
	"mk": u"Macédonien", 
	"ms": u"Malaisien", 
	"new": u"Newar", 
	"nl": u"Néerlandais", 
	"nn": u"Norvégien", 
	"no": u"Norvégien", 
	"oc": u"Occitan", 
	"pms": u"Piémontais", 
	"pl": u"Polonais",
	"pt": u"Portugais", 
	"ro": u"Roumain", 
	"ru": u"Russe", 
	"sh": u"Serbo-croate", 
	"sk": u"Slovaque", 
	"sl": u"Slovène", 
	"sr": u"Serbe", 
	"sv": u"Suédois", 
	"ta": u"Tamoul", 
	"te": u"Télougou", 
	"th": u"Thaï", 
	"tl": u"Tagalog", 
	"tr": u"Turc", 
	"tt": u"Tatar", 
	"uk": u"Ucrainien", 
	"ur": u"Urdu", 
	"uz": u"Ouzbek", 
	"vi": u"Vietnamien", 
	"vo": u"Volapük", 
	"war": u"Waray-waray", 
	"zh": u"Chinois", 
	"zh-min-nan": u"Minnan"
	}

catalogueAlphabets = {
	"BENGALI":"bn", 
	"GEORGIAN":"ka", 
	"GREEK":"el", 
	"GUJARATI":"gu", 
	"HANGUL":"ko", 
	"HIRAGANA":"ja", 
	"KATAKANA":"ja", 
	"TAMIL":"ta", 
	"THAI":"th", 
	"THAANA":"dv"
	}

#--------------ENDdeclarations-------------------


#--------------FONCTIONS-ALPHABET-------------------

def systemeEcriture(texte):
	"""
	la fonction systemeEcriture prend un texte en entrée et retourne le système d'écriture 
	le plus couramment rencontré parmi les lettres présentes dans le texte
	"""
	dicoCatFreq = defaultdict(int)
	for car in texte:
		if car.isalpha():
			typeCaractere = unicodedata.name(car).split()[0]
			dicoCatFreq[typeCaractere] += 1
	freqMax = max(dicoCatFreq, key=dicoCatFreq.get)
	return freqMax

#--------------ENDfonctions-alphabet-------------------


#--------------FONCTIONS-TOKENS-------------------

def tokeniseur(texteASegmenter):
	"""
	la fonction tokeniseur segmente une txt en un dictionnaire de ses mots, 
	si ceux-ci sont segmentables par les moyens traditionnels, aucune 
	exception n'est prise en compte
	"""	
	texteASegmenter = re.sub('\d+', '', texteASegmenter)
	texteDejaSegmenteMot = re.findall(r"[\w']+", texteASegmenter)
	return texteDejaSegmenteMot

def intersectionListeDeStrings(texteIntersection1, texteIntersection2):
	"""
	la fonction intersectionListeDeStrings return une liste avec 
	l'intersection (les éléments communs) aux deux listes
	"""
	intersection = []
	texteIntersection1 = tokeniseur(texteIntersection1)
	texteIntersection2 = tokeniseur(texteIntersection2)
	for elementDeListe in texteIntersection1:
		if elementDeListe in texteIntersection2:
			intersection.append(elementDeListe)
	return intersection

def identifieurDeLangueDeMots(texteAnaliser):
    """
    la fonction identifieurDeLangueDeMots return la langue avec les plus 
    d'occurences du txt
    """
    dicoOccurenceMotsParLangue = {}
    for codeL in nomLangues:
    	MotsTexteRessource = ouvrirFichier("ressource/"+codeL+".txt")
    	dicoOccurenceMotsParLangue[codeL] = len(intersectionListeDeStrings(texteAnaliser, MotsTexteRessource))
    dicoOccurenceMotsParLangueOrdonne = sorted(dicoOccurenceMotsParLangue, key=dicoOccurenceMotsParLangue.get)
    return dicoOccurenceMotsParLangueOrdonne[-1]

#--------------ENDfonctions-tokens-------------------


#--------------FONCTIONS-DISTANCE-------------------

def compaDico3(dicoRessource, dicoTexteAnaliser):
    """
    comparer toutes les lettres qui apparaissent dans l'un ou l'autre dico
    """
    distance = 0
    for cle in dicoRessource:
        distance += abs(dicoRessource[cle] - dicoTexteAnaliser.get(cle, 0))
    for cle in dicoTexteAnaliser:
        if cle not in dicoRessource:
            distance += dicoTexteAnaliser[cle]
    return distance


#--------------ENDfonctions-distance-------------------


#--------------FONCTIONS-NGRAM-------------------

def ngrammes(texte, Ngram=2):
    """
    la fonction ngrammes prend un texte t comme entrée et retourne les bigrammes de ce texte
    """
    listeNgram = []
    for indexNgram in range(2, Ngram, 1):
        for indexTexte in range(len(texte) - 1):
            listeNgram += [texte[indexTexte:indexTexte + indexNgram]]
    return listeNgram

def textefreq(texte):
    """
    la fonction textefreq prend un texte comme entrée et retourne un dictionnaire 
    avec les fréquences relatives de chaque caractère
    """
    dicoFreq = {}
    for car in texte:
        dicoFreq[car] = dicoFreq.get(car, 0) + 1.0 / len(texte)
    return dicoFreq

def compaTextes(texte, n):
    """
    la fonction compaTextes prend deux textes et une valeur de n-gramme en argument et
    calcule la fréquence des n-grammes dans les deux textes et elle retourne la distance
    provenant de la comparaison symmétrique entre les deux dictionnaires ainsi obtenus
    """
    compteRenduDistances = {}
    dicoforcompa = textefreq(ngrammes(texte, n))
    for codeL in nomLangues:
        dicoComparaison = textefreq(ngrammes(ouvrirFichier("ressource/" + codeL + ".txt"), n))
        distanceNgram = compaDico3(dicoforcompa, dicoComparaison)
        compteRenduDistances[codeL] = distanceNgram
    compteRenduDistancesOrdonne = min(compteRenduDistances, key=compteRenduDistances.get)
    return compteRenduDistancesOrdonne


#--------------ENDfonctions-ngram-------------------


#--------------FONCTIONS-URL-------------------

def deURLATexte(url):
	"""
	la fonction deURLATexte aspire le texte d'une page web
	"""
	contenuURL = requests.get(url.encode("UTF8"))
	texteURL = contenuURL.text
	soup = BeautifulSoup(texteURL)
	return (str(soup)).decode("UTF8")

#--------------ENDfonctions-url-------------------


#--------------FONCTIONS-RESULTATS-------------------

def langue(texte, Ngram=4):
    """
	la fonction langue prend un txt en parametre, il execute les fonctions precedentes et 
	return le nom de la langue du txt ecrit en tt lettres, en se basant sur la liste des 
	noms de langue; on peut spécifier le n dans n-gram pour obtenir bigramme, trigramme, 
	quadrigramme, etc ou on peut le laisser vide et par défaut il retournera les 4-grams
    """
    freqMax = systemeEcriture(texte)
    if freqMax in catalogueAlphabets:
        output = nomLangues[catalogueAlphabets[freqMax]]
    elif len(texte) < 160:
    	resultat = identifieurDeLangueDeMots(texte)
    	output = nomLangues[resultat]
    else:
        resultat = compaTextes(texte, Ngram)
        output = nomLangues[resultat]
    return output
	
#--------------ENDfonctions-resultats-------------------