### GLM Pretty Printer

Provided the GDB pretty printers of GLM types such as vec4, and mat4 ..etc.
You can find the supported GLM types in testbed.cpp.

### Test Application
#### Build the testbed:
1. cmake -S . -B build -D CMAKE_BUILD_TYPE=Debug
2. cmake --build build

#### Run with gdb CLI
1. Configure the `.gdbinit` ([how gdb locate it](https://sourceware.org/gdb/current/onlinedocs/gdb.html/Initialization-Files.html)) to load pretty printers. See [,gdbinit](./.gdbinit) for an example.
3. gdb ./build/GLMPrettyPrinter
4. (gdb) break main
5. (gdb) run
6. (gdb) n 10
7. (gdb) p testMat4

#### Run within vscode
1. Create a launch task. See [.vscode/launch.json](./.vscode/launch.json) for an example
2. In vscode, add breakpoints in `testbed.cpp` and run it with `Start Debugging`


#### Additional Resources on GDB pretty printer
- [Gcc libsrdcxx pretty printer](https://github.com/gcc-mirror/gcc/blob/master/libstdc%2B%2B-v3/python/libstdcxx/v6/printers.py)
- [Clang libcxx pretty printer](https://github.com/koutheir/libcxx-pretty-printers)
- [Boost pretty printer](https://github.com/ruediger/Boost-Pretty-Printer)
- [Pretty printer of eigen types](https://github.com/dmillard/eigengdb): display the 2D matrix in the array format
- [Kokkos pretty printer ](https://github.com/Char-Aznable/GDBKokkos): display the data in a table like format

#### Known Issues
