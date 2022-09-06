# encoding: utf-8
# module sys
# from (built-in)
# by generator 1.147
"""
This module provides access to some objects used or maintained by the
interpreter and to functions that interact strongly with the interpreter.

Dynamic objects:

argv -- command line arguments; argv[0] is the script pathname if known
path -- module search path; path[0] is the script directory, else ''
modules -- dictionary of loaded modules

displayhook -- called to show results in an interactive session
excepthook -- called to handle any uncaught exception other than SystemExit
  To customize printing in an interactive session or to install a custom
  top-level exception handler, assign other functions to replace these.

stdin -- standard input file object; used by input()
stdout -- standard output file object; used by print()
stderr -- standard error object; used for error messages
  By assigning other file objects (or objects that behave like files)
  to these, it is possible to redirect all of the interpreter's I/O.

last_type -- type of last uncaught exception
last_value -- value of last uncaught exception
last_traceback -- traceback of last uncaught exception
  These three are only available in an interactive session after a
  traceback has been printed.

Static objects:

builtin_module_names -- tuple of module names built into this interpreter
copyright -- copyright notice pertaining to this interpreter
exec_prefix -- prefix used to find the machine-specific Python library
executable -- absolute path of the executable binary of the Python interpreter
float_info -- a named tuple with information about the float implementation.
float_repr_style -- string indicating the style of repr() output for floats
hash_info -- a named tuple with information about the hash algorithm.
hexversion -- version information encoded as a single integer
implementation -- Python implementation information.
int_info -- a named tuple with information about the int implementation.
maxsize -- the largest supported length of containers.
maxunicode -- the value of the largest Unicode code point
platform -- platform identifier
prefix -- prefix used to find the Python library
thread_info -- a named tuple with information about the thread implementation.
version -- the version of this interpreter as a string
version_info -- version information as a named tuple
__stdin__ -- the original stdin; don't touch!
__stdout__ -- the original stdout; don't touch!
__stderr__ -- the original stderr; don't touch!
__displayhook__ -- the original displayhook; don't touch!
__excepthook__ -- the original excepthook; don't touch!

Functions:

displayhook() -- print an object to the screen, and save it in builtins._
excepthook() -- print an exception and its traceback to sys.stderr
exc_info() -- return thread-safe information about the current exception
exit() -- exit the interpreter by raising SystemExit
getdlopenflags() -- returns flags to be used for dlopen() calls
getprofile() -- get the global profiling function
getrefcount() -- return the reference count for an object (plus one :-)
getrecursionlimit() -- return the max recursion depth for the interpreter
getsizeof() -- return the size of an object in bytes
gettrace() -- get the global debug tracing function
setdlopenflags() -- set the flags to be used for dlopen() calls
setprofile() -- set the global profiling function
setrecursionlimit() -- set the max recursion depth for the interpreter
settrace() -- set the global debug tracing function
"""
# no imports

# Variables with simple values

abiflags = ''

api_version = 1013

base_exec_prefix = '/usr'

base_prefix = '/usr'

byteorder = 'little'

copyright = 'Copyright (c) 2001-2022 Python Software Foundation.\nAll Rights Reserved.\n\nCopyright (c) 2000 BeOpen.com.\nAll Rights Reserved.\n\nCopyright (c) 1995-2001 Corporation for National Research Initiatives.\nAll Rights Reserved.\n\nCopyright (c) 1991-1995 Stichting Mathematisch Centrum, Amsterdam.\nAll Rights Reserved.'

dont_write_bytecode = False

executable = '/home/ramona/PycharmProjects/DjangoProjects/demo/venv/bin/python'

exec_prefix = '/home/ramona/PycharmProjects/DjangoProjects/demo/venv'

float_repr_style = 'short'

hexversion = 50988272

maxsize = 9223372036854775807
maxunicode = 1114111

platform = 'linux'
platlibdir = 'lib'

prefix = '/home/ramona/PycharmProjects/DjangoProjects/demo/venv'

pycache_prefix = None

version = '3.10.4 (main, Jun 29 2022, 12:14:53) [GCC 11.2.0]'

_base_executable = '/home/ramona/PycharmProjects/DjangoProjects/demo/venv/bin/python'

_framework = ''

_home = '/usr'

# functions

def addaudithook(*args, **kwargs): # real signature unknown
    """ Adds a new audit hook callback. """
    pass

def audit(event, *args): # real signature unknown; restored from __doc__
    """
    audit(event, *args)
    
    Passes the event to any audit hooks that are attached.
    """
    pass

def breakpointhook(*args, **kws): # real signature unknown; restored from __doc__
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def call_tracing(*args, **kwargs): # real signature unknown
    """
    Call func(*args), while tracing is enabled.
    
    The tracing state is saved, and restored afterwards.  This is intended
    to be called from a debugger from a checkpoint, to recursively debug
    some other code.
    """
    pass

def displayhook(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def excepthook(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def exc_info(*args, **kwargs): # real signature unknown
    """
    Return current exception information: (type, value, traceback).
    
    Return information about the most recent exception caught by an except
    clause in the current stack frame or in an older stack frame.
    """
    pass

def exit(*args, **kwargs): # real signature unknown
    """
    Exit the interpreter by raising SystemExit(status).
    
    If the status is omitted or None, it defaults to zero (i.e., success).
    If the status is an integer, it will be used as the system exit status.
    If it is another kind of object, it will be printed and the system
    exit status will be one (i.e., failure).
    """
    pass

def getallocatedblocks(*args, **kwargs): # real signature unknown
    """ Return the number of memory blocks currently allocated. """
    pass

def getdefaultencoding(*args, **kwargs): # real signature unknown
    """ Return the current default encoding used by the Unicode implementation. """
    pass

def getdlopenflags(*args, **kwargs): # real signature unknown
    """
    Return the current value of the flags that are used for dlopen calls.
    
    The flag constants are defined in the os module.
    """
    pass

def getfilesystemencodeerrors(*args, **kwargs): # real signature unknown
    """ Return the error mode used Unicode to OS filename conversion. """
    pass

def getfilesystemencoding(*args, **kwargs): # real signature unknown
    """ Return the encoding used to convert Unicode filenames to OS filenames. """
    pass

def getprofile(*args, **kwargs): # real signature unknown
    """
    Return the profiling function set with sys.setprofile.
    
    See the profiler chapter in the library manual.
    """
    pass

def getrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Return the current value of the recursion limit.
    
    The recursion limit is the maximum depth of the Python interpreter
    stack.  This limit prevents infinite recursion from causing an overflow
    of the C stack and crashing Python.
    """
    pass

def getrefcount(): # real signature unknown; restored from __doc__
    """
    Return the reference count of object.
    
    The count returned is generally one higher than you might expect,
    because it includes the (temporary) reference as an argument to
    getrefcount().
    """
    pass

def getsizeof(p_object, default=None): # real signature unknown; restored from __doc__
    """
    getsizeof(object [, default]) -> int
    
    Return the size of object in bytes.
    """
    return 0

def getswitchinterval(*args, **kwargs): # real signature unknown
    """ Return the current thread switch interval; see sys.setswitchinterval(). """
    pass

def gettrace(*args, **kwargs): # real signature unknown
    """
    Return the global debug tracing function set with sys.settrace.
    
    See the debugger chapter in the library manual.
    """
    pass

def get_asyncgen_hooks(*args, **kwargs): # real signature unknown
    """
    Return the installed asynchronous generators hooks.
    
    This returns a namedtuple of the form (firstiter, finalizer).
    """
    pass

def get_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """ Check status of origin tracking for coroutine objects in this thread. """
    pass

def intern(*args, **kwargs): # real signature unknown
    """
    ``Intern'' the given string.
    
    This enters the string in the (global) table of interned strings whose
    purpose is to speed up dictionary lookups. Return the string itself or
    the previously interned string object with the same value.
    """
    pass

def is_finalizing(*args, **kwargs): # real signature unknown
    """ Return True if Python is exiting. """
    pass

def setdlopenflags(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    Set the flags used by the interpreter for dlopen calls.
    
    This is used, for example, when the interpreter loads extension
    modules. Among other things, this will enable a lazy resolving of
    symbols when importing a module, if called as sys.setdlopenflags(0).
    To share symbols across extension modules, call as
    sys.setdlopenflags(os.RTLD_GLOBAL).  Symbolic names for the flag
    modules can be found in the os module (RTLD_xxx constants, e.g.
    os.RTLD_LAZY).
    """
    pass

def setprofile(function): # real signature unknown; restored from __doc__
    """
    setprofile(function)
    
    Set the profiling function.  It will be called on each function call
    and return.  See the profiler chapter in the library manual.
    """
    pass

def setrecursionlimit(*args, **kwargs): # real signature unknown
    """
    Set the maximum depth of the Python interpreter stack to n.
    
    This limit prevents infinite recursion from causing an overflow of the C
    stack and crashing Python.  The highest possible limit is platform-
    dependent.
    """
    pass

def setswitchinterval(*args, **kwargs): # real signature unknown
    """
    Set the ideal thread switching delay inside the Python interpreter.
    
    The actual frequency of switching threads can be lower if the
    interpreter executes long sequences of uninterruptible code
    (this is implementation-specific and workload-dependent).
    
    The parameter must represent the desired switching delay in seconds
    A typical value is 0.005 (5 milliseconds).
    """
    pass

def settrace(function): # real signature unknown; restored from __doc__
    """
    settrace(function)
    
    Set the global debug tracing function.  It will be called on each
    function call.  See the debugger chapter in the library manual.
    """
    pass

def set_asyncgen_hooks(*args, **kwargs): # real signature unknown; NOTE: unreliably restored from __doc__ 
    """
    set_asyncgen_hooks(* [, firstiter] [, finalizer])
    
    Set a finalizer for async generators objects.
    """
    pass

def set_coroutine_origin_tracking_depth(*args, **kwargs): # real signature unknown
    """
    Enable or disable origin tracking for coroutine objects in this thread.
    
    Coroutine objects will track 'depth' frames of traceback information
    about where they came from, available in their cr_origin attribute.
    
    Set a depth of 0 to disable.
    """
    pass

def unraisablehook(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

def _clear_type_cache(*args, **kwargs): # real signature unknown
    """ Clear the internal type lookup cache. """
    pass

def _current_exceptions(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's identifier to its current raised exception.
    
    This function should be used for specialized purposes only.
    """
    pass

def _current_frames(*args, **kwargs): # real signature unknown
    """
    Return a dict mapping each thread's thread id to its current stack frame.
    
    This function should be used for specialized purposes only.
    """
    pass

def _deactivate_opcache(*args, **kwargs): # real signature unknown
    """ Deactivate the opcode cache permanently """
    pass

def _debugmallocstats(*args, **kwargs): # real signature unknown
    """
    Print summary info to stderr about the state of pymalloc's structures.
    
    In Py_DEBUG mode, also perform some expensive internal consistency
    checks.
    """
    pass

def _getframe(*args, **kwargs): # real signature unknown
    """
    Return a frame object from the call stack.
    
    If optional integer depth is given, return the frame object that many
    calls below the top of the stack.  If that is deeper than the call
    stack, ValueError is raised.  The default for depth is zero, returning
    the frame at the top of the call stack.
    
    This function should be used for internal and specialized purposes
    only.
    """
    pass

def __breakpointhook__(*args, **kwargs): # real signature unknown
    """
    breakpointhook(*args, **kws)
    
    This hook function is called by built-in breakpoint().
    """
    pass

def __displayhook__(*args, **kwargs): # real signature unknown
    """ Print an object to sys.stdout and also save it in builtins._ """
    pass

def __excepthook__(*args, **kwargs): # real signature unknown
    """ Handle an exception by displaying it with a traceback on sys.stderr. """
    pass

def __interactivehook__(): # reliably restored by inspect
    # no doc
    pass

def __unraisablehook__(*args, **kwargs): # real signature unknown
    """
    Handle an unraisable exception.
    
    The unraisable argument has the following attributes:
    
    * exc_type: Exception type.
    * exc_value: Exception value, can be None.
    * exc_traceback: Exception traceback, can be None.
    * err_msg: Error message, can be None.
    * object: Object causing the exception, can be None.
    """
    pass

# classes

class __loader__(object):
    """
    Meta path import for built-in modules.
    
        All methods are either class or static methods to avoid the need to
        instantiate the class.
    """
    def create_module(spec): # reliably restored by inspect
        """ Create a built-in module """
        pass

    def exec_module(module): # reliably restored by inspect
        """ Exec a built-in module """
        pass

    @classmethod
    def find_module(cls, *args, **kwargs): # real signature unknown
        """
        Find the built-in module.
        
                If 'path' is ever specified then the search is considered a failure.
        
                This method is deprecated.  Use find_spec() instead.
        """
        pass

    @classmethod
    def find_spec(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def get_code(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have code objects. """
        pass

    @classmethod
    def get_source(cls, *args, **kwargs): # real signature unknown
        """ Return None as built-in modules do not have source code. """
        pass

    @classmethod
    def is_package(cls, *args, **kwargs): # real signature unknown
        """ Return False as built-in modules are never packages. """
        pass

    @classmethod
    def load_module(cls, *args, **kwargs): # real signature unknown
        """
        Load the specified module into sys.modules and return it.
        
            This method is deprecated.  Use loader.exec_module() instead.
        """
        pass

    def module_repr(module): # reliably restored by inspect
        """
        Return repr for the module.
        
                The method is deprecated.  The import machinery does the job itself.
        """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    __weakref__ = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """list of weak references to the object (if defined)"""


    _ORIGIN = 'built-in'
    __dict__ = None # (!) real value is "mappingproxy({'__module__': '_frozen_importlib', '__doc__': 'Meta path import for built-in modules.\\n\\n    All methods are either class or static methods to avoid the need to\\n    instantiate the class.\\n\\n    ', '_ORIGIN': 'built-in', 'module_repr': <staticmethod(<function BuiltinImporter.module_repr at 0x7f611f64a290>)>, 'find_spec': <classmethod(<function BuiltinImporter.find_spec at 0x7f611f64a320>)>, 'find_module': <classmethod(<function BuiltinImporter.find_module at 0x7f611f64a3b0>)>, 'create_module': <staticmethod(<function BuiltinImporter.create_module at 0x7f611f64a440>)>, 'exec_module': <staticmethod(<function BuiltinImporter.exec_module at 0x7f611f64a4d0>)>, 'get_code': <classmethod(<function BuiltinImporter.get_code at 0x7f611f64a5f0>)>, 'get_source': <classmethod(<function BuiltinImporter.get_source at 0x7f611f64a710>)>, 'is_package': <classmethod(<function BuiltinImporter.is_package at 0x7f611f64a830>)>, 'load_module': <classmethod(<function _load_module_shim at 0x7f611f649750>)>, '__dict__': <attribute '__dict__' of 'BuiltinImporter' objects>, '__weakref__': <attribute '__weakref__' of 'BuiltinImporter' objects>})"


# variables with complex values

argv = [] # real value of type <class 'list'> skipped

builtin_module_names = () # real value of type <class 'tuple'> skipped

flags = (
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    1,
    0,
    False,
    0,
    0,
)

float_info = (
    1.7976931348623157e+308,
    1024,
    308,
    2.2250738585072014e-308,
    -1021,
    -307,
    15,
    53,
    2.220446049250313e-16,
    2,
    1,
)

hash_info = (
    64,
    2305843009213693951,
    314159,
    0,
    1000003,
    'siphash24',
    64,
    128,
    0,
)

implementation = None # (!) real value is "namespace(name='cpython', cache_tag='cpython-310', version=sys.version_info(major=3, minor=10, micro=4, releaselevel='final', serial=0), hexversion=50988272, _multiarch='x86_64-linux-gnu')"

int_info = (
    30,
    4,
)

meta_path = [
    None, # (!) real value is '<_distutils_hack.DistutilsMetaFinder object at 0x7f611f3c7700>'
    None, # (!) real value is '<_virtualenv._Finder object at 0x7f611f4e2f50>'
    __loader__,
    None, # (!) real value is "<class '_frozen_importlib.FrozenImporter'>"
    None, # (!) real value is "<class '_frozen_importlib_external.PathFinder'>"
    None, # (!) real value is '<six._SixMetaPathImporter object at 0x7f611eb96e30>'
]

modules = {} # real value of type <class 'dict'> skipped

orig_argv = [
    '/home/ramona/PycharmProjects/DjangoProjects/demo/venv/bin/python',
    '/snap/pycharm-professional/300/plugins/python/helpers/generator3/__main__.py',
    '-d',
    '/home/ramona/.cache/JetBrains/PyCharm2022.2/python_stubs/-1954032839',
    '-s',
    '/usr/lib/python3.10:/usr/lib/python3.10/lib-dynload:/home/ramona/PycharmProjects/DjangoProjects/demo/venv/lib/python3.10/site-packages:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stdlib:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/six:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/boto:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/mock:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pytz:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/toml:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/annoy:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/babel:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/emoji:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/first:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/fpdf2:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ldap3:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/polib:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/redis:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/regex:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/retry:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ujson:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Pillow:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/PyYAML:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/bleach:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/caldav:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/docopt:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/enum34:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/hdbcli:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/invoke:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/passpy:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/psutil:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pycurl:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pynput:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pysftp:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/stripe:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/xxhash:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/PyMySQL:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/appdirs:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/certifi:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/chardet:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/chevron:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/passlib:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyaudio:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyvmomi:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/slumber:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/tzlocal:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/urllib3:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/vobject:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Markdown:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Pygments:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/aiofiles:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/colorama:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/croniter:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/docutils:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/filelock:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/html5lib:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/httplib2:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/jmespath:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/oauthlib:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/openpyxl:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/paramiko:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/psycopg2:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyflakes:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/requests:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/selenium:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/tabulate:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/toposort:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/waitress:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/braintree:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/decorator:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/freezegun:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ipaddress:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/playsound:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyOpenSSL:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyRFC3339:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/termcolor:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ttkthemes:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/typed-ast:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Deprecated:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Flask-Cors:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/SQLAlchemy:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Send2Trash:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/cachetools:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/commonmark:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/dateparser:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/frozendict:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/jsonschema:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyfarmhash:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/setuptools:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/simplejson:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/JACK-Client:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/contextvars:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/dataclasses:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/entrypoints:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-2020:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/mysqlclient:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/opentracing:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pep8-naming:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/prettytable:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-nmap:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/atomicwrites:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/aws-xray-sdk:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/cryptography:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/editdistance:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/DateTimeRange:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/backports_abc:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/click-spinner:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/humanfriendly:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-gflags:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/beautifulsoup4:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/characteristic:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-bugbear:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-slugify:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/singledispatch:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-builtins:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-simplify:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/mypy-extensions:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-dateutil:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Flask-SQLAlchemy:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-docstrings:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-plugin-utils:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pytest-lazy-fixture:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-rst-docstrings:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-typing-imports:/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/backports.ssl_match_hostname',
]

path = [
    '/snap/pycharm-professional/300/plugins/python/helpers',
    '/snap/pycharm-professional/300/plugins/python/helpers/generator3',
    '/snap/pycharm-professional/300/plugins/python/helpers',
    '/usr/lib/python310.zip',
    '/usr/lib/python3.10',
    '/usr/lib/python3.10/lib-dynload',
    '/home/ramona/PycharmProjects/DjangoProjects/demo/venv/lib/python3.10/site-packages',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stdlib',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/six',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/boto',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/mock',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pytz',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/toml',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/annoy',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/babel',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/emoji',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/first',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/fpdf2',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ldap3',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/polib',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/redis',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/regex',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/retry',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ujson',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Pillow',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/PyYAML',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/bleach',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/caldav',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/docopt',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/enum34',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/hdbcli',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/invoke',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/passpy',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/psutil',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pycurl',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pynput',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pysftp',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/stripe',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/xxhash',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/PyMySQL',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/appdirs',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/certifi',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/chardet',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/chevron',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/passlib',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyaudio',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyvmomi',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/slumber',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/tzlocal',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/urllib3',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/vobject',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Markdown',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Pygments',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/aiofiles',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/colorama',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/croniter',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/docutils',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/filelock',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/html5lib',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/httplib2',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/jmespath',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/oauthlib',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/openpyxl',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/paramiko',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/psycopg2',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyflakes',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/requests',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/selenium',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/tabulate',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/toposort',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/waitress',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/braintree',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/decorator',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/freezegun',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ipaddress',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/playsound',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyOpenSSL',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyRFC3339',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/termcolor',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/ttkthemes',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/typed-ast',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Deprecated',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Flask-Cors',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/SQLAlchemy',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Send2Trash',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/cachetools',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/commonmark',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/dateparser',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/frozendict',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/jsonschema',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pyfarmhash',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/setuptools',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/simplejson',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/JACK-Client',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/contextvars',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/dataclasses',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/entrypoints',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-2020',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/mysqlclient',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/opentracing',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pep8-naming',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/prettytable',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-nmap',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/atomicwrites',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/aws-xray-sdk',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/cryptography',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/editdistance',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/DateTimeRange',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/backports_abc',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/click-spinner',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/humanfriendly',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-gflags',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/beautifulsoup4',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/characteristic',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-bugbear',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-slugify',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/singledispatch',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-builtins',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-simplify',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/mypy-extensions',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/python-dateutil',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/Flask-SQLAlchemy',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-docstrings',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-plugin-utils',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/pytest-lazy-fixture',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-rst-docstrings',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/flake8-typing-imports',
    '/snap/pycharm-professional/300/plugins/python/helpers/typeshed/stubs/backports.ssl_match_hostname',
]

path_hooks = [
    None, # (!) real value is "<class 'zipimport.zipimporter'>"
    None, # (!) real value is '<function FileFinder.path_hook.<locals>.path_hook_for_FileFinder at 0x7f611f648af0>'
]

path_importer_cache = {} # real value of type <class 'dict'> skipped

stderr = None # (!) real value is "<_io.TextIOWrapper name='<stderr>' mode='w' encoding='utf-8'>"

stdin = None # (!) real value is "<_io.TextIOWrapper name=5 mode='r' encoding='utf-8'>"

stdlib_module_names = None # (!) real value is "frozenset({'genericpath', 'imp', 'mimetypes', '_stat', 'ftplib', '_codecs_hk', 'opcode', '_symtable', 'zipimport', '_pydecimal', 'getopt', 'hmac', 'aifc', 'fnmatch', 'traceback', '_pickle', '_posixshmem', 'msvcrt', 'warnings', 'decimal', 'contextlib', 'http', 'nturl2path', 'concurrent', '_zoneinfo', '_weakrefset', 'pwd', '_curses', 'sqlite3', 'configparser', '_threading_local', 'cmath', 'collections', 'quopri', 'rlcompleter', 'sys', 'gettext', 'mmap', 'socket', 'unittest', '_ssl', 'select', 'posix', '_codecs', 'trace', 'xmlrpc', '_random', 'grp', 'pdb', 'pyexpat', 'code', 'pprint', '_sitebuiltins', 'struct', 'copyreg', 'cmd', 'webbrowser', 'bdb', 'winsound', 'nis', 'pathlib', '_elementtree', '_sha1', 'site', 'weakref', '_warnings', '_tracemalloc', '_tkinter', 'threading', 'symtable', 'netrc', '_bz2', 'json', '_ctypes', 'selectors', '_markupbase', 'sched', 'audioop', 'curses', 'sunau', '__future__', 'pipes', 'socketserver', 'string', '_sha3', 'shelve', 'fcntl', 'mailbox', 'encodings', 'pickletools', 'pkgutil', '_gdbm', '_uuid', 'sndhdr', 'array', 'base64', '_weakref', 'errno', 'inspect', 'numbers', '_sre', 'tarfile', 'codeop', 'idlelib', 'subprocess', '_operator', 'operator', 'functools', '_struct', 'graphlib', '_codecs_iso2022', '_compression', 'keyword', '_abc', 'ctypes', 'py_compile', 'importlib', '_collections', '_imp', 'gc', '_osx_support', 'bz2', '_overlapped', 'modulefinder', 'typing', 'xml', '_multiprocessing', 'tabnanny', 'filecmp', 'enum', 'glob', 'tkinter', 'marshal', 'math', 'difflib', 'tty', '_winapi', 'lib2to3', 'posixpath', 'cgitb', '_codecs_tw', 'secrets', 'xdrlib', 'turtledemo', '_hashlib', 'sre_parse', 'urllib', 'html', '_sha512', 'abc', 'multiprocessing', 'sysconfig', 'pydoc', 'platform', 'venv', 'binascii', 're', 'bisect', 'sre_constants', '_json', '_csv', 'plistlib', 'calendar', '_dbm', 'profile', 'turtle', 'zipapp', '_pyio', '_statistics', '_signal', 'types', 'compileall', 'asyncore', 'crypt', '_md5', '_heapq', '_sqlite3', 'binhex', 'doctest', 'datetime', 'ipaddress', 'heapq', '_py_abc', 'shlex', 'termios', 'asynchat', '_queue', 'csv', 'dis', '_thread', 'ensurepip', 'cProfile', 'pstats', '_frozen_importlib_external', '_string', 'dbm', '_lzma', 'tempfile', 'zipfile', 'locale', '_frozen_importlib', '_socket', '_functools', 'builtins', 'copy', 'signal', '_opcode', 'asyncio', '_decimal', '_msi', '_lsprof', '_multibytecodec', 'stringprep', 'timeit', 'imghdr', 'runpy', 'textwrap', 'contextvars', '_blake2', '_contextvars', 'fractions', 'readline', 'syslog', 'io', 'tracemalloc', '_crypt', 'uu', 'ast', '_compat_pickle', 'antigravity', 'faulthandler', '_strptime', 'queue', '_io', 'reprlib', 'unicodedata', 'uuid', 'wsgiref', 'imaplib', '_posixsubprocess', 'argparse', 'pty', '_codecs_jp', '_bisect', 'chunk', 'pickle', 'zoneinfo', 'gzip', 'token', 'nntplib', 'dataclasses', 'spwd', 'atexit', '_aix_support', 'lzma', 'email', '_bootsubprocess', 'fileinput', 'distutils', 'colorsys', '_datetime', 'hashlib', 'ntpath', 'optparse', 'random', 'smtplib', 'telnetlib', 'statistics', 'logging', '_codecs_cn', '_ast', 'shutil', 'mailcap', 'poplib', 'time', 'os', 'getpass', 'winreg', '_locale', '_codecs_kr', 'msilib', 'pyclbr', 'zlib', 'ssl', '_curses_panel', 'wave', 'smtpd', 'sre_compile', 'codecs', '_collections_abc', '_asyncio', 'cgi', 'itertools', 'ossaudiodev', 'tokenize', '_scproxy', 'stat', 'resource', 'linecache', '_sha256', 'this', 'nt', 'pydoc_data'})"

stdout = None # (!) forward: __stdout__, real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

thread_info = (
    'pthread',
    'semaphore',
    'NPTL 2.35',
)

version_info = (
    3,
    10,
    4,
    'final',
    0,
)

warnoptions = []

_git = (
    'CPython',
    '',
    '',
)

_xoptions = {}

__spec__ = None # (!) real value is "ModuleSpec(name='sys', loader=<class '_frozen_importlib.BuiltinImporter'>, origin='built-in')"

__stderr__ = stderr

__stdin__ = None # (!) real value is "<_io.TextIOWrapper name='<stdin>' mode='r' encoding='utf-8'>"

__stdout__ = None # (!) real value is "<_io.TextIOWrapper name='<stdout>' mode='w' encoding='utf-8'>"

# intermittent names
exc_value = Exception()
exc_traceback=None
