class FileManipulator():
    def __init__(self,fileName):
        self.fileName=fileName
        try:
            self.arxeio= open(self.fileName, 'rb+')#raises error if file doesnt already exists 
        except:
            self.arxeio= open(self.fileName, 'wb+')#creates file 
    def run(self):
        pass

    def write(self,data):
        self.arxeio.write(data)

    def close(self):
        self.arxeio.close()
    def read(self):
        with self.arxeio as f:
            byte = f.read(1)
            while byte:
                print(int.from_bytes(byte,byteorder='big'))
                byte = f.read(1)


   

if __name__ == "__main__": 
    FileManipulator("TelemetryData.tlmdt").read()
    input('Press enter to terminate...')