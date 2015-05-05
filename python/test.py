__author__ = 'Maxim'

from dbxml import *


# try:
# container = mgr.createContainer("labs.dbxml")

# container = mgr.openContainer("labs.dbxml")

# document = container.putDocument('lab5', '<lab><name>Lab5</name><state>Not completed</state></lab>', uc)

# CREATE
def add(name, about, status):
    mgr = XmlManager()
    container = mgr.openContainer("labs.dbxml")
    uc = mgr.createUpdateContext()
    try:
        container.putDocument(name, '<lab><about>%s</about><state>%s</state></lab>' % (about, status), uc)
    except:
        return 'already exist with this name'
    return 'OK'


# READ
def read():
    mgr = XmlManager()
    container = mgr.openContainer("labs.dbxml")
    qc = mgr.createQueryContext()
    results = mgr.query("collection('labs.dbxml')", qc)
    results.reset()
    for value in results:
        document = value.asDocument()
        print document.getName(), "=", value.asString()


# UPDATE
def update(name, field, new_value):
    mgr = XmlManager()
    uc = mgr.createUpdateContext()
    container = mgr.openContainer("labs.dbxml")

    document = container.getDocument(name)
    name = document.getName()
    content = document.getContent()

    if field == 'name':
        try:
            container.deleteDocument(name, uc)
            container.putDocument(new_value, content, uc)
        except:
            container.putDocument(name, content, uc)
            return 'already exist with this name'
        return 'OK'

    import xml.etree.ElementTree as ET
    tree = ET.fromstring(content)
    tree.find(field).text = new_value

    content_new = ET.tostring(tree, encoding="utf8", method="html")

    container.deleteDocument(name, uc)
    container.putDocument(name, content_new, uc)


# DELETE
def delete():
    mgr = XmlManager()
    container = mgr.openContainer("labs.dbxml")
    uc = mgr.createUpdateContext()

    # document = container.getDocument('lab1')
    # document.removeDocument()
    container.deleteDocument('Lab 1', uc)
    # mgr.removeContainer('Lab1', uc)


print('Before')
read()

print('\n' + add('Lab 2', 'Web workers', 'Completed'))
# delete()
# print('\n' + update('Lab 31', 'name', 'Lab 1'))

print('\nAfter')
read()

