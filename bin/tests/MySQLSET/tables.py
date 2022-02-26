#!/usr/bin/env python3
# -- coding:utf-8 --
# @Author: markushammered@gmail.com
# @Development Tool: PyCharm
# @Create Time: 2022/2/26
# @File Name: tables.py


from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

"""所有已保存的主题均在此处列出"""


class ReqCount(Base):
    """计数器数据库模型"""

    __tablename__ = 'ReqCount'
    name = Column(String(20), primary_key=True)  # 名称
    times = Column(Integer())  # 次数


class gelbooru(Base):
    __tablename__ = 'gelbooru'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class moebooru(Base):
    __tablename__ = 'moebooru'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class g(Base):
    __tablename__ = 'g'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class cripple(Base):
    __tablename__ = 'cripple'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class blacked(Base):
    __tablename__ = 'blacked'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class rule34(Base):
    __tablename__ = 'rule34'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class steambanner(Base):
    __tablename__ = 'steambanner'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class lefty(Base):
    __tablename__ = 'lefty'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class crewbooru(Base):
    __tablename__ = 'crewbooru'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class sthg(Base):
    __tablename__ = 'sthg'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class rfck(Base):
    __tablename__ = 'rfck'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class lisu(Base):
    __tablename__ = 'lisu'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class tv(Base):
    __tablename__ = 'tv'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class lewd(Base):
    __tablename__ = 'lewd'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class amibooru(Base):
    __tablename__ = 'amibooru'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class blankatlas(Base):
    __tablename__ = 'blankatlas'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class mmballbusting(Base):
    __tablename__ = 'mmballbusting'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class sss(Base):
    __tablename__ = 'sss'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class legolamb(Base):
    __tablename__ = 'legolamb'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class goldengator(Base):
    __tablename__ = 'goldengator'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class r6gdrawfriends(Base):
    __tablename__ = 'r6gdrawfriends'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class vivi(Base):
    __tablename__ = 'vivi'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class twifanartsfw(Base):
    __tablename__ = 'twifanartsfw'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class hololive(Base):
    __tablename__ = 'hololive'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class vglobby(Base):
    __tablename__ = 'vglobby'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class jaypee(Base):
    __tablename__ = 'jaypee'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class melanin(Base):
    __tablename__ = 'melanin'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class orb(Base):
    __tablename__ = 'orb'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class min(Base):
    __tablename__ = 'min'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class mjg(Base):
    __tablename__ = 'mjg'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class cloppers(Base):
    __tablename__ = 'cloppers'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class townofgravityfalls(Base):
    __tablename__ = 'townofgravityfalls'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class brown(Base):
    __tablename__ = 'brown'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class enacdoa(Base):
    __tablename__ = 'enacdoa'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class daifuku(Base):
    __tablename__ = 'daifuku'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class osc(Base):
    __tablename__ = 'osc'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class girlsfeet(Base):
    __tablename__ = 'girlsfeet'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class hybreedsgeneral(Base):
    __tablename__ = 'hybreedsgeneral'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class sr(Base):
    __tablename__ = 'sr'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class mono(Base):
    __tablename__ = 'mono'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class riskofrain(Base):
    __tablename__ = 'riskofrain'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class neovb(Base):
    __tablename__ = 'neovb'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


class ffsr(Base):
    __tablename__ = 'ffsr'
    k = Column(Text, primary_key=True)
    v = Column(Text)
    w = Column(Integer())
    h = Column(Integer())


__all__ = ['ReqCount', 'gelbooru', 'moebooru', 'g', 'cripple', 'blacked', 'rule34', 'steambanner', 'lefty', 'crewbooru',
           'sthg', 'rfck', 'lisu', 'tv', 'lewd', 'amibooru', 'blankatlas', 'mmballbusting', 'sss', 'legolamb',
           'goldengator', 'r6gdrawfriends', 'vivi', 'twifanartsfw', 'hololive', 'vglobby', 'jaypee', 'melanin', 'orb',
           'min', 'mjg', 'cloppers', 'townofgravityfalls', 'brown', 'enacdoa', 'daifuku', 'osc', 'girlsfeet',
           'hybreedsgeneral', 'sr', 'mono', 'riskofrain', 'neovb', 'ffsr']
