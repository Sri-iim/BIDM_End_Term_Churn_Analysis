{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNgvCoG0d24/y5XPuyEI66W",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Sri-iim/BIDM_End_Term_Churn_Analysis/blob/main/Churn_Analysis.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Dzvn5nDw2dv",
        "outputId": "93ca548e-f6c7-4019-830c-431a6411bad5"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.42.2-py2.py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: pandas in /usr/local/lib/python3.11/dist-packages (2.2.2)\n",
            "Requirement already satisfied: scikit-learn in /usr/local/lib/python3.11/dist-packages (1.6.1)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.1)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.25.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m1.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas) (2025.1)\n",
            "Requirement already satisfied: scipy>=1.6.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (1.13.1)\n",
            "Requirement already satisfied: joblib>=1.2.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (1.4.2)\n",
            "Requirement already satisfied: threadpoolctl>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from scikit-learn) (3.5.0)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.5)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.27.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas) (1.17.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Downloading streamlit-1.42.2-py2.py3-none-any.whl (9.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.6/9.6 MB\u001b[0m \u001b[31m61.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m96.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m5.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.42.2 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "pip install streamlit pandas scikit-learn"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from google.colab import files\n",
        "\n",
        "uploaded = files.upload()\n",
        "\n",
        "for fn in uploaded.keys():\n",
        "  print('User uploaded file \"{name}\" with length {length} bytes'.format(\n",
        "      name=fn, length=len(uploaded[fn])))"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 90
        },
        "id": "5swXA6hEMGxJ",
        "outputId": "6162fed3-b2b9-4cd5-f301-3d8df0720cc4"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-a155321c-5fef-44ed-9464-07f148801cd6\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-a155321c-5fef-44ed-9464-07f148801cd6\">\n",
              "      Upload widget is only available when the cell has been executed in the\n",
              "      current browser session. Please rerun this cell to enable.\n",
              "      </output>\n",
              "      <script>// Copyright 2017 Google LLC\n",
              "//\n",
              "// Licensed under the Apache License, Version 2.0 (the \"License\");\n",
              "// you may not use this file except in compliance with the License.\n",
              "// You may obtain a copy of the License at\n",
              "//\n",
              "//      http://www.apache.org/licenses/LICENSE-2.0\n",
              "//\n",
              "// Unless required by applicable law or agreed to in writing, software\n",
              "// distributed under the License is distributed on an \"AS IS\" BASIS,\n",
              "// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.\n",
              "// See the License for the specific language governing permissions and\n",
              "// limitations under the License.\n",
              "\n",
              "/**\n",
              " * @fileoverview Helpers for google.colab Python module.\n",
              " */\n",
              "(function(scope) {\n",
              "function span(text, styleAttributes = {}) {\n",
              "  const element = document.createElement('span');\n",
              "  element.textContent = text;\n",
              "  for (const key of Object.keys(styleAttributes)) {\n",
              "    element.style[key] = styleAttributes[key];\n",
              "  }\n",
              "  return element;\n",
              "}\n",
              "\n",
              "// Max number of bytes which will be uploaded at a time.\n",
              "const MAX_PAYLOAD_SIZE = 100 * 1024;\n",
              "\n",
              "function _uploadFiles(inputId, outputId) {\n",
              "  const steps = uploadFilesStep(inputId, outputId);\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  // Cache steps on the outputElement to make it available for the next call\n",
              "  // to uploadFilesContinue from Python.\n",
              "  outputElement.steps = steps;\n",
              "\n",
              "  return _uploadFilesContinue(outputId);\n",
              "}\n",
              "\n",
              "// This is roughly an async generator (not supported in the browser yet),\n",
              "// where there are multiple asynchronous steps and the Python side is going\n",
              "// to poll for completion of each step.\n",
              "// This uses a Promise to block the python side on completion of each step,\n",
              "// then passes the result of the previous step as the input to the next step.\n",
              "function _uploadFilesContinue(outputId) {\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  const steps = outputElement.steps;\n",
              "\n",
              "  const next = steps.next(outputElement.lastPromiseValue);\n",
              "  return Promise.resolve(next.value.promise).then((value) => {\n",
              "    // Cache the last promise value to make it available to the next\n",
              "    // step of the generator.\n",
              "    outputElement.lastPromiseValue = value;\n",
              "    return next.value.response;\n",
              "  });\n",
              "}\n",
              "\n",
              "/**\n",
              " * Generator function which is called between each async step of the upload\n",
              " * process.\n",
              " * @param {string} inputId Element ID of the input file picker element.\n",
              " * @param {string} outputId Element ID of the output display.\n",
              " * @return {!Iterable<!Object>} Iterable of next steps.\n",
              " */\n",
              "function* uploadFilesStep(inputId, outputId) {\n",
              "  const inputElement = document.getElementById(inputId);\n",
              "  inputElement.disabled = false;\n",
              "\n",
              "  const outputElement = document.getElementById(outputId);\n",
              "  outputElement.innerHTML = '';\n",
              "\n",
              "  const pickedPromise = new Promise((resolve) => {\n",
              "    inputElement.addEventListener('change', (e) => {\n",
              "      resolve(e.target.files);\n",
              "    });\n",
              "  });\n",
              "\n",
              "  const cancel = document.createElement('button');\n",
              "  inputElement.parentElement.appendChild(cancel);\n",
              "  cancel.textContent = 'Cancel upload';\n",
              "  const cancelPromise = new Promise((resolve) => {\n",
              "    cancel.onclick = () => {\n",
              "      resolve(null);\n",
              "    };\n",
              "  });\n",
              "\n",
              "  // Wait for the user to pick the files.\n",
              "  const files = yield {\n",
              "    promise: Promise.race([pickedPromise, cancelPromise]),\n",
              "    response: {\n",
              "      action: 'starting',\n",
              "    }\n",
              "  };\n",
              "\n",
              "  cancel.remove();\n",
              "\n",
              "  // Disable the input element since further picks are not allowed.\n",
              "  inputElement.disabled = true;\n",
              "\n",
              "  if (!files) {\n",
              "    return {\n",
              "      response: {\n",
              "        action: 'complete',\n",
              "      }\n",
              "    };\n",
              "  }\n",
              "\n",
              "  for (const file of files) {\n",
              "    const li = document.createElement('li');\n",
              "    li.append(span(file.name, {fontWeight: 'bold'}));\n",
              "    li.append(span(\n",
              "        `(${file.type || 'n/a'}) - ${file.size} bytes, ` +\n",
              "        `last modified: ${\n",
              "            file.lastModifiedDate ? file.lastModifiedDate.toLocaleDateString() :\n",
              "                                    'n/a'} - `));\n",
              "    const percent = span('0% done');\n",
              "    li.appendChild(percent);\n",
              "\n",
              "    outputElement.appendChild(li);\n",
              "\n",
              "    const fileDataPromise = new Promise((resolve) => {\n",
              "      const reader = new FileReader();\n",
              "      reader.onload = (e) => {\n",
              "        resolve(e.target.result);\n",
              "      };\n",
              "      reader.readAsArrayBuffer(file);\n",
              "    });\n",
              "    // Wait for the data to be ready.\n",
              "    let fileData = yield {\n",
              "      promise: fileDataPromise,\n",
              "      response: {\n",
              "        action: 'continue',\n",
              "      }\n",
              "    };\n",
              "\n",
              "    // Use a chunked sending to avoid message size limits. See b/62115660.\n",
              "    let position = 0;\n",
              "    do {\n",
              "      const length = Math.min(fileData.byteLength - position, MAX_PAYLOAD_SIZE);\n",
              "      const chunk = new Uint8Array(fileData, position, length);\n",
              "      position += length;\n",
              "\n",
              "      const base64 = btoa(String.fromCharCode.apply(null, chunk));\n",
              "      yield {\n",
              "        response: {\n",
              "          action: 'append',\n",
              "          file: file.name,\n",
              "          data: base64,\n",
              "        },\n",
              "      };\n",
              "\n",
              "      let percentDone = fileData.byteLength === 0 ?\n",
              "          100 :\n",
              "          Math.round((position / fileData.byteLength) * 100);\n",
              "      percent.textContent = `${percentDone}% done`;\n",
              "\n",
              "    } while (position < fileData.byteLength);\n",
              "  }\n",
              "\n",
              "  // All done.\n",
              "  yield {\n",
              "    response: {\n",
              "      action: 'complete',\n",
              "    }\n",
              "  };\n",
              "}\n",
              "\n",
              "scope.google = scope.google || {};\n",
              "scope.google.colab = scope.google.colab || {};\n",
              "scope.google.colab._files = {\n",
              "  _uploadFiles,\n",
              "  _uploadFilesContinue,\n",
              "};\n",
              "})(self);\n",
              "</script> "
            ]
          },
          "metadata": {}
        },
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Saving WA_Fn-UseC_-Telco-Customer-Churn.csv to WA_Fn-UseC_-Telco-Customer-Churn.csv\n",
            "User uploaded file \"WA_Fn-UseC_-Telco-Customer-Churn.csv\" with length 977501 bytes\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import os\n",
        "\n",
        "\n",
        "\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import os\n",
        "\n",
        "\n",
        "\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import seaborn as sns\n",
        "import matplotlib.pyplot as plt\n",
        "import pandas as pd\n",
        "import os\n",
        "\n",
        "import pandas as pd\n",
        "data = pd.read_csv('WA_Fn-UseC_-Telco-Customer-Churn.csv')\n",
        "print(data.head()) # Display the first few rows\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BUFCj98Kydz0",
        "outputId": "f8485e35-4e84-4d31-b17f-b670a0fbf094"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   customerID  gender  SeniorCitizen Partner Dependents  tenure PhoneService  \\\n",
            "0  7590-VHVEG  Female              0     Yes         No       1           No   \n",
            "1  5575-GNVDE    Male              0      No         No      34          Yes   \n",
            "2  3668-QPYBK    Male              0      No         No       2          Yes   \n",
            "3  7795-CFOCW    Male              0      No         No      45           No   \n",
            "4  9237-HQITU  Female              0      No         No       2          Yes   \n",
            "\n",
            "      MultipleLines InternetService OnlineSecurity  ... DeviceProtection  \\\n",
            "0  No phone service             DSL             No  ...               No   \n",
            "1                No             DSL            Yes  ...              Yes   \n",
            "2                No             DSL            Yes  ...               No   \n",
            "3  No phone service             DSL            Yes  ...              Yes   \n",
            "4                No     Fiber optic             No  ...               No   \n",
            "\n",
            "  TechSupport StreamingTV StreamingMovies        Contract PaperlessBilling  \\\n",
            "0          No          No              No  Month-to-month              Yes   \n",
            "1          No          No              No        One year               No   \n",
            "2          No          No              No  Month-to-month              Yes   \n",
            "3         Yes          No              No        One year               No   \n",
            "4          No          No              No  Month-to-month              Yes   \n",
            "\n",
            "               PaymentMethod MonthlyCharges  TotalCharges Churn  \n",
            "0           Electronic check          29.85         29.85    No  \n",
            "1               Mailed check          56.95        1889.5    No  \n",
            "2               Mailed check          53.85        108.15   Yes  \n",
            "3  Bank transfer (automatic)          42.30       1840.75    No  \n",
            "4           Electronic check          70.70        151.65   Yes  \n",
            "\n",
            "[5 rows x 21 columns]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "   import numpy as np\n"
      ],
      "metadata": {
        "id": "skZOIcZuM36I"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "from io import StringIO  # To read the string data as a file\n"
      ],
      "metadata": {
        "id": "Us1KX9KGM5wz"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(data.head())  # See the first few rows\n",
        "print(data.info())  # Check data types and missing values\n",
        "print(data.describe()) # Summary statistics for numerical columns"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "46-9oXppNE_9",
        "outputId": "3b2c8113-c964-46ef-d5a9-1e6c52298f7e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   customerID  gender  SeniorCitizen Partner Dependents  tenure PhoneService  \\\n",
            "0  7590-VHVEG  Female              0     Yes         No       1           No   \n",
            "1  5575-GNVDE    Male              0      No         No      34          Yes   \n",
            "2  3668-QPYBK    Male              0      No         No       2          Yes   \n",
            "3  7795-CFOCW    Male              0      No         No      45           No   \n",
            "4  9237-HQITU  Female              0      No         No       2          Yes   \n",
            "\n",
            "      MultipleLines InternetService OnlineSecurity  ... DeviceProtection  \\\n",
            "0  No phone service             DSL             No  ...               No   \n",
            "1                No             DSL            Yes  ...              Yes   \n",
            "2                No             DSL            Yes  ...               No   \n",
            "3  No phone service             DSL            Yes  ...              Yes   \n",
            "4                No     Fiber optic             No  ...               No   \n",
            "\n",
            "  TechSupport StreamingTV StreamingMovies        Contract PaperlessBilling  \\\n",
            "0          No          No              No  Month-to-month              Yes   \n",
            "1          No          No              No        One year               No   \n",
            "2          No          No              No  Month-to-month              Yes   \n",
            "3         Yes          No              No        One year               No   \n",
            "4          No          No              No  Month-to-month              Yes   \n",
            "\n",
            "               PaymentMethod MonthlyCharges  TotalCharges Churn  \n",
            "0           Electronic check          29.85         29.85    No  \n",
            "1               Mailed check          56.95        1889.5    No  \n",
            "2               Mailed check          53.85        108.15   Yes  \n",
            "3  Bank transfer (automatic)          42.30       1840.75    No  \n",
            "4           Electronic check          70.70        151.65   Yes  \n",
            "\n",
            "[5 rows x 21 columns]\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 7043 entries, 0 to 7042\n",
            "Data columns (total 21 columns):\n",
            " #   Column            Non-Null Count  Dtype  \n",
            "---  ------            --------------  -----  \n",
            " 0   customerID        7043 non-null   object \n",
            " 1   gender            7043 non-null   object \n",
            " 2   SeniorCitizen     7043 non-null   int64  \n",
            " 3   Partner           7043 non-null   object \n",
            " 4   Dependents        7043 non-null   object \n",
            " 5   tenure            7043 non-null   int64  \n",
            " 6   PhoneService      7043 non-null   object \n",
            " 7   MultipleLines     7043 non-null   object \n",
            " 8   InternetService   7043 non-null   object \n",
            " 9   OnlineSecurity    7043 non-null   object \n",
            " 10  OnlineBackup      7043 non-null   object \n",
            " 11  DeviceProtection  7043 non-null   object \n",
            " 12  TechSupport       7043 non-null   object \n",
            " 13  StreamingTV       7043 non-null   object \n",
            " 14  StreamingMovies   7043 non-null   object \n",
            " 15  Contract          7043 non-null   object \n",
            " 16  PaperlessBilling  7043 non-null   object \n",
            " 17  PaymentMethod     7043 non-null   object \n",
            " 18  MonthlyCharges    7043 non-null   float64\n",
            " 19  TotalCharges      7043 non-null   object \n",
            " 20  Churn             7043 non-null   object \n",
            "dtypes: float64(1), int64(2), object(18)\n",
            "memory usage: 1.1+ MB\n",
            "None\n",
            "       SeniorCitizen       tenure  MonthlyCharges\n",
            "count    7043.000000  7043.000000     7043.000000\n",
            "mean        0.162147    32.371149       64.761692\n",
            "std         0.368612    24.559481       30.090047\n",
            "min         0.000000     0.000000       18.250000\n",
            "25%         0.000000     9.000000       35.500000\n",
            "50%         0.000000    29.000000       70.350000\n",
            "75%         0.000000    55.000000       89.850000\n",
            "max         1.000000    72.000000      118.750000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Replace empty strings with NaN in 'TotalCharges'\n",
        "data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)"
      ],
      "metadata": {
        "id": "CeCxtll-NSxx"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Get summary statistics\n",
        "print(data.describe())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CQvQ44IVNbow",
        "outputId": "7f15b4a4-76e8-47df-c000-71b61c823b8c"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       SeniorCitizen       tenure  MonthlyCharges\n",
            "count    7043.000000  7043.000000     7043.000000\n",
            "mean        0.162147    32.371149       64.761692\n",
            "std         0.368612    24.559481       30.090047\n",
            "min         0.000000     0.000000       18.250000\n",
            "25%         0.000000     9.000000       35.500000\n",
            "50%         0.000000    29.000000       70.350000\n",
            "75%         0.000000    55.000000       89.850000\n",
            "max         1.000000    72.000000      118.750000\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Check data types and missing values\n",
        "print(data.info())\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "edh5UdH5Niyj",
        "outputId": "ce323e0e-a010-42a7-c0f8-1a17f18aac45"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 7043 entries, 0 to 7042\n",
            "Data columns (total 21 columns):\n",
            " #   Column            Non-Null Count  Dtype  \n",
            "---  ------            --------------  -----  \n",
            " 0   customerID        7043 non-null   object \n",
            " 1   gender            7043 non-null   object \n",
            " 2   SeniorCitizen     7043 non-null   int64  \n",
            " 3   Partner           7043 non-null   object \n",
            " 4   Dependents        7043 non-null   object \n",
            " 5   tenure            7043 non-null   int64  \n",
            " 6   PhoneService      7043 non-null   object \n",
            " 7   MultipleLines     7043 non-null   object \n",
            " 8   InternetService   7043 non-null   object \n",
            " 9   OnlineSecurity    7043 non-null   object \n",
            " 10  OnlineBackup      7043 non-null   object \n",
            " 11  DeviceProtection  7043 non-null   object \n",
            " 12  TechSupport       7043 non-null   object \n",
            " 13  StreamingTV       7043 non-null   object \n",
            " 14  StreamingMovies   7043 non-null   object \n",
            " 15  Contract          7043 non-null   object \n",
            " 16  PaperlessBilling  7043 non-null   object \n",
            " 17  PaymentMethod     7043 non-null   object \n",
            " 18  MonthlyCharges    7043 non-null   float64\n",
            " 19  TotalCharges      7032 non-null   object \n",
            " 20  Churn             7043 non-null   object \n",
            "dtypes: float64(1), int64(2), object(18)\n",
            "memory usage: 1.1+ MB\n",
            "None\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Checking for missing values\n",
        "print(data.isnull().sum())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "p3ixoh8JOPDL",
        "outputId": "11be84bb-a347-4adc-ac64-ef435b4e99ef"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "customerID           0\n",
            "gender               0\n",
            "SeniorCitizen        0\n",
            "Partner              0\n",
            "Dependents           0\n",
            "tenure               0\n",
            "PhoneService         0\n",
            "MultipleLines        0\n",
            "InternetService      0\n",
            "OnlineSecurity       0\n",
            "OnlineBackup         0\n",
            "DeviceProtection     0\n",
            "TechSupport          0\n",
            "StreamingTV          0\n",
            "StreamingMovies      0\n",
            "Contract             0\n",
            "PaperlessBilling     0\n",
            "PaymentMethod        0\n",
            "MonthlyCharges       0\n",
            "TotalCharges        11\n",
            "Churn                0\n",
            "dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Identify missing values (represented by empty strings) and replace them with NaN\n",
        "data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)\n",
        "\n"
      ],
      "metadata": {
        "id": "QZYq0m-7OjGB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Convert the 'TotalCharges' column to numeric (float) type.  This is crucial\n",
        "# because pandas won't treat non-numeric values as NaN unless you force it.\n",
        "data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')\n"
      ],
      "metadata": {
        "id": "tETLhdcKPgk2"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "# Replace NaN values in 'TotalCharges' with 0\n",
        "data['TotalCharges'] = data['TotalCharges'].fillna(0)\n",
        "\n",
        "# (Optional) Verify that the missing values have been handled\n",
        "print(data['TotalCharges'].isnull().sum())  # Should output 0\n",
        "\n",
        "# (Optional) Check the data type of the column\n",
        "print(data['TotalCharges'].dtype)  # Should output float64 (or float32)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "69FvhRLTPjM-",
        "outputId": "b6db8d36-c54b-46a6-f8b7-6ba22d97f8e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "float64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import plotly.express as px\n",
        "import matplotlib.pyplot as plt\n",
        "from sklearn.linear_model import LinearRegression,Lasso,Ridge\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.metrics import r2_score"
      ],
      "metadata": {
        "id": "EbYFbWphQGDm"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install streamlit"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "S4RDuIt8Q7Zu",
        "outputId": "7c2fc5a6-744e-4b2f-931d-14e282037834"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.42.2-py2.py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.0.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.1)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.26.4)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.1.0)\n",
            "Requirement already satisfied: protobuf<6,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.25.6)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (17.0.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: rich<14,>=10.14.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (13.9.4)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.0.0)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.12.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.5)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.27.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.8.2)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.1)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.1.31)\n",
            "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (3.0.0)\n",
            "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich<14,>=10.14.0->streamlit) (2.18.0)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.1.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2024.10.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.22.3)\n",
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.42.2-py2.py3-none-any.whl (9.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.6/9.6 MB\u001b[0m \u001b[31m65.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m48.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m4.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.42.2 watchdog-6.0.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import streamlit as st\n",
        "st.title(':Graph: Customer Churn Analysis :Graph:')\n",
        "st.text('Lets perform Customer Churn Analysis')"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "fZX_GwMZQLTd",
        "outputId": "b1a886c3-ef90-49b0-d619-5bd6e99a59f7"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-24 18:41:47.970 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 18:41:48.165 \n",
            "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
            "  command:\n",
            "\n",
            "    streamlit run /usr/local/lib/python3.11/dist-packages/colab_kernel_launcher.py [ARGUMENTS]\n",
            "2025-02-24 18:41:48.169 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 18:41:48.172 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-24 18:41:48.175 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "DeltaGenerator()"
            ]
          },
          "metadata": {},
          "execution_count": 41
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from io import StringIO  # To read the string data as a file"
      ],
      "metadata": {
        "id": "cZiW9S8MUpHc"
      },
      "execution_count": 48,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#  Map 'Yes' to 1 and 'No' to 0 in the 'Churn' column\n",
        "data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})\n",
        "\n",
        "# Print the updated 'Churn' column to verify\n",
        "print(data['Churn'].head())\n",
        "\n",
        "# Print the counts to verify (more thorough)\n",
        "print(data['Churn'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "PfRKHEgvUx0T",
        "outputId": "856db307-8218-4cc7-9be9-a0960ac19d30"
      },
      "execution_count": 51,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0   NaN\n",
            "1   NaN\n",
            "2   NaN\n",
            "3   NaN\n",
            "4   NaN\n",
            "Name: Churn, dtype: float64\n",
            "Series([], Name: count, dtype: int64)\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "st.image('CHURN.jpg')\n",
        "st.video('https://www.youtube.com/watch?v=_dzr1pm3Ymw')\n",
        "\n"
      ],
      "metadata": {
        "id": "dJs_jDuuR9F2",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 425
        },
        "outputId": "fc1ddf01-60aa-4ce2-b2b2-3d8b74cf7aa4"
      },
      "execution_count": 52,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-24 19:01:13.951 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "RuntimeError",
          "evalue": "Runtime hasn't been created!",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/streamlit/elements/lib/image_utils.py\u001b[0m in \u001b[0;36mimage_to_url\u001b[0;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[1;32m    285\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 286\u001b[0;31m             \u001b[0;32mwith\u001b[0m \u001b[0mopen\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m\"rb\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    287\u001b[0m                 \u001b[0mimage_data\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mf\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mread\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'CHURN.jpg'",
            "\nDuring handling of the above exception, another exception occurred:\n",
            "\u001b[0;31mRuntimeError\u001b[0m                              Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-52-f9d2c8bbcb52>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[0;32m----> 1\u001b[0;31m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mimage\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'CHURN.jpg'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      2\u001b[0m \u001b[0mst\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mvideo\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m'https://www.youtube.com/watch?v=_dzr1pm3Ymw'\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/streamlit/runtime/metrics_util.py\u001b[0m in \u001b[0;36mwrapped_func\u001b[0;34m(*args, **kwargs)\u001b[0m\n\u001b[1;32m    408\u001b[0m                 \u001b[0m_LOGGER\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdebug\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Failed to collect command telemetry\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mex\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    409\u001b[0m         \u001b[0;32mtry\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 410\u001b[0;31m             \u001b[0mresult\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mnon_optional_func\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    411\u001b[0m         \u001b[0;32mexcept\u001b[0m \u001b[0mRerunException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0mex\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    412\u001b[0m             \u001b[0;31m# Duplicated from below, because static analysis tools get confused\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/streamlit/elements/image.py\u001b[0m in \u001b[0;36mimage\u001b[0;34m(self, image, caption, width, use_column_width, clamp, channels, output_format, use_container_width)\u001b[0m\n\u001b[1;32m    179\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    180\u001b[0m         \u001b[0mimage_list_proto\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mImageListProto\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 181\u001b[0;31m         marshall_images(\n\u001b[0m\u001b[1;32m    182\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdg\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_get_delta_path_str\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    183\u001b[0m             \u001b[0mimage\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/streamlit/elements/lib/image_utils.py\u001b[0m in \u001b[0;36mmarshall_images\u001b[0;34m(coordinates, image, caption, width, proto_imgs, clamp, channels, output_format)\u001b[0m\n\u001b[1;32m    437\u001b[0m         \u001b[0mimage_id\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"%s-%i\"\u001b[0m \u001b[0;34m%\u001b[0m \u001b[0;34m(\u001b[0m\u001b[0mcoordinates\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mcoord_suffix\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    438\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 439\u001b[0;31m         proto_img.url = image_to_url(\n\u001b[0m\u001b[1;32m    440\u001b[0m             \u001b[0mimage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mwidth\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mclamp\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mchannels\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0moutput_format\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mimage_id\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    441\u001b[0m         )\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/streamlit/elements/lib/image_utils.py\u001b[0m in \u001b[0;36mimage_to_url\u001b[0;34m(image, width, clamp, channels, output_format, image_id)\u001b[0m\n\u001b[1;32m    296\u001b[0m                 \u001b[0mmimetype\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m\"application/octet-stream\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    297\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 298\u001b[0;31m             \u001b[0murl\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mruntime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mget_instance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mmedia_file_mgr\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0madd\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmimetype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mimage_id\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    299\u001b[0m             \u001b[0mcaching\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0msave_media_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mimage\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mmimetype\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mimage_id\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    300\u001b[0m             \u001b[0;32mreturn\u001b[0m \u001b[0murl\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/streamlit/runtime/__init__.py\u001b[0m in \u001b[0;36mget_instance\u001b[0;34m()\u001b[0m\n\u001b[1;32m     26\u001b[0m     \u001b[0mRuntime\u001b[0m \u001b[0mhasn\u001b[0m\u001b[0;31m'\u001b[0m\u001b[0mt\u001b[0m \u001b[0mbeen\u001b[0m \u001b[0mcreated\u001b[0m \u001b[0myet\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     27\u001b[0m     \"\"\"\n\u001b[0;32m---> 28\u001b[0;31m     \u001b[0;32mreturn\u001b[0m \u001b[0mRuntime\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0minstance\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     29\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     30\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/streamlit/runtime/runtime.py\u001b[0m in \u001b[0;36minstance\u001b[0;34m(cls)\u001b[0m\n\u001b[1;32m    161\u001b[0m         \"\"\"\n\u001b[1;32m    162\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_instance\u001b[0m \u001b[0;32mis\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 163\u001b[0;31m             \u001b[0;32mraise\u001b[0m \u001b[0mRuntimeError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Runtime hasn't been created!\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    164\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mcls\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_instance\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    165\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mRuntimeError\u001b[0m: Runtime hasn't been created!"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install dash\n",
        "!pip install jupyter-dash # Required to run dash apps in notebooks\n",
        "import dash\n",
        "import dash_core_components as dcc\n",
        "import dash_html_components as html\n",
        "from dash.dependencies import Input, Output\n",
        "import plotly.express as px  # Import Plotly Express"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "pHUHb-gnVw9-",
        "outputId": "4833e274-0b1b-42c0-b440-0d701a694851"
      },
      "execution_count": 54,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting dash\n",
            "  Downloading dash-2.18.2-py3-none-any.whl.metadata (10 kB)\n",
            "Collecting Flask<3.1,>=1.0.4 (from dash)\n",
            "  Downloading flask-3.0.3-py3-none-any.whl.metadata (3.2 kB)\n",
            "Collecting Werkzeug<3.1 (from dash)\n",
            "  Downloading werkzeug-3.0.6-py3-none-any.whl.metadata (3.7 kB)\n",
            "Requirement already satisfied: plotly>=5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (5.24.1)\n",
            "Collecting dash-html-components==2.0.0 (from dash)\n",
            "  Downloading dash_html_components-2.0.0-py3-none-any.whl.metadata (3.8 kB)\n",
            "Collecting dash-core-components==2.0.0 (from dash)\n",
            "  Downloading dash_core_components-2.0.0-py3-none-any.whl.metadata (2.9 kB)\n",
            "Collecting dash-table==5.0.0 (from dash)\n",
            "  Downloading dash_table-5.0.0-py3-none-any.whl.metadata (2.4 kB)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.11/dist-packages (from dash) (8.6.1)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from dash) (4.12.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from dash) (2.32.3)\n",
            "Collecting retrying (from dash)\n",
            "  Downloading retrying-1.3.4-py3-none-any.whl.metadata (6.9 kB)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.11/dist-packages (from dash) (1.6.0)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from dash) (75.1.0)\n",
            "Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (3.1.5)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (2.2.0)\n",
            "Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (8.1.8)\n",
            "Requirement already satisfied: blinker>=1.6.2 in /usr/local/lib/python3.11/dist-packages (from Flask<3.1,>=1.0.4->dash) (1.9.0)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from plotly>=5.0.0->dash) (9.0.0)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from plotly>=5.0.0->dash) (24.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from Werkzeug<3.1->dash) (3.0.2)\n",
            "Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.11/dist-packages (from importlib-metadata->dash) (3.21.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->dash) (2025.1.31)\n",
            "Requirement already satisfied: six>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from retrying->dash) (1.17.0)\n",
            "Downloading dash-2.18.2-py3-none-any.whl (7.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m7.8/7.8 MB\u001b[0m \u001b[31m75.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading dash_core_components-2.0.0-py3-none-any.whl (3.8 kB)\n",
            "Downloading dash_html_components-2.0.0-py3-none-any.whl (4.1 kB)\n",
            "Downloading dash_table-5.0.0-py3-none-any.whl (3.9 kB)\n",
            "Downloading flask-3.0.3-py3-none-any.whl (101 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m101.7/101.7 kB\u001b[0m \u001b[31m7.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading werkzeug-3.0.6-py3-none-any.whl (227 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m228.0/228.0 kB\u001b[0m \u001b[31m17.3 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading retrying-1.3.4-py3-none-any.whl (11 kB)\n",
            "Installing collected packages: dash-table, dash-html-components, dash-core-components, Werkzeug, retrying, Flask, dash\n",
            "  Attempting uninstall: Werkzeug\n",
            "    Found existing installation: Werkzeug 3.1.3\n",
            "    Uninstalling Werkzeug-3.1.3:\n",
            "      Successfully uninstalled Werkzeug-3.1.3\n",
            "  Attempting uninstall: Flask\n",
            "    Found existing installation: Flask 3.1.0\n",
            "    Uninstalling Flask-3.1.0:\n",
            "      Successfully uninstalled Flask-3.1.0\n",
            "Successfully installed Flask-3.0.3 Werkzeug-3.0.6 dash-2.18.2 dash-core-components-2.0.0 dash-html-components-2.0.0 dash-table-5.0.0 retrying-1.3.4\n",
            "Collecting jupyter-dash\n",
            "  Downloading jupyter_dash-0.4.2-py3-none-any.whl.metadata (3.6 kB)\n",
            "Requirement already satisfied: dash in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (2.18.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (2.32.3)\n",
            "Requirement already satisfied: flask in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (3.0.3)\n",
            "Requirement already satisfied: retrying in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (1.3.4)\n",
            "Requirement already satisfied: ipython in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (7.34.0)\n",
            "Requirement already satisfied: ipykernel in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (6.17.1)\n",
            "Collecting ansi2html (from jupyter-dash)\n",
            "  Downloading ansi2html-1.9.2-py3-none-any.whl.metadata (3.7 kB)\n",
            "Requirement already satisfied: nest-asyncio in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (1.6.0)\n",
            "Requirement already satisfied: Werkzeug<3.1 in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (3.0.6)\n",
            "Requirement already satisfied: plotly>=5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (5.24.1)\n",
            "Requirement already satisfied: dash-html-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (2.0.0)\n",
            "Requirement already satisfied: dash-core-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (2.0.0)\n",
            "Requirement already satisfied: dash-table==5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (5.0.0)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (8.6.1)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (4.12.2)\n",
            "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from dash->jupyter-dash) (75.1.0)\n",
            "Requirement already satisfied: Jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from flask->jupyter-dash) (3.1.5)\n",
            "Requirement already satisfied: itsdangerous>=2.1.2 in /usr/local/lib/python3.11/dist-packages (from flask->jupyter-dash) (2.2.0)\n",
            "Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from flask->jupyter-dash) (8.1.8)\n",
            "Requirement already satisfied: blinker>=1.6.2 in /usr/local/lib/python3.11/dist-packages (from flask->jupyter-dash) (1.9.0)\n",
            "Requirement already satisfied: debugpy>=1.0 in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (1.8.0)\n",
            "Requirement already satisfied: jupyter-client>=6.1.12 in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (6.1.12)\n",
            "Requirement already satisfied: matplotlib-inline>=0.1 in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (0.1.7)\n",
            "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (24.2)\n",
            "Requirement already satisfied: psutil in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (5.9.5)\n",
            "Requirement already satisfied: pyzmq>=17 in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (24.0.1)\n",
            "Requirement already satisfied: tornado>=6.1 in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (6.4.2)\n",
            "Requirement already satisfied: traitlets>=5.1.0 in /usr/local/lib/python3.11/dist-packages (from ipykernel->jupyter-dash) (5.7.1)\n",
            "Collecting jedi>=0.16 (from ipython->jupyter-dash)\n",
            "  Downloading jedi-0.19.2-py2.py3-none-any.whl.metadata (22 kB)\n",
            "Requirement already satisfied: decorator in /usr/local/lib/python3.11/dist-packages (from ipython->jupyter-dash) (4.4.2)\n",
            "Requirement already satisfied: pickleshare in /usr/local/lib/python3.11/dist-packages (from ipython->jupyter-dash) (0.7.5)\n",
            "Requirement already satisfied: prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0 in /usr/local/lib/python3.11/dist-packages (from ipython->jupyter-dash) (3.0.50)\n",
            "Requirement already satisfied: pygments in /usr/local/lib/python3.11/dist-packages (from ipython->jupyter-dash) (2.18.0)\n",
            "Requirement already satisfied: backcall in /usr/local/lib/python3.11/dist-packages (from ipython->jupyter-dash) (0.2.0)\n",
            "Requirement already satisfied: pexpect>4.3 in /usr/local/lib/python3.11/dist-packages (from ipython->jupyter-dash) (4.9.0)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests->jupyter-dash) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests->jupyter-dash) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests->jupyter-dash) (2.3.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests->jupyter-dash) (2025.1.31)\n",
            "Requirement already satisfied: six>=1.7.0 in /usr/local/lib/python3.11/dist-packages (from retrying->jupyter-dash) (1.17.0)\n",
            "Requirement already satisfied: parso<0.9.0,>=0.8.4 in /usr/local/lib/python3.11/dist-packages (from jedi>=0.16->ipython->jupyter-dash) (0.8.4)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from Jinja2>=3.1.2->flask->jupyter-dash) (3.0.2)\n",
            "Requirement already satisfied: jupyter-core>=4.6.0 in /usr/local/lib/python3.11/dist-packages (from jupyter-client>=6.1.12->ipykernel->jupyter-dash) (5.7.2)\n",
            "Requirement already satisfied: python-dateutil>=2.1 in /usr/local/lib/python3.11/dist-packages (from jupyter-client>=6.1.12->ipykernel->jupyter-dash) (2.8.2)\n",
            "Requirement already satisfied: ptyprocess>=0.5 in /usr/local/lib/python3.11/dist-packages (from pexpect>4.3->ipython->jupyter-dash) (0.7.0)\n",
            "Requirement already satisfied: tenacity>=6.2.0 in /usr/local/lib/python3.11/dist-packages (from plotly>=5.0.0->dash->jupyter-dash) (9.0.0)\n",
            "Requirement already satisfied: wcwidth in /usr/local/lib/python3.11/dist-packages (from prompt-toolkit!=3.0.0,!=3.0.1,<3.1.0,>=2.0.0->ipython->jupyter-dash) (0.2.13)\n",
            "Requirement already satisfied: zipp>=3.20 in /usr/local/lib/python3.11/dist-packages (from importlib-metadata->dash->jupyter-dash) (3.21.0)\n",
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.11/dist-packages (from jupyter-core>=4.6.0->jupyter-client>=6.1.12->ipykernel->jupyter-dash) (4.3.6)\n",
            "Downloading jupyter_dash-0.4.2-py3-none-any.whl (23 kB)\n",
            "Downloading ansi2html-1.9.2-py3-none-any.whl (17 kB)\n",
            "Downloading jedi-0.19.2-py2.py3-none-any.whl (1.6 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.6/1.6 MB\u001b[0m \u001b[31m32.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: jedi, ansi2html, jupyter-dash\n",
            "Successfully installed ansi2html-1.9.2 jedi-0.19.2 jupyter-dash-0.4.2\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "<ipython-input-54-4cab49680b14>:4: UserWarning:\n",
            "\n",
            "\n",
            "The dash_core_components package is deprecated. Please replace\n",
            "`import dash_core_components as dcc` with `from dash import dcc`\n",
            "\n",
            "<ipython-input-54-4cab49680b14>:5: UserWarning:\n",
            "\n",
            "\n",
            "The dash_html_components package is deprecated. Please replace\n",
            "`import dash_html_components as html` with `from dash import html`\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# 1. Calculate Average Monthly Charges by Tenure\n",
        "\n",
        "# Group by 'tenure' and calculate the average 'MonthlyCharges' for each tenure.\n",
        "avg_monthly_charges = data.groupby('tenure')['MonthlyCharges'].mean().reset_index()\n",
        "\n",
        "# 2. Create the Scatter Plot\n",
        "\n",
        "# Use Plotly Express to create the scatter plot.\n",
        "fig = px.scatter(avg_monthly_charges,\n",
        "                 x='tenure',\n",
        "                 y='MonthlyCharges',\n",
        "                 title='Average Monthly Charges vs. Tenure',\n",
        "                 labels={'tenure': 'Tenure (Months)',\n",
        "                         'MonthlyCharges': 'Average Monthly Charges'})\n",
        "\n",
        "# 3. Dash App\n",
        "app = dash.Dash(__name__)\n",
        "\n",
        "app.layout = html.Div([\n",
        "    html.H1(\"Customer Churn Visualization\"),\n",
        "    dcc.Graph(id='churn-plot', figure=fig),\n",
        "    html.Div([\n",
        "        html.Label(\"Tenure Range:\"),\n",
        "        dcc.RangeSlider(\n",
        "            id='tenure-slider',\n",
        "            min=data['tenure'].min(),\n",
        "            max=data['tenure'].max(),\n",
        "            value=[data['tenure'].min(), data['tenure'].max()],\n",
        "            marks={str(tenure): str(tenure) for tenure in data['tenure'].unique()}\n",
        "        )\n",
        "    ], style={'width': '80%', 'margin': '0 auto'}),\n",
        "    html.Div(id='slider-output-container', style={'marginTop': '20px'})\n",
        "])\n",
        "@app.callback(\n",
        "    Output('slider-output-container', 'children'),\n",
        "    Input('tenure-slider', 'value'))\n",
        "def update_output(value):\n",
        "    return f'You have selected a tenure range of {value[0]} - {value[1]}'\n",
        "# Callback to update the graph based on the slider\n",
        "@app.callback(\n",
        "    Output('churn-plot', 'figure'),\n",
        "    Input('tenure-slider', 'value')\n",
        ")\n",
        "def update_graph(tenure_range):\n",
        "    # Filter data based on the tenure range from the slider\n",
        "    filtered_data = data[(data['tenure'] >= tenure_range[0]) & (data['tenure'] <= tenure_range[1])]\n",
        "\n",
        "    # Group by 'tenure' and calculate the average 'MonthlyCharges' for the filtered data.\n",
        "    avg_monthly_charges = filtered_data.groupby('tenure')['MonthlyCharges'].mean().reset_index()\n",
        "\n",
        "    # Update the scatter plot with the filtered data\n",
        "    fig = px.scatter(avg_monthly_charges,\n",
        "                    x='tenure',\n",
        "                    y='MonthlyCharges',\n",
        "                    title='Average Monthly Charges vs. Tenure',\n",
        "                    labels={'tenure': 'Tenure (Months)',\n",
        "                            'MonthlyCharges': 'Average Monthly Charges'})\n",
        "    return fig\n",
        "\n",
        "# Run the Dash app\n",
        "if __name__ == '__main__':\n",
        "    app.run_server(debug=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 672
        },
        "id": "hyFDdRTJVeK4",
        "outputId": "543c59d7-fbeb-474b-9bfb-4511ad8156dc"
      },
      "execution_count": 55,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "(async (port, path, width, height, cache, element) => {\n",
              "    if (!google.colab.kernel.accessAllowed && !cache) {\n",
              "      return;\n",
              "    }\n",
              "    element.appendChild(document.createTextNode(''));\n",
              "    const url = await google.colab.kernel.proxyPort(port, {cache});\n",
              "    const iframe = document.createElement('iframe');\n",
              "    iframe.src = new URL(path, url).toString();\n",
              "    iframe.height = height;\n",
              "    iframe.width = width;\n",
              "    iframe.style.border = 0;\n",
              "    iframe.allow = [\n",
              "        'accelerometer',\n",
              "        'autoplay',\n",
              "        'camera',\n",
              "        'clipboard-read',\n",
              "        'clipboard-write',\n",
              "        'gyroscope',\n",
              "        'magnetometer',\n",
              "        'microphone',\n",
              "        'serial',\n",
              "        'usb',\n",
              "        'xr-spatial-tracking',\n",
              "    ].join('; ');\n",
              "    element.appendChild(iframe);\n",
              "  })(8050, \"/\", \"100%\", 650, false, window.element)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "import plotly.express as px\n",
        "import dash\n",
        "from dash import dcc, html\n",
        "from dash.dependencies import Input, Output\n",
        "\n",
        "# 1. Load and Preprocess the Data\n",
        "data = pd.read_csv(\"WA_Fn-UseC_-Telco-Customer-Churn.csv\")\n",
        "\n",
        "# Handle missing values in 'TotalCharges'\n",
        "data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)\n",
        "data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')\n",
        "data['TotalCharges'] = data['TotalCharges'].fillna(0)\n",
        "\n",
        "# Convert 'Churn' to numerical (0 and 1)\n",
        "data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})\n",
        "\n",
        "# Convert SeniorCitizen to object for categorical treatment\n",
        "data['SeniorCitizen'] = data['SeniorCitizen'].astype(object)\n",
        "\n",
        "# 2.  Dashboard Layout\n",
        "\n",
        "app = dash.Dash(__name__)\n",
        "\n",
        "app.layout = html.Div([\n",
        "    html.H1(\"Telco Customer Churn Analysis\", style={'textAlign': 'center'}),\n",
        "\n",
        "    # 2.1. Demographics Section\n",
        "    html.H2(\"Demographics\", style={'textAlign': 'left'}),\n",
        "    html.Div([\n",
        "        html.Label(\"Select Demographic Feature:\"),\n",
        "        dcc.Dropdown(\n",
        "            id='demographic-feature',\n",
        "            options=[\n",
        "                {'label': 'Gender', 'value': 'gender'},\n",
        "                {'label': 'Senior Citizen', 'value': 'SeniorCitizen'},\n",
        "                {'label': 'Partner', 'value': 'Partner'},\n",
        "                {'label': 'Dependents', 'value': 'Dependents'}\n",
        "            ],\n",
        "            value='gender'  # Default selected value\n",
        "        ),\n",
        "        dcc.Graph(id='demographics-plot')\n",
        "    ], style={'width': '48%', 'display': 'inline-block'}),\n",
        "\n",
        "    # 2.2. Service Usage Section\n",
        "    html.H2(\"Service Usage\", style={'textAlign': 'left'}),\n",
        "    html.Div([\n",
        "        html.Label(\"Select Service Feature:\"),\n",
        "        dcc.Dropdown(\n",
        "            id='service-feature',\n",
        "            options=[\n",
        "                {'label': 'Phone Service', 'value': 'PhoneService'},\n",
        "                {'label': 'Multiple Lines', 'value': 'MultipleLines'},\n",
        "                {'label': 'Internet Service', 'value': 'InternetService'},\n",
        "                {'label': 'Online Security', 'value': 'OnlineSecurity'},\n",
        "                {'label': 'Online Backup', 'value': 'OnlineBackup'},\n",
        "                {'label': 'Device Protection', 'value': 'DeviceProtection'},\n",
        "                {'label': 'Tech Support', 'value': 'TechSupport'},\n",
        "                {'label': 'Streaming TV', 'value': 'StreamingTV'},\n",
        "                {'label': 'Streaming Movies', 'value': 'StreamingMovies'}\n",
        "            ],\n",
        "            value='PhoneService'  # Default selected value\n",
        "        ),\n",
        "        dcc.Graph(id='service-usage-plot')\n",
        "    ], style={'width': '48%', 'display': 'inline-block'}),\n",
        "\n",
        "    # 2.3 Tenure vs Monthly Charges Scatter Plot with Tenure Slider\n",
        "    html.H2(\"Tenure vs. Monthly Charges\", style={'textAlign': 'left'}),\n",
        "    html.Div([\n",
        "        dcc.Graph(id='tenure-monthly-charges-plot'),\n",
        "        html.Label(\"Select Tenure Range:\"),\n",
        "        dcc.RangeSlider(\n",
        "            id='tenure-slider',\n",
        "            min=data['tenure'].min(),\n",
        "            max=data['tenure'].max(),\n",
        "            value=[data['tenure'].min(), data['tenure'].max()],\n",
        "            marks={str(tenure): str(tenure) for tenure in data['tenure'].unique()}\n",
        "        ),\n",
        "    ], style={'width': '96%', 'margin': '0 auto'})\n",
        "])\n",
        "\n",
        "# 3.  Callbacks for Interactivity\n",
        "\n",
        "# 3.1. Callback for Demographics Plot\n",
        "@app.callback(\n",
        "    Output('demographics-plot', 'figure'),\n",
        "    Input('demographic-feature', 'value')\n",
        ")\n",
        "def update_demographics_plot(selected_feature):\n",
        "    demographics_counts = data.groupby([selected_feature, 'Churn']).size().reset_index(name='counts')\n",
        "    fig = px.bar(demographics_counts, x=selected_feature, y='counts', color='Churn',\n",
        "                 barmode='group', title=f\"Churn by {selected_feature.capitalize()}\")\n",
        "    fig.update_layout(yaxis_title=\"Number of Customers\")\n",
        "    return fig\n",
        "\n",
        "# 3.2. Callback for Service Usage Plot\n",
        "@app.callback(\n",
        "    Output('service-usage-plot', 'figure'),\n",
        "    Input('service-feature', 'value')\n",
        ")\n",
        "def update_service_usage_plot(selected_feature):\n",
        "    service_counts = data.groupby([selected_feature, 'Churn']).size().reset_index(name='counts')\n",
        "    fig = px.bar(service_counts, x=selected_feature, y='counts', color='Churn',\n",
        "                 barmode='group', title=f\"Churn by {selected_feature.capitalize()}\")\n",
        "    fig.update_layout(yaxis_title=\"Number of Customers\")\n",
        "    return fig\n",
        "\n",
        "# 3.3 Callback to update the Tenure vs Monthly Charges Scatter Plot based on the slider\n",
        "@app.callback(\n",
        "    Output('tenure-monthly-charges-plot', 'figure'),\n",
        "    Input('tenure-slider', 'value')\n",
        ")\n",
        "def update_tenure_monthly_charges_plot(tenure_range):\n",
        "    filtered_data = data[(data['tenure'] >= tenure_range[0]) & (data['tenure'] <= tenure_range[1])]\n",
        "    fig = px.scatter(filtered_data, x='tenure', y='MonthlyCharges', color='Churn',\n",
        "                     title=\"Tenure vs. Monthly Charges (Filtered)\",\n",
        "                     labels={'tenure': 'Tenure (Months)', 'MonthlyCharges': 'Monthly Charges'})\n",
        "    return fig\n",
        "\n",
        "# 4. Run the App\n",
        "if __name__ == '__main__':\n",
        "    app.run_server(debug=True)\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 672
        },
        "id": "s5g5LbbSXOVH",
        "outputId": "07ba8413-a4d8-4c1f-a648-d99cb0be987f"
      },
      "execution_count": 56,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.Javascript object>"
            ],
            "application/javascript": [
              "(async (port, path, width, height, cache, element) => {\n",
              "    if (!google.colab.kernel.accessAllowed && !cache) {\n",
              "      return;\n",
              "    }\n",
              "    element.appendChild(document.createTextNode(''));\n",
              "    const url = await google.colab.kernel.proxyPort(port, {cache});\n",
              "    const iframe = document.createElement('iframe');\n",
              "    iframe.src = new URL(path, url).toString();\n",
              "    iframe.height = height;\n",
              "    iframe.width = width;\n",
              "    iframe.style.border = 0;\n",
              "    iframe.allow = [\n",
              "        'accelerometer',\n",
              "        'autoplay',\n",
              "        'camera',\n",
              "        'clipboard-read',\n",
              "        'clipboard-write',\n",
              "        'gyroscope',\n",
              "        'magnetometer',\n",
              "        'microphone',\n",
              "        'serial',\n",
              "        'usb',\n",
              "        'xr-spatial-tracking',\n",
              "    ].join('; ');\n",
              "    element.appendChild(iframe);\n",
              "  })(8050, \"/\", \"100%\", 650, false, window.element)"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import dash\n",
        "from dash import dcc, html\n",
        "from dash.dependencies import Input, Output"
      ],
      "metadata": {
        "id": "KH0AhXPJYAvH"
      },
      "execution_count": 57,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2. Calculate Churn Rate by Tenure\n",
        "churn_rate_by_tenure = data.groupby('tenure')['Churn'].mean().reset_index()\n",
        "churn_rate_by_tenure.columns = ['Tenure', 'Churn Rate'] # Rename columns for clarity\n",
        "\n",
        "# 3. Create the initial scatter plot\n",
        "fig = px.scatter(churn_rate_by_tenure,\n",
        "                    x='Tenure',\n",
        "                    y='Churn Rate',\n",
        "                    title='Churn Rate vs. Tenure',\n",
        "                    labels={'Tenure': 'Tenure (Months)',\n",
        "                            'Churn Rate': 'Churn Rate'})"
      ],
      "metadata": {
        "id": "RdGu7z4gYHb-"
      },
      "execution_count": 58,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "app.layout = html.Div([\n",
        "    html.H1(\"Churn Rate Analysis by Tenure\", style={'textAlign': 'center'}),\n",
        "\n",
        "    dcc.Graph(id='churn-rate-plot', figure=fig),  # Initial plot\n",
        "\n",
        "    html.Div([\n",
        "        html.Label(\"Select Tenure Range:\"),\n",
        "        dcc.RangeSlider(\n",
        "            id='tenure-slider',\n",
        "            min=data['tenure'].min(),\n",
        "            max=data['tenure'].max(),\n",
        "            value=[data['tenure'].min(), data['tenure'].max()],\n",
        "            marks={str(tenure): str(tenure) for tenure in data['tenure'].unique()}\n",
        "        )\n",
        "    ], style={'width': '80%', 'margin': '0 auto'})\n",
        "])\n",
        "\n",
        "# 5. Callback to update the graph based on the slider\n",
        "@app.callback(\n",
        "    Output('churn-rate-plot', 'figure'),\n",
        "    Input('tenure-slider', 'value')\n",
        ")\n",
        "def update_graph(tenure_range):\n",
        "    # Filter data based on the tenure range from the slider\n",
        "    filtered_data = data[(data['tenure'] >= tenure_range[0]) & (data['tenure'] <= tenure_range[1])]\n",
        "\n",
        "    # Recalculate Churn Rate by Tenure for the filtered data\n",
        "    churn_rate_by_tenure = filtered_data.groupby('tenure')['Churn'].mean().reset_index()\n",
        "    churn_rate_by_tenure.columns = ['Tenure', 'Churn Rate']\n",
        "\n",
        "    # Update the scatter plot with the filtered data\n",
        "    fig = px.scatter(churn_rate_by_tenure,\n",
        "                    x='Tenure',\n",
        "                    y='Churn Rate',\n",
        "                    title='Churn Rate vs. Tenure (Filtered)',\n",
        "                    labels={'Tenure': 'Tenure (Months)',\n",
        "                            'Churn Rate': 'Churn Rate'})\n",
        "    return fig\n",
        "\n",
        "# 6. Run the App\n",
        "#if __name__ == '__main__':\n",
        "   # app.run_server(debug=True)"
      ],
      "metadata": {
        "id": "6GvrH5DCYNxC"
      },
      "execution_count": 61,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "# New Section"
      ],
      "metadata": {
        "id": "bPW6T1KZEjyW"
      }
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "q4tks4wnUNOG"
      }
    }
  ]
}