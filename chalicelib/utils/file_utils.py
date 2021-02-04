import os
import logging

logger = logging.getLogger()


def find_file(file_name: str, search_from_base_path: str = None) -> str:
    """ Function to return full path from the system

    Args:
        file_name (str): Target file name
        search_from_base_path (str, optional): [base search path]. Defaults to None.

    Raises:
        FileNotFoundError: When function failed to find the target file

     Returns:
        str: Target full path.
    """
    if search_from_base_path is None:
        search_from_base_path = os.path.dirname(
            os.path.dirname(os.path.abspath(__file__)))
    logger.info(f"Start find_file: {file_name}, search from {search_from_base_path}")

    file_path = None
    # Get current location as base path
    for root, directories, files in os.walk(search_from_base_path, topdown=False):
        for name in files:
            if name == file_name:
                logger.debug(f"File: {file_name} found. {root}")
                file_path = os.path.join(root, name)
    if file_path is None:
        raise FileNotFoundError(f"File {file_name} not found.")

    logger.info(f"End file_file: {file_name}: {file_path}")
    return file_path


def get_static_file(file_name: str, search_from_base_path: str = None) -> str:
    """Function to return file content

    Args:
        file_name (str): Target file
        search_from_base_path (str, optional): [base search path]. Defaults to None.

    Returns:
        str: Return content of the file as string
    """
    try:
        logger.info(f"get_static_file: {file_name}")
        content = None
        static_file_path = find_file(
            file_name, search_from_base_path)
        if static_file_path is not None:
            with open(static_file_path) as f:
                content = f.read()
                logger.debug(content)
                # print(content)
                if content is None or len(content) == 0:
                    raise ValueError(f"Empty content {file_name}")
        return content
    except Exception as ex:
        logger.error(f"Failed to read '{file_name}: Error: {ex}'")
        raise
