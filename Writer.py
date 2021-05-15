from threading import Thread


class Write(Thread):
    def writefile(self, filename, data):
        print(len(data))
        f = open(filename,'a')
        for d in data:
            print(d)
            f.write(d)
        f.close()