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

This project is still in develop. The core of a project is already implemented, I am still working on a notification system, frontend (React) and adding new scrapers.

<!-- ABOUT THE PROJECT -->
## About The Project



## Key Features
- User system: registration, login, logout, password change
- Payment system: stripe, after registration user get a trial version which allows to use advanced scraping 5 times. User is able to buy "Basic" and "Premium" package to get all features like unlimited usage of advanced scraping and notification system.
- Scrapers: there are 2 types of scrapers:
  - dynamic scrapers can be run while making an advanced search and the data are scraped based on user's preferences
  - static scrapers are run automatically once a day and data are saved to database
- Contact form

### Built With

- Python
  - Django Rest Framework
  - Celery
  - Django Celery Beat
- PostgreSQL
- Docker and Docker-compose
- JavaScript
  - React

## Endpoints
### Users
1. Register
```bash
localhost:8000/users/register

{
  "username": "user",
  "email": "user@example.com",
  "password": "user123"
}
```
2. Login
```bash
localhost:8000/users/login

{
  "username": "user",
  "password": "user123"
} 
```
3. Logout
```bash
localhost:8000/users/logout

Headers:
{
  X-CSRFToken: XXXX
}

```
4. Change password
```bash
localhost:8000/users/change-password

{
  "new_password": "user1",
  "old_password": "user123"
}

Headers:
{
  X-CSRFToken: XXXX
}

```
5. Account delete
```bash
localhost:8000/users/account-delete

{
  "username": "user",
  "email": "user@example.com",
  "password": "user1"
}
```

### Payment
1. Get available packages
```bash
localhost:8000/payment/
```
2. User's free uses
```bash
localhost:8000/payment/user-free-uses
```
3. Create checkout session
```bash
localhost:8000/payment/chs/<int:package_id>/
```
4. Success & Cancelled checkout 
```bash
localhost:8000/payment/<str:custom_id>/
localhost:8000/payment/cancel
```
5. User's package
```bash
localhost:8000/payment/user-package
```

### Offers
1. Return job offers
```bash
localhost:8000/offers/

params:
- query [str]
- country [str]
- city [str]
- min_salary [int]
- max_salary [int]
- experience_level [str]
- advanced [bool]
```

### Contact
1. Send message
```bash
localhost:8000/contact/send

{
  "name": "User1",
  "email": "user@example.com",
  "content": "Message content"
}
```


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
docker-compose -f docker-compose.dev.yml up
```

5. Create Packages
```bash
python manage.py default_package 
```

### Tests

To run pytests use this command
```bash
pytest
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
