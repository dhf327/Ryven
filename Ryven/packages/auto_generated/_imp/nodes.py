import ryvencore_qt as rc
import _imp


class AutoNode__imp__fix_co_filename(rc.Node):
    title = '_fix_co_filename'
    type_ = '_imp'
    description = '''Changes code.co_filename to specify the passed-in file path.

  code
    Code object to change.
  path
    File path to use.'''
    init_inputs = [
        rc.NodeInputBP(label='code'),
rc.NodeInputBP(label='path'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp._fix_co_filename(self.input(0), self.input(1)))
        


class AutoNode__imp_acquire_lock(rc.Node):
    title = 'acquire_lock'
    type_ = '_imp'
    description = '''Acquires the interpreter's import lock for the current thread.

This lock should be used by import hooks to ensure thread-safety when importing
modules. On platforms without threads, this function does nothing.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.acquire_lock())
        


class AutoNode__imp_create_builtin(rc.Node):
    title = 'create_builtin'
    type_ = '_imp'
    description = '''Create an extension module.'''
    init_inputs = [
        rc.NodeInputBP(label='spec'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.create_builtin(self.input(0)))
        


class AutoNode__imp_exec_builtin(rc.Node):
    title = 'exec_builtin'
    type_ = '_imp'
    description = '''Initialize a built-in module.'''
    init_inputs = [
        rc.NodeInputBP(label='mod'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.exec_builtin(self.input(0)))
        


class AutoNode__imp_exec_dynamic(rc.Node):
    title = 'exec_dynamic'
    type_ = '_imp'
    description = '''Initialize an extension module.'''
    init_inputs = [
        rc.NodeInputBP(label='mod'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.exec_dynamic(self.input(0)))
        


class AutoNode__imp_extension_suffixes(rc.Node):
    title = 'extension_suffixes'
    type_ = '_imp'
    description = '''Returns the list of file suffixes used to identify extension modules.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.extension_suffixes())
        


class AutoNode__imp_get_frozen_object(rc.Node):
    title = 'get_frozen_object'
    type_ = '_imp'
    description = '''Create a code object for a frozen module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.get_frozen_object(self.input(0)))
        


class AutoNode__imp_init_frozen(rc.Node):
    title = 'init_frozen'
    type_ = '_imp'
    description = '''Initializes a frozen module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.init_frozen(self.input(0)))
        


class AutoNode__imp_is_builtin(rc.Node):
    title = 'is_builtin'
    type_ = '_imp'
    description = '''Returns True if the module name corresponds to a built-in module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.is_builtin(self.input(0)))
        


class AutoNode__imp_is_frozen(rc.Node):
    title = 'is_frozen'
    type_ = '_imp'
    description = '''Returns True if the module name corresponds to a frozen module.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.is_frozen(self.input(0)))
        


class AutoNode__imp_is_frozen_package(rc.Node):
    title = 'is_frozen_package'
    type_ = '_imp'
    description = '''Returns True if the module name is of a frozen package.'''
    init_inputs = [
        rc.NodeInputBP(label='name'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.is_frozen_package(self.input(0)))
        


class AutoNode__imp_lock_held(rc.Node):
    title = 'lock_held'
    type_ = '_imp'
    description = '''Return True if the import lock is currently held, else False.

On platforms without threads, return False.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.lock_held())
        


class AutoNode__imp_release_lock(rc.Node):
    title = 'release_lock'
    type_ = '_imp'
    description = '''Release the interpreter's import lock.

On platforms without threads, this function does nothing.'''
    init_inputs = [
        
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.release_lock())
        


class AutoNode__imp_source_hash(rc.Node):
    title = 'source_hash'
    type_ = '_imp'
    description = ''''''
    init_inputs = [
        rc.NodeInputBP(label='key'),
rc.NodeInputBP(label='source'),
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = '#32DA22'

    def update_event(self, input_called=-1):
        self.set_output_val(0, _imp.source_hash(self.input(0), self.input(1)))
        