#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

import sys


def printTable():
    """This function prints table of genetic code.
    """
    print('+------------------------------------------------------------------------------+\n'
          '|                            Table of genetic code                             |\n'
          '+-----------------------+----------------+------------------+------------------+\n'
          '| TTT - Phenylalanine   | TCT - Serine   | TAT - Tyrosine   | TGT - Cysteine   |\n'
          '| TTC   (Phe)           | TCC   (Ser)    | TAC   (Tyr)      | TGC   (Cys)      |\n'
          '+-----------------------+ TCA            +------------------+------------------+\n'
          '| TTA - Leucine         | TCG            | TAA - STOP CODON | TGA - STOP CODON |\n'
          '| TTG   (Leu)           +----------------+ TAG              |------------------+\n'
          '| CTT                   | CCT - Proline  |------------------| TGG - Tryptophan |\n'
          '| CTC                   | CCC   (Pro)    | CAT - Histidine  |       (Try)      |\n'
          '| CTA                   | CCA            | CAC   (His)      |------------------|\n' 
          '| CTG                   | CCG            |------------------| CGT - Arginine   |\n' 
          '+-----------------------+----------------+ CAA - Glutamine  | CGC   (Arg)      |\n'
          '| ATT - Isoleucine      | ACT - Threonine| CAG   (Gln)      | CGA              |\n'
          '| ATC   (Ile)           | ACC   (Thr)    +------------------+ CGG              |\n'
          '| ATA                   | ACA            | AAT - Asparagine |------------------+\n'
          '+-----------------------+ ACG            | AAC   (Asn)      | AGT - Serine     |\n'
          '| ATG - Methionine (Met)|----------------+------------------+ AGC   (Ser)      |\n'
          '|-----------------------+ GCT - Alanine  | AAA - Lysine     |------------------+\n'
          '| GTT - Valine          | GCC   (Ala)    | AAG   (Lys)      | AGA - Arginine   |\n'
          '| GTC   (Val)           | GCA            +------------------+ AGG   (Arg)      |\n'
          '| GTA                   | GCG            | GAT - Aspartic   |------------------+\n' 
          '| GTG                   |----------------| GAC   acid (Asp) | GGT - Glycine    |\n'
          '+-----------------------+                |------------------| GGC   (Gly)      |\n'
          '+ The bases: adenine (A), cytosine (C),  | GAA - Glutamic   | GGA              |\n'
          '+            guanine (G), thymine (T)    | GAG   acid (Glu) | GGG              |\n'
          '+-----------------------+----------------+------------------+------------------+')


def printHelp():
    """This function prints manual of how to use application.
    """
    print("Usage:\n"
          "    ./app.py [Key Parameters] [Optional]\n"
          "Following table contains posslible parameters:\n"
          "+------------------------------------------------------------------------------+\n"
          "|  Key Parameter  |                          Description                       |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|  -h  or -help   | This pamateter displays manual how to run this application.|\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|  -s [sequence]  | This parameter needs aditional input [sequence] which      |\n"
          "|                 | is to be transformed. Sequence can be both upper and lower |\n"
          "|                 | case and can only contain characters:                      |\n"
          "|                 |    - A,C,G,T,U                                             |\n"
          "|                 | Example of use: ./app.py -s AUGCCAUAA                      |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|  -f [filename]  | This parameter needs additional file name along with       |\n"
          "|                 | its path. File can olny be in FESTA format with sufixes:   |\n"
          "|                 |   .fasta, .fna, .fa                                        |\n"
          "|                 | Example of use:                                            |\n"
          "|                 |   ./app.py -f /root/directory/subdirectory/filename.fna    |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|      -g -d      | This parameter is used to generate as input DNA sequence.  |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|      -g -r      | This parameter is used to generate as input mRNA sequence. |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|     Optional    |                          Description                       |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|       -t        | This pamateter displays table of genetic code and can be   |\n"
          "|                 | used with all parameters except for parameter -h.          |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|      -sub       | This parameter displays start and stop positons            |\n"
          "|                 | of subseqences and can be used with all parameters         |\n"
          "|                 | except for parameter -h.                                   |\n"
          "+-----------------+------------------------------------------------------------+\n"
          "|       -c        | Using this parameter, input sequence will be transformed   |\n"
          "|                 | into complementary sequence. This parameter can be         |\n"
          "|                 | used with all except for parameter -h, -g.                 |\n"
          "+-----------------+------------------------------------------------------------+\n")

def printError(err_num):
    """This function prints error messages on the screen.

    :param err_num: Code of error occurred.
    :type err_num: Integer
    """
    if err_num == 3:
        print("Error in input DNA sequence! Cannot contain both uracil and thymine\n")
    if err_num == 4:
        print("Error in input mRNA sequence! Cannot contain both uracil and thymine\n")
    if err_num == 5:
        print("Error in input sequence! Cannot contain characters other than A,C,G,T,U.\n")
    if err_num == 6:
        print("Error in input sequence! Contains wrong number of nucleotides.\n")
    if err_num == 7:
        print("Error input file format!\n")


def printresult(seq, subsequence):
    """This function prints results of code transformation on the screen.

    :param seq: Input sequence.
    :type seq: :class:`Sequence` object
    :param subsequence: If true, prints subsequences and their [start, stop] position.
    :type subsequence: bool
    """
    s_lengh = len(seq.code)
    for i in range(80):
        sys.stdout.write("-")
    if seq.type == 1:
        if s_lengh > 47:  #24+5 koniec +4
            count = s_lengh // 47
            tmp_string = seq.code[0:47]
            sys.stdout.write("\n|   Input DNA sequence:     " + tmp_string + "    |")
            position = 47
            for i in range(count):
                if (s_lengh - position) < 47 and (s_lengh - position) != 0:
                    tmp_string = seq.code[position:(position+47)]
                    sys.stdout.write("\n|                           " + tmp_string)
                    for i in range(51 - (s_lengh - position)):
                        sys.stdout.write(" ")
                    sys.stdout.write("|\n")
                    continue
                if (s_lengh - position) != 0:
                    tmp_string = seq.code[position:(position+47)]
                    sys.stdout.write("\n|                           " + tmp_string + "    |")
                    position += 47
                else:
                    if not subsequence:
                        sys.stdout.write("\n")

            for i in range(80):
                sys.stdout.write("-")
        else:
            sys.stdout.write("\n|   Input DNA sequence:     " + seq.code)
            for i in range(51 - s_lengh):
                sys.stdout.write(" ")
            sys.stdout.write("|\n")
            for i in range(80):
                sys.stdout.write("-")

    if seq.type == 2:
        if s_lengh > 47: #25 +5 +3
            count = s_lengh // 47
            tmp_string = seq.code[0:47]
            sys.stdout.write("\n|   Input mRNA sequence:    " + tmp_string + "    |")
            position = 47
            for i in range(count):
                if (s_lengh - position) < 47 and (s_lengh - position) != 0:
                    tmp_string = seq.code[position:(position+47)]
                    sys.stdout.write("\n|                           " + tmp_string)
                    for i in range(51 - (s_lengh - position)):
                        sys.stdout.write(" ")
                    if not subsequence:
                        sys.stdout.write("|\n")
                    else:
                        sys.stdout.write("|")
                    continue
                if (s_lengh - position) != 0:
                    tmp_string = seq.code[position:(position+47)]
                    sys.stdout.write("\n|                           " + tmp_string + "    |")
                    position += 47
                else:
                    if not subsequence:
                        sys.stdout.write("\n")
            if not subsequence:
                for i in range(80):
                    sys.stdout.write("-")
        else:
            sys.stdout.write("\n|   Input mRNA sequence:    " + seq.code)
            for i in range(51 - s_lengh):
                sys.stdout.write(" ")
            if not subsequence:
                sys.stdout.write("|\n")
                for i in range(80):
                    sys.stdout.write("-")
            else:
                sys.stdout.write("|")


    t_lengh = len(seq.transcription)
    #-----------------------transcription
    if seq.type == 1:
        if t_lengh > 47:  # 26 +5
            count = t_lengh // 47
            tmp_string = seq.transcription[0:47]
            sys.stdout.write("\n|   Transcription result:   " + tmp_string + "    |")
            position = 47
            for i in range(count):
                if (t_lengh - position) < 47 and (t_lengh - position) != 0:
                    tmp_string = seq.transcription[position:(position+47)]
                    sys.stdout.write("\n|                           " + tmp_string)
                    for i in range(51 - (t_lengh - position)):
                        sys.stdout.write(" ")
                    if not subsequence:
                        sys.stdout.write("|\n")
                    else:
                        sys.stdout.write("|")
                    continue
                if (t_lengh - position) != 0:
                    tmp_string = seq.transcription[position:(position+47)]
                    sys.stdout.write("\n|                           " + tmp_string + "    |")
                    position += 47
                else:
                    if not subsequence:
                        sys.stdout.write("\n")
            if not subsequence:
                for i in range(80):
                    sys.stdout.write("-")
        else:
            sys.stdout.write("\n|   Transcription result:   " + seq.transcription)
            for i in range(51 - t_lengh):
                sys.stdout.write(" ")
            if not subsequence:
                sys.stdout.write("|\n")
                for i in range(80):
                    sys.stdout.write("-")
            else:
                sys.stdout.write("|")

    #----------------------------------------------------------------------------
    if subsequence:
        sub_order = 0
        sys.stdout.write("\n")
        for i in range(80):
            sys.stdout.write("-")
        for str_a in seq.s_array:
            str_len = len(str_a)
            if str_len > 47:  # long seq   17+3+1+1 +3 +3 = 28 +5
                count = str_len // 47
                tmp_string = str_a[0:47]
                if seq.start_kodon[sub_order] < 10 and 10 > seq.stop_kodon[sub_order]:  # <0-9, 0-9>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:     " + tmp_string + "    |")
                if seq.start_kodon[sub_order] < 10 and (100 > seq.stop_kodon[sub_order] > 9):  #<0-9, 10-99>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:    " + tmp_string + "    |")
                if seq.start_kodon[sub_order] < 10 and (seq.stop_kodon[sub_order] > 100):  #<0-9, 100+>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:   " + tmp_string + "    |")
                if (10 <= seq.start_kodon[sub_order] < 100) and (100 > seq.stop_kodon[sub_order] >= 10):  #<10-99, 10-99>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:   " + tmp_string + "    |")
                if (10 <= seq.start_kodon[sub_order] < 100) and seq.stop_kodon[sub_order] >= 100:  #<10-99, 100+>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:  " + tmp_string + "    |")
                if seq.start_kodon[sub_order] >= 100 <= seq.stop_kodon[sub_order]:  #<100+, 100+>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]: " + tmp_string + "    |")
                position = 47
                for i in range(count):
                    if (str_len - position) >= 47:
                        tmp_string = str_a[position:(position+47)]
                        sys.stdout.write("\n|                           " + tmp_string)
                        for i in range(80 - len(tmp_string) - 29):
                            sys.stdout.write(" ")
                        sys.stdout.write("|")
                        position += 47
                        continue
                    else:
                        if (str_len - position) == 0:
                            continue
                        tmp_string = str_a[position:(position+(str_len - position))]
                        sys.stdout.write("\n|                           " + tmp_string)
                        for i in range(80 - len(tmp_string) - 29):
                            sys.stdout.write(" ")
                        sys.stdout.write("|")
                        continue
            else:
                if seq.start_kodon[sub_order] < 10 and 10 > seq.stop_kodon[sub_order]:  # <0-9, 0-9>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:     " + str_a)
                if seq.start_kodon[sub_order] < 10 and (100 > seq.stop_kodon[sub_order] > 9):  #<0-9, 10-99>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:    " + str_a)
                if seq.start_kodon[sub_order] < 10 and (seq.stop_kodon[sub_order] > 100):  #<0-9, 100+>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:   " + str_a)
                if (10 <= seq.start_kodon[sub_order] < 100) and (100 > seq.stop_kodon[sub_order] >= 10):  #<10-99, 10-99>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:   " + str_a)
                if (10 <= seq.start_kodon[sub_order] < 100) and seq.stop_kodon[sub_order] >= 100:  #<10-99, 100+>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]:  " + str_a)
                if seq.start_kodon[sub_order] >= 100 <= seq.stop_kodon[sub_order]:  #<100+, 100+>
                    sys.stdout.write(f"\n|   Subsequence [{seq.start_kodon[sub_order]}, {seq.stop_kodon[sub_order]}]: " + str_a)
                for i in range(80 - str_len - 29):
                    sys.stdout.write(" ")
                sys.stdout.write("|")
            sub_order += 1
        sys.stdout.write("\n")
        for i in range(80):
            sys.stdout.write("-")
    #-----------------------------------
    seq_in_order = 1
    sys.stdout.write("\n|   Translation result: ")
    for i in range(55):
        sys.stdout.write(" ")
    sys.stdout.write("|")
    for str in seq.amino:
        str_len = len(str)
        if str_len > 57:  # 23
            count = str_len // 57
            tmp_string = str[0:57]
            if seq_in_order > 9:
                sys.stdout.write(f"\n|   Protein {seq_in_order} : " + tmp_string + "     |")
            else:
                sys.stdout.write(f"\n|   Protein  {seq_in_order} : " + tmp_string + "     |")
            position = 57
            for i in range(count):
                if (str_len - position) >= 57:
                    tmp_string = str[position:(position+57)]
                    sys.stdout.write("\n|                " + tmp_string)
                    for i in range(80 - len(tmp_string) - 18):
                        sys.stdout.write(" ")
                    sys.stdout.write("|")
                    position += 57
                    continue
                else:
                    if (str_len - position) == 0:
                        continue
                    tmp_string = str[position:(position+(str_len - position))]
                    sys.stdout.write("\n|                " + tmp_string)
                    for i in range(80 - len(tmp_string) - 18):
                        sys.stdout.write(" ")
                    sys.stdout.write("|")
                #tmp_string = str[position:(position+57)]
                #sys.stdout.write("|                " + tmp_string + "    |")
                #position += 57
        else:
            if seq_in_order > 9:
                sys.stdout.write(f"\n|   Protein {seq_in_order} : " + str)
            else:
                sys.stdout.write(f"\n|   Protein  {seq_in_order} : " + str)
            #sys.stdout.write(f"\n|   Protein  {seq_in_order} : " + str)
            for i in range(80 - str_len - 18):
                sys.stdout.write(" ")
            sys.stdout.write("|")
        #sys.stdout.write(f"\n|   Protein  {seq_in_order} :" + str)
        seq_in_order += 1
    sys.stdout.write("\n")
    for i in range(80):
        sys.stdout.write("-")
    sys.stdout.write("\n")
    #print(seq.transcription)
