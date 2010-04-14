{
    'target_defaults': {
        'include_dirs': [
            '.',
            'include',
        ],
        'xcode_settings': {
            'GCC_TREAT_WARNINGS_AS_ERRORS': 'YES',
            'GCC_SYMBOLS_PRIVATE_EXTERN': 'YES',
            'SDKROOT': 'macosx10.4',
            'GCC_VERSION': '4.0',
            'ARCHS': 'ppc x86_64 i386',
            'WARNING_CFLAGS': [
                '-Wall',
                '-Wendif-labels',
            ],
        },
    },
    'targets': [
        {
            'target_name': 'gtest',
            'type': '<(library)',
            'sources': [
                'src/gtest-death-test.cc',
                'src/gtest-filepath.cc',
                'src/gtest-port.cc',
                'src/gtest-test-part.cc',
                'src/gtest-typed-test.cc',
                'src/gtest.cc',
            ],
        },
        {
            'target_name': 'gtest_main',
            'type': '<(library)',
            'sources': [
                'src/gtest_main.cc',
            ],
            'dependencies': [
                ':gtest',
            ],
        },
    ],
}
