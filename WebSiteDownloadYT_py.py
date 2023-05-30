{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/diatl/yt-download-project/blob/main/WebSiteDownloadYT_py.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# **Donwload Video Youtube**\n",
        "\n",
        "---\n",
        "*Diego Armando Torres López*\n",
        "\n",
        "---\n",
        "\n",
        "\n",
        "***NOTA:*** ***En ocasiones se genera un error debido que la API de YouTube no toma en cuenta las restricciones de edad, por lo que al mostrar los resultados se genera un error.***\n"
      ],
      "metadata": {
        "id": "JbizyGJ0h2BQ"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "XkD0DcYvGHfz",
        "outputId": "d55ba317-b1f2-4b07-d567-60b6f3b4111d"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit\n",
            "  Downloading streamlit-1.22.0-py2.py3-none-any.whl (8.9 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m8.9/8.9 MB\u001b[0m \u001b[31m79.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: altair<5,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.2.2)\n",
            "Collecting blinker>=1.0.0 (from streamlit)\n",
            "  Downloading blinker-1.6.2-py3-none-any.whl (13 kB)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (5.3.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.1.3)\n",
            "Collecting importlib-metadata>=1.4 (from streamlit)\n",
            "  Downloading importlib_metadata-6.6.0-py3-none-any.whl (22 kB)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.22.4)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (23.1)\n",
            "Requirement already satisfied: pandas<3,>=0.25 in /usr/local/lib/python3.10/dist-packages (from streamlit) (1.5.3)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.4.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.10/dist-packages (from streamlit) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (9.0.0)\n",
            "Collecting pympler>=0.9 (from streamlit)\n",
            "  Downloading Pympler-1.0.1-py3-none-any.whl (164 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m164.8/164.8 kB\u001b[0m \u001b[31m22.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.8.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.10/dist-packages (from streamlit) (2.27.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (13.3.4)\n",
            "Requirement already satisfied: tenacity<9,>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (8.2.2)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.10/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.5.0)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.10/dist-packages (from streamlit) (4.3)\n",
            "Collecting validators>=0.2 (from streamlit)\n",
            "  Downloading validators-0.20.0.tar.gz (30 kB)\n",
            "  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "Collecting gitpython!=3.1.19 (from streamlit)\n",
            "  Downloading GitPython-3.1.31-py3-none-any.whl (184 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m184.3/184.3 kB\u001b[0m \u001b[31m25.0 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hCollecting pydeck>=0.1.dev5 (from streamlit)\n",
            "  Downloading pydeck-0.8.1b0-py2.py3-none-any.whl (4.8 MB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m4.8/4.8 MB\u001b[0m \u001b[31m67.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit) (6.3.1)\n",
            "Collecting watchdog (from streamlit)\n",
            "  Downloading watchdog-3.0.0-py3-none-manylinux2014_x86_64.whl (82 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m82.1/82.1 kB\u001b[0m \u001b[31m4.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (3.1.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit) (0.12.0)\n",
            "Collecting gitdb<5,>=4.0.1 (from gitpython!=3.1.19->streamlit)\n",
            "  Downloading gitdb-4.0.10-py3-none-any.whl (62 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m62.7/62.7 kB\u001b[0m \u001b[31m9.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=1.4->streamlit) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=0.25->streamlit) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->streamlit) (1.16.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit) (3.4)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit) (2.14.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal>=1.1->streamlit) (0.1.0.post0)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators>=0.2->streamlit) (4.4.2)\n",
            "Collecting smmap<6,>=3.0.1 (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit)\n",
            "  Downloading smmap-5.0.0-py3-none-any.whl (24 kB)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<5,>=3.2.0->streamlit) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal>=1.1->streamlit) (2023.3)\n",
            "Building wheels for collected packages: validators\n",
            "  Building wheel for validators (setup.py) ... \u001b[?25l\u001b[?25hdone\n",
            "  Created wheel for validators: filename=validators-0.20.0-py3-none-any.whl size=19579 sha256=dd07e8cc4632054cd010d43fed418898fd26734c16312e1d578a5049f1eaecc4\n",
            "  Stored in directory: /root/.cache/pip/wheels/f2/ed/dd/d3a556ad245ef9dc570c6bcd2f22886d17b0b408dd3bbb9ac3\n",
            "Successfully built validators\n",
            "Installing collected packages: watchdog, validators, smmap, pympler, importlib-metadata, blinker, pydeck, gitdb, gitpython, streamlit\n",
            "Successfully installed blinker-1.6.2 gitdb-4.0.10 gitpython-3.1.31 importlib-metadata-6.6.0 pydeck-0.8.1b0 pympler-1.0.1 smmap-5.0.0 streamlit-1.22.0 validators-0.20.0 watchdog-3.0.0\n"
          ]
        }
      ],
      "source": [
        "pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xiOsd1TWGN7C",
        "outputId": "f7a1d457-5ada-4fa0-f374-fa11ef53a966"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting streamlit_lottie\n",
            "  Downloading streamlit_lottie-0.0.3-py3-none-any.whl (769 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m769.4/769.4 kB\u001b[0m \u001b[31m50.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: streamlit>=0.63 in /usr/local/lib/python3.10/dist-packages (from streamlit_lottie) (1.22.0)\n",
            "Requirement already satisfied: altair<5,>=3.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (4.2.2)\n",
            "Requirement already satisfied: blinker>=1.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (1.6.2)\n",
            "Requirement already satisfied: cachetools>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (5.3.0)\n",
            "Requirement already satisfied: click>=7.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (8.1.3)\n",
            "Requirement already satisfied: importlib-metadata>=1.4 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (6.6.0)\n",
            "Requirement already satisfied: numpy in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (1.22.4)\n",
            "Requirement already satisfied: packaging>=14.1 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (23.1)\n",
            "Requirement already satisfied: pandas<3,>=0.25 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (1.5.3)\n",
            "Requirement already satisfied: pillow>=6.2.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (8.4.0)\n",
            "Requirement already satisfied: protobuf<4,>=3.12 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (3.20.3)\n",
            "Requirement already satisfied: pyarrow>=4.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (9.0.0)\n",
            "Requirement already satisfied: pympler>=0.9 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (1.0.1)\n",
            "Requirement already satisfied: python-dateutil in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (2.8.2)\n",
            "Requirement already satisfied: requests>=2.4 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (2.27.1)\n",
            "Requirement already satisfied: rich>=10.11.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (13.3.4)\n",
            "Requirement already satisfied: tenacity<9,>=8.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (8.2.2)\n",
            "Requirement already satisfied: toml in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions>=3.10.0.0 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (4.5.0)\n",
            "Requirement already satisfied: tzlocal>=1.1 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (4.3)\n",
            "Requirement already satisfied: validators>=0.2 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (0.20.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (3.1.31)\n",
            "Requirement already satisfied: pydeck>=0.1.dev5 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (0.8.1b0)\n",
            "Requirement already satisfied: tornado>=6.0.3 in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (6.3.1)\n",
            "Requirement already satisfied: watchdog in /usr/local/lib/python3.10/dist-packages (from streamlit>=0.63->streamlit_lottie) (3.0.0)\n",
            "Requirement already satisfied: entrypoints in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_lottie) (0.4)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_lottie) (3.1.2)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_lottie) (4.3.3)\n",
            "Requirement already satisfied: toolz in /usr/local/lib/python3.10/dist-packages (from altair<5,>=3.2.0->streamlit>=0.63->streamlit_lottie) (0.12.0)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.10/dist-packages (from gitpython!=3.1.19->streamlit>=0.63->streamlit_lottie) (4.0.10)\n",
            "Requirement already satisfied: zipp>=0.5 in /usr/local/lib/python3.10/dist-packages (from importlib-metadata>=1.4->streamlit>=0.63->streamlit_lottie) (3.15.0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.10/dist-packages (from pandas<3,>=0.25->streamlit>=0.63->streamlit_lottie) (2022.7.1)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.10/dist-packages (from python-dateutil->streamlit>=0.63->streamlit_lottie) (1.16.0)\n",
            "Requirement already satisfied: urllib3<1.27,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_lottie) (1.26.15)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_lottie) (2022.12.7)\n",
            "Requirement already satisfied: charset-normalizer~=2.0.0 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_lottie) (2.0.12)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests>=2.4->streamlit>=0.63->streamlit_lottie) (3.4)\n",
            "Requirement already satisfied: markdown-it-py<3.0.0,>=2.2.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit>=0.63->streamlit_lottie) (2.2.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.10/dist-packages (from rich>=10.11.0->streamlit>=0.63->streamlit_lottie) (2.14.0)\n",
            "Requirement already satisfied: pytz-deprecation-shim in /usr/local/lib/python3.10/dist-packages (from tzlocal>=1.1->streamlit>=0.63->streamlit_lottie) (0.1.0.post0)\n",
            "Requirement already satisfied: decorator>=3.4.0 in /usr/local/lib/python3.10/dist-packages (from validators>=0.2->streamlit>=0.63->streamlit_lottie) (4.4.2)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.10/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19->streamlit>=0.63->streamlit_lottie) (5.0.0)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from jinja2->altair<5,>=3.2.0->streamlit>=0.63->streamlit_lottie) (2.1.2)\n",
            "Requirement already satisfied: attrs>=17.4.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit>=0.63->streamlit_lottie) (23.1.0)\n",
            "Requirement already satisfied: pyrsistent!=0.17.0,!=0.17.1,!=0.17.2,>=0.14.0 in /usr/local/lib/python3.10/dist-packages (from jsonschema>=3.0->altair<5,>=3.2.0->streamlit>=0.63->streamlit_lottie) (0.19.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.10/dist-packages (from markdown-it-py<3.0.0,>=2.2.0->rich>=10.11.0->streamlit>=0.63->streamlit_lottie) (0.1.2)\n",
            "Requirement already satisfied: tzdata in /usr/local/lib/python3.10/dist-packages (from pytz-deprecation-shim->tzlocal>=1.1->streamlit>=0.63->streamlit_lottie) (2023.3)\n",
            "Installing collected packages: streamlit_lottie\n",
            "Successfully installed streamlit_lottie-0.0.3\n"
          ]
        }
      ],
      "source": [
        "pip install streamlit_lottie"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Jw0uMBhzGN9J",
        "outputId": "990cbcb1-078c-44d7-c3a4-ea11c6064777"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Collecting pytube\n",
            "  Downloading pytube-15.0.0-py3-none-any.whl (57 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m57.6/57.6 kB\u001b[0m \u001b[31m5.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pytube\n",
            "Successfully installed pytube-15.0.0\n"
          ]
        }
      ],
      "source": [
        "pip install pytube"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "pip install flask"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "OE4MsucDTDsX",
        "outputId": "422cd83d-b270-48cd-9e82-957769e7407a"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Looking in indexes: https://pypi.org/simple, https://us-python.pkg.dev/colab-wheels/public/simple/\n",
            "Requirement already satisfied: flask in /usr/local/lib/python3.10/dist-packages (2.2.4)\n",
            "Requirement already satisfied: Werkzeug>=2.2.2 in /usr/local/lib/python3.10/dist-packages (from flask) (2.3.0)\n",
            "Requirement already satisfied: Jinja2>=3.0 in /usr/local/lib/python3.10/dist-packages (from flask) (3.1.2)\n",
            "Requirement already satisfied: itsdangerous>=2.0 in /usr/local/lib/python3.10/dist-packages (from flask) (2.1.2)\n",
            "Requirement already satisfied: click>=8.0 in /usr/local/lib/python3.10/dist-packages (from flask) (8.1.3)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.10/dist-packages (from Jinja2>=3.0->flask) (2.1.2)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "dubpVZFLGN_p",
        "outputId": "2bfaeb66-ff75-4096-e41a-dd6261c23fa8"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Overwriting yt_download.py\n"
          ]
        }
      ],
      "source": [
        "%%writefile yt_download.py\n",
        "import requests\n",
        "import streamlit as st\n",
        "from streamlit_lottie import st_lottie\n",
        "from PIL import Image\n",
        "from pytube import YouTube\n",
        "from googleapiclient.discovery import build\n",
        "from pytube import YouTube\n",
        "from flask import Flask, request, render_template, send_file\n",
        "import tempfile\n",
        "import os\n",
        "# Configuración de la API de YouTube\n",
        "API_KEY = \"AIzaSyAocEc2RaxB59kggaEEIN0_YcVPGDY_BcI\"  \n",
        "\n",
        "# Crear un cliente para la API de YouTube\n",
        "youtube = build(\"youtube\", \"v3\", developerKey=API_KEY)\n",
        "\n",
        "\n",
        "def search_video(query, max_results=10):\n",
        "    response = youtube.search().list(\n",
        "        q=query,\n",
        "        part=\"snippet\",\n",
        "        type=\"video\",\n",
        "    ).execute()\n",
        "\n",
        "    videos = response[\"items\"]\n",
        "    return videos\n",
        "\n",
        "\n",
        "st.set_page_config(page_title=\"YT - Download\", page_icon=\":tada:\", layout=\"wide\")\n",
        "\n",
        "# Use local CSS\n",
        "def local_css(file_name):\n",
        "    with open(file_name) as f:\n",
        "        st.markdown(f\"<style>{f.read()}</style>\", unsafe_allow_html=True)\n",
        "\n",
        "#Animate\n",
        "def load_lottieurl(url):\n",
        "    r = requests.get(url)\n",
        "    if r.status_code != 200:\n",
        "        return None\n",
        "    return r.json()\n",
        "\n",
        "local_css(\"/content/drive/MyDrive/CP/style/style.css\")\n",
        "\n",
        "animate_image = load_lottieurl(\"https://assets3.lottiefiles.com/packages/lf20_szdrhwiq.json\")\n",
        "\n",
        "\n",
        "# ---- HEADER SECTION ----\n",
        "with st.container():\n",
        "    st.markdown(\n",
        "        \"\"\"\n",
        "        <style>\n",
        "        .centered-text {\n",
        "            text-align: center;\n",
        "        }\n",
        "        </style>\n",
        "        \"\"\",\n",
        "        unsafe_allow_html=True\n",
        "    )\n",
        "        \n",
        "    st_lottie(animate_image, height=200, key=\"coding\")\n",
        "    st.write(\"<h1 class='centered-text'>Welcome to YT Download</h1>\", unsafe_allow_html=True)\n",
        "    st.write(\"<h2 class='centered-text'>Final project of the subject basic computing, the page allows you to search for videos stored on YouTube and allows you to download the desired video.</h1>\", unsafe_allow_html=True)\n",
        "    st.write(\"<p class='centered-text'>Presented by: Diego Armando Torres López.</p>\", unsafe_allow_html=True)\n",
        "\n",
        "# ---- Contaienr ----\n",
        "with st.container():\n",
        "    st.write(\"---\")        \n",
        "    #Busqueda de videos\n",
        "    search_query = st.text_input(\"Enter your search query\")\n",
        "    if st.button(\"Search\"):\n",
        "        if search_query:\n",
        "            videos = search_video(search_query)\n",
        "\n",
        "            for video in videos:\n",
        "              video_title = video[\"snippet\"][\"title\"]\n",
        "              video_id = video[\"id\"][\"videoId\"]\n",
        "              video_url = f\"https://www.youtube.com/watch?v={video_id}\"\n",
        "              video_image = video[\"snippet\"][\"thumbnails\"][\"default\"][\"url\"]\n",
        "              youtube_video = YouTube(video_url)\n",
        "              video_title = youtube_video.title\n",
        "              # Descarga el video a un archivo temporal\n",
        "              stream = youtube_video.streams.get_highest_resolution()\n",
        "              temp_file_path = os.path.join(tempfile.gettempdir(), f'{video_title}.mp4')\n",
        "              archivo = stream.download(output_path=tempfile.gettempdir(), filename=f'{video_title}.mp4')\n",
        "              #file = request.files(archivo)\n",
        "              temp_file_prueba = tempfile.NamedTemporaryFile(delete=False)\n",
        "              st.write(\"---\")\n",
        "              st.write(\"##\")\n",
        "              image_column, text_column = st.columns((1, 2))\n",
        "              with image_column:\n",
        "                st.image(video_image)\n",
        "              with text_column:\n",
        "                st.subheader(video_title)\n",
        "                st.markdown(f\"URL del video:  {video_url}\")\n",
        "\n",
        "                with open(archivo, \"rb\") as file:\n",
        "\n",
        "                  btn =  st.download_button(\n",
        "                      label=\"Download video\",\n",
        "                      data=file,\n",
        "                      file_name=archivo,\n",
        "                      mime=\"mp4\"\n",
        "                  )\n",
        "\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "wuSf_8ddX9Jx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "1. Al ejecutar la celda siguiente, se generara un link temporal con el cual se podrá tener acceso a la pagina web. \n",
        "2. Al ingresar a la página pedirá ingresar una ip (EXTERNAL IP), la cual se genera de igual manera en la siguiente celda.\n",
        "\n",
        " **NOTA: Colocar solo la ip, sin* http://*, ni tampoco colocar el puerto. Solo IP**\n"
      ],
      "metadata": {
        "id": "wkgKsujuiy_e"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "DSoy9wxbHO_r",
        "outputId": "2db536c1-64ff-4b57-9344-1ca2d564f0ae"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "\u001b[K\u001b[?25h\n",
            "Collecting usage statistics. To deactivate, set browser.gatherUsageStats to False.\n",
            "\u001b[0m\n",
            "npx: installed 22 in 1.799s\n",
            "\u001b[0m\n",
            "\u001b[34m\u001b[1m  You can now view your Streamlit app in your browser.\u001b[0m\n",
            "\u001b[0m\n",
            "\u001b[34m  Network URL: \u001b[0m\u001b[1mhttp://172.28.0.12:8501\u001b[0m\n",
            "\u001b[34m  External URL: \u001b[0m\u001b[1mhttp://35.221.8.107:8501\u001b[0m\n",
            "\u001b[0m\n",
            "your url is: https://tender-swans-act.loca.lt\n",
            "2023-05-30 21:14:28.058 Uncaught app exception\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/streamlit/runtime/scriptrunner/script_runner.py\", line 565, in _run_script\n",
            "    exec(code, module.__dict__)\n",
            "  File \"/content/yt_download.py\", line 85, in <module>\n",
            "    archivo = stream.download(output_path=tempfile.gettempdir(), filename=f'{video_title}.mp4')\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/pytube/streams.py\", line 312, in download\n",
            "    with open(file_path, \"wb\") as fh:\n",
            "FileNotFoundError: [Errno 2] No such file or directory: '/tmp/Mana Grandes Exitos / Completo.mp4'\n",
            "\u001b[34m  Stopping...\u001b[0m\n",
            "Exception in callback _HandlerDelegate.execute.<locals>.<lambda>(<Task cancell.../web.py:1742>>) at /usr/local/lib/python3.10/dist-packages/tornado/web.py:2434\n",
            "handle: <Handle _HandlerDelegate.execute.<locals>.<lambda>(<Task cancell.../web.py:1742>>) at /usr/local/lib/python3.10/dist-packages/tornado/web.py:2434>\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/tornado/web.py\", line 1786, in _execute\n",
            "    result = await result\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/tornado/web.py\", line 2756, in get\n",
            "    await self.flush()\n",
            "asyncio.exceptions.CancelledError\n",
            "\n",
            "During handling of the above exception, another exception occurred:\n",
            "\n",
            "Traceback (most recent call last):\n",
            "  File \"/usr/lib/python3.10/asyncio/events.py\", line 80, in _run\n",
            "    self._context.run(self._callback, *self._args)\n",
            "  File \"/usr/local/lib/python3.10/dist-packages/tornado/web.py\", line 2434, in <lambda>\n",
            "    fut.add_done_callback(lambda f: f.result())\n",
            "asyncio.exceptions.CancelledError\n",
            "^C\n"
          ]
        }
      ],
      "source": [
        "!streamlit run yt_download.py & npx localtunnel --port 8501"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1XI11seCK8kl9UaeNxqn2FJGHmVYsJYIv",
      "authorship_tag": "ABX9TyMCqySG7DoQf0rhzsgtbJsL",
      "include_colab_link": true
    },
    "kernelspec": {
      "display_name": "Python 3",
      "name": "python3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "nbformat": 4,
  "nbformat_minor": 0
}