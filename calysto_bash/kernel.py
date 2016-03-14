from __future__ import print_function

from metakernel import MetaKernel

from . import __version__


class BashKernel(MetaKernel):
    implementation = 'Calysto Bash'
    implementation_version = __version__
    language = 'bash'
    language_version = __version__
    banner = "Calysto Bash - interact with bash"
    language_info = {
        'mimetype': 'text/x-sh',
        'name': 'bash',
        'file_extension': '.sh',
        "version": __version__,
        'help_links': MetaKernel.help_links,
    }

    def get_usage(self):
        return "This is the bash kernel."

    def do_execute_direct(self, code):
        if not code.strip():
            return
        self.log.debug('execute: %s' % code)
        shell_magic = self.line_magics['shell']
        shell_magic.eval(code.strip())
        self.log.debug('execute done')

    def get_completions(self, info):
        shell_magic = self.line_magics['shell']
        return shell_magic.get_completions(info)

    def get_kernel_help_on(self, info, level=1, none_on_fail=False):
        code = info['code'].strip()
        if not code or len(code.split()) > 1:
            if none_on_fail:
                return None
            else:
                return ""
        shell_magic = self.line_magics['shell']
        return shell_magic.get_help_on(info, 1)

    def repr(self, data):
        return data
