import os
from tkinter.filedialog import askdirectory

caminho = askdirectory(title="Selecione uma pasta")
lista_arquivos = os.listdir(caminho)


locais = {
    "Imagens": [".png", ".jpg", ".jpeg", ".avif", ".webp", ".bmp", ".svg", ".gif", ".jfif"],
    "Planilhas": [".xlsx", ".xls", ".csv"],
    "PDFs": [".pdf"],
    "Word": [".docx", ".doc"],
    "Texto": [".txt", ".md", ".rtf", ".log"],
    "Vídeos": [".mp4", ".avi", ".mov", ".mkv", ".flv", ".wmv", ".mpeg"],
    "Compactados": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Executáveis": [".exe", ".msi"],
    "Audio": [".mp3", ".ogg", ".wav", ".aac", ".m4a"],
    "Apresentações": [".pptx", ".ppt"],
    "Apk": [".apk"],
    "Códigos Python": [".py"],
    "Web": [".html", ".css", ".js"],
    "Temporários": [".tmp", ".temp"],
    "Criptografados / Protegidos": [".rem"],
    "XML": [".xml"]
}

for arquivo in lista_arquivos:
    nome, extensao = os.path.splitext(f"{caminho}/{arquivo}")
    for pasta in locais:
        if extensao in locais[pasta]:
            destino = os.path.join(caminho, pasta, arquivo)
            if not os.path.exists(os.path.join(caminho, pasta)):
                os.mkdir(os.path.join(caminho, pasta))
            os.rename(os.path.join(caminho, arquivo), destino)
