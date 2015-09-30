from sqlalchemy import Column, Integer

from database import Base


class Cnt(Base):
    __tablename__ = 'cnt'
    id = Column(Integer, primary_key=True)
    visit_cnt = Column(Integer)

    def __init__(self, visit_cnt):
        self.visit_cnt = int(visit_cnt)

    def __repr__(self):
        return '%d' % self.visit_cnt