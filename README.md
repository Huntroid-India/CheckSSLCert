# CheckSSLCert
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")


[![Huntroid-India - SSLCheckerr](https://img.shields.io/static/v1?label=Huntroid-India&message=CheckSSLCert&color=blue&logo=github)](https://github.com/Huntroid-India/CheckSSLCert "Go to GitHub repo")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![stars - SSLChecker](https://img.shields.io/github/stars/Huntroid-India/CheckSSLCert?style=social)](https://github.com/Huntroid-India/CheckSSLCert)
[![forks - SSLChecker](https://img.shields.io/github/forks/Huntroid-India/CheckSSLCert?style=social)](https://github.com/Huntroid-India/CheckSSLCert)
[![GitHub release](https://img.shields.io/github/release/Huntroid-India/CheckSSLCert?include_prereleases=&sort=semver&color=blue)](https://github.com/Huntroid-India/CheckSSLCert/releases/)
[![issues - SSLCheckerr](https://img.shields.io/github/issues/Huntroid-India/CheckSSLCert)](https://github.com/Huntroid-India/CheckSSLCert/issues)

CheckSSLCert is a Python library that allows you to check the SSL certificate status for single or multiple domains. It provides an easy way to determine if an SSL certificate is active, the number of days left until it expires, and additional certificate information. 

## Installation
You can install CheckSSLCert using pip:
```
pip install CheckSSLCert
```

## Usage
### SSL Validation (Single Domain)
To check the SSL certificate status for a single domain, you can use the from_link function from validate class. Here's a sample code demonstrating the usage:
```
from CheckSSLCert import validate

# Create an sslchecker object for the domain
checker = validate.from_link("example.com")

# Check the SSL certificate status
status = checker.IsActive()
days_left = checker.getDayLeft()
info = checker.getInfo()

# Print the results
print("SSL Status:", status)
print("Days Left:", days_left)
print("Certificate Info:", info)

# Print the SSL certificate Report
print(checker)
```

### Bulk SSL Validation (Multiple Domains - CSV File)
To check the SSL certificate status for multiple domains, you can use the from_file function from validate class. Here's a sample code demonstrating the usage:
```
from CheckSSLCert import validate

# Create a bulksslchecker object with the path to the domain list file (CSV format)
checker = validate.from_file("domain_list.csv")

# Print the SSL certificate status report to the console
checker.print_report()

# Save the SSL certificate status report to a file (HTML format)
checker.save_report("C:\Users\YourUsername\Desktop") # By default HTML is selected
checker.save_report("C:\Users\YourUsername\Desktop", "html")

# Save the SSL certificate status report to a file (CSV format)
checker.save_report("C:\Users\YourUsername\Desktop", "csv")
```
### Domain List File Format
The domain list file should be in CSV format. The first row should contain the column names. Here's a sample domain list file:

[![CSV - Documentation](https://img.shields.io/badge/Download-CSV-blue?style=for-the-badge)](https://raw.githubusercontent.com/Huntroid-India/CheckSSLCert/main/domain_list.csv "Go to project documentation")

#### File Format


| S.No | Website_Name      | Website_URL        |
|------|-------------------|--------------------|
| 1 | Google            | https://google.com |
| 2 | Facebook - Mobile | https://m.facebook.com     |
| 3 | Twitter           | www.twitter.com    |





## Contribution
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request.

## License

Released under [MIT](/LICENSE) by [@Huntroid-India](https://github.com/Huntroid-India).


