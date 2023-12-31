[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<br />
<div align="center">

  <h2 align="center">FJob</h3>

  <p align="center">
    Application to search for job advertisements around the world. By scraping multiple job portals, you won't miss anything. 
    <br />
    <br />
    <a href="https://github.com/DEENUU1/fjob/issues">Report Bug</a>
    ·
    <a href="https://github.com/DEENUU1/fjob/issues">Request Feature</a>
  </p>

  <a href="https://github.com/DEENUU1/">

  </a>
</div>

<img src="assets/1.png"  alt="homepage"/>
<img src="assets/4.png"  alt="offers1"/>
<img src="assets/5.png"  alt="offers2"/>
<img src="assets/2.png"  alt="profile"/>
<img src="assets/3.png"  alt="contact"/>


<!-- ABOUT THE PROJECT -->
## About The Project
FJob is a project that will make it easier for you to look for a new job. 
Every day, scrapers search popular job sites, process the collected data to provide 
you with new offers that can change your life.
In the future, it will be possible for companies to add their own offers that will be specially marked as sponsored to distinguish them from those collected from other websites.
The website is translated into two languages - Polish and English.
Currently, data on job offers is collected from: nofluffjobs.com, justjoin.it, olx.pl, Pracuj.pl, praca.pl
I'm still working on improving the website and adding new scrapers to expand the database of job offers.

### Key Features
1. Scraping and processing data from various websites
2. Authentication with JWT 
3. Automated scrapers by using Celery, Redis and Django Celery Beat 
4. Reporting broken offers just with a few clicks
5. Registration, login, password change and account deletion
6. Contact form 


## How does scrapers works
Here I used Strategy Pattern to easily add additional scrapers.
The first module is GetContentStrategy which is responsible for downloading the content (html) of the page and then saving it to the database.

The second module - Process is responsible for processing data that was saved in a raw state in the first module.
Here, details such as the name of the offer, salary, work mode, type of contract, 
location, skills and much more are extracted. Then the processed data is saved to the 
database and waits for approval by the administrator in order to display it to users.
<img src="assets/Screenshot_1.png" alt="diagram" />

### List of scrapers
- <a href="https://justjoin.it/"> JustJoin.it </a>
- <a href="https://nofluffjobs.com/pl"> nofluffjobs.com </a>
- <a href="https://www.olx.pl/praca/"> OLX.pl </a>
- <a href="https://www.praca.pl/"> Praca.pl </a>
- <a href="https://www.pracuj.pl/"> Pracuj.pl </a>
- <a href="https://theprotocol.it/"> TheProtocol.it </a>



## Built With

- Python
  - Django Rest Framework  
  - Django Celery Beat
  - Celery
  - Selenium
  - Gunicorn
- PostgreSQL (production), SQLite (dev)
- Docker and Docker-compose
- React (Javascript + Vite)
- Redis 
- Nginx


## Installation

### Development 
1. Clone git repository
```bash
git clone https://github.com/DEENUU1/fjob.git
```

2. Create dotenv file and add required data
```bash
cp .env_example .env
```

3. Install all requirements
```bash
pip install -r requirements.txt
```

4. Run DRF application
```bash
python manage.py runserver
```

5. Create superuser
```bash
python manage.py createsuperuser  
```

6. Run React application
```bash
npm run dev
```

### Production 
1. Clone git repository
```bash
git clone https://github.com/DEENUU1/fjob.git
```

2. Create dotenv file and add required data
```bash
cp .env_example .env
```
3. Run docker-compose
```bash
docker-compose build
docker-compose up 
```

### Tests

To run pytests use this command
```bash
pytest
```


### Custom Django commands 
1. Scraper commands
```bash
python manage.py olx
python manage.py justjoinit
python manage.py nfj
python manage.py pracujpl
python manage.py pracapl
python manage.py theprotocol
```


<!-- LICENSE -->
## License

See `LICENSE.txt` for more information.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/DEENUU1/fjob.svg?style=for-the-badge
[contributors-url]: https://github.com/DEENUU1/fjob/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/DEENUU1/fjob.svg?style=for-the-badge
[forks-url]: https://github.com/DEENUU1/fjob/network/members
[stars-shield]: https://img.shields.io/github/stars/DEENUU1/fjob.svg?style=for-the-badge
[stars-url]: https://github.com/DEENUU1/fjob/stargazers
[issues-shield]: https://img.shields.io/github/issues/DEENUU1/fjob.svg?style=for-the-badge
[issues-url]: https://github.com/DEENUU1/fjob/issues
[license-shield]: https://img.shields.io/github/license/DEENUU1/fjob.svg?style=for-the-badge
[license-url]: https://github.com/DEENUU1/fjob/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/kacper-wlodarczyk
