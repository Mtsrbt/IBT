#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

import classes


def seqtranscription(seq):
    """This function acts as acts as AutomataM2 and transcripts sequence from AutomataM1 output sequence.

    :param seq: Input sequence.
    :type seq: :class:`Sequence` object
    :return: seq
    :rtype: :class:`Sequence` object
    """
    START_STATE = 's'
    STATE_Q1 = 'q1'
    STATE_Q2 = 'q2'
    STATE_Q3 = 'q3'
    STATE_Q4 = 'q4'
    STATE_Q5 = 'q5'
    STATE_Q6 = 'q6'
    STATE_Q7 = 'q7'
    STATE_Q8 = 'q8'
    STATE_Q9 = 'q9'
    STATE_Q10 = 'q10'
    END_STATE = 'f'
    END_SYMBOL = '#'
    automata = classes.AutomataM2()
    #seq.code += END_SYMBOL
    automata.input = seq.code
    automata.input += END_SYMBOL
    automata.state = START_STATE


    ord_A = ord("A")
    ord_T = ord('T')
    ord_U = ord('U')
    ord_C = ord('C')
    ord_G = ord('G')
    ord_hash = ord('#')
    automata.stack.push("S")
    automata.top = "S"
    counter = 0

    for i in automata.input:
        char = ord(i)
        stack_top = automata.top
        if char == ord_hash:
            automata.state = END_STATE
            automata.stack.push(i)
            automata.top = i
            continue

        # state S
        if automata.state == START_STATE and char == ord_A and stack_top == "S":
            automata.state = STATE_Q1
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_T and stack_top == "S":
            automata.state = STATE_Q2
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_U and stack_top == "S":
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_C and stack_top == "S":
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_G and stack_top == "S":
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        # -----------------------------------------------------------------------------------

        if automata.state == START_STATE and char == ord_A:
            automata.state = STATE_Q1
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_T:
            automata.state = STATE_Q2
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_U:
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_C:
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == START_STATE and char == ord_G:
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q1
        if automata.state == STATE_Q1 and char == ord_A and stack_top == "A":
            automata.state = STATE_Q3
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q1 and char == ord_T and stack_top == "A":
            automata.state = STATE_Q4
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q1 and char == ord_U and stack_top == "A":
            automata.state = STATE_Q4
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q1 and char == ord_C and stack_top == "A":
            automata.state = STATE_Q3
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q1 and char == ord_G and stack_top == "A":
            automata.state = STATE_Q3
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q2
        if automata.state == STATE_Q2 and char == ord_A:
            automata.state = STATE_Q3
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q2 and char == ord_T:
            automata.state = STATE_Q3
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q2 and char == ord_U:
            automata.state = STATE_Q3
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q2 and char == ord_C:
            automata.state = STATE_Q3
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q2 and char == ord_G:
            automata.state = STATE_Q3
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q3
        if automata.state == STATE_Q3 and char == ord_A:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q3 and char == ord_T:
            automata.state = START_STATE
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q3 and char == ord_U:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q3 and char == ord_C:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q3 and char == ord_G:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q4
        if automata.state == STATE_Q4 and char == ord_G and stack_top == "U":
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            seq.start_kodon.append(counter - 2)
            continue
        if automata.state == STATE_Q4 and char == ord_G and stack_top == "T":
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            seq.start_kodon.append(counter - 2)
            continue
        if automata.state == STATE_Q4 and char == ord_A:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q4 and char == ord_C:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q4 and char == ord_T:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q4 and char == ord_U:
            automata.state = START_STATE
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue


        # state Q5
        if automata.state == STATE_Q5 and char == ord_A:
            automata.state = STATE_Q7
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q5 and char == ord_T:
            automata.state = STATE_Q6
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q5 and char == ord_U:
            automata.state = STATE_Q6
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q5 and char == ord_C:
            automata.state = STATE_Q7
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q5 and char == ord_G:
            automata.state = STATE_Q7
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q6          #check error
        if automata.state == STATE_Q6 and char == ord_A and stack_top == "U":
            automata.state = STATE_Q8
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q6 and char == ord_T and stack_top == "U":
            automata.state = STATE_Q9
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q6 and char == ord_U and stack_top == "U":
            automata.state = STATE_Q9
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q6 and char == ord_C and stack_top == "U":
            automata.state = STATE_Q9
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q6 and char == ord_G and stack_top == "U":
            automata.state = STATE_Q8
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q7
        if automata.state == STATE_Q7 and char == ord_A:
            automata.state = STATE_Q9
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q7 and char == ord_T:
            automata.state = STATE_Q9
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q7 and char == ord_U:
            automata.state = STATE_Q9
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q7 and char == ord_C:
            automata.state = STATE_Q9
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q7 and char == ord_G:
            automata.state = STATE_Q9
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q8
        if automata.state == STATE_Q8 and char == ord_A and stack_top == "A":
            automata.state = STATE_Q10
            automata.stack.push(i)
            automata.top = i
            counter += 1
            seq.stop_kodon.append(counter - 2)
            continue
        if automata.state == STATE_Q8 and char == ord_G and stack_top == "A":
            automata.state = STATE_Q10
            automata.stack.push(i)
            automata.top = i
            counter += 1
            seq.stop_kodon.append(counter - 2)
            continue
        if automata.state == STATE_Q8 and char == ord_T and stack_top == "A":
            automata.state = STATE_Q5
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q8 and char == ord_U and stack_top == "A":
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q8 and char == ord_C and stack_top == "A":
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q8 and char == ord_A and stack_top == "G":
            automata.state = STATE_Q10
            automata.stack.push(i)
            automata.top = i
            counter += 1
            seq.stop_kodon.append(counter - 2)
            continue
        if automata.state == STATE_Q8 and char == ord_T and stack_top == "G":
            automata.state = STATE_Q5
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q8 and char == ord_U and stack_top == "G":
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q8 and char == ord_C and stack_top == "G":
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q8 and char == ord_G and stack_top == "G":
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        # state f
        if automata.state == STATE_Q10 and char == ord_A:
            automata.state = STATE_Q1
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q10 and char == ord_T:
            automata.state = STATE_Q2
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q10 and char == ord_U:
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q10 and char == ord_C:
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q10 and char == ord_G:
            automata.state = STATE_Q2
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue

        # state Q9
        if automata.state == STATE_Q9 and char == ord_A:
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q9 and char == ord_T:
            automata.state = STATE_Q5
            automata.stack.push("U")
            automata.top = "U"
            counter += 1
            continue
        if automata.state == STATE_Q9 and char == ord_U:
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q9 and char == ord_C:
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
        if automata.state == STATE_Q9 and char == ord_G:
            automata.state = STATE_Q5
            automata.stack.push(i)
            automata.top = i
            counter += 1
            continue
    #if seq.type == 1:
    classes.Sequence.getSequence(seq, automata.stack, 'transcription')
    return seq

