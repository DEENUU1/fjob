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



## Info
**This project is still in develop.**

<!-- ABOUT THE PROJECT -->
## About The Project

<img src="assets/frontend/1.png " alt="frontend 1" />
<img src="assets/frontend/2.png " alt="frontent 2" />
<img src="assets/frontend/3.png " alt="frontend 3" />
<img src="assets/frontend/4.png " alt="frontend 4" />


## Endpoints

<img src="assets/1.png " alt="endpoints list" />
<img src="assets/2.png " alt="endpoints list" />



## Key Features
... 

### Built With

- Python
  - Django Rest Framework
  - Celery
  - Django Celery Beat
- PostgreSQL
- Docker and Docker-compose
- React (Javascript + Vite)

## List of scrapers
- <a href="https://www.olx.pl/praca/"> OLX </a>




<!-- GETTING STARTED -->
## Getting Started


### Installation

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

4. Run docker-compose
```bash
docker-compose up
```

5. Create super user
```bash
python manage.py createsuperuser  
```

### Tests

To run pytests use this command
```bash
pytest
```


### Scraper commands
1. Run OLX scraper
```bash
python manage.py olx <city_name> --query <query>  
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
