#!/usr/bin/env python
#
#       signal.py
#       
#       Copyright 2010 Euripedes Rocha Filho <rocha.euripedes@gmail.com>
#       
#       This program is free software; you can redistribute it and/or modify
#       it under the terms of the GNU General Public License as published by
#       the Free Software Foundation; either version 2 of the License, or
#       (at your option) any later version.
#       
#       This program is distributed in the hope that it will be useful,
#       but WITHOUT ANY WARRANTY; without even the implied warranty of
#       MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#       GNU General Public License for more details.
#       
#       You should have received a copy of the GNU General Public License
#       along with this program; if not, write to the Free Software
#       Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#       MA 02110-1301, USA.
import numpy as np
class Signal:
	""" 
		Class designed to show all necessary information in a signal analysis
	"""
	def __init__(self,input_signal=None):
		self.signal = np.array(input_signal)
	pass

def main():
	simbolo = Signal([1,2])
	print simbolo
	return 0

if __name__ == '__main__': main()
