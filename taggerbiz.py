# taggerbiz.py
# sample parameters windows
# python taggerbiz.py -i E:\tagger.biz\input -l
#  D:\Lightroom -o E:\Lightroom -d
#  E:\LightroomDuplicates
import sys, getopt, os, shutil, glob
import taggerbizControlCentre


class inputfile:
    def __init__(self, name, directory):
        self.name = name
        self.directory = directory


class directory:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class filenameonly:
    def __init__(self, name, filecount):
        self.name = name
        self.filecount = filecount


class createinput:
    def create_inputfilesCollection(self, inputdirectory):
        # https://www.bogotobogo.com/python/python_traversing_directory_tree_recursively_os_walk.php
        path = inputdirectory

        fnameonly = []
        for root, d_names, f_names in os.walk(path):
            for f in f_names:
                nameonly = str(f)
                nameonly = nameonly.replace('.jpg', '')
                nameonly = nameonly.replace('.JPG', '')
                nameonly = nameonly.replace('.jpeg', '')
                nameonly = nameonly.replace('.JPEG', '')

                fnameonly.append(filenameonly(nameonly, 0))

        print("fnameonly = %s" % fnameonly)

        return fnameonly


class createoutput:
    def removeContent(self, directoryname):
        contentname = directoryname + "/**/*.*"
        files = glob.glob(contentname, recursive=True)
        for f in files:
            try:
                os.remove(f)
            except OSError as e:
                print("Error: %s : %s" % (f, e.strerror))

    def refill_lightroomdirectory(self, outputlightroomdirectoryname, inputlightroomdirectory):
        # try:
        #     shutil.rmtree(outputlightroomdirectoryname)
        # except OSError as e:
        #     print("Error: %s : %s" % (outputlightroomdirectoryname, e.strerror))
        # try:
        #     shutil.rmtree(doublelightroomdirectoryname)
        # except OSError as e:
        #     print("Error: %s : %s" % (doublelightroomdirectoryname, e.strerror))

        logoutput = inputlightroomdirectory + "/" + "taggerbizlogfile.txt"
        logfile = open(logoutput, 'w')
        fnamefull = self.fillFnameFull(outputlightroomdirectoryname)
        for f in fnamefull:
            self.copyToLightroomDirectoryFromFnamefull(f.name, f.directory, outputlightroomdirectoryname,
                                                       inputlightroomdirectory, logfile)
        logfile.close()
        # print("fnamefull = %s" % fnamefull)

    def fill_outputlightroomdirectory(self, fnameonly, inputlightroomdirectory, outputlightroomdirectoryname,
                                      doublelightroomdirectoryname):
        outputlightroomdirectory = []
        doublelightroomdirectory = []
        self.removeContent(outputlightroomdirectoryname)
        self.removeContent(doublelightroomdirectoryname)
        # try:
        #     shutil.rmtree(outputlightroomdirectoryname)
        # except OSError as e:
        #     print("Error: %s : %s" % (outputlightroomdirectoryname, e.strerror))
        # try:
        #     shutil.rmtree(doublelightroomdirectoryname)
        # except OSError as e:
        #     print("Error: %s : %s" % (doublelightroomdirectoryname, e.strerror))

        fnamefull = self.fillFnameFull(inputlightroomdirectory)
        fnameonly = self.countOccurencesFilename(fnameonly, fnamefull)
        logoutputNoDuplicates = outputlightroomdirectoryname + "/" + "logfile.txt"
        logoutputDuplicates = doublelightroomdirectoryname + "/" + "logfile.txt"
        logfile_noduplicates = open(logoutputNoDuplicates, 'w')
        logfile_duplicates = open(logoutputDuplicates, 'w')
        for f in fnamefull:

            for filenameonly in fnameonly:
                if filenameonly.name in f.name:
                    if (filenameonly.filecount > 0):

                        if (filenameonly.filecount < 4):

                            if (("xmp" in f.name.lower()) | ("jpg" in f.name.lower())):
                               self.copyToLightroomDirectoryFromFnamefull(f.name, f.directory, inputlightroomdirectory,
                                                                       outputlightroomdirectoryname,
                                                                       logfile_noduplicates)
                        else:
                            if (("xmp" in f.name.lower())  | ("jpg" in f.name.lower())):
                               self.copyToLightroomDirectoryFromFnamefull(f.name, f.directory, inputlightroomdirectory,
                                                                       doublelightroomdirectoryname,
                                                                       logfile_duplicates)
                    break
        logfile_noduplicates.close()
        logfile_duplicates.close()
        # print("fnamefull = %s" % fnamefull)
        return outputlightroomdirectory, doublelightroomdirectory

    def make_archive(self, archivename, source, destination):
        base = os.path.basename(destination)
        name = archivename
        format = 'zip'
        archive_from = os.path.dirname(source)
        archive_to = os.path.basename(source.strip(os.sep))
        shutil.make_archive(name, format, archive_from, archive_to)
        shutil.move('%s.%s' % (name, format), destination)

    def fill_taggerbizexportdirectory(self, taggerbizexportdirectory, customeremail, inputdirectory,  outputlightroomdirectory ):
        # https://stackoverflow.com/questions/32640053/compressing-directory-using-shutil-make-archive-while-preserving-directory-strever
        # https://stackoverflow.com/questions/3451111/unzipping-files-in-python
        print ("taggerbizexportdirectory: " + taggerbizexportdirectory)
        print("customeremail: " + customeremail)
        print("inputdirectory: " + inputdirectory)
        print("outputlightroomdirectory: " + outputlightroomdirectory)
        archivename = customeremail
        self.removeContent(taggerbizexportdirectory)
        self.make_archive(archivename, inputdirectory, taggerbizexportdirectory )

        oldoutputfilename = outputlightroomdirectory + "/" + "logfile.txt"
        newoutputfilename = taggerbizexportdirectory + "/" + customeremail + "_logfile.txt"
        newpath = shutil.copy(oldoutputfilename, newoutputfilename)
        fromzip = taggerbizexportdirectory + "/" + archivename + ".zip"
        totxt = fromzip + ".txt"
        os.rename(fromzip, totxt)


        return True


    def copyToLightroomDirectoryFromFnamefull(self, filenamefull, directory, inputlightroomdirectory,
                                              outputlightroomdirectoryname, logfile):

        oldoutputfilename = filenamefull
        #                 print("oldfile:", oldoutputfilename)
        newoutputfilename = oldoutputfilename
        newoutputfilename = newoutputfilename.replace(inputlightroomdirectory,
                                                      outputlightroomdirectoryname)
        print("newfile:", newoutputfilename)

        try:
            newdirectory = directory
            newdirectory = newdirectory.replace(inputlightroomdirectory, outputlightroomdirectoryname)

            os.makedirs(newdirectory)
        # except FileExistsError:
        except OSError as e:
            dummy = 1
            #                    print("Directory ",f.directory, " already exists")
        try:
            newpath = shutil.copy(oldoutputfilename, newoutputfilename)
            logfile.write(newoutputfilename + '\n')
        except OSError as e:
            print("error file copy ", oldoutputfilename, e.strerror)
            # don't program a break here! raw files have an additional xmp sidecar file

            # print("newpath:", newpath)

    def countOccurencesFilename(self, fnameonly, fnamefull):
        filecount = 0
        filetobecopied = False
        fnamefullOutput = []
        for inputfile in fnamefull:
            for filenameonly in fnameonly:
                if (filenameonly.name in inputfile.name):
                    if (("original" in inputfile.name) == False):
                        filenameonly.filecount += 1
                        fnamefullOutput.append(filenameonly)

        # filenameonly can have 3 files (jpg, raw and xmp)
        return fnamefullOutput

    def fillFnameFull(self, inputlightroomdirectory):
        fnamefull = []
        for root, d_names, f_names in os.walk(inputlightroomdirectory):

            for f in f_names:
                fnamefull.append(inputfile(os.path.join(root, f), root))

            # filenameonly can have 3 files (jpg, raw and xmp)
        return fnamefull


class setdirectories:
    def __init__(self):
        self.filepath = "./taggerbizexportconfig.txt"

    def set_directories(self, argv):
        # Use a breakpoint in the code line below to debug your script.
        # print('directories: {argv}')  # Press Ctrl+F8 to toggle the breakpoint.
        # print('Number of arguments:', len(sys.argv), 'arguments.')
        #
        print('Argument List:', str(sys.argv[1:]))
        inputdirectoryOpt = ""
        lightroomirectoryOpt = ""
        outputdirectoryOpt = ""
        doubleLightroomdirectoryOpt = ""
        executerunOpt = ""
        taggerbizexportdirectory = ""
        taggerbizimportdirectory = ""
        customeremail = ""

        try:
            opts, args = getopt.getopt(argv, "x:i:l:o:d:",
                                       ["execute=", "idirectory=", "ilightroomdirectory=", "olightroomdirectory=",
                                        "dlightroomdirectory="])
        except getopt.GetoptError:
            print('taggerbiz.py -i <inputdirectory> -o <outputdirectroy> error: ' + getopt.error)
            sys.exit(2)
        executerunOpt, inputdirectoryOpt, inputlightroomdirectoryOpt, outputlightroomdirectoryOpt, doubleLightroomdirectoryOpt = self.extractOpts(
            opts)
        print("executerunOpt: " + executerunOpt)
        # inputdirectory = inputdirectory.replace('<', '')
        # inputdirectory = inputdirectory.replace('>', '')
        # inputlightroomdirectory = inputlightroomdirectory.replace('<', '')
        # inputlightroomdirectory = inputlightroomdirectory.replace('>', '')
        # outputlightroomdirectory = outputlightroomdirectory.replace('<', '')
        # outputlightroomdirectory = outputlightroomdirectory.replace('>', '')
        # doubleLightroomdirectory = doubleLightroomdirectory.replace('<', '')
        # doubleLightroomdirectory = doubleLightroomdirectory.replace('>', '')
        # print('Input directory is:', inputdirectory)
        # print('Input Lightoom directory is: ', inputlightroomdirectory)
        # directoryCollection = []
        # directoryCollection.append(directory('inputdirectory', inputdirectory))
        # directoryCollection.append(directory('inputlightroomdirectory', inputlightroomdirectory))
        # directoryCollection.append(directory('outputlightroomdirectory', outputlightroomdirectory))
        # directoryCollection.append(directory('doubleLightroomdirectory', doubleLightroomdirectory))
        ii = 0

        with open(self.filepath, "r") as self.input_file:
            for x in self.input_file:
                ii = ii + 1
                if (ii == 1):
                    inputdirectory = x.rstrip("\n")
                elif (ii == 2):
                    inputlightroomdirectory = x.rstrip("\n")
                elif (ii == 3):
                    outputlightroomdirectory = x.rstrip("\n")
                elif (ii == 4):
                    doubleLightroomdirectory = x.rstrip("\n")
                elif (ii == 5):
                    taggerbizexportdirectory = x.rstrip("\n")
                elif (ii == 6):
                    taggerbizimportdirectory = x.rstrip("\n")
                elif (ii == 7):
                    customeremail = x.rstrip("\n")

        return executerunOpt, inputdirectory, inputlightroomdirectory, outputlightroomdirectory, doubleLightroomdirectory, taggerbizexportdirectory, taggerbizimportdirectory, customeremail

    def extractDirectories(self, opts):
        inputdirectory = ""
        inputlightroomdirectory = ""
        outputlightroomdirectory = ""
        doublelightroomdirectory = ""
        executerun = ""

        for opt, arg in opts:
            if opt in ("-i", "--idirectory"):
                inputdirectory = arg
            elif opt in ("-l", "--ldirectory"):
                inputlightroomdirectory = arg
            elif opt in ("-d", "--ddirectory"):
                doublelightroomdirectory = arg
            elif opt in ("-x", "--run"):
                executerun = arg
            else:
                if opt in ("-o", "--odirectory"):
                    outputlightroomdirectory = arg
        return inputdirectory, inputlightroomdirectory, outputlightroomdirectory, doublelightroomdirectory, executerun

    def extractOpts(self, opts):
        inputdirectoryOpt = ""
        inputlightroomdirectoryOpt = ""
        outputlightroomdirectoryOpt = ""
        doublelightroomdirectoryOpt = ""
        executerunOpt = ""

        for opt, arg in opts:
            if opt in ("-i", "--idirectory"):
                inputdirectoryOpt = arg
            elif opt in ("-l", "--ldirectory"):
                inputlightroomdirectoryOpt = arg
            elif opt in ("-d", "--ddirectory"):
                doublelightroomdirectoryOpt = arg
            elif opt in ("-x", "--run"):
                executerunOpt = arg
            else:
                if opt in ("-o", "--odirectory"):
                    outputlightroomdirectoryOpt = arg
        return executerunOpt, inputdirectoryOpt, inputlightroomdirectoryOpt, outputlightroomdirectoryOpt, doublelightroomdirectoryOpt


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    setdirectories = setdirectories()
    executerunOpt, inputdirectory, inputlightroomdirectory, outputlightroomdirectory, doublelightroomdirectory, taggerbizexportdirectory, taggerbizimportdirectory, customeremail = setdirectories.set_directories(
        sys.argv[1:])
    if (executerunOpt == "STARTIMPORT"):
        print("STARTIMPORT")
        createoutput = createoutput()
        print("LIGHTROOM directory: " + inputlightroomdirectory)
        print("LIGHTROOM extractDirectory: " + outputlightroomdirectory)
        createoutput.refill_lightroomdirectory(outputlightroomdirectory, inputlightroomdirectory)
    elif (executerunOpt == "PACKAGE"):
        createoutput = createoutput()
        askcompletion = createoutput.fill_taggerbizexportdirectory(taggerbizexportdirectory, customeremail,
                                                                   inputdirectory, outputlightroomdirectory)
    else:
        createinput = createinput()
        inputfilenames = createinput.create_inputfilesCollection(inputdirectory)
        for obj in inputfilenames:
            print(obj.name + " " + str(obj.filecount))
        createoutput = createoutput()
        NewOutputlightroomdirectory, NewOoublelightroomdirectory = createoutput.fill_outputlightroomdirectory(
            inputfilenames,
            inputlightroomdirectory,
            outputlightroomdirectory,
            doublelightroomdirectory)
        askcompletion = createoutput.fill_taggerbizexportdirectory(taggerbizexportdirectory,customeremail,inputdirectory,outputlightroomdirectory)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
