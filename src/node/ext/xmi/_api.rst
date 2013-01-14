XMI IO
======

Import and instanciate XMINode::

    >>> import os
    >>> from node.ext.xmi import XMINode
    >>> paths = [
    ...     os.path.sep.join([datadir, 'examplegg.uml']),
    ...     os.path.sep.join([datadir, 'pyegg.profile.uml']),
    ... ]
    >>> xmi = XMINode('simplepyegg', paths)
    >>> xmi
    <XMINode object 'simplepyegg' at ...>

Now 2 XML nodes are contained in the XMI node::

    >>> xmi.keys()
    ['.../data/examplegg.uml', '.../data/pyegg.profile.uml']

    >>> xmi.values()
    [<XMLNode object '.../data/examplegg.uml' at ...>, 
    <XMLNode object '.../data/pyegg.profile.uml' at ...>]

We expect the the xml node to return a reference node of any tree of it. Take a
look at the test data for more details::

    <pyegg:pyegg
      xmi:id="_DqB9UMQgEd62q_MLW0kltQ"
      base_Package="_LS6T4MQYEd62q_MLW0kltQ"
    />

    >>> stereotype = xmi.reference('_DqB9UMQgEd62q_MLW0kltQ')
    >>> stereotype
    <XMLNode object '...pyegg' at ...>

    >>> referencedpackage = xmi.reference(stereotype.attributes['base_Package'])
    >>> referencedpackage
    <XMLNode object '...packagedElement' at ...>
