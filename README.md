# SSLChecker

[![Huntroid-India - SSLCheckerr](https://img.shields.io/static/v1?label=Huntroid-India&message=SSLCheckerr&color=blue&logo=github)](https://github.com/Huntroid-India/SSLCheckerr "Go to GitHub repo")
[![stars - SSLCheckerr](https://img.shields.io/github/stars/Huntroid-India/SSLCheckerr?style=social)](https://github.com/Huntroid-India/SSLCheckerr)
[![forks - SSLCheckerr](https://img.shields.io/github/forks/Huntroid-India/SSLCheckerr?style=social)](https://github.com/Huntroid-India/SSLCheckerr)


[![GitHub release](https://img.shields.io/github/release/Huntroid-India/SSLCheckerr?include_prereleases=&sort=semver&color=blue)](https://github.com/Huntroid-India/SSLCheckerr/releases/)
[![License](https://img.shields.io/badge/License-MIT-blue)](#license)
[![issues - SSLCheckerr](https://img.shields.io/github/issues/Huntroid-India/SSLCheckerr)](https://github.com/Huntroid-India/SSLCheckerr/issues)

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



