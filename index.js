function deleteSong(song){
    for (var i = 0; i < songs.length; i++) {
        if (songs[i].songId == song) {
            songs[i].deleted = true;
        }
    }
    renderSongs(songs)
}
function favoriteSong(song){
    for (var i = 0; i < songs.length; i++) {
        if (songs[i].songId == song) {
            songs[i].favorited = !songs[i].favorited;
        }
    }
    renderSongs(songs)
}