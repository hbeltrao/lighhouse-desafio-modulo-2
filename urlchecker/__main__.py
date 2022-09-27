import sys
import pathlib
import asyncio

import time
import datetime

import csv


from urlchecker.cli import read_user_cli_args, display_check_result, store_check_result
from urlchecker.checker import connectivity_checker, async_connectivity_checker


def _get_websites_urls(user_args):

    urls= user_args.urls

    if user_args.input_file:

        urls += _read_urls_from_file(user_args.input_file)
    
    return urls


def _read_urls_from_file(file):

    file_path = pathlib.Path(file)

    if file_path.is_file():

        with file_path.open() as urls_file:

            urls = [url.strip() for url in urls_file]

            if urls:

                return urls
            
            print(f"Error: empty input file, {file}", file= sys.stderr)

    else :

        print("Error: File not found", file= sys.stderr)

    return []


def _synchronous_check(urls):

    check_result = []

    for url in urls:

        error = ""


        try:

            result = connectivity_checker(url)
        
        except Exception as e:

            result = False
            error = str(e)

        display_check_result(result,url, error)

        check_result.append(store_check_result(result,url, error))
    
    return check_result


async def _asynchronous_check(urls):

    async def _check(url):

        error = ""
        try:
            result = await async_connectivity_checker(url)
        
        except Exception as e:
            result = False
            error = str(e)
        
        display_check_result(result, url, error)
    
    await asyncio.gather(*(_check(url) for url in urls))


def main():
    """
    Run URL Checker.
    """

    user_args = read_user_cli_args()

    urls = _get_websites_urls(user_args)

    timestamp = str(datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d_%H-%M-%S'))

    if not urls:

        print("Error: No URLs to check", file=sys.stderr)
        sys.exit(1)
    
    if user_args.asynchronous:
        
        asyncio.run(_asynchronous_check(urls))
    
    else:

        check_results = _synchronous_check(urls)

    if user_args.save_result:

        with open("results/"+timestamp+".csv", "a") as file:   
            #configure writer to write standard csv file
            writer = csv.writer(file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            writer.writerow(['timestamp', 'URL', 'result', 'error'])
            for item in check_results:
                #Write item to file
                writer.writerow([item[0], item[1], item[2], item[3]])
    


if __name__ == "__main__":

    main()

