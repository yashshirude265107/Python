'''Q.3)Create list of urls and you need to filter out only those that start with 'https'
for Example:
 urls = [
 "http://example.com",
 "https://secure-site.com",
 "ftp://files.example.org",
 "https://another-secure-site.com"
 ]'''
 
urls = [
    "http://example.com",
    "https://secure-site.com",
    "ftp://files.example.org",
    "https://another-secure-site.com"
]

# Filter out URLs that start with 'https'
https_urls = [url for url in urls if url.startswith('https')]

print(https_urls)
