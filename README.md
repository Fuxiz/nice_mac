# Nice mac

Formats MAC addresses to every type of format.

A handy tool when working with diffrent tools that require diffrent type of mac address formats.

## Formats

- AA:AA:AA:AA:AA:AA
- AAAAAA-AAAAAA
- AAAA-AAAA-AAAA
- AA.AA.AA.AA.AA.AA
- AAAA.AAAA.AAAA
- AAAAAAAAAAAA

```
usage: nice_mac.py [-h] [-u] [mac [mac ...]]

positional arguments:
  mac          Mac address

optional arguments:
  -h, --help   show this help message and exit
  -u, --upper  Print mac addresses in uppercase
```

## Userful command

Couldn't quite get it to work with reading mac addresses from a text file with STDIN but this works until I have figured it out.

cat macfile.txt | xargs -L 1 -I {} python3 nice_mac.py {}
