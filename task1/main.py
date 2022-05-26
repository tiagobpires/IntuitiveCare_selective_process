from annexes_scraper import annexScrapper
import requests

if __name__ == "__main__":
    # Lista dos anexos para serem baixados
    documents_download = ["Anexo I", "Anexo II", "Anexo III", "Anexo IV"]
    # Nome do arquivo zip a ser criado
    zip_name = "task1"

    try:
        scrapper = annexScrapper(zip_name)
        scrapper.scrape_documents(documents_download)
    except requests.exceptions.HTTPError as err:
        raise SystemExit(err)
    else:
        print(f"{zip_name}.zip criado")
