import json


class Mars(object):
    def __init__(self, input_file, output_file):
        '''Initialize the class with necessary files'''
        self.input_file = input_file
        self.output_file = output_file

    def send(self, dict1):
        '''Takes an argument of type dict. Returns 1 on success'''
        try:
            if type(dict1) != dict:
                raise Exception
        except Exception:
            print "Unknown Exception in send"
            return None
        with open(self.output_file, 'w') as jsonfile:
                json.dump(dict1, jsonfile)
                return 1

    def receive(self):
        '''Returns json object as dictionary on success'''
        try:
            with open(self.input_file, 'r') as jsonfile:
                data = json.load(jsonfile)
        except:
            print "couldnt decode"
        try:
            if type(data) != dict:
                raise Exception
            else:
                return data
        except:
            print 'Not dictionary'


if __name__ == '__main__':
    infile = raw_input("Enter input file name ")
    outfile = raw_input("Enter output file name ")
    mars = Mars(infile, outfile)
    print '--> Executing receive() with input file as %s' % infile
    data = mars.receive()
    print '--> Received json object as %s' % data
    print '--> Executing send() with json object as argument'
    status = mars.send(data)
    if status == 1:
        print 'Succesfull'
    else:
        print 'Unsuccesful'
