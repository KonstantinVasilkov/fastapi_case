[![Python](https://camo.githubusercontent.com/f13f8c8fd603bd94f3c006d5650ea82b0213e94c54ac4b93e1d56f765a068882/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f4d616465253230776974682d507974686f6e2d677265656e3f6c6f676f3d707974686f6e266c6f676f436f6c6f723d776869746526636f6c6f72)](https://www.python.org/) 
[![Docker](https://camo.githubusercontent.com/68b1b15acde4efc8a882ad9dc399d73a7d72d6ffb69fd47f95c60772976d1218/68747470733a2f2f696d672e736869656c64732e696f2f7374617469632f76313f6d6573736167653d646f636b6572266c6f676f3d646f636b6572266c6162656c436f6c6f723d35633563356326636f6c6f723d303032633636266c6f676f436f6c6f723d7768697465266c6162656c3d253230267374796c653d706c6173746963)](https://www.docker.com/)
[![FastAPI](https://camo.githubusercontent.com/df632781b6517556307a8930711b0a92b2085f99a3a3ddad6433b96e315f0767/68747470733a2f2f696d672e736869656c64732e696f2f62616467652f466173744150492d302e36332e302d3030393638382e7376673f7374796c653d666c6174266c6f676f3d46617374415049266c6f676f436f6c6f723d7768697465)](https://fastapi.tiangolo.com/)
![Actions Status](https://github.com/KonstantinVasilkov/monite_test_case/actions/workflows/main.yml/badge.svg)


# Image Saver API

This application is a simple API that allows you to upload images and save them to the server. The application is built using FastAPI and Python 3.10.

## Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
You will need to have Docker installed on your machine.

### Installing
1. Clone the repository to your local machine

`
$ git clone git@github.com:KonstantinVasilkov/monite_test_case.git
`
2. Change directory to the cloned repository

`$ cd image-saver`
3. Build the Docker image

`$ docker build -t image-saver .`
4. Run the Docker container

`$ docker run -p 8000:8000 image-saver`

The application should now be running on http://localhost:8000

## Deployment
To deploy the application to a remote server, you will need to build the Docker image and run the container on the server. Make sure to expose the correct port and configure any necessary environment variables.

## Testing functionality 
To test the functionality of the API once your Docker container running you 
may to execute the script called ***sender_script.py*** from the root of 
the project using command:
`$ python3 sender_script.py <path/to/the/folder/with/images>`

## Built With
- [FastAPI](https://fastapi.tiangolo.com/) - The web framework used
- [Docker](https://www.docker.com/) - Containerization

## Authors
- Konstantin Vasilkov - Initial work