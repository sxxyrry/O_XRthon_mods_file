import os, pathlib, time

folder = pathlib.Path(__file__).parent.resolve()

class XRthon_main():
    def __init__(self):
        self.var_ = {}

    def raisess(self, text, types, code_=1):
        print(f' > {types}: Error: {text}, Status code: {code_}')

    def XRthon_text(self, text_code):
        texts = ''.join(text_code)
        list_1 = texts.split('\n')
        for text in list_1:
            if '#' in text:
                continue
            elif '=' in text:
                list_ = text.split('=')
                name = list_[0]
                v = list_[1]
                if 'input' in v:
                    v_list_ = v.split(':')
                    text_2 = list_[1].split('\'')
                    for text_1 in text_2:
                        if  text_1 == '__name__' or text_1 ==  '__path__' or text_1 == '__init__' or text_1 == '__file__' or text_1 == '__package__':
                            time.sleep(0.5)
                            self.raisess('Variable cannot be printed', 'Variable cannot be printed')
                        if not text_1 in self.var_:
                            time.sleep(0.5)
                            self.raisess('Variable cannot be printed', 'Variable cannot be printed')
                        else:
                            print(' > ' + self.var_[text_1], end='')
                        if text_1 in self.var_:
                            print(' > ' + self.var_[text_1], end='')
                        else:
                            if not text_1 == '':
                                print(' > ' + v_list_[1], end='')
                        v = input('')
                elif '{}' in v:
                    vs = set()
                    v_list_ = v.split('{}')
                    for vars in v_list_:
                        vars_list_ = vars.split(',')
                        for vars_ in vars_list_:
                            vs.update({vars_})
                            self.var_.update({name : vs})
                self.var_.update({name : v})
                time.sleep(0.5)
                print(' > A variable has been created')
            elif ':' in text:
                list_ = text.split(':')
                f = list_[0]
                if f == 'print':
                    text_2 = list_[1].split('\'')
                    for text_1 in text_2:
                        if  text_1 == '__name__' or text_1 == '__path__' or text_1 == '__init__' or text_1 == '__file__' or text_1 == '__package__':
                            time.sleep(0.5)
                            self.raisess('Variable cannot be printed', 'Variable cannot be printed')
                        if not text_1 in self.var_:
                            time.sleep(0.5)
                            self.raisess('Variable cannot be printed', 'Variable cannot be printed')
                        else:
                            print(' > ' + self.var_[text_1])
                        if text_1 in self.var_:
                            print(' > ' + self.var_[text_1])
                        else:
                            if not text_1 == '':
                                print(' > ' + list_[1])
                elif f == 'input':
                    text_2 = list_[1].split('\'')
                    for text_1 in text_2:
                        if  text_1 == '__name__' or text_1 ==  '__path__' or text_1 == '__init__' or text_1 == '__file__' or text_1 == '__package__':
                            time.sleep(0.5)
                            self.raisess('Variable cannot be printed', 'Variable cannot be printed')
                        if not text_1 in self.var_:
                            time.sleep(0.5)
                            self.raisess('Variable cannot be printed', 'Variable cannot be printed')
                        else:
                            print(' > ' + self.var_[text_1], end='')
                        if text_1 in self.var_:
                            print(' > ' + self.var_[text_1], end='')
                        else:
                            if not text_1 == '':
                                print(' > ' + self.var_[1], end='')
                elif f == 'init':
                    time.sleep(0.5)
                    self.raisess('Failed to initialize', 'Failed to initialize')
            else:
                time.sleep(0.5)
                self.raisess(f'unknown code, code: {text}', 'unknown code')

    def XRthon_file(self, file, path=os.path.join(folder, './test_files/TEST.XRn')):
        var = {}
        run_codes_ = []
        texts = ''.join(file.read())
        file_now_line = 0
        list_1 = texts.split('\n')
        for text in list_1:
            code_isE = False
            file_now_line += 1
            if file_now_line == 1:
                if 'init' in text:
                    list_ = text.split(':')
                    if '#' in list_[0]:
                        time.sleep(0.5)
                        self.raisess('\'init\'undefined', '\'init\'undefined')
                        continue
                    paths_ = ''.join(path)
                    path_ = paths_.split('\\')
                    path_len_ = len(path_) - 1
                    pathss_ = path_[path_len_].split('.')
                    pathss_len_ = len(pathss_) - 1
                    var.update({'__name__' : pathss_[pathss_len_ -1], '__path__' : path, '__init__' : list_[1] , '__file__' : path_[path_len_], '__package__' : path_[path_len_ - 1]})
                    continue
                else:
                    time.sleep(0.5)
                    self.raisess('\'init\'undefined', '\'init\'undefined')
                    continue
            if '#' in text:
                continue
            elif '=' in text:
                list_ = text.split('=')
                v_name_ = list_[0]
                v = list_[1]
                if 'input' in v:
                    v_list_ = v.split(':')
                    if v_list_[0] == 'input':
                        text_2 = v_list_[1].split('\'')
                        for text_1 in text_2:
                            if text_1 in var:
                                print(' > ' + var[text_1], end='')
                            else:
                                if not text_1 == '':
                                    print(' > ' + v_list_[1], end='')
                            v = input('')
                elif '{' in v and '}' in v:
                    vs = set( )
                    v_list_ = v.split('{')[1].split('}')
                    for vars in v_list_:
                        if vars == '':
                            continue
                        vars_list_ = vars.split(',')
                        for vars_ in vars_list_:
                            vs.update({vars_})
                            var.update({v_name_ : vs})
                var.update({v_name_ : v})
            elif ':' in text:
                list_ = text.split(':')
                f = list_[0]
                if f == 'print':
                    text_2 = list_[1].split('\'')
                    for text_1 in text_2:
                        if  text_1 == '__name__' or text_1 == '__path__' or text_1 == '__init__' or text_1 == '__file__' or text_1 == '__package__':
                            if not text_1 in var:
                                time.sleep(0.5)
                                self.raisess('\'init\' undefined, special variable cannot be printed', '\'init\' undefined')
                            else:
                                print(' > ' + var[text_1])
                        elif text_1 in var:
                            print(' > ' + var[text_1])
                        else:
                            if not text_1 == '':
                                print(' > ' + list_[1])
                elif f == 'input':
                    text_2 = list_[1].split('\'')
                    for text_1 in text_2:
                        if  text_1 == '__name__' or text_1 ==  '__path__' or text_1 == '__init__' or text_1 == '__file__' or text_1 == '__package__':
                            if not text_1 in var:
                                time.sleep(0.5)
                                self.raisess('\'init\' undefined, special variable cannot be printed', '\'init\' undefined')
                            else:
                                print(' > ' + var[text_1], end='')
                        elif text_1 in var:
                            print(' > ' + var[text_1], end='')
                        else:
                            if not text_1 == '':
                                print(list_[1], end='')
                        input('')
                elif f == 'return':
                    print(' > The program has exited')
                    return
                elif f == 'raise':
                    text_2 = list_[1].split(',')
                    if len(text_2) == 2:
                        self.raisess(text_2[0], text_2[1])
                        return
                    if len(text_2) == 3:
                        self.raisess(text_2[0], text[1], int(text_2[2]))
                        return
                else:
                    time.sleep(0.5)
                    code_isE = True
                    self.raisess(f'Unknown code, code: {text}', 'unknown code')
            else:
                time.sleep(0.5)
                code_isE = True
                self.raisess(f'Unknown code, code: {text}', 'unknown code')
            if code_isE == True:
                pass
            elif code_isE == False:
                run_codes_.append(text)

_XRthon_main_ = XRthon_main()
