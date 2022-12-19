from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import Integer, DateTime


class BaseModel(object):

    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow())
    modified_at = Column(DateTime, default=datetime.utcnow())
