# -*- mode: python -*-

def common(ctx):
    ctx.load("compiler_cxx")
    ctx.load("core externals", "ext/waf-sfiera")

def options(opt):
    common(opt)

def configure(cnf):
    common(cnf)
    cnf.check(lib="pthread", uselib_store="googletest/system/pthread")

def build(bld):
    common(bld)

    bld.stlib(
        target="googletest/gtest",
        features="universal",
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
        defines="GTEST_USE_OWN_TR1_TUPLE",
        includes=". ./include",
        export_includes="./include",
        use="googletest/system/pthread",
    )

    bld.stlib(
        target="googletest/gtest_main",
        features="universal",
        source="src/gtest_main.cc",
        cxxflags="-Wall -Werror",
        defines="GTEST_USE_OWN_TR1_TUPLE",
        use="googletest/gtest",
    )
