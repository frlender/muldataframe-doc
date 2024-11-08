from bs4 import BeautifulSoup
import qn

paths = qn.getallfiles('/Users/qn/Documents/NuMedii_mac/Jandas/muldataframe_doc2','html')
print(len(paths))

for path in paths:
    print(path)
    with open(path,'r') as ff:
        soup = BeautifulSoup(ff, 'html.parser')
    print(soup.find_all(True,href=True))
    break

