import os

class drivelist():
    
    def ls(self):
        drive = ["A:", "B:", "C:", "D:", "E:", "F:" ,"G:", "H:", "I:", "J:", "K:", "L:", "M:", "N", "O:", "P:", "Q:", "R:", "S:", "T:", "U:", "V:", "W:", "X:", "Y:", "Z:"]

        founddrives = []

        for x in drive:
            if os.path.exists(x):
                founddrives.append(x)
        
        
        return founddrives