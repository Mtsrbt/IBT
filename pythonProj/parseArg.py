#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

import sys
import ScanAutomat
import classes
import transcription
import translation
import re
import generator
import printer
import os.path

sequence_rcode = 0


def checkSequence(seq):
    """This function checks if input sequence code is in upper case or not.

    :param seq: Input sequence.
    :type seq: :class:`Sequence` object
    """
    if seq.code.isupper():
        return True
    else:
        return False


def checkfile(file):
    """This function checks syntax of FASTA format files.

    :param file: Input file in FASTA format.
    :type file: file
    """
    file_seqences = []
    sequence = ""
    comment = False
    s_sign = False
    n_count = 0
    filename, file_extension = os.path.splitext(file)
    if os.path.exists(file):
        if ((file_extension == ".fasta") or (file_extension == '.fa') or (file_extension == '.fna')):
            with open(file) as openfileobject:
                for line in openfileobject:
                    if len(line) < 80:
                        if re.search("^;.+", line) and not comment:
                            comment = True
                            continue
                        elif re.search("^>.+", line) and not s_sign:
                            n_count = 0
                            s_sign = True
                            continue
                        elif (line == "\n" and s_sign) and n_count == 0:
                            s_sign = False
                            comment = False
                            n_count += 1
                            if not sequence == "":
                                # sequence = sequence.strip("\n")
                                sequence = sequence.replace('\n', '')
                                file_seqences.append(sequence)
                            sequence = ""
                            continue
                        elif s_sign and comment and not (
                                re.search("[^ACUTG\n]+", line)):  # feed nucleoidov, todo pridat pole pre viac sequencii
                            # print(line, end="")
                            sequence += line
                            #comment = False
                            continue
                        elif s_sign and not comment and not (
                                re.search("[^ACUTG\n]+", line)):  # feed nucleoidov todo pridat pole pre viac sequencii
                            # print(line, end="")
                            sequence += line
                            #s_sign = False
                            continue
                        elif not line.strip():
                            s_sign = False
                            comment = False
                            if not sequence == "":
                                # sequence = sequence.strip("\n")
                                sequence = sequence.replace('\n', '')
                                file_seqences.append(sequence)
                            sequence = ""
                            continue
                        else:
                            return -1
        else:
            print("Input file is not supported. Supported file formats are: .fasta, .fa, .fna!")
            exit(-1)
    else:
        print("Input file does not exists!")
        exit(-1)
    if comment or s_sign:
        return -1
    if sequence != "":
        file_seqences.append(sequence)
    return file_seqences


def complementfunc(sequence):
    """This function creates complementary sequence to intup sequence

    :param sequence: Input sequence
    :type sequence: :class:`Sequence` object
    """
    complementary_seq = ""
    if sequence.type == 1:
        for i in sequence.code:
            if ord(i) == ord("A"):
                complementary_seq += "T"
            if ord(i) == ord("C"):
                complementary_seq += "G"
            if ord(i) == ord("G"):
                complementary_seq += "C"
            if ord(i) == ord("T"):
                complementary_seq += "A"

    if sequence.type == 2:
        for i in sequence.code:
            if ord(i) == ord("A"):
                complementary_seq += "U"
            if ord(i) == ord("C"):
                complementary_seq += "G"
            if ord(i) == ord("G"):
                complementary_seq += "C"
            if ord(i) == ord("U"):
                complementary_seq += "A"

    sequence.code = complementary_seq


def callfunctios(sequence, option, filecounter=None, complement=None, table=None):
    """This function calls function to process input sequences.

    :param sequence: Input sequence
    :type sequence: :class:`Sequence` object
    :param option: Print argument if subsequences should be printed.
    :type option: bool
    :param filecounter: Sequence order in file
    :type filecounter: Integer
    :param complement: Used to create complementary sequence from input sequence
    :type complement: bool
    :param table: Arguments of application
    :type table: bool
    """
    if not checkSequence(sequence):
        sequence.code = sequence.code.upper()
    sequence = ScanAutomat.seqScan(sequence)
    if 3 <= sequence.type <= 6:
        printer.printError(sequence.type)
        exit(-1)
    else:
        if complement is not None:
            complementfunc(sequence)
        sequence = transcription.seqtranscription(sequence)
        translation.seqtranslation(sequence)
        if sequence.type == -1:
            if filecounter is None:
                print("Sequence is missing stop codon and therefore cannot be translated!")
            else:
                print(f"Sequence {filecounter} is missing stop codon and therefore cannot be translated!")
        else:
            if table and (filecounter is None or filecounter == 1):
                printer.printTable()
            if option:
                printer.printresult(sequence, True)
            else:
                printer.printresult(sequence, False)


def parseArgs(argv):
    """This function parse arguments of application.

    :param argv: Arguments of application
    :type argv: list
    """
    argumentscount = len(sys.argv)
    if argumentscount == 2 and ((sys.argv[1] == '-h') or (sys.argv[1] == '-help')):
        printer.printHelp()
        exit(0)
    elif argumentscount == 2 and sys.argv[1] == '-s':
        sys.stderr.write("Wrong number of arguments. Missing input sequence!\n"
                         "Try argument -h to display help.\n")
        exit(-1)
    elif argumentscount == 2 and sys.argv[1] == '-f':
        sys.stderr.write("Wrong number of arguments. Missing input filename!\n"
                         "Try argument -h to display help.\n")
        exit(-1)
    elif argumentscount == 2 and sys.argv[1] == '-g':
        sys.stderr.write("Wrong number of arguments. To generate sequence you need ta add addition arguments!\n"
                         "Try argument -h to display help.\n")
        exit(-1)

    elif argumentscount == 3:
        if sys.argv[1] == '-s':
            sequence = classes.Sequence()
            sequence.code = sys.argv[2]
            callfunctios(sequence, False)
        elif sys.argv[1] == '-f':
            ret_val = checkfile(sys.argv[2])
            if ret_val == -1:
                printer.printError(7)
                exit(-1)
            else:
                counter = 0
                for seq in ret_val:
                    counter += 1
                    sequence = classes.Sequence()
                    sequence.code = seq
                    callfunctios(sequence, False, filecounter=counter)
        elif sys.argv[1] == '-g' and (sys.argv[2] == '-d' or sys.argv[2] == '-r'):
            sequence = classes.Sequence()
            sequence.code = generator.generate(sys.argv[2])
            callfunctios(sequence, False)
        else:
            sys.stderr.write("Wrong number of arguments.\n"
                             "Try argument -h to display help.\n")
            exit(-1)

    elif argumentscount == 4:
        if sys.argv[1] == '-s':
            if sys.argv[3] == '-c':
                sequence = classes.Sequence()
                sequence.code = sys.argv[2]
                callfunctios(sequence, False, complement=True)
            if sys.argv[3] == '-sub':
                sequence = classes.Sequence()
                sequence.code = sys.argv[2]
                callfunctios(sequence, True)
            if sys.argv[3] == '-t':
                sequence = classes.Sequence()
                sequence.code = sys.argv[2]
                callfunctios(sequence, False, table=True)
        elif sys.argv[1] == '-g':
            if sys.argv[2] == '-r' or sys.argv[2] == '-d':
                if sys.argv[3] == '-sub':
                    sequence = classes.Sequence()
                    sequence.code = generator.generate(sys.argv[2])
                    callfunctios(sequence, True)
                if sys.argv[3] == '-t':
                    sequence = classes.Sequence()
                    sequence.code = generator.generate(sys.argv[2])
                    callfunctios(sequence, False, table=True)
        elif sys.argv[1] == '-f':
            if sys.argv[3] == '-c' or sys.argv[3] == '-sub' or sys.argv[3] == '-t':
                ret_val = checkfile(sys.argv[2])
                if ret_val == -1:
                    printer.printError(7)
                    exit(-1)
                else:
                    counter = 0
                    for seq in ret_val:
                        counter += 1
                        sequence = classes.Sequence()
                        sequence.code = seq
                        if sys.argv[3] == '-c':
                            callfunctios(sequence, False, filecounter=counter, complement=True)
                        if sys.argv[3] == '-sub':
                            callfunctios(sequence, True, filecounter=counter)
                        if sys.argv[3] == '-t':
                            callfunctios(sequence, False, filecounter=counter, table=True)
        else:
            sys.stderr.write("Wrong number of arguments.\n"
                             "Try argument -h to display help.\n")
            exit(-1)
    elif argumentscount == 5:
        if sys.argv[1] == '-s' and ((sys.argv[3] == '-c' and sys.argv[4] == '-sub') or
                                    (sys.argv[3] == '-c' and sys.argv[4] == '-t') or
                                    (sys.argv[3] == '-sub' and sys.argv[4] == '-c') or
                                    (sys.argv[3] == '-sub' and sys.argv[4] == '-t') or
                                    (sys.argv[3] == '-t' and sys.argv[4] == '-sub') or
                                    (sys.argv[3] == '-t' and sys.argv[4] == '-c')):
            sequence = classes.Sequence()
            sequence.code = sys.argv[2]
            if sys.argv[3] == '-c' and sys.argv[4] == '-t' or sys.argv[3] == '-t' and sys.argv[4] == '-c':
                callfunctios(sequence, False, complement=True, table=True)
            if sys.argv[3] == '-sub' and sys.argv[4] == '-c' or sys.argv[3] == '-c' and sys.argv[4] == '-sub':
                callfunctios(sequence, True, complement=True)
            if sys.argv[3] == '-sub' and sys.argv[4] == '-t' or sys.argv[3] == '-t' and sys.argv[4] == '-sub':
                callfunctios(sequence, True, table=True)

        elif sys.argv[1] == '-g' and (sys.argv[2] == '-r' or sys.argv[2] == '-d') and \
                ((sys.argv[3] == '-sub' and sys.argv[4] == '-t') or (sys.argv[3] == '-t' and sys.argv[4] == '-sub')):
            sequence = classes.Sequence()
            sequence.code = generator.generate(sys.argv[2])
            callfunctios(sequence, True, table=True)

        elif sys.argv[1] == '-f':
            if (sys.argv[3] == '-c' and sys.argv[4] == '-sub') or \
                    sys.argv[3] == '-sub' and sys.argv[4] == '-c' or \
                    sys.argv[3] == '-sub' and sys.argv[4] == '-t' or \
                    sys.argv[3] == '-c' and sys.argv[4] == '-t' or \
                    sys.argv[3] == '-t' and sys.argv[4] == '-sub' or \
                    sys.argv[3] == '-t' and sys.argv[4] == '-c':
                ret_val = checkfile(sys.argv[2])
                if ret_val == -1:
                    printer.printError(7)
                    exit(-1)
                else:
                    counter = 0
                    for seq in ret_val:
                        counter += 1
                        sequence = classes.Sequence()
                        sequence.code = seq
                        if sys.argv[3] == '-c' and sys.argv[4] == '-t' or sys.argv[3] == '-t' and sys.argv[4] == '-c':
                            callfunctios(sequence, False, filecounter=counter, complement=True)
                        if sys.argv[3] == '-sub' and sys.argv[4] == '-t' or sys.argv[3] == '-t' and sys.argv[4] == '-sub':
                            callfunctios(sequence, True, filecounter=counter, table=True)
                        if sys.argv[3] == '-sub' and sys.argv[4] == '-c' or sys.argv[3] == '-c' and sys.argv[4] == '-sub':
                            callfunctios(sequence, True, filecounter=counter, complement=True)
            else:
                sys.stderr.write("Wrong number of arguments.\n"
                                 "Try argument -h to display help.\n")
                exit(-1)
        else:
            sys.stderr.write("Wrong number of arguments.\n"
                             "Try argument -h to display help.\n")
            exit(-1)
    elif argumentscount == 6:
        if ((sys.argv[3] == '-sub' and sys.argv[4] == '-c' and sys.argv[5] == '-t') or
                (sys.argv[3] == '-t' and sys.argv[4] == '-sub' and sys.argv[5] == '-c') or
                (sys.argv[3] == '-sub' and sys.argv[4] == '-t' and sys.argv[5] == '-c') or
                (sys.argv[3] == '-t' and sys.argv[4] == '-c' and sys.argv[5] == '-sub') or
                (sys.argv[3] == '-c' and sys.argv[4] == '-sub' and sys.argv[5] == '-t') or
                (sys.argv[3] == '-c' and sys.argv[4] == '-t' and sys.argv[5] == '-sub')):
            if sys.argv[1] == '-s':
                sequence = classes.Sequence()
                sequence.code = sys.argv[2]
                callfunctios(sequence, True, complement=True, table=True)
            if sys.argv[1] == '-f':
                ret_val = checkfile(sys.argv[2])
                if ret_val == -1:
                    printer.printError(7)
                    exit(-1)
                else:
                    counter = 0
                    for seq in ret_val:
                        counter += 1
                        sequence = classes.Sequence()
                        sequence.code = seq
                        callfunctios(sequence, True, filecounter=counter, complement=True, table=True)
        else:
            sys.stderr.write("Wrong number of arguments.\n"
                             "Try argument -h to display help.\n")
            exit(-1)
    else:
        sys.stderr.write("Wrong number of arguments.\n"
                         "Try argument -h to display help.\n")
        exit(-1)


'''
    if argumentscount == 4 and sys.argv[1] == '-s' and sys.argv[3] == '-k': #complemet
        sequence = classes.Sequence()
        sequence.code = sys.argv[2]
        callfunctios(sequence, False, complement=True)

    if argumentscount == 4 and sys.argv[1] == '-s' and sys.argv[3] == '-c':
        sequence = classes.Sequence()
        sequence.code = sys.argv[2]
        callfunctios(sequence, True)


    if argumentscount == 4 and sys.argv[1] == '-g' and (sys.argv[2] == '-d' or sys.argv[2] == '-r') and sys.argv[3] == '-c':
        sequence = classes.Sequence()
        sequence.code = generator.generate(sys.argv[2])
        callfunctios(sequence, True)
    if argumentscount == 4 and sys.argv[1] == '-f' and sys.argv[3] == '-c':   #file procesing  -c
        ret_val = checkfile(sys.argv[2])
        if ret_val == -1:
            printer.printError(7)
            exit(-1)
        else:
            counter = 0
            for seq in ret_val:
                counter += 1
                sequence = classes.Sequence()
                sequence.code = seq
                callfunctios(sequence, True, filecounter=counter)
'''
