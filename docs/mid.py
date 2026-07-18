#!/usr/bin/env python
"""Create a MID csv table from the ITU web page.

Locations with more than one line of MID values will have a dash in
their country name.  After creating a draft mid.csv, you will need
to edit those entries.

There are multiple locations listed for a MID (e.g. 306).  It is unclear how
to handle those.
"""

import re
import urllib.request
from bs4 import BeautifulSoup
from bs4.element import Tag

mid_url: str = 'http://www.itu.int/online/mms/glad/cga_mids.sh?lng=E'

data: bytes = urllib.request.urlopen(mid_url).read()
# print data[:100]



soup: BeautifulSoup = BeautifulSoup(data, "html.parser")

with open('dacs.h', 'w') as dac_out, open('mid2.csv', 'w') as mid_out:

  mid_out.write("""prefix,country
# prefix is used as DAC for binary messages or as the 1st three of the MMSI
# http://www.itu.int/online/mms/glad/cga_mids.sh?lng=E\n""")

  tr: Tag
  for tr in soup.find_all('tr'):
    td: Tag | None = tr.find('td')
    try:
      if td is not None:
        text: str = td.get_text()
      else:
        continue
    except AttributeError:
      continue
    if re.match(r'^\d{3}', text):
      # print 'td', td
      # print text
      mid_vals: list[int] = [int(val) for val in text.split(',')]
     #  print mid_vals
    else:
      continue

    next_sibling: Tag | None = td.findNextSibling()
    if next_sibling is None:
        continue

    country: str = next_sibling.get_text().strip()
    mid: int
    for mid in mid_vals:
      try:
        mid_out.write(f'{mid},"{country}"\n')
      except UnicodeEncodeError:
        mid_out.write('BAD mid %s\n"' % mid)
        print('BAD mid', mid)

    for mid in mid_vals:
      try:
        header_country: str = country.replace(' ', '_').split('(')[0].upper()
        header_country = header_country.rstrip('_')
        header_country = header_country.split('_-_')[0]
        dac_out.write('  AIS_DAC_%d_%s = %d,\n' % (mid,
                                                  header_country,
                                                  mid))
      except UnicodeEncodeError:
        dac_out.write('BAD mid %s\n"' % mid)

# WARNING: This does not handle the last line of the table.
