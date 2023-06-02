class from_file:

    def __init__(self, path):
        import datetime
        self.__path = path
        self.__subject = "SSL Certificate Status Report on " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M:%S %p %z")
        self.__d_sno = []
        self.__d_name = []
        self.__d_link = []
        self.__d_status = []
        self.__d_days = []
        self.__d_info = []
        self.__m_row = [["S.NO", "Site Name", "Domain", "Status", "Days Left", "Error Info"]]
        if str(self.__path).endswith(".csv"):
            self.__bulksslchecker()
        else:
            raise IOError("Invalid File Format : " + str(self.__path).split('.')[-1])
        self.__mail_data = ""

    def __bulksslchecker(self):
        cnt, ttl = 0, 0

        try:
            with open(self.__path, 'r') as f:
                ttl = len(f.readlines())

            with open(self.__path, 'r') as f:
                print("Bulk SSL Validation Started")
                for line in f:

                    cnt += 1
                    print("\rProgress : " + str(round((cnt / ttl) * 100, 0)) + " % ", end='')

                    if not line.split(',')[0].isnumeric():
                        continue

                    line = str(line).replace('\n', '')
                    self.__d_sno.append(line.split(',')[0])
                    self.__d_name.append(line.split(',')[1])
                    self.__d_link.append(line.split(',')[2])
                    sc = from_link(self.__d_link[-1])
                    if sc.IsActive():
                        self.__d_status.append("Active")
                        self.__d_info.append("-")
                    else:
                        self.__d_status.append("Inactive")
                        self.__d_info.append(sc.getInfo().split('\n')[0])
                    self.__d_days.append(sc.getDayLeft())

                    if len(self.__m_row) > 0:
                        self.__m_row.append(
                            [self.__d_sno[-1], self.__d_name[-1], self.__d_link[-1], self.__d_status[-1],
                             self.__d_days[-1],
                             self.__d_info[-1]])

            print("\nBulk SSL Validation Completed")
            return self.__m_row
        except FileNotFoundError:
            print("\nError : File Not Found")
        except Exception as e:
            print("\nError : " + str(e))

    def __compose_email_with_table(self, table_data):
        # Create the email body with HTML formatting
        email_body = """
        <html>
            <head>
                  <title>{head}</title>
                  <style>
                    body {{
                        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Oxygen, Ubuntu, Cantarell, 'Open Sans', 'Helvetica Neue', sans-serif;
                        background-color: #fafcff;
                        display: table-cell;
                        vertical-align: middle;
                      }}

                    html {{
                        display: table;
                        margin: auto;
                      }}
                  </style>
                </head>

                <body>
                  <h2>{subject}</h2>
                  <table border=".5" cellpadding="5" cellspacing="0">
                    <tr>{headers}</tr>
                    {rows}
                  </table>
                </body>
        </html>
           """.format(head=self.__subject,
                      subject=self.__subject,
                      headers=''.join(['<th>{}</th>'.format(header) for header in table_data[0]]),
                      rows=''.join([
                          '<tr style="background-color: #C70039;">{}</tr>'.format(''.join(
                              ['<td>{}</td>'.format(cell) for cell in row]
                          )) if row[3] == 'Inactive' or int(row[4]) in range(0, 8) else (
                              '<tr style="background-color: #FF5733;">{}</tr>'.format(''.join(
                                  ['<td>{}</td>'.format(cell) for cell in row]
                              ))) if int(row[4]) in range(8, 15) else (
                              '<tr style="background-color: #FFC300 ;">{}</tr>'.format(''.join(
                                  ['<td>{}</td>'.format(cell) for cell in row]
                              ))) if int(row[4]) in range(15, 31) else (
                              '<tr style="background-color: #DAF7A6 ;">{}</tr>'.format(''.join(
                                  ['<td>{}</td>'.format(cell) for cell in row]
                              ))) if int(row[4]) in range(31, 61) else '<tr>{}</tr>'.format(''.join(
                              ['<td>{}</td>'.format(cell) for cell in row]
                          )) for row in table_data[1:]
                      ])
                      )
        print("Content Composed")
        return email_body

    def send_report(self, sender, pwd, receiver, subject):
        import smtplib, ssl
        from email.mime.text import MIMEText
        from email.mime.multipart import MIMEMultipart

        try:
            self.__mail_data = self.__compose_email_with_table(self.__getrawdata())
            context = ssl.create_default_context()
            with smtplib.SMTP('smtp.gmail.com', 587) as server:
                print("Sending Email")
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.ehlo()
                server.login(sender, pwd, initial_response_ok=True)
                message = MIMEMultipart()
                message['From'] = sender
                message['To'] = receiver
                message['Subject'] = subject
                message.attach(MIMEText(self.__getmaildata(), 'html'))
                text = message.as_string()
                server.ehlo()
                server.sendmail(sender, receiver, text)
                server.quit()
                print("Email Sent")
        except Exception as e:
            print("Error: ", e)

    def __getmaildata(self):
        return self.__mail_data

    def __getrawdata(self):
        return self.__m_row

    def print_report(self):
        headers = self.__getrawdata()[0]
        data = self.__getrawdata()[1:]
        if not data:
            print("No data to display.")
            return

        column_widths = self.__get_column_widths(data, headers)
        print("\n")
        width = self.__print_separator(column_widths)
        self.__print_header(width)
        self.__print_separator(column_widths)
        self.__print_row(headers, column_widths)
        self.__print_separator(column_widths)
        for row in data:
            self.__print_row(row, column_widths)
        self.__print_separator(column_widths)
        print("\n")

    def __print_header(self, width):
        msg = self.__subject
        header_line = "| {:^{}s} |".format(msg, width - 4)
        print(header_line)

    def __print_row(self, row, column_widths):
        row_str = "|"
        for i, item in enumerate(row):
            row_str += f" {item:{column_widths[i]}} |"
        print(row_str)

    def __print_separator(self, column_widths):
        separator = "+"
        for width in column_widths:
            separator += f"{'-' * (width + 2)}+"
        print(separator)
        return len(separator)

    def __get_column_widths(self, data, headers=None):
        column_count = len(data[0]) if data else 0
        column_widths = [0] * column_count

        if headers:
            for i, header in enumerate(headers):
                column_widths[i] = max(column_widths[i], len(str(header)))

        for row in data:
            for i, item in enumerate(row):
                column_widths[i] = max(column_widths[i], len(str(item)))

        return column_widths

    def save_report(self, path, ftype='html'):

        path = path + "\\" + "report." + ftype

        if ftype == 'html':
            with open(path, 'w') as f:
                f.write(self.__compose_email_with_table(self.__getrawdata()))
        else:
            import csv
            with open(path, 'w', newline='') as f:
                writer = csv.writer(f)
                writer.writerows(self.__m_row)
        print("Report Saved to {}".format(path))


class from_link:
    def __init__(self, domain):
        self.__domain = self.__domain_finder(domain)
        self.__verified = self.__IsInternetAvailable()
        if self.__verified:
            self.__ssl_status, self.__day_left, self.__info = self.__check_expiration_date()
        else:
            self.__ssl_status, self.__day_left, self.__info = None, None, "Internet Not Available"

    def __check_expiration_date(self):
        import ssl
        import socket
        import datetime

        try:
            context = ssl.create_default_context()
            conn = context.wrap_socket(socket.socket(socket.AF_INET), server_hostname=self.__domain)
            conn.connect((self.__domain, 443))
            ssl_info = conn.getpeercert()
            expiry_date = ssl_info['notAfter']
            current_date = datetime.datetime.now()
            expiry_date = datetime.datetime.strptime(expiry_date, '%b %d %H:%M:%S %Y %Z').date()
            days_left = (expiry_date - current_date.date()).days
            return True, days_left, "SSL Certificate is Valid"
        except ssl.SSLCertVerificationError as e:
            return False, -1, "SSL Certificate is Expired\nError : " + str(e.reason)
        except socket.gaierror as e:
            return False, -1, "Domain Not Found\nError : " + str(e.strerror)
        except socket.timeout as e:
            return False, -1, "Timeout\nError : " + str(e.strerror)
        except socket.error as e:
            return False, -1, "Socket Error\nError : " + str(e.strerror)
        except KeyboardInterrupt:
            return False, -1, "Keyboard Interrupt"
        except Exception as e:
            return False, -1, "\nError : " + str(e)

    def IsActive(self):
        return self.__ssl_status

    def getDayLeft(self):
        return self.__day_left

    def getInfo(self):
        return self.__info

    def __domain_finder(self, link):

        if link.find("://") != -1:
            link = link.split("://")[1]

        if link.find("/") != -1:
            link = link.split("/")[0]

        if link.find(":") != -1:
            link = link.split(":")[0]
        return link

    def getDomain(self):
        return self.__domain

    def __IsInternetAvailable(self):
        import socket
        try:
            socket.create_connection(("www.google.com", 80))
            return True
        except OSError:
            pass
        return False

    def __str__(self):
        if self.__verified:
            return "====================================" + "\nDomain : " + self.__domain + "\n====================================" + \
                   "\nSSL Status : " + str(self.__ssl_status) + " | Day's Left : " + str(
                self.__day_left) + "\nInfo : " + self.__info + "\n"
        else:
            return str(self.__info)
