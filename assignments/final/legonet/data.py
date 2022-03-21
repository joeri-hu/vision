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


# def findentries(check: Callable[[os.DirEntry], bool], path: str='.') -> Iterator[str]:
def findentries(path: str='.') -> Iterator[str]:
    """!
    @brief Finds files or directories within the given path.

    @param[in] check Criteria that must be satisfied by each entry.
    @param[in] path  Location where to look.

    @return Yields the name of each file or directory found.
    """
    # with os.scandir(path) as it:
    #     for entry in it:
    #         if check(entry):
    #             yield entry.name
    with os.scandir(path) as iter:
        yield from iter


def getentryname(entry: os.DirEntry, path: str='.') -> str:
    """!
    @brief Finds directories within the given path.
    @param[in] path Location where to look.
    @return Yields the name of each directory found.
    """
    return f'{path}/{entry.name}'


def finddirs(path: str='.') -> Iterator[str]:
    """!
    @brief Finds directories within the given path.
    @param[in] path Location where to look.
    @return Yields the name of each directory found.
    """
    # yield from _find_entries(os.DirEntry.is_dir, path)
    # for entry
    # (item for item in _find_entries(path) if item.is_dir())
    # yield from filter(os.DirEntry.is_dir, findentries(path))
    # yield from filter(lambda entry: entry.name if entry.is_dir() else False, findentries(path))
    # yield from map(getentryname, filter(os.DirEntry.is_dir, findentries(path)))
    yield from map(lambda entry: getentryname(entry, path),
        filter(os.DirEntry.is_dir, findentries(path)))
    # for entry in findentries(path):
    #     if entry.is_dir():
    #         yield entry.name


def rfinddirs(path: str='.') -> Iterator[str]:
    """!
    @brief  Recursively finds files within the given path with the given file extension.
    @detail Walks through each subdirectory to find files.
    @param[in] path Location where to look.
    @return Yields the name of each file found.
    """
    for dir in finddirs(path):
        # rdir: str = f'{path}/{dir}'
        # yield rdir
        # yield from rfinddirs(rdir)
        yield dir
        # yield from rfinddirs(f'{path}/{dir}')
        yield from rfinddirs(dir)


def findfiles(path: str='.', ext: str='') -> Iterator[str]:
    """!
    @brief  Finds files within the given path with the given file extension.
    @detail If no file extension is provided, any file matches.

    @param[in] path Location where to look.
    @param[in] ext  Extension of the files to find.

    @return Yields the name of each file found.
    """
    # yield from _find_entries(path=path,
    #     check=os.DirEntry.is_file if not ext else lambda entry:
    #         entry.is_file() and entry.name.endswith('.' + ext))
    #
    # yield from filter(os.DirEntry.is_file if not ext else lambda entry:
    #     entry.is_file() and entry.name.endswith('.' + ext), findentries(path))
    yield from map(lambda entry: getentryname(entry, path),
        filter(getfilecheck(ext), findentries(path)))


def getfilecheck(ext: str='') -> bool:
    """!
    @brief  Recursively finds files within the given path with the given file extension.
    @detail Walks through each subdirectory to find files.
    @param[in] path Location where to look.
    @return Yields the name of each file found.
    """
    return (os.DirEntry.is_file if not ext else lambda entry:
        entry.is_file() and entry.name.endswith('.' + ext))


def rfindfiles(path: str='.', ext: str='') -> Iterator[str]:
    """!
    @brief  Recursively finds files within the given path with the given file extension.
    @detail Walks through each subdirectory to find files.

    @param[in] path Location where to look.
    @param[in] ext  Extension of the files to find.

    @return Yields the name of each file found.
    """
    # yield from findfiles(path, ext)
    # for dir in finddirs(path):
    #     yield from rfindfiles(f'{path}/{dir}', ext)
    #
    check = getfilecheck(ext)
    for entry in findentries(path):
        if check(entry):
            yield getentryname(entry, path)
        elif entry.is_dir():
            yield from rfindfiles(getentryname(entry, path), ext)




