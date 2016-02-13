"""Example use of jupyter_kernel_test, with tests for IPython."""

import unittest
import jupyter_kernel_test as jkt


class BashKernelTests(jkt.KernelTests):
    kernel_name = "calysto_bash"

    language_name = "bash"

    code_hello_world = "echo 'hello, world'"

    completion_samples = [
        {
            'text': 'fdis',
            'matches': {'fdisk'},
        },
    ]

    code_page_something = "ls?"

if __name__ == '__main__':
    unittest.main()
