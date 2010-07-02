{
    'target_defaults': {
        'include_dirs': [
            '.',
            'include',
        ],
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
            'dependencies': [
                ':check-deps',
            ],
        },
        {
            'target_name': 'gtest_main',
            'type': '<(library)',
            'sources': [
                'src/gtest_main.cc',
            ],
            'dependencies': [
                ':check-deps',
                ':gtest',
            ],
        },
    ],
}
