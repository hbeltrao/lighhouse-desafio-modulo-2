# importing function to create a HTTP connection
from http.client import HTTPConnection

# importing function to handle url data easier
from urllib.parse import urlparse

# importing library to handle asynchronous execution
import asyncio
import aiohttp


def connectivity_checker(url, timeout=2):

    """
    Return True if the target URL is online.

    Raise an exception otherwise.
    """

    error = Exception("unknown error")
    parser = urlparse(url)

    # variable containing the hostname of the target url
    host = parser.netloc or parser.path.split("/")[0]

    # using the for loop to test booth 80 and 443 ports
    for port in (80, 443):

        connection = HTTPConnection(host=host, port=port, timeout=timeout)

        try:
            connection.request("HEAD", "/")
            return True

        except Exception as e:
            error = e
        
        finally:
            connection.close()
    
    raise error

# Function for test connectivity of URLs asynchronously
async def async_connectivity_checker(url, timeout=2):
    """
    Return True if the target URL is online.

    Raise an exception otherwise.
    """

    error = Exception("unknown error")
    parser = urlparse(url)

    host = parser.netloc or parser.path.split("/")[0]

    for scheme in ("http", "https"):

        target_url = scheme + "://" + host

        async with aiohttp.ClientSession() as session:
            try:
                await session.head(target_url, timeout= timeout)
                return True
            
            except asyncio.exceptions.TimeoutError:
                error = Exception("timed out")
            
            except Exception as e:
                error = e

    raise error


