from db import Base
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    youtube_token = Column(String, default="")
    spotify_token = Column(String, default="")
    soundCloud_token = Column(String, default="")
    itunes_token = Column(String, default="")
    appleMusic_token = Column(String, default="")

    playlist = relationship("Playlist", back_populates="user")


class Playlist(Base):
    __tablename__ = "playlists"
    id = Column(Integer, primary_key=True, index=True)
    playlistName = Column(String)
    userId = Column(Integer, ForeignKey("users.id"))

    user = relationship("User", back_populates="playlist")
