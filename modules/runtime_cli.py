"""
This is a runtime cli interface to call system data callbacks
"""
from threading import Thread, Event
from modules.shared import log
import datetime
import time

functions = {}
rtcli_thread = None
watch_thread = None
is_alive = False


def help():
    print('Usage: function [arg1 [arg2 [...]]]\n\tCallable functions:')
    list_functions()
    return ''


def clock():
    return datetime.datetime.now().strftime("%H:%M:%S")


def call_function(funcs):
    ret = False

    if funcs[0] not in functions and len(funcs[0]) > 2:
        if funcs[0][-2:] == '()' and len(funcs[0]) > 4:
            funcs[0] = funcs[0][:-2]

        cands = []
        for f in functions:
            if funcs[0] in f:
                cands.append(f)

        if len(cands) == 1:
            print('Assumed: ' + cands[0] + '()')
            funcs[0] = cands[0]
        elif len(cands) > 1:
            print('Multiple options for \033[3m {} \033[0m: '.format(funcs[0]), end='')
            print(*cands, sep=', ')
            return True

    if funcs[0] == 'watch':
        if len(funcs) <= 1:
            log.warn('No function to watch!')
            return True
        return watch(funcs[1:])

    for func in funcs:
        if func not in functions:
            return False
        f = functions[func]
        msg = f()
        if msg is not None:
            print(str(msg))
        ret = True
    return ret


def watch(func):
    ext = Event()

    if not call_function(func):
        return False

    def _watch_thread(func, ext):
        while call_function(func) and not ext.is_set():
            time.sleep(2)

    if is_alive and watch_thread is None:
        trd = Thread(target=_watch_thread, args=(func, ext,))
        print('Press enter to exit')
        trd.start()
        input()
        ext.set()
        trd.join()

    return True


def add_function(function):
    global functions
    # assert type(function) == types.FunctionType, 'Function is not a function!' # todo fix for class functions
    name = function.__name__

    functions[name] = function
    log.blue('function {}{} added to cli functions'.format(name, function.__code__.co_varnames))


def list_functions():
    for f in functions:
        func = functions[f]
        arg_count = func.__code__.co_argcount

        arg_names = ''
        arg_defs = func.__defaults__
        for idx, arg in enumerate(func.__code__.co_varnames[:arg_count]):
            if arg not in ['self', ',']:
                if arg_defs is not None and idx >= arg_count - len(arg_defs):
                    arg_def = arg_defs[idx - arg_count + len(arg_defs)]
                    if arg_def is None:
                        arg_def = 'DEFAULT'
                    arg += '=' + str(arg_def)

                if idx + 1 == arg_count:
                    arg_names += str(arg)
                else:
                    arg_names += str(arg) + ', '

        print('\t' + '\033[94m' + f + '\033[0m' + '(' + '\033[92m' + arg_names + '\033[0m' + ')')


def _rtcli_thread(funcs=None):
    if funcs is not None:
        for f in funcs:
            add_function(f)

    while is_alive:
        inp = input('>>')
        if inp is '':
            print('Callable Functions:')
            list_functions()
            continue

        if inp == 'q':
            end()  # todo cause program shutdown

        inp = inp.split()

        if type(inp[0]) == str:
            if not call_function(inp):
                log.warn('Input(s) {} not defined! Defined inputs:'.format(inp))
                list_functions()
        else:
            log.warn('Input [{}] not supported!'.format(inp[0]))


def init(funcs=None):
    global rtcli_thread, is_alive
    rtcli_thread = Thread(name='rtcli_thread', target=_rtcli_thread, args=(funcs,))
    is_alive = Thread
    rtcli_thread.start()


def end():
    global is_alive, rtcli_thread

    if is_alive:
        is_alive = False
        rtcli_thread.join()


# add default functions
for func in [help, watch, clock]:
    add_function(func)

if __name__ == '__main__':
    try:
        init()
        rtcli_thread.join()
    except KeyboardInterrupt:
        pass
end()
