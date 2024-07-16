#!/usr/bin/env python3
"""task 8 module"""

def list_all(mongo_collection):
    """
    List all documents in a collection

    Parameters:
    mongo_collection: a pymongo collection object
    return: a list of documents, or empty list if no documents are found
    """
    return [doc for doc in mongo_collection.find()]
