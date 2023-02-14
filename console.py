import pdb
from models.album import Album
from models.artist import Artist
import repositories.album_repository as album_repository
import repositories.artist_repository as artist_repository

album_repository.delete_all()
artist_repository.delete_all()

artist_1 = Artist("Talking Heads")
album_1 = Album("Speaking in Tongues", "New Wave", artist_1)
album_2 = Album("Little Creatures", "New Wave", artist_1)
artist_repository.save(artist_1)
album_repository.save(album_1)
album_repository.save(album_2)

artist_2 = Artist("Aphex Twin")
album_3 = Album("Syro", "Electronica", artist_2)
artist_repository.save(artist_2)
album_repository.save(album_3)

pdb.set_trace()