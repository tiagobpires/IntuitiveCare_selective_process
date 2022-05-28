import os
import re
import shutil
import tempfile

import requests
from bs4 import BeautifulSoup


class AnnexScrapper:
    URL = "https://www.gov.br/ans/pt-br/assuntos/consumidor/o-que-o-seu-plano-de-saude-deve-cobrir-1/o-que-e-o-rol-de-procedimentos-e-evento-em-saude"

    def __init__(self, zip_name):
        # Cria diretório temporário
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path_dir = self.temp_dir.name
        self.zip_name = zip_name

    def scrape_documents(self, list_download):
        r = requests.get(self.URL)

        if r.status_code == 200:
            page_content = r.text
            soup = BeautifulSoup(page_content, "html.parser")

            tags_a = soup.find_all("a", class_="internal-link")

            for document in tags_a:
                document_text = document.getText()

                # Se algum elemento da lista de download está contido no nome documento atual
                if any(map(document_text.__contains__, list_download)):

                    # Remove espaços e parêntesis
                    # Anexo II - Diretrizes de utilização (.pdf) -> AnexoII-Diretrizesdeutilização.pdf
                    document_name = re.sub("[ ]|[()]", "", document.text)
                    document_url = document.get("href")

                    self.__download_document(document_name, document_url)

            self.__zip_dir()
        else:
            r.raise_for_status()

    def __download_document(self, document_name, document_url):
        r_download = requests.get(document_url)

        if r_download.status_code == 200:
            with open(os.path.join(self.path_dir, document_name), "wb") as f:
                f.write(r_download.content)
        else:
            r_download.raise_for_status()

    def __zip_dir(self):
        shutil.make_archive(self.zip_name, "zip", self.path_dir)

        # Exclui diretório temporário
        self.temp_dir.cleanup()
