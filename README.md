# Cogent MNIST

Cogent MNIST is a Python application for generating MNIST digits sequences.

Code source repository on [GitHub](https://github.com/hugochau/cogent-mnist)

## Prerequisite

To be able to run this app in production, you must have [Docker](https://docs.docker.com/get-docker/) installed on your machine.

For the testing environment, you need python 3.6 and pipenv. It can be installed through pip.

```bash
pip install pipenv
```

## Installation

Please run commands under package root

### Production

Build and run the dedicated docker image

```bash
# build docker image
docker build -t cogentmnist .

# run cogentmnist
# interactive mode with bash
# bind port 80 to port 8000
docker run -it --rm -p 80:8000 cogentmnist bash
```

### Test

For testing purpose, you can also quickly deploy a virtual environment

```bash
# check if virtual environment is found
# install if not, incl. Pipfile packages
# launch python shell
pipenv --venv || pipenv install --skip-lock && pipenv shell
```

## Structure

```bash
tree .

.
├── Dockerfile
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── data
│   ├── log
│   │   └── blank
│   ├── mnist
│   │   ├── t10k-images-idx3-ubyte
│   │   └── t10k-labels-idx1-ubyte
│   └── output
│       └── blank
├── doc
│   ├── homework.md
│   └── notes.txt
├── requirements.txt
└── src
    ├── config
    │   └── constant.py
    ├── main.py
    ├── main.sh
    ├── module
    │   ├── __init__.py
    │   ├── _formatter.py
    │   ├── generator.py
    │   ├── loader.py
    │   ├── logger.py
    │   ├── npy.py
    │   ├── parser.py
    │   └── png.py
    ├── test.py
    └── util
        └── util.py

9 directories, 25 files
```

## Results

Results are saved under `data/output`. To open the .png output image outside of the container, we choose to run a simple http server and access results at http://docker-machine-ip:80

## Usage

Inside the container, run `src/main.sh` to execute both the CLI script and the http server activation command. It accepts the same arguments as the CLI script. 

In testing mode, you can run CLI script as is.

```bash
# run bash
# ex sh src/main.sh "1,4,8,6,3" 10 20 200
sh src/main.sh sequence min_spacing max_spacing image_width

# run python
# ex python src/main.py "1,4,8,6,3" 10 20 200
python src/main.py sequence min_spacing max_spacing image_width

# main.py help
main.py [-h] sequence min_spacing max_spacing image_width

CLI arguments parser for cogentmnist app

positional arguments:
  sequence     the sequence of digits to be generated. ex: "0 1 2 3"
  min_spacing  minimum spacing between consecutive digits. ex: 1
  max_spacing  maximum spacing between consecutive digits. ex: 10
  image_width  width of the generated image. ex: 128

optional arguments:
  -h, --help   show this help message and exit
```

## Implementation

For the sake of simplicity and scalability, the code follows an object-oriented approach:
- classes are stored in the `src/module` folder. Can be imported by a 3rd party
  program.
- utility functions in `src/util`
- constants and config files in `src/config`

`src/main.py` provides both the API - `generate_numbers_sequence` - and a script - `main` - that acts as a command line tool.

From a high level perspective, the CLI script is implemented as follows:
  - parse CLI arguments - `Parser`
  - generate numbers sequence - `Generator`
  - save image as .png - `Png`
  - save image as .npy - `Npy`

Logs are saved under `data/log`. A logging decorator is defined in `util.log_item` and can be used throughout the code.

Should you need more information on the API itself, please navigate through the code. Comments and method headers are intented to give a more detailed explanation.

## Test

Unit tests are defined in `src/test.py`. Tested functionnalities are:
- `Loader.load_mnist()`
- `Png.save()`
- `Parser.parse()`
- `util.get_spacing()`
- `util.classify_labels()`
- `generator.generate()`
- `Npy.save()`
- `Npy.load()`

## Improvements

Further improvements to the code, listed by order of priority:

Currently images are represented as uint8 numpy arrays with a scale from 0 to 255. Instead, images should be represented as floating point 32bits numpy arrays with a scale ranging from 0 to 1

This app generates only one image. To generate many images, we could define digits sequences in a csv file and pass it as an argument. To improve running time, we could leverage the `multiprocessing` python module

In production mode, we can persist results by setting up a docker volume and binding it to a local folder. This would remove the need of having to run a http server to access results. Or we could save the results to a cloud storage.

The logging module is not yet used at its full capacity and can be improved as follows:
- Enrich log record with additional attributes
- Add `logging.info` messages throughout the code, if need be
- Decorate other methods

## License
This product is licensed under the [MIT](https://choosealicense.com/licenses/mit/) license.

## Contribute

Want to work on the project? Any kind of contribution is welcome!

Follow these steps:

  - Fork the project.
  - Create a new branch.
  - Make your changes and write tests when practical.
  - Commit your changes to the new branch.
  - Send a pull request.


## Contact

Please reach out to chauvary.hugo@gmail.com

# Thank you!