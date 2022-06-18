# -*- coding: utf-8 -*-
"""
Created on Sat Jun 18 17:33:37 2022

@author: kumar
"""


######## Linked List #####################################################

# Rerence:
# 1. Linked List Implementation copied from a post at https://www.tutorialspoint.com/python_data_structure/python_linked_lists.htm


class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None


class SLinkedList:
    """Singly Linked List"""

    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print(printval.dataval)
            printval = printval.nextval

    def AtBegining(self, newdata):
        """Insert node at the begining"""
        NewNode = Node(newdata)
        # Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

    def AtEnd(self, newdata):
        """Insert node at the end"""
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval = NewNode

    def Inbetween(self, middle_node, newdata):
        """Insert node at the inbetween"""
        if middle_node is None:
            print("The mentioned node is absent")
            return
        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

    def RemoveNode(self, Removekey):
        """remove a node"""
        HeadVal = self.headval

        if (HeadVal is not None):
            if (HeadVal.dataval == Removekey):
                self.headval = HeadVal.next
                HeadVal = None
                return
        while (HeadVal is not None):
            if HeadVal.dataval == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.nextval

        if (HeadVal == None):
            return

        prev.nextval = HeadVal.nextval
        HeadVal = None


if __name__ == "__main__":
    llist = SLinkedList()
    llist.AtBegining("Mon")
    llist.AtEnd("Tue")
    llist.AtBegining("Sun")
    llist.AtEnd("Wed")
    llist.listprint()
    llist.RemoveNode("Tue")
    print('after removing Tue')
    llist.listprint()
