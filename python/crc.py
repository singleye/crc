# MIT License
# 
# Copyright (c) 2017 singleye
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class CRC8(object):
    def __init__(self, polynomial=0x31, init_sum=0xFF):
        self.__polynomial = polynomial
        self.__sum = init_sum
        self.__table = []
        self.__update_table()

    def __crc_byte(self, byte):
        val = byte
        for i in range(0, 8):
            if val & 0x80:
                val <<= 1
                val ^= self.__polynomial
            else:
                val <<= 1
            val &= 0xFF
        return val

    def __update_table(self):
        self.__table = []
        for i in range(0, 256):
            self.__table.append(self.__crc_byte(i))

    def table(self):
        if not self.__table:
            return
        for i in range(0, 256):
            if i>0 and i%16==0:
                print ""
            print "0x%02x" % self.__table[i],
        print ""

    def update(self, data):
        """
        Input:
          * data: the data to be crc. For example: b'\x01\x02'
        """
        for byte in data:
            #self.__sum = self.__crc_byte(self.__sum ^ ord(byte))
            self.__sum = self.__table[self.__sum ^ ord(byte)]

    def digest(self):
        return chr(self.__sum)

    def hexdigest(self):
        return "%02x" % self.__sum
