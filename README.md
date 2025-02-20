# Burp Suite Request Parser

## Overview

This Python application parses Burp Suite request and response logs stored in XML format. It extracts relevant information from the requests and responses, including method, URL, headers, body, status, and MIME type.

## Features

- Parses Burp Suite XML request and response logs.

- Decodes Base64-encoded request and response bodies.

- Stores parsed data in structured classes.

- Provides easy access to request and response attributes.

## Usage

Create an instance and read the exported Burp Suite file.

```python
from burp_reader import BurpRequests

burp_requests = BurpRequests("path/to/burp_export.xml")
```

Access the parsed date in the burp_requests object.

```python
for req, res in burp_requests.items:
    print("Method:", req.method)
    print("URL:", req.url)
    print("Decoded Request:", req.raw_request[:500])  # Print first 500 characters
    print("Response MIME Type:", res.mimetype)
    print("Decoded Response:", res.raw_response[:500])  # Print first 500 characters
```

Example output:

```bash
Request Method: POST
Request URL: http://127.0.0.1:8888/csrf_3.php
Decoded Request: POST /csrf_3.php HTTP/1.1\nHost: 127.0.0.1:8888\nContent-Length: 34\n...
Response MIME Type: HTML
Decoded Response: HTTP/1.1 200 OK\nDate: Mon, 17 Feb 2025 15:14:09 GMT\nServer: Apache/2.4.7 (Ubuntu)\n...
```


## Extracting Requests Only

Use the burp_request_extract python library.

```python
from burp_request_extract import BurpReader

reader = BurpReader()
reader.parse_requests(file_path='path/to/burp_file')
raw_http_requests = reader.get_raw_requests()
```





