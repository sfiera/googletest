# -*- mode: python -*-

DEFAULTS = {
    "cxxflags": "-Wall -Werror",
    "arch": "x86_64 i386 ppc",
}

def common(ctx):
    ctx.load("compiler_cxx")
    ctx.load("externals", "ext/waf-sfiera")
    ctx.load("platforms", "ext/waf-sfiera")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)

def build(bld):
    common(bld)

    bld.stlib(
        target="googletest/gtest",
        source=[
            "src/gtest-death-test.cc",
            "src/gtest-filepath.cc",
            "src/gtest-port.cc",
            "src/gtest-printers.cc",
            "src/gtest-test-part.cc",
            "src/gtest-typed-test.cc",
            "src/gtest.cc",
        ],
        cxxflags="-Wall -Werror",
        arch="x86_64 i386 ppc",
        includes=". ./include",
        export_includes="./include",
        use="googletest/common",
    )

    bld.stlib(
        target="googletest/gtest_main",
        source="src/gtest_main.cc",
        cxxflags="-Wall -Werror",
        arch="x86_64 i386 ppc",
        use=[
            "googletest/common",
            "googletest/gtest",
        ],
    )
