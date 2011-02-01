# Copyright BlueDynamics Alliance - http://bluedynamics.com
# GNU General Public License Version 2

from zope.interface import (
    Interface,
    Attribute,
)
from node.interfaces import INode

class IXMINode(INode):
    """An XMI Node.
    
    An XMI Node only exist once and holds XML trees as children.
    
    This node contains one or more xml nodes, representing the entire xmi
    model, commonly one or more profiles and the model itself.
    """
    
    xmi = Attribute(u"The XMI flavour")
    
    def __init__(name, paths):
        """Create the XMI node.
        
        @param name: the name of the XMI node
        @param paths: contains a list of xml file names.
        """
    
    def reference(id):
        """Get XMLNode referenced by id or none if inexistent.
        
        Looks up reference in all contained XML trees.
        """
