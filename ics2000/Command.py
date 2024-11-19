from ics2000.Cryptographer import encrypt
from ics2000.Bytes import np, insertbytes, insertint16, insertint32


class Command:

    def __init__(self):
        self._header = bytearray(43)
        self._data = bytearray()
        self.setframe(1)

    def setframe(self, num):
        if 0 <= num <= 255:
            self._header[0] = np.uint8(num)

    def settype(self, num):
        if 0 <= num <= 255:
            self._header[2] = np.uint8(num)

    def setmac(self, mac: str):
        arr = bytes.fromhex(mac.replace(":", ""))
        if len(arr) == 6:
            insertbytes(self._header, arr, 3)

    def setmagic(self):
        num = 653213
        insertint32(self._header, num, 9)

    def setentityid(self, entityid):
        insertint32(self._header, entityid, 29)

    def setdata(self, data, aes):
        self._data = encrypt(data, aes)
        insertint16(self._header, len(self._data), 41)

    def getcommand(self) -> str:
        """ Return hex string for header and data combined """
        return self._header.hex() + self._data.hex()

    def getcommandbytes(self) -> bytearray:
        """ Return bytearray for header and data combined """
        return self._header + self._data
