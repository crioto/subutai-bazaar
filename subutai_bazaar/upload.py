import cdn
import optparse
import sys
import os.path

def delete_previous(c, filename):
    no_such_file = False
    while no_such_file == False:
        try:
            result = c.Info(filename)
            if result != None:
                rc = c.Delete(result["id"])
                if rc == True:
                    print("File deleted")
                else:
                    print("File delete failed")
            else:
                no_such_file = True
        except Exception as e:
            print("Error occured during delete: " + str(e))
            sys.exit(2)


if __name__ == '__main__':
    parser = optparse.OptionParser()
    parser.add_option('-t', '--host', action='store', dest='host',
                      help='hostname of the CDN', default='bazaar.subutai.io')
    parser.add_option('-f', '--file', action='store', dest='srcfile',
                      help='file to upload', default='')
    parser.add_option('-u', '--user', action='store', dest='gpguser',
                      help='GPG key ID', default='')
    parser.add_option('-p', '--fingerprint',
                      action='store',
                      dest='fingerprint',
                      help='GPG fingerprint',
                      default='')

    options, args = parser.parse_args()

    if options.srcfile == '':
        print("Specify source file with --file=<pathtofile> option")
        sys.exit(2)

    if options.gpguser == '':
        print("Specify GPG key ID with --user=<id> option")
        sys.exit(3)

    if options.fingerprint == '':
        print("Specify fingerprint with --fingerprint=<fingerprint> option")
        sys.exit(4)

    if not os.path.isfile(options.srcfile):
        print("Specified file was not found")
        sys.exit(5)

    c = cdn.CDN(options.host,
                user=options.gpguser,
                fingerprint=options.fingerprint, verify=False)

    filename = os.path.basename(options.srcfile)

    try:
        previous_files = c.List(filename)

        rc = c.Upload(options.srcfile)
        if rc is None:
            print("File upload failed")
            sys.exit(2)
        print("File upload complete")

        for f in previous_files:
            c.Delete(f["id"])
    except Exception as e:
        print("Error occured during upload: " + str(e))
        sys.exit(2)
