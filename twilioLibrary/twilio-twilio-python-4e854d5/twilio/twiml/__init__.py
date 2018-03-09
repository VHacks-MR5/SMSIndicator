# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

import json
import re
import xml.etree.ElementTree as ET


def lower_camel(string):
    if not string or '_' not in string:
        return string

    result = "".join([x.title() for x in string.split('_')])
    return result[0].lower() + result[1:]


def format_language(language):
    """
    Attempt to format language parameter as 'ww-WW'.

    :param string language: language parameter
    """
    if not language:
        return language

    if not re.match('^[a-zA-Z]{2}[_-][a-zA-Z]{2}$', language):
        raise TwiMLException('Invalid value for language parameter.')

    return language[0:2].lower() + '-' + language[3:5].upper()


class TwiMLException(Exception):
    pass


class TwiML(object):
    MAP = {
        'from_': 'from'
    }

    def __init__(self, **kwargs):
        self.name = self.__class__.__name__
        self.value = None
        self.verbs = []
        self.attrs = {}

        for k, v in kwargs.items():
            if v is not None:
                self.attrs[lower_camel(self.MAP.get(k, k))] = v

    def __str__(self):
        return self.to_xml()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        return False

    def to_xml(self, xml_declaration=True):
        """
        Return the contents of this verb as an XML string

        :param bool xml_declaration: Include the XML declaration. Defaults to True
        """
        xml = ET.tostring(self.xml()).decode('utf-8')
        return '<?xml version="1.0" encoding="UTF-8"?>{}'.format(xml) if xml_declaration else xml

    def append(self, verb):
        """
        Add a TwiML doc

        :param verb: TwiML Document

        :returns: self
        """
        if not isinstance(verb, TwiML):
            raise TwiMLException('Only appending of TwiML is allowed')

        self.verbs.append(verb)
        return self

    def nest(self, verb):
        """
        Add a TwiML doc. Unlike `append()`, this returns the created verb.

        :param verb: TwiML Document

        :returns: the TwiML verb
        """
        if not isinstance(verb, TwiML):
            raise TwiMLException('Only nesting of TwiML is allowed')

        self.verbs.append(verb)
        return verb

    def xml(self):
        el = ET.Element(self.name)

        keys = self.attrs.keys()
        keys = sorted(keys)
        for a in keys:
            value = self.attrs[a]

            if isinstance(value, bool):
                el.set(a, str(value).lower())
            else:
                el.set(a, str(value))

        if self.value:
            if isinstance(self.value, dict):
                self.value = json.dumps(self.value)

            el.text = self.value

        for verb in self.verbs:
            el.append(verb.xml())

        return el
