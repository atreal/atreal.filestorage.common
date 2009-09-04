#!/usr/bin/env python

from zope.interface import Interface

class IAnnotFileStore(Interface):
    """
    """
    
class IOfsFile(Interface):
    """
    """

class IOmniFile(Interface):
    """
    """
    
    def setContenType(value):
        """
        """
    
    def getContentType():
        """
        """
    
    def open():
        """
        """

class IArFileData(Interface):
    
    def read(size):
        """
        """
    
    def write(buffer):
        """
        """
    
    def seek(pos, rel):
        """
        """
    
    def tell():
        """
        """
    
    