from http.server import BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import requests

def handler(request):
    # Get the site URL from the query string (?site=...)
    parsed_url = urlparse(request.url)
    query_params = parse_qs(parsed_url.query)
    target_site = query_params.get('site', [None])[0]

    if not target_site:
        return {
            'statusCode': 400,
            'body': 'Missing "site" parameter'
        }

    try:
        # Fetch the content of the target site
        response = requests.get(target_site)
        return {
            'statusCode': 200,
            'headers': {
                'Content-Type': 'text/html',
                'Access-Control-Allow-Origin': '*'
            },
            'body': response.text
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': f'Error fetching site: {str(e)}'
        }
