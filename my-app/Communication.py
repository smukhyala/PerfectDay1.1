from __future__ import print_function, unicode_literals, absolute_import
from threading import *
import subprocess
import json
import tempfile
import os
from os.path import exists

#flet imports
import flet as ft

class Editor(ft.UserControl):

    def build(self):
        Container = ft.Container()

        #set items
        self.fieldCol = ft.Column(scroll = 'auto', height = 400, controls = [])

        return Container