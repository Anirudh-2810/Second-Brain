import glob
import hashlib

import pymupdf

p = glob.glob(r"raw-sources\drive-download-20260908T190927Z-1-001\Semester 1\Bee\Module 1 DC Circuits\Chapter_1.8_THEVENIN_DC.pdf")[0]
d = pymupdf.open(p)
for idx in (2, 4, 6):
    name = "thinking\\vfy-{}-{}.png".format(idx, hashlib.md5(("k{}".format(idx)).encode()).hexdigest()[:4])
    d[idx].get_pixmap(dpi=140).save(name)
    print(name, "|", d[idx].get_text()[:70].replace("\n", " "))
