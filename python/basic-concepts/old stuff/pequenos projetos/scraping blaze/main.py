from web_scraping_init import ChromeAuto

chrome = ChromeAuto()
chrome.acessa_site('https://blaze.com/pt/games/crash')
# --------------------------------
chrome.procura_valores_blaze()


# --------------------------------
chrome.exibe_lista() # PROVISÓRIO, OBJETIVO PRINCIPAL: Acrescentar um banco de dados para pegar os valores
# --------------------------------
chrome.exit()
