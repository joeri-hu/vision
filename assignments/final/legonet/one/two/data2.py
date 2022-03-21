##
# @file       data.py
# @brief      ...
# @version    0.1
# @date       March 2022
# @author     Joeri Kok (joeri.j.kok@student.hu.nl)
# @copyright  GPL-3.0 License
#
import os
from collections.abc import Callable, Iterator


def findpaths(check: Callable[[os.DirEntry], bool], path: str='.') -> Iterator[str]:
    """!
    @brief List files within a given path with a given extension.
    @details ...

    @param[in] path ..
    @param[in] ext ..
    @return ..
    """
    with os.scandir(path) as it:
        for entry in it:
            print(entry.name)
            if check(entry):
                yield entry.name


def findfiles(path: str='.', ext: str='') -> Iterator[str]:
    """!
    @brief List files within a given path with a given extension.
    @details ...

    @param[in] path ..
    @param[in] ext ..
    @return ..
    """
    yield from findpaths(os.DirEntry.is_file if not ext
        else lambda entry: entry.is_file()
            and entry.name.endswith('.' + ext))
            # and entry.name.endswith('.'.join(ext)))


def finddirs(path: str='.') -> Iterator[str]:
    """!
    @brief List files within a given path with a given extension.
    @details ...

    @param[in] path ..
    @param[in] ext ..
    @return ..
    """
    yield from findpaths(os.DirEntry.is_dir)

