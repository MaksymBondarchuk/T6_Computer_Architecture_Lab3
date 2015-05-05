__author__ = 'Maxim'

from dbxml import *


# try:
# container = mgr.createContainer("labs.dbxml")

# container = mgr.openContainer("labs.dbxml")

# document = container.putDocument('lab5', '<lab><name>Lab5</name><state>Not completed</state></lab>', uc)

# CREATE
def add():
    mgr = XmlManager()
    container = mgr.openContainer("labs.dbxml")
    uc = mgr.createUpdateContext()
    container.putDocument('Lab 3', '<lab><about>CRUD</about><state>We\'re working on</state></lab>', uc)


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
def update():
    mgr = XmlManager()
    uc = mgr.createUpdateContext()
    container = mgr.openContainer("labs.dbxml")

    qc = mgr.createQueryContext()
    # qc.setNamespace("labs2", "labs.dbxml")

    results = mgr.query("collection('labs.dbxml')//*[status='None']", qc)
    results.reset()
    for value in results:
        document = value.asDocument()
        print document.getName(), "=", value.asString()


# DELETE
def delete():
    import os
    mgr = XmlManager()
    container = mgr.openContainer("labs.dbxml")
    uc = mgr.createUpdateContext()

    # document = container.getDocument('lab1')
    # document.removeDocument()
    container.deleteDocument('Lab 1', uc)
    # mgr.removeContainer('Lab1', uc)


print('Before')
read()
add()
# delete()
print('\nAfter')
read()
# update()
