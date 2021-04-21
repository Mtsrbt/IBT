#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

import random


def generate(option): #todo option DNA / RNA
    """This function generates sequence to be translated.

    :param option: Represents type of sequence generated. (DNA or mRNA).
    :type option: String
    :return: String of generated code sequence.
    :rtype: String
    """
    amino = ["UUU", "UUC", "UUG", "CUU", "CUC", "CUA", "CUG", "AUU", "AUC", "AUA", "GUU", "GUC", "AUG",
             "GUA", "GUG", "UCU", "UCC", "UCA", "UCG", "CCU", "CCC", "CCA", "CCG", "ACU", "ACC", "ACA",
             "ACG", "GCU", "GCC", "GCA", "GCG", "UAU", "UAC", "CAU", "CAC", "CAA", "CAG", "AAU", "AAC",
             "AAA", "AAG", "UGU", "UGC",  "UGG", "CGU", "CGC", "CGA", "CGG", "AGA", "AGG", "AGU", "AGC",
             "GAU", "GAC", "GGU", "GGC", "GGA", "GGG", "UUA", "GAA", "GAG"]
    stop_c = ["UGA", "UAA", "UAG"]
    length = random.randint(2, 40)  #max length of sequencein codons
    count_limit = length // 2  #number of sequences
    res = []  #array for lengths of subseqences
    count = 0
    if count_limit == 1:
        count = random.randint(1, count_limit)
    else:
        count = random.randint(1, count_limit // 2)
    avail_len = length - (2 * count)
    for i in range(count):
        if avail_len > 1:
            generated = random.randrange(1, avail_len, 1)
            res.append(generated)
        elif avail_len == 1:
            generated = 1
            res.append(generated)
        else:
            generated = 0
            res.append(generated)
        avail_len -= generated
    a_string = ""
    a_array = []
    for x in range(count):
        a_string += "AUG"
        times_x = res[x]
        for y in range(times_x):
            a_string += amino[random.randint(0, 60)]
        a_string += stop_c[random.randint(0, 2)]
        a_array.append(a_string)
        a_string = ""
    if avail_len > 0:
        for i in range(avail_len):
            if (avail_len % 2) == 0:
                a_string = amino[random.randint(0, 60)] + a_string
            else:
                a_string += amino[random.randint(0, 60)]

    for x in a_array:
        a_string += x
    if option == '-d':
        a_string = a_string.replace("U", "T")
    return a_string



