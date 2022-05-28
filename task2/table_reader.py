import os
import shutil
import tempfile
import zipfile

import pandas as pd
import tabula


class TempDir:
    """ "
    Cria, zipa e exclui diretório temporário
    """

    def __init__(self):
        # Cria diretório temporário
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path_dir = self.temp_dir.name

    def get_path(self):
        return self.path_dir

    def zip_dir(self, zip_name):
        shutil.make_archive(zip_name, "zip", self.path_dir)

        # Exclui diretório temporário
        self.temp_dir.cleanup()


def read_table(zip_origin, pdf_archive, pages, destination_name, csv_archive):

    with zipfile.ZipFile(zip_origin, "r") as zf:
        pdf = zf.open(pdf_archive)

        list_tables = tabula.read_pdf(pdf, pages=pages, encoding="cp1252")

        # Concatena todas as tabelas em um dataframe
        df = pd.concat(list_tables)

        # Substitui dados das colunas conforme legenda
        df["OD"] = df["OD"].replace(["OD"], "Seg. Odontológica")
        df["AMB"] = df["AMB"].replace(["AMB"], "Seg. Ambulatorial")

        # Cria diretório temporário que vai conter arquivo
        temp_dir = TempDir()

        # Cria arquivo csv com a tabela obtida
        df.to_csv(os.path.join(temp_dir.get_path(), csv_archive), encoding="cp1252")

        # Zipa o diretório
        temp_dir.zip_dir(destination_name)
