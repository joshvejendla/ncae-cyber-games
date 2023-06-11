import ctypes
import ctypes.util
import mmap
#{# This should look like: fn = b'\xeb\x13\xb8\x01\x00\x00\x00\xbf\x01' #}
fn = {{ escaped_hex }}

def create_function_from_shellcode(shell_code, restype=ctypes.c_int64, argtypes=()):
    mm = mmap.mmap(-1, len(shell_code), flags=mmap.MAP_SHARED | mmap.MAP_ANONYMOUS, prot=mmap.PROT_WRITE | mmap.PROT_READ | mmap.PROT_EXEC)
    mm.write(shell_code)
    ctypes_buffer = ctypes.c_int.from_buffer(mm)
    function = ctypes.CFUNCTYPE(restype, *argtypes)(ctypes.addressof(ctypes_buffer))
    function._avoid_gc_for_mmap = mm
    return function

if __name__ == '__main__':
    function = create_function_from_shellcode(fn)
    result = function()
