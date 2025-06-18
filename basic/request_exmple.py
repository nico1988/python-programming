import requests
import logging

x = requests.get('https://www.runoob.com/')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"Response status code: {x.status_code}")
logging.info(f"Response headers: {x.headers}")
logging.info(f"Response content: {x.text[:100]}...")  # Log only the first 100 characters of the content
logging.info(f"Response URL: {x.url}")
logging.info(f"Response encoding: {x.encoding}")
logging.info(f"Response elapsed time: {x.elapsed.total_seconds()} seconds")
logging.info(f"Response history: {x.history}")
logging.info(f"Response cookies: {x.cookies}")
logging.info(f"Response JSON (if available): {x.json() if x.headers.get('Content-Type') == 'application/json' else 'No JSON response'}")
logging.info(f"Response request method: {x.request.method}")
logging.info(f"Response request URL: {x.request.url}")
logging.info(f"Response request headers: {x.request.headers}")
logging.info(f"Response request body: {x.request.body if x.request.body else 'No request body'}")
logging.info(f"Response status code description: {requests.status_codes._codes[x.status_code][0] if x.status_code in requests.status_codes._codes else 'Unknown status code'}")
logging.info(f"Response reason phrase: {x.reason}")
logging.info(f"Response connection status: {'x.connection' in x.__dict__ and x.connection or 'No connection info available'}")
logging.info(f"Response content type: {x.headers.get('Content-Type', 'No Content-Type header')}")
logging.info(f"Response content length: {x.headers.get('Content-Length', 'No Content-Length header')}")