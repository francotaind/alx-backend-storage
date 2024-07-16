#!/usr/bin/env python3
"""Module for inserting a new document in a MongoDB collection"""

def insert_school(mongo_collection, **kwargs):
    """
    Insert a new document in a collection based on kwargs

    Parameters:
    mongo_collection: a pymongo collection object
    **kwargs: keyword arguments representing the document to insert

    Returns:
    The new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
