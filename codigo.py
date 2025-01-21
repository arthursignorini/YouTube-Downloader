import yt_dlp

# URLs das playlists
playlists_urls = [
    "https://youtube.com/playlist", # Link do vídeo ou playlist desejada
    "https://youtube.com/playlist", # Mais um vídeo ou playlist
]

# Configuração de download
ydl_opts = {
    'format': 'worst',  # Baixar na qualidade mais baixa
    'outtmpl': './downloads/%(playlist)s/%(title)s.%(ext)s',  # Diretório e nome dos arquivos
    'noplaylist': False,  # Permitir o download de playlists completas
    'geo_bypass': True,  # Ignorar restrições de região
    # 'cookiefile': 'cookies.txt',  # Descomente esta linha se precisar usar cookies para autenticação
}

# Baixar as playlists
with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    for url in playlists_urls:
        print(f"Baixando a playlist: {url}")
        ydl.download([url])

print("Download concluído para todas as playlists!")
