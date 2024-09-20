import requests
from bs4 import BeautifulSoup
url_linkedin = "https://pe.linkedin.com/jobs"

def get_jobs(job_title):
    job_title = job_title.replace(' ', '-')

    url = f"{url_linkedin}/{job_title}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    ## save in HTML file
    with open('linkedin.html', 'w', encoding='utf-8') as file:
        file.write(soup.prettify())

    job_elements = soup.find_all('li', class_='')

    jobs_data = []

    size = len(job_elements)

    print("Cantidad de trabajos encontrados:")
    print(size)

    for job_element in job_elements:

        # Extraer el título del trabajo
        title_element = job_element.find('h3', class_='base-search-card__title')
        title = title_element.get_text(strip=True) if title_element else 'No title'

        if (title == 'No title'):
            print(job_element)

        # Extraer el nombre de la empresa
        company_element = job_element.find('h4', class_='base-search-card__subtitle')
        company = company_element.get_text(strip=True) if company_element else 'No company'

        # Extraer la ubicación
        location_element = job_element.find('span', class_='job-search-card__location')
        location = location_element.get_text(strip=True) if location_element else 'No location'

        # Extraer la fecha de publicación
        date_element = job_element.find('time', class_='job-search-card__listdate')
        date_posted = date_element.get_text(strip=True) if date_element else 'No date'

        # Extraer el enlace del trabajo
        link_element = job_element.find('a', class_='base-card__full-link')
        job_link = link_element['href'] if link_element else 'No link'


        img = job_element.find('img', class_='artdeco-entity-image--square-4')
        img_url = img['data-delayed-url'] if img else 'No image'


        special_time = job_element.find('time', class_='job-search-card__listdate')

        specific_time = ''

        if special_time:
            specific_time = special_time['datetime']


        # Guardar la información en un diccionario
        job_data = {
            'Título': title,
            'Empresa': company,
            'Ubicación': location,
            'Fecha de publicación': date_posted,
            'Enlace': job_link,
            'Imagen': img_url,
            'Tiempo específico': specific_time
        }

        # Agregar el diccionario a la lista de trabajos
        jobs_data.append(job_data)

    return jobs_data