#!/usr/bin/env python3

# **********************************************************************************
# Title:      Code Analysis and Transformation Based on Regulated Grammars
# Author:     Matúš Arbet
# Supervisor: Meduna Alexander, prof. RNDr., CSc., UIFS FIT VUT
# **********************************************************************************

class Stack:
    """This class represents stack and its methodes.
    """
    def __init__(self):
        """Constructor method
        """
        self.items = []

    def isEmpty(self):
        """Returns empty stack.
        """
        return self.items == []

    def push(self, item):
        """Pushes item onto stack.
        """
        self.items.append(item)

    def pop(self):
        """Pops item from stack.
        """
        return self.items.pop()

    def size(self):
        """Returns stack size.
        """
        return len(self.items)

    def top(self):
        """Returns item from top of the stack.
        """
        return self.items[len(self.items)-1]


class Sequence:
    """This is a conceptual class representation of input genetic code sequence.

    :param code: Input sequence
    :type code: string
    :param start_kodon: List of starting translation positions
    :type start_kodon: list
    :param stop_kodon: List of stop translation positions
    :type stop_kodon: list
    :param type: Type of input sequence.
    :type type: integer
    :param transcription: Transcribed sequence
    :type transcription: string
    :param s_array: List of sequences that are translatable from input sequence code.
    :type s_array:  list
    :param amino: List of amino acides.
    :type amino: list

    """
    code = ""
    start_kodon = []
    stop_kodon = []
    type = 0
    transcription = ""
    s_array = []
    amino = []

    def getSequence(self, stack, destination):
        """This method obtains sequence from stack.

            :param stack: Input stack.
            :type seq: :class:`Stack` object.
            :param destination: Storage of extracted sequence.
            :type destination: string
        """
        s_str = ''
        while not stack.isEmpty():
            poped = stack.pop()
            if poped != '#' and poped != 'S':
                s_str = poped + s_str
        if destination == 'transcription':
            self.transcription = s_str
        if destination == 'amino':
            self.amino.append(s_str)


class AutomataM1:
    """Class representing AutomataM1 used in first phase of scanning sequence.
    """
    input = ""
    state = ""


class AutomataM2(Stack):
    """Class representing AutomataM2 used in transcription sequence phase.
    """
    input = ""
    state = ""
    stack = Stack()
    top = ""


class AutomataM3(Stack):
    """Class representing AutomataM3 used in translation sequence phase.
    """
    input = ""
    stack = Stack()
    top = ""
