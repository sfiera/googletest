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
                'src/gtest-printers.cc',
                'src/gtest-test-part.cc',
                'src/gtest-typed-test.cc',
                'src/gtest.cc',
            ],
            'direct_dependent_settings': {
                'include_dirs': [
                    'include',
                ],
            },
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
            'export_dependent_settings': [
                ':gtest',
            ],
        },
    ],
}
