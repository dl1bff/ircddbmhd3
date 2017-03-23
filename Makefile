# 
# 
# ircDDB-mheard
# 
# Copyright (C) 2017   Michael Dirska, DL1BFF (dl1bff@mdx.de)
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
# 



CFLAGS=-Wall

LDLIBS=-lpcap -lconfig

all: ircddbmhd3


ircddbmhd3.o: ircddbmhd_version.h

dstar_dv.o: dstar_dv.h golay23.h

golay23.o: golay23.h


ircddbmhd3: ircddbmhd3.o dstar_dv.o golay23.o


ircddbmhd_version.h:
	touch ircddbmhd_version.h



clean:
	rm -f *.o

distclean: clean
	rm -f ircddbmhd3 ircddbmhd_version.h


