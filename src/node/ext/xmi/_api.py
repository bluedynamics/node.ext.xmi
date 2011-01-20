# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

import os
from zipfile import ZipFile
from zope.interface import implements
from zope.interface import alsoProvides
from zope.interface import noLongerProvides
from zope.component import getUtility
from zodict.node import Node
from zodict.interfaces import ICallableNode
from zodict.interfaces import IRoot
from node.ext.xml.interfaces import IXMLFactory
from node.ext.xml.interfaces import IXMLNode
from interfaces import IXMINode
    
class XMINode(Node):
    implements(IXMINode, ICallableNode, IRoot)
    
    def __init__(self, name, paths):
        Node.__init__(self, name)
        self.xmi = None
        factory = getUtility(IXMLFactory)
        for path in paths:
            buf = self._extract_from_archive(path)
            # XXX: fix this id stuff in node.ext.xml
            if buf:
                xml = factory(path,
                              '{http://schema.omg.org/spec/XMI/2.1}id',
                              buf)
            else:
                xml = factory(path, '{http://schema.omg.org/spec/XMI/2.1}id')
            self[path] = xml
    
    def __setitem__(self, key, val):
        if not IXMLNode.providedBy(val) or not IRoot.providedBy(val):
            raise ValueError(u"Could only contain complete XML trees.")
        noLongerProvides(val, IRoot)
        Node.__setitem__(self, key, val)
    
    def reference(self, id):
        for tree in self.values():
            ref = tree.reference(id)
            if ref is not None:
                return ref
        return None
    
    def _extract_from_archive(self, path):
        """XXX: improve
        """
        ext = os.path.splitext(path)[1].lower()
        if ext in ('.zargo'):
            archive = ZipFile(path)
            xmi = [n for n in archive.namelist() \
                   if os.path.splitext(n)[1].lower() == '.xmi']
            assert(len(xmi) == 1)
            buf = archive.read(xmi[0])
            return buf
        return None