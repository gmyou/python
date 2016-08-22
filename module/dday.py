from datetime import datetime, timedelta
import sys, getopt

def dday(argv):
    now = datetime.now()

    try:
        opts, args = getopt.getopt(argv, "d:h:", ["days=", "hours="])
    except getopt.GetoptError:
        print "dday.py -d <days> -h <hours>"

    print now.ctime()
    _dday = now
    # print _dday
    for opt, arg in opts:
        # print opt, arg
        # pass

        if opt == '-d':
            _dday = _dday + timedelta(days=int(arg))
            print '+', arg, ' days '
        if opt == '-h':
            _dday = _dday + timedelta(hours=int(arg))
            print '+', arg, ' hours '

    print _dday.ctime()

# dday(1, 10)
#print sys.argv[2]
#dday(int(sys.argv[1]), int(sys.argv[2]))
if __name__ == "__main__":
    dday(sys.argv[1:])
