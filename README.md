# SSLChecker
[![Made with Python](https://img.shields.io/badge/Python->=3.6-blue?logo=python&logoColor=white)](https://python.org "Go to Python homepage")


[![Huntroid-India - SSLCheckerr](https://img.shields.io/static/v1?label=Huntroid-India&message=SSLChecker&color=blue&logo=github)](https://github.com/Huntroid-India/SSLChecker "Go to GitHub repo")
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![stars - SSLChecker](https://img.shields.io/github/stars/Huntroid-India/SSLChecker?style=social)](https://github.com/Huntroid-India/SSLChecker)
[![forks - SSLChecker](https://img.shields.io/github/forks/Huntroid-India/SSLChecker?style=social)](https://github.com/Huntroid-India/SSLChecker)
[![GitHub release](https://img.shields.io/github/release/Huntroid-India/SSLChecker?include_prereleases=&sort=semver&color=blue)](https://github.com/Huntroid-India/SSLChecker/releases/)
[![issues - SSLCheckerr](https://img.shields.io/github/issues/Huntroid-India/SSLChecker)](https://github.com/Huntroid-India/SSLChecker/issues)

SSLChecker is a Python library that allows you to check the SSL certificate status for single or multiple domains. It provides an easy way to determine if an SSL certificate is active, the number of days left until it expires, and additional certificate information. 

## Installation
You can install SSLChecker using pip:
```
pip install SSLChecker
```

## Usage
### SSL Checker (Single Domain)
To check the SSL certificate status for a single domain, you can use the sslchecker class. Here's a sample code demonstrating the usage:
```
from SSLChecker import sslchecker

# Create an sslchecker object for the domain
checker = sslchecker.sslchecker("example.com")

# Check the SSL certificate status
status = checker.IsActive()
days_left = checker.getDayLeft()
info = checker.getInfo()

# Print the results
print("SSL Status:", status)
print("Days Left:", days_left)
print("Certificate Info:", info)
```

### Bulk SSL Checker (Multiple Domains)
To check the SSL certificate status for multiple domains in bulk, you can use the bulksslchecker class. Here's a sample code demonstrating the usage:
```
from SSLChecker import bulksslchecker

# Create a bulksslchecker object with the path to the domain list file (CSV format)
checker = bulksslchecker.bulksslchecker("domain_list.csv")

# Print the SSL certificate status report to the console
checker.print_report()

# Save the SSL certificate status report to a file (HTML format)
checker.save_report("C:\Users\YourUsername\Desktop") # By default HTML is selected
checker.save_report("C:\Users\YourUsername\Desktop", "html")

# Save the SSL certificate status report to a file (CSV format)
checker.save_report("C:\Users\YourUsername\Desktop", "csv")
```

## Contribution
Contributions are welcome! If you have any suggestions, improvements, or bug fixes, please submit a pull request.

## License

Released under [MIT](/LICENSE) by [@Huntroid-India](https://github.com/Huntroid-India).



