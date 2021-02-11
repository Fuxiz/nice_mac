# nice_mac
Formats MAC addresses

## Formats
- AA:AA:AA:AA:AA:AA
- AAAAAA-AAAAAA 
- AAAA-AAAA-AAAA
- AA.AA.AA.AA.AA.AA
- AAAA.AAAA.AAAA
- AAAAAAAAAAAA

## Userful command
cat macfile.txt | xargs -L 1 -I {} python3 nice_mac.py {}
