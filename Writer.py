from threading import Thread


class Write(Thread):
    def writefile(self, filename, data):
        f = open(filename,'a')
        for d in data:
            f.write(d)
        f.close()