from eulexistdb import db
from localsettings import EXISTDB_SERVER_URL

import os
# must be set before importing anything from django
os.environ['DJANGO_SETTINGS_MODULE'] = 'localsettings.py'


class TryExist:

    def __init__(self):
        self.db = db.ExistDB(server_url=EXISTDB_SERVER_URL)

    def get_data(self, query):
        result = list()
        qresult = self.db.executeQuery(query)
        hits = self.db.getHits(qresult)
        for i in range(hits):
            result.append(str(self.db.retrieve(qresult, i)))
        return result

    def upload_file(self,dir,file):
        query = "xmldb:store-files-from-pattern('/db/tryone'"+",'"+dir+"','"+file+"')"
        res = self.db.executeQuery(query)
        print query + "   " + str(res)


