#!/usr/bin/env python3
"""Module for updating topics of a school document"""

def update_topics(mongo_collection, name, topics):
    """
    Changes all topics of a school document based on the name

    Parameters:
    mongo_collection: a pymongo collection object
    name: (string) the school name to update
    topics: (list of strings) the list of topics approached in the school

    Returns:
    None
    """
    mongo_collection.update_many(
        {"name": name},
        {"$set": {"topics": topics}}
    )
