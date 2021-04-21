#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

import classes


def removeUnused(seq):
    """This function removes parts of sequence that are not translated to proteins.

    :param seq: Input sequence.
    :type seq: :class:`Sequence` object
    """
    start_count = len(seq.start_kodon)
    stop_count = len(seq.stop_kodon)
    if 0 < start_count == stop_count and stop_count > 0:
        for (i, n) in zip(seq.start_kodon, seq.stop_kodon):
            seq.s_array.append(seq.transcription[(i - 1):(n - 1)])
    if start_count > 0 and stop_count == 0:
        seq.type = -1
        return seq
    if 0 < start_count > stop_count > 0:
        for (i, n) in zip(seq.start_kodon, seq.stop_kodon):
            seq.s_array.append(seq.transcription[(i - 1):(n - 1)])
    # print(seq.s_array)
    # if seq.start_kodon[0] > 0 :
    # n = seq.start_kodon[0] - 1
    # seq.code = seq.code[n:]
    return seq


def seqtranslation(seq):
    """This function acts as acts as AutomataM3 and translates sequence from transcription output.

    :param seq: Input sequence.
    :type seq: :class:`Sequence` object
    """
    automata = classes.AutomataM3()
    seq = removeUnused(seq)
    amino = ""
    for element in seq.s_array:
        if element == -1:
            continue
        for char in range(0, len(element), 3):
            amino = element[char:char + 3]
            if any(amino == i for i in ("UUU", "UUC")):
                automata.stack.push("Phe")
            elif any(amino == i for i in ("UUA", "UUG", "CUU", "CUC", "CUA", "CUG")):
                automata.stack.push("Leu")
            elif any(amino == i for i in ("AUU", "AUC", "AUA")):
                automata.stack.push("Ile")
            elif amino == "AUG":
                automata.stack.push("Met")
            elif any(amino == i for i in ("GUU", "GUC", "GUA", "GUG")):
                automata.stack.push("Val")
            elif any(amino == i for i in ("UCU", "UCC", "UCA", "UCG")):
                automata.stack.push("Ser")
            elif any(amino == i for i in ("CCU", "CCC", "CCA", "CCG")):
                automata.stack.push("Pro")
            elif any(amino == i for i in ("ACU", "ACC", "ACA", "ACG")):
                automata.stack.push("Thr")
            elif any(amino == i for i in ("GCU", "GCC", "GCA", "GCG")):
                automata.stack.push("Ala")
            elif any(amino == i for i in ("UAU", "UAC")):
                automata.stack.push("Tyr")
            elif any(amino == i for i in ("CAU", "CAC")):
                automata.stack.push("His")
            elif any(amino == i for i in ("CAA", "CAG")):
                automata.stack.push("Gln")
            elif any(amino == i for i in ("AAU", "AAC")):
                automata.stack.push("Ans")
            elif any(amino == i for i in ("AAA", "AAG")):
                automata.stack.push("Lys")
            elif any(amino == i for i in ("UGU", "UGC")):
                automata.stack.push("Cys")
            elif amino == "UGG":
                automata.stack.push("Trp")
            elif any(amino == i for i in ("CGU", "CGC", "CGA", "CGG", "AGA", "AGG")):
                automata.stack.push("Arg")
            elif any(amino == i for i in ("AGU", "AGC")):
                automata.stack.push("Ser")
            elif any(amino == i for i in ("GAG", "GAA")):
                automata.stack.push("Glu")
            elif any(amino == i for i in ("GAU", "GAC")):
                automata.stack.push("Asp")
            elif any(amino == i for i in ("GGU", "GGC", "GGA", "GGG")):
                automata.stack.push("Gly")
        seq.getSequence(automata.stack, 'amino')
