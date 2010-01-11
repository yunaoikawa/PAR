#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Copyright (C) 2009, Zhang Initiative Research Unit,
Advance Science Institute, Riken
2-1 Hirosawa, Wako, Saitama 351-0198, Japan
If you use and like our software, please send us a postcard! ^^
---
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
---
"""

class MetaData:
    def __init___(self, fillename):
        self.name          = filename
        self.size          = None
        self.creation_time = None
        self.data          = []
        # maybe some day: user, group, perms (UGO or ACL)
        # get current date
        # try to:  get the file size
        #          create its chunks
        self.flag = False # set it if everything went alright

    def was_created_successfully(self):
        return self.flag == True

    # FBR: complete this when chunks are described
    #def list_chunks(self):
