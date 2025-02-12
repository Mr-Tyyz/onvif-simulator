import sys
import collections

if sys.version_info >= (3, 3):
    import collections.abc
    collections.Sequence = collections.abc.Sequence
    collections.Mapping = collections.abc.Mapping
    collections.MutableMapping = collections.abc.MutableMapping
    collections.Iterator = collections.abc.Iterator