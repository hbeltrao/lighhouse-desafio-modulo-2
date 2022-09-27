import argparse
from os import times

import time
import datetime

def read_user_cli_args():
    """
    handle the CLI arguments and options.
    """

    parser = argparse.ArgumentParser(
        prog="urlchecker", description= "check website conectivity"
    )

    parser.add_argument(
        "-u",
        "--urls",
        metavar= "URLs",
        nargs= "+",
        type= str,
        default= [],
        help= "enter one or more website URLs"
    )

    parser.add_argument(
        "-f",
        "--input-file",
        metavar= "FILE",
        type= str,
        default= "",
        help= "read URLs from a file"
    )

    parser.add_argument(
        "-a",
        "--asynchronous",
        action="store_true",
        help="run the connectivity check asynchronously"
    )

    parser.add_argument(
        "-s",
        "--save_result",
        action="store_true",
        help="save the result in a csv file"
    )

    return parser.parse_args()


def display_check_result(result, url, error=""):

    """
    Display the result of a connectivity check.
    """

    print(f'The status of "{url}" is:', end=" ")

    if result:
        print('"Online!" 👍')
        
    else:
        print(f'"Offline?" 👎 \n  Error: "{error}"')

def store_check_result(result, url, error=""):

    timestamp = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')

    result = [timestamp, url, result, error]

    return result


