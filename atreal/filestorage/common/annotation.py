#!/usr/bin/env python

from zope.interface import implements

from zope.annotation.interfaces import IAnnotations
from BTrees.OOBTree import OOBTree

from atreal.filestorage.common.interfaces import IAnnotFileStore

from atreal.filestorage.common.registry import storage_classes
from atreal.filestorage.common.zodbstore import ZodbStore


class _Marker(object): pass

class AnnotFileStore(object):
    
    implements(IAnnotFileStore)
    
    key = "atreal.filestorage.common.AnnotFileStore"
    
    #default factory
    factory = ZodbStore
    
    def __init__(self, original):
        self.original = original
        annotations = IAnnotations(original)
        if annotations.get(self.key, _Marker) is _Marker:
            annotations[self.key] = OOBTree()
        self.btree = annotations[self.key]
    
    def __setitem__(self, name):
        raise Exception("Disallowed")
    
    def __getitem__(self, name):
        return self.btree[name]
    
    def __delitem__(self, name):
        del self.btree[key]
    
    def keys(self):
        return self.btree.keys()
    
    def has_key(self, key):
        return self.btree.has_key(key)
    
    def __contains__(self, name):
        return name in self.btree
    
    def getOrCreate(self, name):
        if not name in self.btree:
            filestore = self.factory(name, self.original)
            self.btree[name] = filestore
        else:
            filestore = self.btree[name]
        return filestore

    def remove(self, name):
        del self.btree[name]


