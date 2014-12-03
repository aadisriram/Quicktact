#!/usr/bin/python2.7
#
# Copyright 2013 Google Inc. All Rights Reserved.

__author__ = 'sharmanitin@google.com (Nitin Sharma)'

from google.appengine.ext import db


class user(db.Model):
    """Models for the Sweeps class."""
    uid = db.StringProperty()
    info = db.StringListProperty()
    contacts = db.StringListProperty()
    connections = db.StringListProperty()
    preferences = db.StringListProperty()
    groups = db.StringListProperty()
