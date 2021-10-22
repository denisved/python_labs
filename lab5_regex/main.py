import re


def main():
    counter = 0
    pattern = re.compile(r'.*((26/Mar/2009:14:49:(2[3-9]|[3-5]\d)|'
                          r'26/Mar/2009:14:5\d:\d\d|'
                          r'26/Mar/2009:(1[5-9]|2[0-3]):\d\d:\d\d|'
                          r'2[7-9]/Mar/2009:\d\d:\d\d:\d\d|'
                          r'30/Mar/2009:09:(0\d|1[0-6]):\d\d|'
                          r'30/Mar/2009:09:17:([0-2]\d|3[0-6])|'
                          r'30/Mar/2009:(0[0-8]):(\d\d):(\d\d)))'
                          r'.*GET.*robots.txt.*200')

    with open('access.log', 'r') as file:
        contents = file.read()
        result = pattern.finditer(contents)
        for match in result:
            print(match.group(0))
            counter += 1
        print(counter)


if __name__ == "__main__":
    main()

