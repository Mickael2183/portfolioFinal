import keyboard
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Configurer Chrome avec des options
options = webdriver.ChromeOptions()
options.add_argument("--disable-gpu")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

# Initialiser WebDriver
driver = webdriver.Chrome(options=options)

# Ouvrir ArtStation
url1 = "https://www.artstation.com/"
driver.get(url1)

try:
    # Attendre et interagir avec la barre de recherche
    search_box = WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.NAME, "q"))
    )
    search_box.send_keys("artstation")
    search_box.send_keys(Keys.RETURN)

    # Attendre le lien ArtStation et cliquer
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'ArtStation')]"))
    ).click()

except Exception as e:
    print("Erreur :", e)

# Attendre l'appui sur la touche Suppr avant de fermer
print("Appuyez sur la touche 'Suppr' pour fermer le navigateur...")
keyboard.wait("delete")  # Attend que l'utilisateur appuie sur Suppr

# Fermer le navigateur
driver.quit()
print("Navigateur fermé.")
