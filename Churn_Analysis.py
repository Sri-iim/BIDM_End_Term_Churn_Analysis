{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPqGKsu1HSLHHKIBskoqjyH",
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
      "execution_count": 184,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "2Dzvn5nDw2dv",
        "outputId": "9e5933a5-63e6-4436-a46f-f58d518c8e0b"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.11/dist-packages (1.42.2)\n",
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
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.9.1)\n",
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
            "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich<14,>=10.14.0->streamlit) (0.1.2)\n"
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
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
        "from sklearn.compose import ColumnTransformer\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
        "import plotly.express as px  # For visualizations"
      ],
      "metadata": {
        "id": "Dbpl2vwFdA__"
      },
      "execution_count": 130,
      "outputs": []
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
        "outputId": "b24fea8e-88e3-4e86-f536-1dac537029d5"
      },
      "execution_count": 198,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<IPython.core.display.HTML object>"
            ],
            "text/html": [
              "\n",
              "     <input type=\"file\" id=\"files-46c133fc-c5bf-4a28-a54f-df035e14647f\" name=\"files[]\" multiple disabled\n",
              "        style=\"border:none\" />\n",
              "     <output id=\"result-46c133fc-c5bf-4a28-a54f-df035e14647f\">\n",
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
            "Saving WA_Fn-UseC_-Telco-Customer-Churn.csv to WA_Fn-UseC_-Telco-Customer-Churn (4).csv\n",
            "User uploaded file \"WA_Fn-UseC_-Telco-Customer-Churn (4).csv\" with length 977501 bytes\n"
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
        "\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "BUFCj98Kydz0",
        "outputId": "40afd67e-8104-4732-adc8-bfee6c7a6bed"
      },
      "execution_count": 132,
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
        "print(data.head()) # Display the first few rows"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xRERDy4iIS1_",
        "outputId": "1f992106-a7df-4051-8ba5-e4fd8b3fe90e"
      },
      "execution_count": 199,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   customerID  gender  SeniorCitizen  Partner  Dependents  tenure  \\\n",
            "0  7590-VHVEG     NaN              0      NaN         NaN       1   \n",
            "1  5575-GNVDE     NaN              0      NaN         NaN      34   \n",
            "2  3668-QPYBK     NaN              0      NaN         NaN       2   \n",
            "3  7795-CFOCW     NaN              0      NaN         NaN      45   \n",
            "4  9237-HQITU     NaN              0      NaN         NaN       2   \n",
            "\n",
            "   PhoneService     MultipleLines InternetService OnlineSecurity  ...  \\\n",
            "0           NaN  No phone service             DSL             No  ...   \n",
            "1           NaN                No             DSL            Yes  ...   \n",
            "2           NaN                No             DSL            Yes  ...   \n",
            "3           NaN  No phone service             DSL            Yes  ...   \n",
            "4           NaN                No     Fiber optic             No  ...   \n",
            "\n",
            "  DeviceProtection TechSupport StreamingTV StreamingMovies        Contract  \\\n",
            "0               No          No          No              No  Month-to-month   \n",
            "1              Yes          No          No              No        One year   \n",
            "2               No          No          No              No  Month-to-month   \n",
            "3              Yes         Yes          No              No        One year   \n",
            "4               No          No          No              No  Month-to-month   \n",
            "\n",
            "  PaperlessBilling              PaymentMethod MonthlyCharges  TotalCharges  \\\n",
            "0              NaN           Electronic check          29.85         29.85   \n",
            "1              NaN               Mailed check          56.95       1889.50   \n",
            "2              NaN               Mailed check          53.85        108.15   \n",
            "3              NaN  Bank transfer (automatic)          42.30       1840.75   \n",
            "4              NaN           Electronic check          70.70        151.65   \n",
            "\n",
            "   Churn  \n",
            "0      0  \n",
            "1      0  \n",
            "2      1  \n",
            "3      0  \n",
            "4      1  \n",
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
      "execution_count": 133,
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
      "execution_count": 134,
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
        "outputId": "6a667e76-0d72-4251-e2e2-d825e104305b"
      },
      "execution_count": 200,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   customerID  gender  SeniorCitizen  Partner  Dependents  tenure  \\\n",
            "0  7590-VHVEG     NaN              0      NaN         NaN       1   \n",
            "1  5575-GNVDE     NaN              0      NaN         NaN      34   \n",
            "2  3668-QPYBK     NaN              0      NaN         NaN       2   \n",
            "3  7795-CFOCW     NaN              0      NaN         NaN      45   \n",
            "4  9237-HQITU     NaN              0      NaN         NaN       2   \n",
            "\n",
            "   PhoneService     MultipleLines InternetService OnlineSecurity  ...  \\\n",
            "0           NaN  No phone service             DSL             No  ...   \n",
            "1           NaN                No             DSL            Yes  ...   \n",
            "2           NaN                No             DSL            Yes  ...   \n",
            "3           NaN  No phone service             DSL            Yes  ...   \n",
            "4           NaN                No     Fiber optic             No  ...   \n",
            "\n",
            "  DeviceProtection TechSupport StreamingTV StreamingMovies        Contract  \\\n",
            "0               No          No          No              No  Month-to-month   \n",
            "1              Yes          No          No              No        One year   \n",
            "2               No          No          No              No  Month-to-month   \n",
            "3              Yes         Yes          No              No        One year   \n",
            "4               No          No          No              No  Month-to-month   \n",
            "\n",
            "  PaperlessBilling              PaymentMethod MonthlyCharges  TotalCharges  \\\n",
            "0              NaN           Electronic check          29.85         29.85   \n",
            "1              NaN               Mailed check          56.95       1889.50   \n",
            "2              NaN               Mailed check          53.85        108.15   \n",
            "3              NaN  Bank transfer (automatic)          42.30       1840.75   \n",
            "4              NaN           Electronic check          70.70        151.65   \n",
            "\n",
            "   Churn  \n",
            "0      0  \n",
            "1      0  \n",
            "2      1  \n",
            "3      0  \n",
            "4      1  \n",
            "\n",
            "[5 rows x 21 columns]\n",
            "<class 'pandas.core.frame.DataFrame'>\n",
            "RangeIndex: 7043 entries, 0 to 7042\n",
            "Data columns (total 21 columns):\n",
            " #   Column            Non-Null Count  Dtype  \n",
            "---  ------            --------------  -----  \n",
            " 0   customerID        7043 non-null   object \n",
            " 1   gender            0 non-null      float64\n",
            " 2   SeniorCitizen     7043 non-null   int64  \n",
            " 3   Partner           0 non-null      float64\n",
            " 4   Dependents        0 non-null      float64\n",
            " 5   tenure            7043 non-null   int64  \n",
            " 6   PhoneService      0 non-null      float64\n",
            " 7   MultipleLines     7043 non-null   object \n",
            " 8   InternetService   7043 non-null   object \n",
            " 9   OnlineSecurity    7043 non-null   object \n",
            " 10  OnlineBackup      7043 non-null   object \n",
            " 11  DeviceProtection  7043 non-null   object \n",
            " 12  TechSupport       7043 non-null   object \n",
            " 13  StreamingTV       7043 non-null   object \n",
            " 14  StreamingMovies   7043 non-null   object \n",
            " 15  Contract          7043 non-null   object \n",
            " 16  PaperlessBilling  0 non-null      float64\n",
            " 17  PaymentMethod     7043 non-null   object \n",
            " 18  MonthlyCharges    7043 non-null   float64\n",
            " 19  TotalCharges      7043 non-null   float64\n",
            " 20  Churn             7043 non-null   int64  \n",
            "dtypes: float64(7), int64(3), object(11)\n",
            "memory usage: 1.1+ MB\n",
            "None\n",
            "       gender  SeniorCitizen  Partner  Dependents       tenure  PhoneService  \\\n",
            "count     0.0    7043.000000      0.0         0.0  7043.000000           0.0   \n",
            "mean      NaN       0.162147      NaN         NaN    32.371149           NaN   \n",
            "std       NaN       0.368612      NaN         NaN    24.559481           NaN   \n",
            "min       NaN       0.000000      NaN         NaN     0.000000           NaN   \n",
            "25%       NaN       0.000000      NaN         NaN     9.000000           NaN   \n",
            "50%       NaN       0.000000      NaN         NaN    29.000000           NaN   \n",
            "75%       NaN       0.000000      NaN         NaN    55.000000           NaN   \n",
            "max       NaN       1.000000      NaN         NaN    72.000000           NaN   \n",
            "\n",
            "       PaperlessBilling  MonthlyCharges  TotalCharges        Churn  \n",
            "count               0.0     7043.000000   7043.000000  7043.000000  \n",
            "mean                NaN       64.761692   2279.734304     0.265370  \n",
            "std                 NaN       30.090047   2266.794470     0.441561  \n",
            "min                 NaN       18.250000      0.000000     0.000000  \n",
            "25%                 NaN       35.500000    398.550000     0.000000  \n",
            "50%                 NaN       70.350000   1394.550000     0.000000  \n",
            "75%                 NaN       89.850000   3786.600000     1.000000  \n",
            "max                 NaN      118.750000   8684.800000     1.000000  \n"
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
      "execution_count": 201,
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
        "outputId": "4332d460-5e8d-48df-8109-09873f3b7ed1"
      },
      "execution_count": 202,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "       gender  SeniorCitizen  Partner  Dependents       tenure  PhoneService  \\\n",
            "count     0.0    7043.000000      0.0         0.0  7043.000000           0.0   \n",
            "mean      NaN       0.162147      NaN         NaN    32.371149           NaN   \n",
            "std       NaN       0.368612      NaN         NaN    24.559481           NaN   \n",
            "min       NaN       0.000000      NaN         NaN     0.000000           NaN   \n",
            "25%       NaN       0.000000      NaN         NaN     9.000000           NaN   \n",
            "50%       NaN       0.000000      NaN         NaN    29.000000           NaN   \n",
            "75%       NaN       0.000000      NaN         NaN    55.000000           NaN   \n",
            "max       NaN       1.000000      NaN         NaN    72.000000           NaN   \n",
            "\n",
            "       PaperlessBilling  MonthlyCharges  TotalCharges        Churn  \n",
            "count               0.0     7043.000000   7043.000000  7043.000000  \n",
            "mean                NaN       64.761692   2279.734304     0.265370  \n",
            "std                 NaN       30.090047   2266.794470     0.441561  \n",
            "min                 NaN       18.250000      0.000000     0.000000  \n",
            "25%                 NaN       35.500000    398.550000     0.000000  \n",
            "50%                 NaN       70.350000   1394.550000     0.000000  \n",
            "75%                 NaN       89.850000   3786.600000     1.000000  \n",
            "max                 NaN      118.750000   8684.800000     1.000000  \n"
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
        "outputId": "990b9edf-a368-42f5-eff7-e94a1af5ece8"
      },
      "execution_count": 203,
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
            " 1   gender            0 non-null      float64\n",
            " 2   SeniorCitizen     7043 non-null   int64  \n",
            " 3   Partner           0 non-null      float64\n",
            " 4   Dependents        0 non-null      float64\n",
            " 5   tenure            7043 non-null   int64  \n",
            " 6   PhoneService      0 non-null      float64\n",
            " 7   MultipleLines     7043 non-null   object \n",
            " 8   InternetService   7043 non-null   object \n",
            " 9   OnlineSecurity    7043 non-null   object \n",
            " 10  OnlineBackup      7043 non-null   object \n",
            " 11  DeviceProtection  7043 non-null   object \n",
            " 12  TechSupport       7043 non-null   object \n",
            " 13  StreamingTV       7043 non-null   object \n",
            " 14  StreamingMovies   7043 non-null   object \n",
            " 15  Contract          7043 non-null   object \n",
            " 16  PaperlessBilling  0 non-null      float64\n",
            " 17  PaymentMethod     7043 non-null   object \n",
            " 18  MonthlyCharges    7043 non-null   float64\n",
            " 19  TotalCharges      7043 non-null   float64\n",
            " 20  Churn             7043 non-null   int64  \n",
            "dtypes: float64(7), int64(3), object(11)\n",
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
        "outputId": "bc62498f-6f68-4dd1-8d84-b9760b27554a"
      },
      "execution_count": 212,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "customerID             0\n",
            "gender                 0\n",
            "SeniorCitizen          0\n",
            "Partner             7043\n",
            "Dependents          7043\n",
            "tenure                 0\n",
            "PhoneService        7043\n",
            "MultipleLines          0\n",
            "InternetService        0\n",
            "OnlineSecurity         0\n",
            "OnlineBackup           0\n",
            "DeviceProtection       0\n",
            "TechSupport            0\n",
            "StreamingTV            0\n",
            "StreamingMovies        0\n",
            "Contract               0\n",
            "PaperlessBilling    7043\n",
            "PaymentMethod          0\n",
            "MonthlyCharges         0\n",
            "TotalCharges           0\n",
            "Churn                  0\n",
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
        "\n",
        "# Print the updated 'TotalCharges' column to verify\n",
        "print(data['TotalCharges'].head())\n",
        "\n",
        "# Print the counts to verify (more thorough)\n",
        "print(data['TotalCharges'].value_counts())"
      ],
      "metadata": {
        "id": "QZYq0m-7OjGB",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "645adf04-71c6-44fa-f5be-1d262d15e9d9"
      },
      "execution_count": 191,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0      29.85\n",
            "1    1889.50\n",
            "2     108.15\n",
            "3    1840.75\n",
            "4     151.65\n",
            "Name: TotalCharges, dtype: float64\n",
            "TotalCharges\n",
            "0.00       11\n",
            "20.20      11\n",
            "19.75       9\n",
            "20.05       8\n",
            "19.90       8\n",
            "           ..\n",
            "6849.40     1\n",
            "692.35      1\n",
            "130.15      1\n",
            "3211.90     1\n",
            "6844.50     1\n",
            "Name: count, Length: 6531, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "iT-sl7cGJABt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Identify missing values (represented by empty strings) and replace them with NaN\n",
        "data['gender'] = data['gender'].replace(' ', np.nan)\n",
        "\n",
        "# Print the updated 'TotalCharges' column to verify\n",
        "print(data['gender'].head())\n",
        "\n",
        "# Print the counts to verify (more thorough)\n",
        "print(data['gender'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "1fd0666e-e917-47d3-a830-c32fde7ca34b",
        "id": "7nZab9eiJAoR"
      },
      "execution_count": 207,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0      29.85\n",
            "1    1889.50\n",
            "2     108.15\n",
            "3    1840.75\n",
            "4     151.65\n",
            "Name: gender, dtype: float64\n",
            "gender\n",
            "0.00       11\n",
            "20.20      11\n",
            "19.75       9\n",
            "20.05       8\n",
            "19.90       8\n",
            "           ..\n",
            "6849.40     1\n",
            "692.35      1\n",
            "130.15      1\n",
            "3211.90     1\n",
            "6844.50     1\n",
            "Name: count, Length: 6531, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Identify missing values (represented by empty strings) and replace them with NaN\n",
        "data['Partner'] = data['Partner'].replace(' ', np.nan)\n",
        "\n",
        "# Print the updated 'TotalCharges' column to verify\n",
        "print(data['Partner'].head())\n",
        "\n",
        "# Print the counts to verify (more thorough)\n",
        "print(data['Partner'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "xnh0ABiyKJ5a",
        "outputId": "396b07c3-2bec-4f53-908e-9e7b1d195bac"
      },
      "execution_count": 211,
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
            "Name: Partner, dtype: float64\n",
            "Series([], Name: count, dtype: int64)\n"
          ]
        }
      ]
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
      "execution_count": 194,
      "outputs": []
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
      "execution_count": 142,
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
        "outputId": "8c6b414f-9ed9-47d3-f462-67f2d3b52d78"
      },
      "execution_count": 143,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: streamlit in /usr/local/lib/python3.11/dist-packages (1.42.2)\n",
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
            "Requirement already satisfied: watchdog<7,>=2.1.5 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.0.0)\n",
            "Requirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Requirement already satisfied: pydeck<1,>=0.8.0b4 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.9.1)\n",
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
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n"
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
        "outputId": "3bf20dae-9ded-4430-e30b-74f864e001a2"
      },
      "execution_count": 144,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-25 03:08:16.732 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:08:16.740 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:08:16.743 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:08:16.746 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
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
          "execution_count": 144
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
      "execution_count": 145,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.2. Convert Binary Columns to Numeric\n",
        "# Include Churn in the columns to be converted to 0 and 1\n",
        "for col in ['gender', 'Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', ]:\n",
        "    data[col] = data[col].map({'Yes': 1, 'No': 0})\n",
        "data['gender'] = data['gender'].map({'Male': 1, 'Female': 0})"
      ],
      "metadata": {
        "id": "cHUNNPVaDScz"
      },
      "execution_count": 178,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#  Map 'Yes' to 1 and 'No' to 0 in the 'Churn' column\n",
        "#data['gender'] = data['gender'].map({'Yes': 1, 'No': 0})\n",
        "\n",
        "# Print the updated 'Churn' column to verify\n",
        "print(data['gender'].head())\n",
        "\n",
        "# Print the counts to verify (more thorough)\n",
        "print(data['gender'].value_counts())"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "4lNJ0ySIH-ku",
        "outputId": "00248f5c-49de-4af9-c98b-fdbbc5396619"
      },
      "execution_count": 213,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0      29.85\n",
            "1    1889.50\n",
            "2     108.15\n",
            "3    1840.75\n",
            "4     151.65\n",
            "Name: gender, dtype: float64\n",
            "gender\n",
            "0.00       11\n",
            "20.20      11\n",
            "19.75       9\n",
            "20.05       8\n",
            "19.90       8\n",
            "           ..\n",
            "6849.40     1\n",
            "692.35      1\n",
            "130.15      1\n",
            "3211.90     1\n",
            "6844.50     1\n",
            "Name: count, Length: 6531, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#  Map 'Yes' to 1 and 'No' to 0 in the 'Churn' column\n",
        "#data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})\n",
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
        "outputId": "3dd3027d-cef9-473f-c905-85761dc87dee"
      },
      "execution_count": 214,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0    0\n",
            "1    0\n",
            "2    1\n",
            "3    0\n",
            "4    1\n",
            "Name: Churn, dtype: int64\n",
            "Churn\n",
            "0    5174\n",
            "1    1869\n",
            "Name: count, dtype: int64\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Upload the image file before using st.image()\n",
        "uploaded_file = st.file_uploader(\"CHURN\", type=\"jpg\")\n",
        "if uploaded_file is not None:\n",
        "    # To read file as bytes:\n",
        "    bytes_data = uploaded_file.getvalue()\n",
        "    st.image(bytes_data, caption='Uploaded Image', use_column_width=True)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "HejwNALR94Rn",
        "outputId": "21c509af-c02a-4277-cd90-f80432efdbeb"
      },
      "execution_count": 151,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-25 03:09:56.687 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:09:56.689 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:09:56.690 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:09:56.692 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:09:56.693 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "import streamlit as st\n",
        "\n",
        "st.title(':Graph: Customer Churn Analysis :Graph:')\n",
        "st.text('Lets perform Customer Churn Analysis')\n",
        "\n",
        "try:\n",
        "    st.image('CHURN.jpg')\n",
        "except FileNotFoundError:\n",
        "    st.write(\"Error: 'CHURN.jpg' not found. Please make sure the image is in the same directory as your script.\")\n",
        "\n",
        "\n",
        "#Embed a Youtube video\n",
        "st.video('https://www.youtube.com/watch?v=_dzr1pm3Ymw')\n",
        "st.write(\"Error: 'CHURN.jpg' not found. Please make sure the image is in the same directory as your script.\")\n",
        "\n",
        "\n",
        "#Embed a Youtube video\n",
        "st.video('https://www.youtube.com/watch?v=_dzr1pm3Ymw')\n",
        "\n"
      ],
      "metadata": {
        "id": "dJs_jDuuR9F2",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "ea047ff8-e7bd-4d83-c61f-6ab7432bf9ee"
      },
      "execution_count": 107,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-02-25 03:02:54.322 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.324 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.325 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.327 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.328 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.331 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.332 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.333 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.334 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.335 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.336 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.338 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.339 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.340 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.341 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.342 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-02-25 03:02:54.343 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
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
          "execution_count": 107
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
          "base_uri": "https://localhost:8080/"
        },
        "id": "pHUHb-gnVw9-",
        "outputId": "5887f80e-756d-4170-81f2-184992ef144c"
      },
      "execution_count": 153,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: dash in /usr/local/lib/python3.11/dist-packages (2.18.2)\n",
            "Requirement already satisfied: Flask<3.1,>=1.0.4 in /usr/local/lib/python3.11/dist-packages (from dash) (3.0.3)\n",
            "Requirement already satisfied: Werkzeug<3.1 in /usr/local/lib/python3.11/dist-packages (from dash) (3.0.6)\n",
            "Requirement already satisfied: plotly>=5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (5.24.1)\n",
            "Requirement already satisfied: dash-html-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (2.0.0)\n",
            "Requirement already satisfied: dash-core-components==2.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (2.0.0)\n",
            "Requirement already satisfied: dash-table==5.0.0 in /usr/local/lib/python3.11/dist-packages (from dash) (5.0.0)\n",
            "Requirement already satisfied: importlib-metadata in /usr/local/lib/python3.11/dist-packages (from dash) (8.6.1)\n",
            "Requirement already satisfied: typing-extensions>=4.1.1 in /usr/local/lib/python3.11/dist-packages (from dash) (4.12.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from dash) (2.32.3)\n",
            "Requirement already satisfied: retrying in /usr/local/lib/python3.11/dist-packages (from dash) (1.3.4)\n",
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
            "Requirement already satisfied: jupyter-dash in /usr/local/lib/python3.11/dist-packages (0.4.2)\n",
            "Requirement already satisfied: dash in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (2.18.2)\n",
            "Requirement already satisfied: requests in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (2.32.3)\n",
            "Requirement already satisfied: flask in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (3.0.3)\n",
            "Requirement already satisfied: retrying in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (1.3.4)\n",
            "Requirement already satisfied: ipython in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (7.34.0)\n",
            "Requirement already satisfied: ipykernel in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (6.17.1)\n",
            "Requirement already satisfied: ansi2html in /usr/local/lib/python3.11/dist-packages (from jupyter-dash) (1.9.2)\n",
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
            "Requirement already satisfied: jedi>=0.16 in /usr/local/lib/python3.11/dist-packages (from ipython->jupyter-dash) (0.19.2)\n",
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
            "Requirement already satisfied: platformdirs>=2.5 in /usr/local/lib/python3.11/dist-packages (from jupyter-core>=4.6.0->jupyter-client>=6.1.12->ipykernel->jupyter-dash) (4.3.6)\n"
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
          "base_uri": "https://localhost:8080/"
        },
        "id": "hyFDdRTJVeK4",
        "outputId": "ab5080ec-1c1b-4a3b-b45a-8e0be384e2b1"
      },
      "execution_count": 216,
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
        "# data = pd.read_csv(\"WA_Fn-UseC_-Telco-Customer-Churn.csv\")\n",
        "\n",
        "# Handle missing values in 'TotalCharges'\n",
        "# data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)\n",
        "# data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')\n",
        "# data['TotalCharges'] = data['TotalCharges'].fillna(0)\n",
        "\n",
        "# Convert 'Churn' to numerical (0 and 1)\n",
        "# data['Churn'] = data['Churn'].map({'Yes': 1, 'No': 0})\n",
        "\n",
        "# Convert SeniorCitizen to object for categorical treatment\n",
        "# data['SeniorCitizen'] = data['SeniorCitizen'].astype(object)\n",
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
        "outputId": "409d89c6-cbac-4453-8a30-91a576c1aacb"
      },
      "execution_count": 155,
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
      "execution_count": 156,
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
      "execution_count": 217,
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
        "#app.run_server(debug=True)"
      ],
      "metadata": {
        "id": "6GvrH5DCYNxC"
      },
      "execution_count": 158,
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
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
        "from sklearn.compose import ColumnTransformer\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
        "import plotly.express as px  # For visualizations"
      ],
      "metadata": {
        "id": "dj8ExQIdZ369"
      },
      "execution_count": 159,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2. Preprocessing\n",
        "# 2.1. Handle Missing Values\n",
        "# data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)\n",
        "# data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')\n",
        "# data['TotalCharges'] = data['TotalCharges'].fillna(0)\n",
        "\n",
        "# 2.1. Handle Missing Values\n",
        "# data['TotalCharges'] = data['TotalCharges'].replace(' ', np.nan)\n",
        "# data['TotalCharges'] = pd.to_numeric(data['TotalCharges'], errors='coerce')\n",
        "# data['TotalCharges'] = data['TotalCharges'].fillna(0)  # Imputation with 0\n"
      ],
      "metadata": {
        "id": "zsjgh3lSZ83e"
      },
      "execution_count": 44,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [],
      "metadata": {
        "id": "l47si84_d-1V"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.2. Convert Binary Columns to Numeric\n",
        "# for col in ['Partner', 'Dependents', 'PhoneService', 'PaperlessBilling', 'Churn']:\n",
        "   #  data[col] = data[col].map({'Yes': 1, 'No': 0})\n",
        "data['gender'] = data['gender'].map({'Male': 1, 'Female': 0})\n"
      ],
      "metadata": {
        "id": "TEXY6yJTb4ez"
      },
      "execution_count": 218,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.3. Identify Categorical and Numerical Features\n",
        "# categorical_features = data.select_dtypes(include='object').columns\n",
        "# numerical_features = data.select_dtypes(include=['int64', 'float64']).columns.drop('Churn')  # Exclude target"
      ],
      "metadata": {
        "id": "MjCtqKaTbTVj"
      },
      "execution_count": 120,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 2.4. Create a ColumnTransformer\n",
        "preprocessor = ColumnTransformer(\n",
        "    transformers=[\n",
        "        ('num', StandardScaler(), numerical_features),\n",
        "        ('cat', OneHotEncoder(handle_unknown='ignore'), categorical_features)  # handle_unknown crucial\n",
        "    ],\n",
        "    remainder='passthrough'  # Crucial: Keep other columns\n",
        ")"
      ],
      "metadata": {
        "id": "ED_os6MLbYGH"
      },
      "execution_count": 161,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# Impute missing values in y_train (e.g., with the most frequent value)\n",
        "from sklearn.impute import SimpleImputer\n",
        "\n",
        "imputer = SimpleImputer(strategy='most_frequent')  # Use most frequent strategy\n",
        "y_train = imputer.fit_transform(y_train.values.reshape(-1, 1))  # Reshape for imputer\n",
        "y_train = y_train.ravel()  # Flatten back to original shape"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "8VEUX4hy_p3R",
        "outputId": "4b72629e-9053-419c-f0a2-6fd7c22e953e"
      },
      "execution_count": 162,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/sklearn/impute/_base.py:635: UserWarning:\n",
            "\n",
            "Skipping features without any observed values: [0]. At least one non-missing value is needed for imputation with strategy='most_frequent'.\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "\n",
        "# 3. Split Data into Training and Testing Sets\n",
        "X = data.drop(['Churn', ], axis=1)  # Drop target and ID\n",
        "y = data['Churn']\n",
        "X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)"
      ],
      "metadata": {
        "id": "-ieLsIsDcJ3x"
      },
      "execution_count": 219,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 4. Apply the Preprocessor\n",
        "# ----> Only apply fit_transform on the training data once\n",
        "X_train_transformed = preprocessor.fit_transform(X_train)\n",
        "X_test_transformed = preprocessor.transform(X_test)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pGEXTfuEcNV0",
        "outputId": "93686025-0758-4842-8308-3498c805dba5"
      },
      "execution_count": 220,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/sklearn/utils/extmath.py:1101: RuntimeWarning:\n",
            "\n",
            "invalid value encountered in divide\n",
            "\n",
            "/usr/local/lib/python3.11/dist-packages/sklearn/utils/extmath.py:1106: RuntimeWarning:\n",
            "\n",
            "invalid value encountered in divide\n",
            "\n",
            "/usr/local/lib/python3.11/dist-packages/sklearn/utils/extmath.py:1126: RuntimeWarning:\n",
            "\n",
            "invalid value encountered in divide\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Now use X_train_transformed and X_test_transformed for your model training\n"
      ],
      "metadata": {
        "id": "X2A-nwwyZ-_x"
      },
      "execution_count": 222,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 4. Apply the Preprocessor (Only transform, not fit_transform on X_train)\n",
        "X_train = preprocessor.fit_transform(X_train) # Fit and transform on the training data\n",
        "X_test = preprocessor.transform(X_test) # Only transform the testing data"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "_eon83X8ai-e",
        "outputId": "6576857f-30c9-41f7-f176-249bd36d56bf"
      },
      "execution_count": 221,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "/usr/local/lib/python3.11/dist-packages/sklearn/utils/extmath.py:1101: RuntimeWarning:\n",
            "\n",
            "invalid value encountered in divide\n",
            "\n",
            "/usr/local/lib/python3.11/dist-packages/sklearn/utils/extmath.py:1106: RuntimeWarning:\n",
            "\n",
            "invalid value encountered in divide\n",
            "\n",
            "/usr/local/lib/python3.11/dist-packages/sklearn/utils/extmath.py:1126: RuntimeWarning:\n",
            "\n",
            "invalid value encountered in divide\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import pandas as pd\n",
        "import numpy as np\n",
        "from sklearn.model_selection import train_test_split\n",
        "from sklearn.preprocessing import StandardScaler, OneHotEncoder\n",
        "from sklearn.compose import ColumnTransformer\n",
        "# Make sure to import LogisticRegression:\n",
        "from sklearn.linear_model import LogisticRegression\n",
        "from sklearn.metrics import accuracy_score, classification_report, confusion_matrix\n",
        "import plotly.express as px  # For visualizations"
      ],
      "metadata": {
        "id": "qIzurWG6_Qj_"
      },
      "execution_count": 223,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "# 5. Train Logistic Regression Model\n",
        "model = LogisticRegression(solver='liblinear', random_state=42)  # 'liblinear' good for smaller datasets\n",
        "model.fit(X_train, y_train)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "pfMLjBSXBVIi",
        "outputId": "e8bee1d8-86b6-494f-d5d3-04df2de39c76"
      },
      "execution_count": 224,
      "outputs": [
        {
          "output_type": "error",
          "ename": "ValueError",
          "evalue": "Input X contains NaN.\nLogisticRegression does not accept missing values encoded as NaN natively. For supervised learning, you might want to consider sklearn.ensemble.HistGradientBoostingClassifier and Regressor which accept missing values encoded as NaNs natively. Alternatively, it is possible to preprocess the data, for instance by using an imputer transformer in a pipeline or drop samples with missing values. See https://scikit-learn.org/stable/modules/impute.html You can find a list of all estimators that handle NaN values at the following page: https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mValueError\u001b[0m                                Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-224-341ddb932e30>\u001b[0m in \u001b[0;36m<cell line: 0>\u001b[0;34m()\u001b[0m\n\u001b[1;32m      1\u001b[0m \u001b[0;31m# 5. Train Logistic Regression Model\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      2\u001b[0m \u001b[0mmodel\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mLogisticRegression\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0msolver\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m'liblinear'\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mrandom_state\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;36m42\u001b[0m\u001b[0;34m)\u001b[0m  \u001b[0;31m# 'liblinear' good for smaller datasets\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 3\u001b[0;31m \u001b[0mmodel\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfit\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX_train\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my_train\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/base.py\u001b[0m in \u001b[0;36mwrapper\u001b[0;34m(estimator, *args, **kwargs)\u001b[0m\n\u001b[1;32m   1387\u001b[0m                 )\n\u001b[1;32m   1388\u001b[0m             ):\n\u001b[0;32m-> 1389\u001b[0;31m                 \u001b[0;32mreturn\u001b[0m \u001b[0mfit_method\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mestimator\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m*\u001b[0m\u001b[0margs\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mkwargs\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   1390\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1391\u001b[0m         \u001b[0;32mreturn\u001b[0m \u001b[0mwrapper\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/linear_model/_logistic.py\u001b[0m in \u001b[0;36mfit\u001b[0;34m(self, X, y, sample_weight)\u001b[0m\n\u001b[1;32m   1220\u001b[0m             \u001b[0m_dtype\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m[\u001b[0m\u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfloat64\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mnp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mfloat32\u001b[0m\u001b[0;34m]\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1221\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1222\u001b[0;31m         X, y = validate_data(\n\u001b[0m\u001b[1;32m   1223\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1224\u001b[0m             \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36mvalidate_data\u001b[0;34m(_estimator, X, y, reset, validate_separately, skip_check_array, **check_params)\u001b[0m\n\u001b[1;32m   2959\u001b[0m             \u001b[0my\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcheck_array\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0minput_name\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;34m\"y\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcheck_y_params\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2960\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 2961\u001b[0;31m             \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mcheck_X_y\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0;34m**\u001b[0m\u001b[0mcheck_params\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m   2962\u001b[0m         \u001b[0mout\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0my\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   2963\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36mcheck_X_y\u001b[0;34m(X, y, accept_sparse, accept_large_sparse, dtype, order, copy, force_writeable, force_all_finite, ensure_all_finite, ensure_2d, allow_nd, multi_output, ensure_min_samples, ensure_min_features, y_numeric, estimator)\u001b[0m\n\u001b[1;32m   1368\u001b[0m     \u001b[0mensure_all_finite\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0m_deprecate_force_all_finite\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mforce_all_finite\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mensure_all_finite\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1369\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1370\u001b[0;31m     X = check_array(\n\u001b[0m\u001b[1;32m   1371\u001b[0m         \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1372\u001b[0m         \u001b[0maccept_sparse\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maccept_sparse\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36mcheck_array\u001b[0;34m(array, accept_sparse, accept_large_sparse, dtype, order, copy, force_writeable, force_all_finite, ensure_all_finite, ensure_non_negative, ensure_2d, allow_nd, ensure_min_samples, ensure_min_features, estimator, input_name)\u001b[0m\n\u001b[1;32m   1012\u001b[0m     \u001b[0;32mif\u001b[0m \u001b[0msp\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0missparse\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marray\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1013\u001b[0m         \u001b[0m_ensure_no_complex_data\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0marray\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m-> 1014\u001b[0;31m         array = _ensure_sparse_format(\n\u001b[0m\u001b[1;32m   1015\u001b[0m             \u001b[0marray\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m   1016\u001b[0m             \u001b[0maccept_sparse\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0maccept_sparse\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36m_ensure_sparse_format\u001b[0;34m(sparse_container, accept_sparse, dtype, copy, ensure_all_finite, accept_large_sparse, estimator_name, input_name)\u001b[0m\n\u001b[1;32m    647\u001b[0m             )\n\u001b[1;32m    648\u001b[0m         \u001b[0;32melse\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 649\u001b[0;31m             _assert_all_finite(\n\u001b[0m\u001b[1;32m    650\u001b[0m                 \u001b[0msparse_container\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mdata\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    651\u001b[0m                 \u001b[0mallow_nan\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mensure_all_finite\u001b[0m \u001b[0;34m==\u001b[0m \u001b[0;34m\"allow-nan\"\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36m_assert_all_finite\u001b[0;34m(X, allow_nan, msg_dtype, estimator_name, input_name)\u001b[0m\n\u001b[1;32m    118\u001b[0m         \u001b[0;32mreturn\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    119\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 120\u001b[0;31m     _assert_all_finite_element_wise(\n\u001b[0m\u001b[1;32m    121\u001b[0m         \u001b[0mX\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    122\u001b[0m         \u001b[0mxp\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0mxp\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.11/dist-packages/sklearn/utils/validation.py\u001b[0m in \u001b[0;36m_assert_all_finite_element_wise\u001b[0;34m(X, xp, allow_nan, msg_dtype, estimator_name, input_name)\u001b[0m\n\u001b[1;32m    167\u001b[0m                 \u001b[0;34m\"#estimators-that-handle-nan-values\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    168\u001b[0m             )\n\u001b[0;32m--> 169\u001b[0;31m         \u001b[0;32mraise\u001b[0m \u001b[0mValueError\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mmsg_err\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    170\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    171\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mValueError\u001b[0m: Input X contains NaN.\nLogisticRegression does not accept missing values encoded as NaN natively. For supervised learning, you might want to consider sklearn.ensemble.HistGradientBoostingClassifier and Regressor which accept missing values encoded as NaNs natively. Alternatively, it is possible to preprocess the data, for instance by using an imputer transformer in a pipeline or drop samples with missing values. See https://scikit-learn.org/stable/modules/impute.html You can find a list of all estimators that handle NaN values at the following page: https://scikit-learn.org/stable/modules/impute.html#estimators-that-handle-nan-values"
          ]
        }
      ]
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