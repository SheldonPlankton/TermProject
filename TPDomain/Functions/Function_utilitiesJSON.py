#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# 15-112: Fundamentals of Comp-Sci
# Template by Evan Tipping
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Name: Evan Tipping
# Andrew ID: eftippin
# Recitation: H

# Functions: JSON Utilities

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Description:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""
    This is a package of JSON related functions that this game needs for its
weapon template loading on start.
"""

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Imports:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import json
import os
from Classes.Items.Item_Wep import BaseWeapon

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Body:
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# This function grabs all of the information from a JSON file and turns
#it into a dictionary
def dataFromJson(name):
    with open(os.path.join('TPDomain', 'Assets', 'JSONTemplates',
                           name + '.json'), mode='r') as file:
        return json.load(file)

# This preloads a JSON so that an object that needs the data can have it
#instead of reading files on the fly
def preloadList(nameList):
    data = {}
    for name in nameList:
        data[name] = dataFromJson(name)
    return data

# This takes a JSON template and formats it to the weapon template
def createWepFromData(wepsDict, name):
    data = wepsDict[name]
    return BaseWeapon(data['name'],
                      data['uses'],
                      data['cool'],
                      data['spd'],
                      data['life'],
                      data['dmg'],
                      data['pRad'],
                      data['pCol'],
                      colorArg = data['color'],
                      imgArg = data['img'] if data['img'] != "" else None,
                      pImgArg = data['pImg'] if data['pImg'] != "" else None)
