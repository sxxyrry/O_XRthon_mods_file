import os, pathlib, time

folder = pathlib.Path(__file__).parent.resolve()

class XRthon_main():
    def __init__(self):
        self.var_ = {}

    def raisess(self, text: str, types: str, code: str, file_: str, line= 0, code_=1):
        Error_table = {
            'VariableError',
            'InitError',
            'CodeError',
            'Error_typeError',
            'NameError',
        }
        if types in Error_table:
            if file_ == 'text':
                print(' > Backtrack (last call):')
                print(f' >   File "{folder}\\main.py"')
                print(f' >     {code}')
                print(f' >     {types}: Error: {text}, Status code: {code_}')
                raise SystemExit()
            else:
                file_ = os.path.join(file_)
                print(' > Backtrack (last call):')
                print(f' >   File "{file_}", line {line}')
                print(f' >     {code}')
                print(f' >     {types}: Error: {text}, Status code: {code_}')
                raise SystemExit()
        else:
            self.raisess(f'name {types} is not defined', 'NameError', code, file_)

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
                            self.raisess('Variable can\'t be printed', 'VariableError', text, 'text')
                        if not text_1 in self.var_:
                            time.sleep(0.5)
                            self.raisess('Variable can\'ot be printed', 'VariableError', text, 'text')
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
                            self.raisess('Variable can\'t be printed', 'VariableError', text, 'text')
                        if not text_1 in self.var_:
                            time.sleep(0.5)
                            self.raisess('Variable can\'t be printed', 'VariableError', text, 'text') 
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
                            self.raisess('Variable can\'t be printed', 'VariableError', text, 'text')
                        if not text_1 in self.var_:
                            time.sleep(0.5)
                            self.raisess('Variable can\'t be printed', 'VariableError', text, 'text')
                        else:
                            print(' > ' + self.var_[text_1], end='')
                        if text_1 in self.var_:
                            print(' > ' + self.var_[text_1], end='')
                        else:
                            if not text_1 == '':
                                print(' > ' + self.var_[1], end='')
                elif f == 'init':
                    time.sleep(0.5)
                    self.raisess('Failed to initialize', 'InitError', text, 'text')
                elif f == 'raise':
                    text_2 = list_[1].split(',')
                    if len(text_2) == 2:
                        self.raisess(text_2[0], text_2[1], text, 'text')
                    elif len(text_2) == 3:
                        try:
                            self.raisess(text_2[0], text_2[1], text, 'text', code_=int(text_2[2]))
                        except SystemExit:
                            pass
                        except:
                            time.sleep(0.5)
                            self.raisess(f'code {text} is ERROR', 'CodeError', text, 'text')  
                    else:
                        time.sleep(0.5)
                        self.raisess(f'code {text} is ERROR', 'CodeError', text, 'text')
                else:
                    time.sleep(0.5)
                    self.raisess(f'name {f} is not defined', 'NameError', text, 'text')
            else:
                time.sleep(0.5)
                self.raisess(f'name {f} is not defined', 'NameError', text, 'text')
        else:
            time.sleep(0.5)
            self.raisess(f'name {text} is not defined', 'NameError', text, 'text')

    def XRthon_file(self, file, path=os.path.join(folder, './test_files/TEST.XRn')):
        var = {}
        texts = ''.join(file.read())
        file_now_line = 0
        list_1 = texts.split('\n')
        for text in list_1:
            file_now_line += 1
            if file_now_line == 1:
                if 'init' in text:
                    list_ = text.split(':')
                    if '#' in list_[0]:
                        time.sleep(0.5)
                        self.raisess('init undefined', 'InitError', text, path, file_now_line)
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
                    self.raisess('init undefined', 'InitError', text, path, file_now_line)
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
                                self.raisess('init undefined, special variable cannot be printed', 'InitError', text, path, file_now_line)
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
                                self.raisess('init undefined, special variable cannot be printed', 'InitError', text, path, file_now_line)
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
                        self.raisess(text_2[0], text_2[1], text, path, file_now_line)
                    elif len(text_2) == 3:
                        try:
                            self.raisess(text_2[0], text_2[1], text, path, file_now_line, int(text_2[2]))
                        except SystemExit:
                            pass
                        except:
                            time.sleep(0.5)
                            self.raisess(f'code {text} is ERROR', 'CodeError', text, path, file_now_line)
                    else:
                        time.sleep(0.5)
                        self.raisess(f'code {text} is ERROR', 'CodeError', text, path, file_now_line)
                else:
                    time.sleep(0.5)
                    self.raisess(f'name {f} is not defined', 'NameError', text, path, file_now_line)
            else:
                time.sleep(0.5)
                self.raisess(f'name {text} is not defined', 'NameError', text, path, file_now_line)

_XRthon_main_ = XRthon_main()
