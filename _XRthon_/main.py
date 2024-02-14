import os, pathlib, time, shutil
from . import XRthon_main

def mains():
    folder = pathlib.Path(__file__).parent.resolve()

    pycache = os.path.join(folder, './__pycache__')
    if os.path.exists(pycache):
        shutil.rmtree(pycache)

    print(''' > 
 >     ##################
 >     #                #
 >     #  XRthon 1.0.0  #
 >     #                #
 >     ##################
 >     ''')

    print(' > Now edition: 0.1 BETA __0.0.2__')
    print(' > Note that the \'BETA\' in the version number is the major version number 0 (beta version)')
    print(' > For example, \'XRthon 0.1 BETA __0.0.1__ V\' means that the XRthon version is \'0.0.1_0.0.1\'')

    time.sleep(0.5)

    def Main_logic():

        running = True

        while running:
            command = input(' > Enter the command (enter "q" to exit, "R_F" run "XRn" file, "T_C" literal code(the interpreter writes the code)) >>>')
            time.sleep(0.5)
            if command == 'q':
                running = False
                return
            elif command == 'R_F':
                path = input(' > Enter the path ("XRn" file type) >>>')
                time.sleep(0.5)
                paths = path.split('.')
                if not paths[len(paths) - 1] == 'XRn':
                    time.sleep(0.5)
                    print(' > Wrong file type (should be "XRn"), or an error has occurred')
                    running = False
                    Main_logic()
                    return
                try:
                    with open(os.path.join(path), 'r', encoding='UTF-8') as file:
                        XRthon_main._XRthon_main_.XRthon_file(file, path=path)
                except:
                    print(' > An error has occurred')
            elif command == 'T_C':
                text_code = input(' > Enter the code >>>')
                time.sleep(0.5)
                try:
                    XRthon_main._XRthon_main_.XRthon_text(text_code)
                except:
                    time.sleep(0.5)
                    print(' > An error has occurred')
            else:
                time.sleep(0.5)
                print(f' > No command \"{command}\"')
                
    Main_logic()
