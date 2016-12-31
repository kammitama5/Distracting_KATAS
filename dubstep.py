def song_decoder(song):
    import re
    s = song
    replaced = s.replace('WUB', " ")
    

    llama = re.sub( '\s+', ' ', replaced ).strip()
    return llama 
	