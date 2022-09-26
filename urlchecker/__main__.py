import sys
import pathlib
import asyncio

from urlchecker.cli import read_user_cli_args, display_check_result
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

    for url in urls:

        error = ""

        try:

            result = connectivity_checker(url)
        
        except Exception as e:

            result = False
            error = str(e)

        display_check_result(result,url, error)


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

    if not urls:

        print("Error: No URLs to check", file=sys.stderr)
        sys.exit(1)
    
    if user_args.asynchronous:
        
        asyncio.run(_asynchronous_check(urls))
    
    else:

        _synchronous_check(urls)



if __name__ == "__main__":

    main()

