from unittest.mock import MagicMock

import _io

_old_open = open

def conditionally_mock_open(path, read_data=None):
    # stolen from mock.patch
    file_spec = list(set(dir(_io.TextIOWrapper)).union(set(dir(_io.BytesIO))))
    handle = MagicMock(spec=file_spec)
    handle.write.return_value = None
    handle.__enter__.return_value = handle
    handle.read.return_value = read_data
    def patched_open(name, mode='r'):
        if path in name:
            return _old_open(name, mode)
        else:
            return handle

    return patched_open
