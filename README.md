# The GENDIFF

[![Hexlet Check Status](https://github.com/igorKolomitseff/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/igorKolomitseff/python-project-50/actions)
[![Gendiff Check Status](https://github.com/igorKolomitseff/python-project-50/workflows/gendiff-check/badge.svg)](https://github.com/igorKolomitseff/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/4ab311c6447fdf43f42b/maintainability)](https://codeclimate.com/github/igorKolomitseff/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/4ab311c6447fdf43f42b/test_coverage)](https://codeclimate.com/github/igorKolomitseff/python-project-50/test_coverage)

Dependencies:
* Python = "^3.10"
* PyYaml = "^6.0.1"

The GENDIFF is the second educational project in the training program "Python developer" on the [Hexlet](https://ru.hexlet.io).

The GENDIFF (GENerator of DIFFerences) is a CLI program that compares two configuration files in JSON or YAML formats and represents the difference between files in the following formats:
- stylish (default)
- plain
- json

The program is installed using [pip](https://pip.pypa.io/en/stable/) by the following command:
```
python3 -m pip install --user git+https://github.com/igorKolomitseff/python-project-50.git
```

[![asciicast](https://asciinema.org/a/614110.svg)](https://asciinema.org/a/614110)

The operability of the program can be checked using the command:
`gendiff -h`

[![asciicast](https://asciinema.org/a/614111.svg)](https://asciinema.org/a/614111)

Comparison of flat JSON files:

[![asciicast](https://asciinema.org/a/614123.svg)](https://asciinema.org/a/614123)

Comparison of flat YAML files:

[![asciicast](https://asciinema.org/a/614125.svg)](https://asciinema.org/a/614125)

Comparison of nested json files in the stylish format:

[![asciicast](https://asciinema.org/a/614127.svg)](https://asciinema.org/a/614127)

Comparison of nested json files in the plain format:

[![asciicast](https://asciinema.org/a/614130.svg)](https://asciinema.org/a/614130)

Comparison of nested json files in the json format:

[![asciicast](https://asciinema.org/a/614131.svg)](https://asciinema.org/a/614131)