from config.database.db import connection_db

DB = connection_db()

from adapters.interfaces.api.views import app
