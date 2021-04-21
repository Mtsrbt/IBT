#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

import classes


def seqScan(seq):
    """This function acts as AutomataM1 and scans input sequence.

    :param seq: Input sequence.
    :type seq: :class:`Sequence` object
    :return: Sequence with discovered type. Those can be:
        DNA_OK, mRNA_OK, DNA_NOK, mRNA_NOK, SEQUENCE_ERR
    :rtype: :class:`Sequence` object
    """
    DNA_OK = 1
    mRNA_OK = 2
    DNA_NOK = 3
    mRNA_NOK = 4
    INPUT_ERR = 5
    SEQUENCE_ERR = 6
    START_STATE = 's'
    STATE_U = 'u'
    STATE_T = 't'
    END_STATE = 'f'
    END_SYMBOL = '#'
    automata = classes.AutomataM1()
    seq.code = seq.code.strip('\n')
    size = len(seq.code)
    if (size % 3) != 0:
        seq.type = SEQUENCE_ERR
        return seq
    #seq.code += END_SYMBOL
    automata.input = seq.code
    automata.input += END_SYMBOL
    automata.state = START_STATE
    ord_A = ord('A')
    ord_T = ord('T')
    ord_U = ord('U')
    ord_C = ord('C')
    ord_G = ord('G')
    ord_hash = ord('#')

    for i in automata.input:
        char = ord(i)
        if automata.state == START_STATE and char == ord_hash:
            seq.type = INPUT_ERR
            return seq
        if (automata.state == STATE_T or automata.state == STATE_U) and char == ord_hash:
            if automata.state == STATE_T:
                seq.type = DNA_OK
            if automata.state == STATE_U:
                seq.type = mRNA_OK
            automata.state = END_STATE
            return seq

        if automata.state == START_STATE:
            if char == ord_A:
                continue
            elif char == ord_C:
                continue
            elif char == ord_T:
                automata.state = STATE_T
                continue
            elif char == ord_U:
                automata.state = STATE_U
                continue
            elif char == ord_G:
                continue
            else:
                automata.state = END_STATE
                seq.type = INPUT_ERR
                return seq

        if automata.state == STATE_T:
            if char == ord_A:
                continue
            elif char == ord_C:
                continue
            elif char == ord_T:
                continue
            elif char == ord_U:
                automata.state = END_STATE
                seq.type = DNA_NOK
                return seq
            elif char == ord_G:
                continue
            else:
                automata.state = END_STATE
                seq.type = INPUT_ERR
                return seq

        if automata.state == STATE_U:
            if char == ord_A:
                continue
            elif char == ord_C:
                continue
            elif char == ord_T:
                automata.state = END_STATE
                seq.type = mRNA_NOK
                return seq
            elif char == ord_U:
                continue
            elif char == ord_G:
                continue
            else:
                automata.state = END_STATE
                seq.type = INPUT_ERR
                return seq

    return seq
