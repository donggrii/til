{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "ADsP_6장_2.ipynb",
      "provenance": [],
      "collapsed_sections": [],
      "toc_visible": true
    },
    "kernelspec": {
      "name": "ir",
      "display_name": "R"
    },
    "language_info": {
      "name": "R"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "BP62LlYCwuIo"
      },
      "source": [
        "# 6장. R 기초와 데이터 마트"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "3uckaBUzwzYg"
      },
      "source": [
        "## 2. 데이터 마트"
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "Dn9K6sHv8lHZ"
      },
      "source": [
        "### (2) reshape 활용"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "mKDdlp7konXR",
        "outputId": "ef596d9b-c806-4c41-ed0c-41afc0e24296"
      },
      "source": [
        "install.packages(\"reshape\")    # cast 함수는 reshape 패키지\n",
        "library(reshape)\n",
        "install.packages(\"reshape2\")\n",
        "library(reshape2)\n",
        "data(airquality)"
      ],
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Installing package into ‘/usr/local/lib/R/site-library’\n",
            "(as ‘lib’ is unspecified)\n",
            "\n",
            "also installing the dependency ‘plyr’\n",
            "\n",
            "\n",
            "Installing package into ‘/usr/local/lib/R/site-library’\n",
            "(as ‘lib’ is unspecified)\n",
            "\n",
            "\n",
            "Attaching package: ‘reshape2’\n",
            "\n",
            "\n",
            "The following objects are masked from ‘package:reshape’:\n",
            "\n",
            "    colsplit, melt, recast\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 192
        },
        "id": "ZrkuRc6urnmV",
        "outputId": "f32eea7d-9fce-4a50-873b-27388f2b1bfe"
      },
      "source": [
        "head(airquality, 3)"
      ],
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  Ozone Solar.R Wind Temp Month Day\n",
              "1 41    190      7.4 67   5     1  \n",
              "2 36    118      8.0 72   5     2  \n",
              "3 12    149     12.6 74   5     3  "
            ],
            "text/latex": "A data.frame: 3 × 6\n\\begin{tabular}{r|llllll}\n  & Ozone & Solar.R & Wind & Temp & Month & Day\\\\\n  & <int> & <int> & <dbl> & <int> & <int> & <int>\\\\\n\\hline\n\t1 & 41 & 190 &  7.4 & 67 & 5 & 1\\\\\n\t2 & 36 & 118 &  8.0 & 72 & 5 & 2\\\\\n\t3 & 12 & 149 & 12.6 & 74 & 5 & 3\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 3 × 6\n\n| <!--/--> | Ozone &lt;int&gt; | Solar.R &lt;int&gt; | Wind &lt;dbl&gt; | Temp &lt;int&gt; | Month &lt;int&gt; | Day &lt;int&gt; |\n|---|---|---|---|---|---|---|\n| 1 | 41 | 190 |  7.4 | 67 | 5 | 1 |\n| 2 | 36 | 118 |  8.0 | 72 | 5 | 2 |\n| 3 | 12 | 149 | 12.6 | 74 | 5 | 3 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 3 × 6</caption>\n",
              "<thead>\n",
              "\t<tr><th></th><th scope=col>Ozone</th><th scope=col>Solar.R</th><th scope=col>Wind</th><th scope=col>Temp</th><th scope=col>Month</th><th scope=col>Day</th></tr>\n",
              "\t<tr><th></th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><th scope=row>1</th><td>41</td><td>190</td><td> 7.4</td><td>67</td><td>5</td><td>1</td></tr>\n",
              "\t<tr><th scope=row>2</th><td>36</td><td>118</td><td> 8.0</td><td>72</td><td>5</td><td>2</td></tr>\n",
              "\t<tr><th scope=row>3</th><td>12</td><td>149</td><td>12.6</td><td>74</td><td>5</td><td>3</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 286
        },
        "id": "xgQy9UkAruYx",
        "outputId": "1c24d1be-afec-4858-dfbf-bd1afddcac62"
      },
      "source": [
        "colnames(airquality) <- tolower(colnames(airquality))    # 소문자로 변환\n",
        "head(airquality)"
      ],
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  ozone solar.r wind temp month day\n",
              "1 41    190      7.4 67   5     1  \n",
              "2 36    118      8.0 72   5     2  \n",
              "3 12    149     12.6 74   5     3  \n",
              "4 18    313     11.5 62   5     4  \n",
              "5 NA     NA     14.3 56   5     5  \n",
              "6 28     NA     14.9 66   5     6  "
            ],
            "text/latex": "A data.frame: 6 × 6\n\\begin{tabular}{r|llllll}\n  & ozone & solar.r & wind & temp & month & day\\\\\n  & <int> & <int> & <dbl> & <int> & <int> & <int>\\\\\n\\hline\n\t1 & 41 & 190 &  7.4 & 67 & 5 & 1\\\\\n\t2 & 36 & 118 &  8.0 & 72 & 5 & 2\\\\\n\t3 & 12 & 149 & 12.6 & 74 & 5 & 3\\\\\n\t4 & 18 & 313 & 11.5 & 62 & 5 & 4\\\\\n\t5 & NA &  NA & 14.3 & 56 & 5 & 5\\\\\n\t6 & 28 &  NA & 14.9 & 66 & 5 & 6\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 6 × 6\n\n| <!--/--> | ozone &lt;int&gt; | solar.r &lt;int&gt; | wind &lt;dbl&gt; | temp &lt;int&gt; | month &lt;int&gt; | day &lt;int&gt; |\n|---|---|---|---|---|---|---|\n| 1 | 41 | 190 |  7.4 | 67 | 5 | 1 |\n| 2 | 36 | 118 |  8.0 | 72 | 5 | 2 |\n| 3 | 12 | 149 | 12.6 | 74 | 5 | 3 |\n| 4 | 18 | 313 | 11.5 | 62 | 5 | 4 |\n| 5 | NA |  NA | 14.3 | 56 | 5 | 5 |\n| 6 | 28 |  NA | 14.9 | 66 | 5 | 6 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 6 × 6</caption>\n",
              "<thead>\n",
              "\t<tr><th></th><th scope=col>ozone</th><th scope=col>solar.r</th><th scope=col>wind</th><th scope=col>temp</th><th scope=col>month</th><th scope=col>day</th></tr>\n",
              "\t<tr><th></th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><th scope=row>1</th><td>41</td><td>190</td><td> 7.4</td><td>67</td><td>5</td><td>1</td></tr>\n",
              "\t<tr><th scope=row>2</th><td>36</td><td>118</td><td> 8.0</td><td>72</td><td>5</td><td>2</td></tr>\n",
              "\t<tr><th scope=row>3</th><td>12</td><td>149</td><td>12.6</td><td>74</td><td>5</td><td>3</td></tr>\n",
              "\t<tr><th scope=row>4</th><td>18</td><td>313</td><td>11.5</td><td>62</td><td>5</td><td>4</td></tr>\n",
              "\t<tr><th scope=row>5</th><td>NA</td><td> NA</td><td>14.3</td><td>56</td><td>5</td><td>5</td></tr>\n",
              "\t<tr><th scope=row>6</th><td>28</td><td> NA</td><td>14.9</td><td>66</td><td>5</td><td>6</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "KbRkgP8FrvAB",
        "outputId": "08dbab98-7cdf-4566-8dd3-70b90cc0b879"
      },
      "source": [
        "names(airquality)    # 변수명 확인"
      ],
      "execution_count": 4,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "[1] \"ozone\"   \"solar.r\" \"wind\"    \"temp\"    \"month\"   \"day\"    "
            ],
            "text/latex": "\\begin{enumerate*}\n\\item 'ozone'\n\\item 'solar.r'\n\\item 'wind'\n\\item 'temp'\n\\item 'month'\n\\item 'day'\n\\end{enumerate*}\n",
            "text/markdown": "1. 'ozone'\n2. 'solar.r'\n3. 'wind'\n4. 'temp'\n5. 'month'\n6. 'day'\n\n\n",
            "text/html": [
              "<style>\n",
              ".list-inline {list-style: none; margin:0; padding: 0}\n",
              ".list-inline>li {display: inline-block}\n",
              ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
              "</style>\n",
              "<ol class=list-inline><li>'ozone'</li><li>'solar.r'</li><li>'wind'</li><li>'temp'</li><li>'month'</li><li>'day'</li></ol>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "OOHwGgJarvM5",
        "outputId": "a7922dcd-45c5-4c6e-a8c6-9cbe1a5d1af5"
      },
      "source": [
        "T <- melt(airquality, id = c(\"month\", \"day\"), na.rm = TRUE)      # melt id에 있는 변수를 기준으로 나머지 변수를 variable이란 이름의 데이터로 만들고, 원래 변숫값을 value에 저장\n",
        "T"
      ],
      "execution_count": 5,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "    month day variable value\n",
              "1   5      1  ozone     41  \n",
              "2   5      2  ozone     36  \n",
              "3   5      3  ozone     12  \n",
              "4   5      4  ozone     18  \n",
              "6   5      6  ozone     28  \n",
              "7   5      7  ozone     23  \n",
              "8   5      8  ozone     19  \n",
              "9   5      9  ozone      8  \n",
              "11  5     11  ozone      7  \n",
              "12  5     12  ozone     16  \n",
              "13  5     13  ozone     11  \n",
              "14  5     14  ozone     14  \n",
              "15  5     15  ozone     18  \n",
              "16  5     16  ozone     14  \n",
              "17  5     17  ozone     34  \n",
              "18  5     18  ozone      6  \n",
              "19  5     19  ozone     30  \n",
              "20  5     20  ozone     11  \n",
              "21  5     21  ozone      1  \n",
              "22  5     22  ozone     11  \n",
              "23  5     23  ozone      4  \n",
              "24  5     24  ozone     32  \n",
              "28  5     28  ozone     23  \n",
              "29  5     29  ozone     45  \n",
              "30  5     30  ozone    115  \n",
              "31  5     31  ozone     37  \n",
              "38  6      7  ozone     29  \n",
              "40  6      9  ozone     71  \n",
              "41  6     10  ozone     39  \n",
              "44  6     13  ozone     23  \n",
              "⋮   ⋮     ⋮   ⋮        ⋮    \n",
              "583 9      1  temp     91   \n",
              "584 9      2  temp     92   \n",
              "585 9      3  temp     93   \n",
              "586 9      4  temp     93   \n",
              "587 9      5  temp     87   \n",
              "588 9      6  temp     84   \n",
              "589 9      7  temp     80   \n",
              "590 9      8  temp     78   \n",
              "591 9      9  temp     75   \n",
              "592 9     10  temp     73   \n",
              "593 9     11  temp     81   \n",
              "594 9     12  temp     76   \n",
              "595 9     13  temp     77   \n",
              "596 9     14  temp     71   \n",
              "597 9     15  temp     71   \n",
              "598 9     16  temp     78   \n",
              "599 9     17  temp     67   \n",
              "600 9     18  temp     76   \n",
              "601 9     19  temp     68   \n",
              "602 9     20  temp     82   \n",
              "603 9     21  temp     64   \n",
              "604 9     22  temp     71   \n",
              "605 9     23  temp     81   \n",
              "606 9     24  temp     69   \n",
              "607 9     25  temp     63   \n",
              "608 9     26  temp     70   \n",
              "609 9     27  temp     77   \n",
              "610 9     28  temp     75   \n",
              "611 9     29  temp     76   \n",
              "612 9     30  temp     68   "
            ],
            "text/latex": "A data.frame: 568 × 4\n\\begin{tabular}{r|llll}\n  & month & day & variable & value\\\\\n  & <int> & <int> & <fct> & <dbl>\\\\\n\\hline\n\t1 & 5 &  1 & ozone &  41\\\\\n\t2 & 5 &  2 & ozone &  36\\\\\n\t3 & 5 &  3 & ozone &  12\\\\\n\t4 & 5 &  4 & ozone &  18\\\\\n\t6 & 5 &  6 & ozone &  28\\\\\n\t7 & 5 &  7 & ozone &  23\\\\\n\t8 & 5 &  8 & ozone &  19\\\\\n\t9 & 5 &  9 & ozone &   8\\\\\n\t11 & 5 & 11 & ozone &   7\\\\\n\t12 & 5 & 12 & ozone &  16\\\\\n\t13 & 5 & 13 & ozone &  11\\\\\n\t14 & 5 & 14 & ozone &  14\\\\\n\t15 & 5 & 15 & ozone &  18\\\\\n\t16 & 5 & 16 & ozone &  14\\\\\n\t17 & 5 & 17 & ozone &  34\\\\\n\t18 & 5 & 18 & ozone &   6\\\\\n\t19 & 5 & 19 & ozone &  30\\\\\n\t20 & 5 & 20 & ozone &  11\\\\\n\t21 & 5 & 21 & ozone &   1\\\\\n\t22 & 5 & 22 & ozone &  11\\\\\n\t23 & 5 & 23 & ozone &   4\\\\\n\t24 & 5 & 24 & ozone &  32\\\\\n\t28 & 5 & 28 & ozone &  23\\\\\n\t29 & 5 & 29 & ozone &  45\\\\\n\t30 & 5 & 30 & ozone & 115\\\\\n\t31 & 5 & 31 & ozone &  37\\\\\n\t38 & 6 &  7 & ozone &  29\\\\\n\t40 & 6 &  9 & ozone &  71\\\\\n\t41 & 6 & 10 & ozone &  39\\\\\n\t44 & 6 & 13 & ozone &  23\\\\\n\t⋮ & ⋮ & ⋮ & ⋮ & ⋮\\\\\n\t583 & 9 &  1 & temp & 91\\\\\n\t584 & 9 &  2 & temp & 92\\\\\n\t585 & 9 &  3 & temp & 93\\\\\n\t586 & 9 &  4 & temp & 93\\\\\n\t587 & 9 &  5 & temp & 87\\\\\n\t588 & 9 &  6 & temp & 84\\\\\n\t589 & 9 &  7 & temp & 80\\\\\n\t590 & 9 &  8 & temp & 78\\\\\n\t591 & 9 &  9 & temp & 75\\\\\n\t592 & 9 & 10 & temp & 73\\\\\n\t593 & 9 & 11 & temp & 81\\\\\n\t594 & 9 & 12 & temp & 76\\\\\n\t595 & 9 & 13 & temp & 77\\\\\n\t596 & 9 & 14 & temp & 71\\\\\n\t597 & 9 & 15 & temp & 71\\\\\n\t598 & 9 & 16 & temp & 78\\\\\n\t599 & 9 & 17 & temp & 67\\\\\n\t600 & 9 & 18 & temp & 76\\\\\n\t601 & 9 & 19 & temp & 68\\\\\n\t602 & 9 & 20 & temp & 82\\\\\n\t603 & 9 & 21 & temp & 64\\\\\n\t604 & 9 & 22 & temp & 71\\\\\n\t605 & 9 & 23 & temp & 81\\\\\n\t606 & 9 & 24 & temp & 69\\\\\n\t607 & 9 & 25 & temp & 63\\\\\n\t608 & 9 & 26 & temp & 70\\\\\n\t609 & 9 & 27 & temp & 77\\\\\n\t610 & 9 & 28 & temp & 75\\\\\n\t611 & 9 & 29 & temp & 76\\\\\n\t612 & 9 & 30 & temp & 68\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 568 × 4\n\n| <!--/--> | month &lt;int&gt; | day &lt;int&gt; | variable &lt;fct&gt; | value &lt;dbl&gt; |\n|---|---|---|---|---|\n| 1 | 5 |  1 | ozone |  41 |\n| 2 | 5 |  2 | ozone |  36 |\n| 3 | 5 |  3 | ozone |  12 |\n| 4 | 5 |  4 | ozone |  18 |\n| 6 | 5 |  6 | ozone |  28 |\n| 7 | 5 |  7 | ozone |  23 |\n| 8 | 5 |  8 | ozone |  19 |\n| 9 | 5 |  9 | ozone |   8 |\n| 11 | 5 | 11 | ozone |   7 |\n| 12 | 5 | 12 | ozone |  16 |\n| 13 | 5 | 13 | ozone |  11 |\n| 14 | 5 | 14 | ozone |  14 |\n| 15 | 5 | 15 | ozone |  18 |\n| 16 | 5 | 16 | ozone |  14 |\n| 17 | 5 | 17 | ozone |  34 |\n| 18 | 5 | 18 | ozone |   6 |\n| 19 | 5 | 19 | ozone |  30 |\n| 20 | 5 | 20 | ozone |  11 |\n| 21 | 5 | 21 | ozone |   1 |\n| 22 | 5 | 22 | ozone |  11 |\n| 23 | 5 | 23 | ozone |   4 |\n| 24 | 5 | 24 | ozone |  32 |\n| 28 | 5 | 28 | ozone |  23 |\n| 29 | 5 | 29 | ozone |  45 |\n| 30 | 5 | 30 | ozone | 115 |\n| 31 | 5 | 31 | ozone |  37 |\n| 38 | 6 |  7 | ozone |  29 |\n| 40 | 6 |  9 | ozone |  71 |\n| 41 | 6 | 10 | ozone |  39 |\n| 44 | 6 | 13 | ozone |  23 |\n| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |\n| 583 | 9 |  1 | temp | 91 |\n| 584 | 9 |  2 | temp | 92 |\n| 585 | 9 |  3 | temp | 93 |\n| 586 | 9 |  4 | temp | 93 |\n| 587 | 9 |  5 | temp | 87 |\n| 588 | 9 |  6 | temp | 84 |\n| 589 | 9 |  7 | temp | 80 |\n| 590 | 9 |  8 | temp | 78 |\n| 591 | 9 |  9 | temp | 75 |\n| 592 | 9 | 10 | temp | 73 |\n| 593 | 9 | 11 | temp | 81 |\n| 594 | 9 | 12 | temp | 76 |\n| 595 | 9 | 13 | temp | 77 |\n| 596 | 9 | 14 | temp | 71 |\n| 597 | 9 | 15 | temp | 71 |\n| 598 | 9 | 16 | temp | 78 |\n| 599 | 9 | 17 | temp | 67 |\n| 600 | 9 | 18 | temp | 76 |\n| 601 | 9 | 19 | temp | 68 |\n| 602 | 9 | 20 | temp | 82 |\n| 603 | 9 | 21 | temp | 64 |\n| 604 | 9 | 22 | temp | 71 |\n| 605 | 9 | 23 | temp | 81 |\n| 606 | 9 | 24 | temp | 69 |\n| 607 | 9 | 25 | temp | 63 |\n| 608 | 9 | 26 | temp | 70 |\n| 609 | 9 | 27 | temp | 77 |\n| 610 | 9 | 28 | temp | 75 |\n| 611 | 9 | 29 | temp | 76 |\n| 612 | 9 | 30 | temp | 68 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 568 × 4</caption>\n",
              "<thead>\n",
              "\t<tr><th></th><th scope=col>month</th><th scope=col>day</th><th scope=col>variable</th><th scope=col>value</th></tr>\n",
              "\t<tr><th></th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;fct&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><th scope=row>1</th><td>5</td><td> 1</td><td>ozone</td><td> 41</td></tr>\n",
              "\t<tr><th scope=row>2</th><td>5</td><td> 2</td><td>ozone</td><td> 36</td></tr>\n",
              "\t<tr><th scope=row>3</th><td>5</td><td> 3</td><td>ozone</td><td> 12</td></tr>\n",
              "\t<tr><th scope=row>4</th><td>5</td><td> 4</td><td>ozone</td><td> 18</td></tr>\n",
              "\t<tr><th scope=row>6</th><td>5</td><td> 6</td><td>ozone</td><td> 28</td></tr>\n",
              "\t<tr><th scope=row>7</th><td>5</td><td> 7</td><td>ozone</td><td> 23</td></tr>\n",
              "\t<tr><th scope=row>8</th><td>5</td><td> 8</td><td>ozone</td><td> 19</td></tr>\n",
              "\t<tr><th scope=row>9</th><td>5</td><td> 9</td><td>ozone</td><td>  8</td></tr>\n",
              "\t<tr><th scope=row>11</th><td>5</td><td>11</td><td>ozone</td><td>  7</td></tr>\n",
              "\t<tr><th scope=row>12</th><td>5</td><td>12</td><td>ozone</td><td> 16</td></tr>\n",
              "\t<tr><th scope=row>13</th><td>5</td><td>13</td><td>ozone</td><td> 11</td></tr>\n",
              "\t<tr><th scope=row>14</th><td>5</td><td>14</td><td>ozone</td><td> 14</td></tr>\n",
              "\t<tr><th scope=row>15</th><td>5</td><td>15</td><td>ozone</td><td> 18</td></tr>\n",
              "\t<tr><th scope=row>16</th><td>5</td><td>16</td><td>ozone</td><td> 14</td></tr>\n",
              "\t<tr><th scope=row>17</th><td>5</td><td>17</td><td>ozone</td><td> 34</td></tr>\n",
              "\t<tr><th scope=row>18</th><td>5</td><td>18</td><td>ozone</td><td>  6</td></tr>\n",
              "\t<tr><th scope=row>19</th><td>5</td><td>19</td><td>ozone</td><td> 30</td></tr>\n",
              "\t<tr><th scope=row>20</th><td>5</td><td>20</td><td>ozone</td><td> 11</td></tr>\n",
              "\t<tr><th scope=row>21</th><td>5</td><td>21</td><td>ozone</td><td>  1</td></tr>\n",
              "\t<tr><th scope=row>22</th><td>5</td><td>22</td><td>ozone</td><td> 11</td></tr>\n",
              "\t<tr><th scope=row>23</th><td>5</td><td>23</td><td>ozone</td><td>  4</td></tr>\n",
              "\t<tr><th scope=row>24</th><td>5</td><td>24</td><td>ozone</td><td> 32</td></tr>\n",
              "\t<tr><th scope=row>28</th><td>5</td><td>28</td><td>ozone</td><td> 23</td></tr>\n",
              "\t<tr><th scope=row>29</th><td>5</td><td>29</td><td>ozone</td><td> 45</td></tr>\n",
              "\t<tr><th scope=row>30</th><td>5</td><td>30</td><td>ozone</td><td>115</td></tr>\n",
              "\t<tr><th scope=row>31</th><td>5</td><td>31</td><td>ozone</td><td> 37</td></tr>\n",
              "\t<tr><th scope=row>38</th><td>6</td><td> 7</td><td>ozone</td><td> 29</td></tr>\n",
              "\t<tr><th scope=row>40</th><td>6</td><td> 9</td><td>ozone</td><td> 71</td></tr>\n",
              "\t<tr><th scope=row>41</th><td>6</td><td>10</td><td>ozone</td><td> 39</td></tr>\n",
              "\t<tr><th scope=row>44</th><td>6</td><td>13</td><td>ozone</td><td> 23</td></tr>\n",
              "\t<tr><th scope=row>⋮</th><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr>\n",
              "\t<tr><th scope=row>583</th><td>9</td><td> 1</td><td>temp</td><td>91</td></tr>\n",
              "\t<tr><th scope=row>584</th><td>9</td><td> 2</td><td>temp</td><td>92</td></tr>\n",
              "\t<tr><th scope=row>585</th><td>9</td><td> 3</td><td>temp</td><td>93</td></tr>\n",
              "\t<tr><th scope=row>586</th><td>9</td><td> 4</td><td>temp</td><td>93</td></tr>\n",
              "\t<tr><th scope=row>587</th><td>9</td><td> 5</td><td>temp</td><td>87</td></tr>\n",
              "\t<tr><th scope=row>588</th><td>9</td><td> 6</td><td>temp</td><td>84</td></tr>\n",
              "\t<tr><th scope=row>589</th><td>9</td><td> 7</td><td>temp</td><td>80</td></tr>\n",
              "\t<tr><th scope=row>590</th><td>9</td><td> 8</td><td>temp</td><td>78</td></tr>\n",
              "\t<tr><th scope=row>591</th><td>9</td><td> 9</td><td>temp</td><td>75</td></tr>\n",
              "\t<tr><th scope=row>592</th><td>9</td><td>10</td><td>temp</td><td>73</td></tr>\n",
              "\t<tr><th scope=row>593</th><td>9</td><td>11</td><td>temp</td><td>81</td></tr>\n",
              "\t<tr><th scope=row>594</th><td>9</td><td>12</td><td>temp</td><td>76</td></tr>\n",
              "\t<tr><th scope=row>595</th><td>9</td><td>13</td><td>temp</td><td>77</td></tr>\n",
              "\t<tr><th scope=row>596</th><td>9</td><td>14</td><td>temp</td><td>71</td></tr>\n",
              "\t<tr><th scope=row>597</th><td>9</td><td>15</td><td>temp</td><td>71</td></tr>\n",
              "\t<tr><th scope=row>598</th><td>9</td><td>16</td><td>temp</td><td>78</td></tr>\n",
              "\t<tr><th scope=row>599</th><td>9</td><td>17</td><td>temp</td><td>67</td></tr>\n",
              "\t<tr><th scope=row>600</th><td>9</td><td>18</td><td>temp</td><td>76</td></tr>\n",
              "\t<tr><th scope=row>601</th><td>9</td><td>19</td><td>temp</td><td>68</td></tr>\n",
              "\t<tr><th scope=row>602</th><td>9</td><td>20</td><td>temp</td><td>82</td></tr>\n",
              "\t<tr><th scope=row>603</th><td>9</td><td>21</td><td>temp</td><td>64</td></tr>\n",
              "\t<tr><th scope=row>604</th><td>9</td><td>22</td><td>temp</td><td>71</td></tr>\n",
              "\t<tr><th scope=row>605</th><td>9</td><td>23</td><td>temp</td><td>81</td></tr>\n",
              "\t<tr><th scope=row>606</th><td>9</td><td>24</td><td>temp</td><td>69</td></tr>\n",
              "\t<tr><th scope=row>607</th><td>9</td><td>25</td><td>temp</td><td>63</td></tr>\n",
              "\t<tr><th scope=row>608</th><td>9</td><td>26</td><td>temp</td><td>70</td></tr>\n",
              "\t<tr><th scope=row>609</th><td>9</td><td>27</td><td>temp</td><td>77</td></tr>\n",
              "\t<tr><th scope=row>610</th><td>9</td><td>28</td><td>temp</td><td>75</td></tr>\n",
              "\t<tr><th scope=row>611</th><td>9</td><td>29</td><td>temp</td><td>76</td></tr>\n",
              "\t<tr><th scope=row>612</th><td>9</td><td>30</td><td>temp</td><td>68</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 173
        },
        "id": "D3XESbBcsL7z",
        "outputId": "445267cf-53c1-47df-b803-db89d86dbde6"
      },
      "source": [
        "cast(T, day~month~variable)       # 행을 day, 열을 month로 각 변수들을 새롭게 배열"
      ],
      "execution_count": 6,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              ", , variable = ozone\n",
              "\n",
              "    month\n",
              "day    5  6   7   8  9\n",
              "  1   41 NA 135  39 96\n",
              "  2   36 NA  49   9 78\n",
              "  3   12 NA  32  16 73\n",
              "  4   18 NA  NA  78 91\n",
              "  5   NA NA  64  35 47\n",
              "  6   28 NA  40  66 32\n",
              "  7   23 29  77 122 20\n",
              "  8   19 NA  97  89 23\n",
              "  9    8 71  97 110 21\n",
              "  10  NA 39  85  NA 24\n",
              "  11   7 NA  NA  NA 44\n",
              "  12  16 NA  10  44 21\n",
              "  13  11 23  27  28 28\n",
              "  14  14 NA  NA  65  9\n",
              "  15  18 NA   7  NA 13\n",
              "  16  14 21  48  22 46\n",
              "  17  34 37  35  59 18\n",
              "  18   6 20  61  23 13\n",
              "  19  30 12  79  31 24\n",
              "  20  11 13  63  44 16\n",
              "  21   1 NA  16  21 13\n",
              "  22  11 NA  NA   9 23\n",
              "  23   4 NA  NA  NA 36\n",
              "  24  32 NA  80  45  7\n",
              "  25  NA NA 108 168 14\n",
              "  26  NA NA  20  73 30\n",
              "  27  NA NA  52  NA NA\n",
              "  28  23 NA  82  76 14\n",
              "  29  45 NA  50 118 18\n",
              "  30 115 NA  64  84 20\n",
              "  31  37 NA  59  85 NA\n",
              "\n",
              ", , variable = solar.r\n",
              "\n",
              "    month\n",
              "day    5   6   7   8   9\n",
              "  1  190 286 269  83 167\n",
              "  2  118 287 248  24 197\n",
              "  3  149 242 236  77 183\n",
              "  4  313 186 101  NA 189\n",
              "  5   NA 220 175  NA  95\n",
              "  6   NA 264 314  NA  92\n",
              "  7  299 127 276 255 252\n",
              "  8   99 273 267 229 220\n",
              "  9   19 291 272 207 230\n",
              "  10 194 323 175 222 259\n",
              "  11  NA 259 139 137 236\n",
              "  12 256 250 264 192 259\n",
              "  13 290 148 175 273 238\n",
              "  14 274 332 291 157  24\n",
              "  15  65 322  48  64 112\n",
              "  16 334 191 260  71 237\n",
              "  17 307 284 274  51 224\n",
              "  18  78  37 285 115  27\n",
              "  19 322 120 187 244 238\n",
              "  20  44 137 220 190 201\n",
              "  21   8 150   7 259 238\n",
              "  22 320  59 258  36  14\n",
              "  23  25  91 295 255 139\n",
              "  24  92 250 294 212  49\n",
              "  25  66 135 223 238  20\n",
              "  26 266 127  81 215 193\n",
              "  27  NA  47  82 153 145\n",
              "  28  13  98 213 203 191\n",
              "  29 252  31 275 225 131\n",
              "  30 223 138 253 237 223\n",
              "  31 279  NA 254 188  NA\n",
              "\n",
              ", , variable = wind\n",
              "\n",
              "    month\n",
              "day     5    6    7    8    9\n",
              "  1   7.4  8.6  4.1  6.9  6.9\n",
              "  2   8.0  9.7  9.2 13.8  5.1\n",
              "  3  12.6 16.1  9.2  7.4  2.8\n",
              "  4  11.5  9.2 10.9  6.9  4.6\n",
              "  5  14.3  8.6  4.6  7.4  7.4\n",
              "  6  14.9 14.3 10.9  4.6 15.5\n",
              "  7   8.6  9.7  5.1  4.0 10.9\n",
              "  8  13.8  6.9  6.3 10.3 10.3\n",
              "  9  20.1 13.8  5.7  8.0 10.9\n",
              "  10  8.6 11.5  7.4  8.6  9.7\n",
              "  11  6.9 10.9  8.6 11.5 14.9\n",
              "  12  9.7  9.2 14.3 11.5 15.5\n",
              "  13  9.2  8.0 14.9 11.5  6.3\n",
              "  14 10.9 13.8 14.9  9.7 10.9\n",
              "  15 13.2 11.5 14.3 11.5 11.5\n",
              "  16 11.5 14.9  6.9 10.3  6.9\n",
              "  17 12.0 20.7 10.3  6.3 13.8\n",
              "  18 18.4  9.2  6.3  7.4 10.3\n",
              "  19 11.5 11.5  5.1 10.9 10.3\n",
              "  20  9.7 10.3 11.5 10.3  8.0\n",
              "  21  9.7  6.3  6.9 15.5 12.6\n",
              "  22 16.6  1.7  9.7 14.3  9.2\n",
              "  23  9.7  4.6 11.5 12.6 10.3\n",
              "  24 12.0  6.3  8.6  9.7 10.3\n",
              "  25 16.6  8.0  8.0  3.4 16.6\n",
              "  26 14.9  8.0  8.6  8.0  6.9\n",
              "  27  8.0 10.3 12.0  5.7 13.2\n",
              "  28 12.0 11.5  7.4  9.7 14.3\n",
              "  29 14.9 14.9  7.4  2.3  8.0\n",
              "  30  5.7  8.0  7.4  6.3 11.5\n",
              "  31  7.4   NA  9.2  6.3   NA\n",
              "\n",
              ", , variable = temp\n",
              "\n",
              "    month\n",
              "day   5  6  7  8  9\n",
              "  1  67 78 84 81 91\n",
              "  2  72 74 85 81 92\n",
              "  3  74 67 81 82 93\n",
              "  4  62 84 84 86 93\n",
              "  5  56 85 83 85 87\n",
              "  6  66 79 83 87 84\n",
              "  7  65 82 88 89 80\n",
              "  8  59 87 92 90 78\n",
              "  9  61 90 92 90 75\n",
              "  10 69 87 89 92 73\n",
              "  11 74 93 82 86 81\n",
              "  12 69 92 73 86 76\n",
              "  13 66 82 81 82 77\n",
              "  14 68 80 91 80 71\n",
              "  15 58 79 80 79 71\n",
              "  16 64 77 81 77 78\n",
              "  17 66 72 82 79 67\n",
              "  18 57 65 84 76 76\n",
              "  19 68 73 87 78 68\n",
              "  20 62 76 85 78 82\n",
              "  21 59 77 74 77 64\n",
              "  22 73 76 81 72 71\n",
              "  23 61 76 82 75 81\n",
              "  24 61 76 86 79 69\n",
              "  25 57 75 85 81 63\n",
              "  26 58 78 82 86 70\n",
              "  27 57 73 86 88 77\n",
              "  28 67 80 88 97 75\n",
              "  29 81 77 86 94 76\n",
              "  30 79 83 83 96 68\n",
              "  31 76 NA 81 94 NA\n"
            ],
            "text/latex": "\\begin{enumerate*}\n\\item 41\n\\item 36\n\\item 12\n\\item 18\n\\item <NA>\n\\item 28\n\\item 23\n\\item 19\n\\item 8\n\\item <NA>\n\\item 7\n\\item 16\n\\item 11\n\\item 14\n\\item 18\n\\item 14\n\\item 34\n\\item 6\n\\item 30\n\\item 11\n\\item 1\n\\item 11\n\\item 4\n\\item 32\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item 23\n\\item 45\n\\item 115\n\\item 37\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item 29\n\\item <NA>\n\\item 71\n\\item 39\n\\item <NA>\n\\item <NA>\n\\item 23\n\\item <NA>\n\\item <NA>\n\\item 21\n\\item 37\n\\item 20\n\\item 12\n\\item 13\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item <NA>\n\\item 135\n\\item 49\n\\item 32\n\\item <NA>\n\\item 64\n\\item 40\n\\item 77\n\\item 97\n\\item 97\n\\item 85\n\\item <NA>\n\\item 10\n\\item 27\n\\item <NA>\n\\item 7\n\\item 48\n\\item 35\n\\item 61\n\\item 79\n\\item 63\n\\item 16\n\\item <NA>\n\\item <NA>\n\\item 80\n\\item 108\n\\item 20\n\\item 52\n\\item 82\n\\item 50\n\\item 64\n\\item 59\n\\item 39\n\\item 9\n\\item 16\n\\item 78\n\\item 35\n\\item 66\n\\item 122\n\\item 89\n\\item 110\n\\item <NA>\n\\item <NA>\n\\item 44\n\\item 28\n\\item 65\n\\item <NA>\n\\item 22\n\\item 59\n\\item 23\n\\item 31\n\\item 44\n\\item 21\n\\item 9\n\\item <NA>\n\\item 45\n\\item 168\n\\item 73\n\\item <NA>\n\\item 76\n\\item 118\n\\item 84\n\\item 85\n\\item 96\n\\item 78\n\\item 73\n\\item 91\n\\item 47\n\\item 32\n\\item 20\n\\item 23\n\\item 21\n\\item 24\n\\item 44\n\\item 21\n\\item 28\n\\item 9\n\\item 13\n\\item 46\n\\item 18\n\\item 13\n\\item 24\n\\item 16\n\\item 13\n\\item 23\n\\item 36\n\\item 7\n\\item 14\n\\item 30\n\\item <NA>\n\\item 14\n\\item 18\n\\item 20\n\\item <NA>\n\\item 190\n\\item 118\n\\item 149\n\\item 313\n\\item <NA>\n\\item <NA>\n\\item 299\n\\item 99\n\\item 19\n\\item 194\n\\item <NA>\n\\item 256\n\\item 290\n\\item 274\n\\item 65\n\\item 334\n\\item 307\n\\item 78\n\\item 322\n\\item 44\n\\item 8\n\\item 320\n\\item 25\n\\item 92\n\\item 66\n\\item 266\n\\item <NA>\n\\item 13\n\\item 252\n\\item 223\n\\item 279\n\\item 286\n\\item 287\n\\item 242\n\\item 186\n\\item 220\n\\item 264\n\\item 127\n\\item 273\n\\item 291\n\\item 323\n\\item 259\n\\item 250\n\\item 148\n\\item 332\n\\item ⋯\n\\item 7.4\n\\item 10.9\n\\item 10.3\n\\item 15.5\n\\item 14.3\n\\item 12.6\n\\item 9.7\n\\item 3.4\n\\item 8\n\\item 5.7\n\\item 9.7\n\\item 2.3\n\\item 6.3\n\\item 6.3\n\\item 6.9\n\\item 5.1\n\\item 2.8\n\\item 4.6\n\\item 7.4\n\\item 15.5\n\\item 10.9\n\\item 10.3\n\\item 10.9\n\\item 9.7\n\\item 14.9\n\\item 15.5\n\\item 6.3\n\\item 10.9\n\\item 11.5\n\\item 6.9\n\\item 13.8\n\\item 10.3\n\\item 10.3\n\\item 8\n\\item 12.6\n\\item 9.2\n\\item 10.3\n\\item 10.3\n\\item 16.6\n\\item 6.9\n\\item 13.2\n\\item 14.3\n\\item 8\n\\item 11.5\n\\item <NA>\n\\item 67\n\\item 72\n\\item 74\n\\item 62\n\\item 56\n\\item 66\n\\item 65\n\\item 59\n\\item 61\n\\item 69\n\\item 74\n\\item 69\n\\item 66\n\\item 68\n\\item 58\n\\item 64\n\\item 66\n\\item 57\n\\item 68\n\\item 62\n\\item 59\n\\item 73\n\\item 61\n\\item 61\n\\item 57\n\\item 58\n\\item 57\n\\item 67\n\\item 81\n\\item 79\n\\item 76\n\\item 78\n\\item 74\n\\item 67\n\\item 84\n\\item 85\n\\item 79\n\\item 82\n\\item 87\n\\item 90\n\\item 87\n\\item 93\n\\item 92\n\\item 82\n\\item 80\n\\item 79\n\\item 77\n\\item 72\n\\item 65\n\\item 73\n\\item 76\n\\item 77\n\\item 76\n\\item 76\n\\item 76\n\\item 75\n\\item 78\n\\item 73\n\\item 80\n\\item 77\n\\item 83\n\\item <NA>\n\\item 84\n\\item 85\n\\item 81\n\\item 84\n\\item 83\n\\item 83\n\\item 88\n\\item 92\n\\item 92\n\\item 89\n\\item 82\n\\item 73\n\\item 81\n\\item 91\n\\item 80\n\\item 81\n\\item 82\n\\item 84\n\\item 87\n\\item 85\n\\item 74\n\\item 81\n\\item 82\n\\item 86\n\\item 85\n\\item 82\n\\item 86\n\\item 88\n\\item 86\n\\item 83\n\\item 81\n\\item 81\n\\item 81\n\\item 82\n\\item 86\n\\item 85\n\\item 87\n\\item 89\n\\item 90\n\\item 90\n\\item 92\n\\item 86\n\\item 86\n\\item 82\n\\item 80\n\\item 79\n\\item 77\n\\item 79\n\\item 76\n\\item 78\n\\item 78\n\\item 77\n\\item 72\n\\item 75\n\\item 79\n\\item 81\n\\item 86\n\\item 88\n\\item 97\n\\item 94\n\\item 96\n\\item 94\n\\item 91\n\\item 92\n\\item 93\n\\item 93\n\\item 87\n\\item 84\n\\item 80\n\\item 78\n\\item 75\n\\item 73\n\\item 81\n\\item 76\n\\item 77\n\\item 71\n\\item 71\n\\item 78\n\\item 67\n\\item 76\n\\item 68\n\\item 82\n\\item 64\n\\item 71\n\\item 81\n\\item 69\n\\item 63\n\\item 70\n\\item 77\n\\item 75\n\\item 76\n\\item 68\n\\item <NA>\n\\end{enumerate*}\n",
            "text/markdown": "1. 41\n2. 36\n3. 12\n4. 18\n5. &lt;NA&gt;\n6. 28\n7. 23\n8. 19\n9. 8\n10. &lt;NA&gt;\n11. 7\n12. 16\n13. 11\n14. 14\n15. 18\n16. 14\n17. 34\n18. 6\n19. 30\n20. 11\n21. 1\n22. 11\n23. 4\n24. 32\n25. &lt;NA&gt;\n26. &lt;NA&gt;\n27. &lt;NA&gt;\n28. 23\n29. 45\n30. 115\n31. 37\n32. &lt;NA&gt;\n33. &lt;NA&gt;\n34. &lt;NA&gt;\n35. &lt;NA&gt;\n36. &lt;NA&gt;\n37. &lt;NA&gt;\n38. 29\n39. &lt;NA&gt;\n40. 71\n41. 39\n42. &lt;NA&gt;\n43. &lt;NA&gt;\n44. 23\n45. &lt;NA&gt;\n46. &lt;NA&gt;\n47. 21\n48. 37\n49. 20\n50. 12\n51. 13\n52. &lt;NA&gt;\n53. &lt;NA&gt;\n54. &lt;NA&gt;\n55. &lt;NA&gt;\n56. &lt;NA&gt;\n57. &lt;NA&gt;\n58. &lt;NA&gt;\n59. &lt;NA&gt;\n60. &lt;NA&gt;\n61. &lt;NA&gt;\n62. &lt;NA&gt;\n63. 135\n64. 49\n65. 32\n66. &lt;NA&gt;\n67. 64\n68. 40\n69. 77\n70. 97\n71. 97\n72. 85\n73. &lt;NA&gt;\n74. 10\n75. 27\n76. &lt;NA&gt;\n77. 7\n78. 48\n79. 35\n80. 61\n81. 79\n82. 63\n83. 16\n84. &lt;NA&gt;\n85. &lt;NA&gt;\n86. 80\n87. 108\n88. 20\n89. 52\n90. 82\n91. 50\n92. 64\n93. 59\n94. 39\n95. 9\n96. 16\n97. 78\n98. 35\n99. 66\n100. 122\n101. 89\n102. 110\n103. &lt;NA&gt;\n104. &lt;NA&gt;\n105. 44\n106. 28\n107. 65\n108. &lt;NA&gt;\n109. 22\n110. 59\n111. 23\n112. 31\n113. 44\n114. 21\n115. 9\n116. &lt;NA&gt;\n117. 45\n118. 168\n119. 73\n120. &lt;NA&gt;\n121. 76\n122. 118\n123. 84\n124. 85\n125. 96\n126. 78\n127. 73\n128. 91\n129. 47\n130. 32\n131. 20\n132. 23\n133. 21\n134. 24\n135. 44\n136. 21\n137. 28\n138. 9\n139. 13\n140. 46\n141. 18\n142. 13\n143. 24\n144. 16\n145. 13\n146. 23\n147. 36\n148. 7\n149. 14\n150. 30\n151. &lt;NA&gt;\n152. 14\n153. 18\n154. 20\n155. &lt;NA&gt;\n156. 190\n157. 118\n158. 149\n159. 313\n160. &lt;NA&gt;\n161. &lt;NA&gt;\n162. 299\n163. 99\n164. 19\n165. 194\n166. &lt;NA&gt;\n167. 256\n168. 290\n169. 274\n170. 65\n171. 334\n172. 307\n173. 78\n174. 322\n175. 44\n176. 8\n177. 320\n178. 25\n179. 92\n180. 66\n181. 266\n182. &lt;NA&gt;\n183. 13\n184. 252\n185. 223\n186. 279\n187. 286\n188. 287\n189. 242\n190. 186\n191. 220\n192. 264\n193. 127\n194. 273\n195. 291\n196. 323\n197. 259\n198. 250\n199. 148\n200. 332\n201. ⋯\n202. 7.4\n203. 10.9\n204. 10.3\n205. 15.5\n206. 14.3\n207. 12.6\n208. 9.7\n209. 3.4\n210. 8\n211. 5.7\n212. 9.7\n213. 2.3\n214. 6.3\n215. 6.3\n216. 6.9\n217. 5.1\n218. 2.8\n219. 4.6\n220. 7.4\n221. 15.5\n222. 10.9\n223. 10.3\n224. 10.9\n225. 9.7\n226. 14.9\n227. 15.5\n228. 6.3\n229. 10.9\n230. 11.5\n231. 6.9\n232. 13.8\n233. 10.3\n234. 10.3\n235. 8\n236. 12.6\n237. 9.2\n238. 10.3\n239. 10.3\n240. 16.6\n241. 6.9\n242. 13.2\n243. 14.3\n244. 8\n245. 11.5\n246. &lt;NA&gt;\n247. 67\n248. 72\n249. 74\n250. 62\n251. 56\n252. 66\n253. 65\n254. 59\n255. 61\n256. 69\n257. 74\n258. 69\n259. 66\n260. 68\n261. 58\n262. 64\n263. 66\n264. 57\n265. 68\n266. 62\n267. 59\n268. 73\n269. 61\n270. 61\n271. 57\n272. 58\n273. 57\n274. 67\n275. 81\n276. 79\n277. 76\n278. 78\n279. 74\n280. 67\n281. 84\n282. 85\n283. 79\n284. 82\n285. 87\n286. 90\n287. 87\n288. 93\n289. 92\n290. 82\n291. 80\n292. 79\n293. 77\n294. 72\n295. 65\n296. 73\n297. 76\n298. 77\n299. 76\n300. 76\n301. 76\n302. 75\n303. 78\n304. 73\n305. 80\n306. 77\n307. 83\n308. &lt;NA&gt;\n309. 84\n310. 85\n311. 81\n312. 84\n313. 83\n314. 83\n315. 88\n316. 92\n317. 92\n318. 89\n319. 82\n320. 73\n321. 81\n322. 91\n323. 80\n324. 81\n325. 82\n326. 84\n327. 87\n328. 85\n329. 74\n330. 81\n331. 82\n332. 86\n333. 85\n334. 82\n335. 86\n336. 88\n337. 86\n338. 83\n339. 81\n340. 81\n341. 81\n342. 82\n343. 86\n344. 85\n345. 87\n346. 89\n347. 90\n348. 90\n349. 92\n350. 86\n351. 86\n352. 82\n353. 80\n354. 79\n355. 77\n356. 79\n357. 76\n358. 78\n359. 78\n360. 77\n361. 72\n362. 75\n363. 79\n364. 81\n365. 86\n366. 88\n367. 97\n368. 94\n369. 96\n370. 94\n371. 91\n372. 92\n373. 93\n374. 93\n375. 87\n376. 84\n377. 80\n378. 78\n379. 75\n380. 73\n381. 81\n382. 76\n383. 77\n384. 71\n385. 71\n386. 78\n387. 67\n388. 76\n389. 68\n390. 82\n391. 64\n392. 71\n393. 81\n394. 69\n395. 63\n396. 70\n397. 77\n398. 75\n399. 76\n400. 68\n401. &lt;NA&gt;\n\n\n",
            "text/html": [
              "<style>\n",
              ".list-inline {list-style: none; margin:0; padding: 0}\n",
              ".list-inline>li {display: inline-block}\n",
              ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
              "</style>\n",
              "<ol class=list-inline><li>41</li><li>36</li><li>12</li><li>18</li><li>&lt;NA&gt;</li><li>28</li><li>23</li><li>19</li><li>8</li><li>&lt;NA&gt;</li><li>7</li><li>16</li><li>11</li><li>14</li><li>18</li><li>14</li><li>34</li><li>6</li><li>30</li><li>11</li><li>1</li><li>11</li><li>4</li><li>32</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>23</li><li>45</li><li>115</li><li>37</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>29</li><li>&lt;NA&gt;</li><li>71</li><li>39</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>23</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>21</li><li>37</li><li>20</li><li>12</li><li>13</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>135</li><li>49</li><li>32</li><li>&lt;NA&gt;</li><li>64</li><li>40</li><li>77</li><li>97</li><li>97</li><li>85</li><li>&lt;NA&gt;</li><li>10</li><li>27</li><li>&lt;NA&gt;</li><li>7</li><li>48</li><li>35</li><li>61</li><li>79</li><li>63</li><li>16</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>80</li><li>108</li><li>20</li><li>52</li><li>82</li><li>50</li><li>64</li><li>59</li><li>39</li><li>9</li><li>16</li><li>78</li><li>35</li><li>66</li><li>122</li><li>89</li><li>110</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>44</li><li>28</li><li>65</li><li>&lt;NA&gt;</li><li>22</li><li>59</li><li>23</li><li>31</li><li>44</li><li>21</li><li>9</li><li>&lt;NA&gt;</li><li>45</li><li>168</li><li>73</li><li>&lt;NA&gt;</li><li>76</li><li>118</li><li>84</li><li>85</li><li>96</li><li>78</li><li>73</li><li>91</li><li>47</li><li>32</li><li>20</li><li>23</li><li>21</li><li>24</li><li>44</li><li>21</li><li>28</li><li>9</li><li>13</li><li>46</li><li>18</li><li>13</li><li>24</li><li>16</li><li>13</li><li>23</li><li>36</li><li>7</li><li>14</li><li>30</li><li>&lt;NA&gt;</li><li>14</li><li>18</li><li>20</li><li>&lt;NA&gt;</li><li>190</li><li>118</li><li>149</li><li>313</li><li>&lt;NA&gt;</li><li>&lt;NA&gt;</li><li>299</li><li>99</li><li>19</li><li>194</li><li>&lt;NA&gt;</li><li>256</li><li>290</li><li>274</li><li>65</li><li>334</li><li>307</li><li>78</li><li>322</li><li>44</li><li>8</li><li>320</li><li>25</li><li>92</li><li>66</li><li>266</li><li>&lt;NA&gt;</li><li>13</li><li>252</li><li>223</li><li>279</li><li>286</li><li>287</li><li>242</li><li>186</li><li>220</li><li>264</li><li>127</li><li>273</li><li>291</li><li>323</li><li>259</li><li>250</li><li>148</li><li>332</li><li>⋯</li><li>7.4</li><li>10.9</li><li>10.3</li><li>15.5</li><li>14.3</li><li>12.6</li><li>9.7</li><li>3.4</li><li>8</li><li>5.7</li><li>9.7</li><li>2.3</li><li>6.3</li><li>6.3</li><li>6.9</li><li>5.1</li><li>2.8</li><li>4.6</li><li>7.4</li><li>15.5</li><li>10.9</li><li>10.3</li><li>10.9</li><li>9.7</li><li>14.9</li><li>15.5</li><li>6.3</li><li>10.9</li><li>11.5</li><li>6.9</li><li>13.8</li><li>10.3</li><li>10.3</li><li>8</li><li>12.6</li><li>9.2</li><li>10.3</li><li>10.3</li><li>16.6</li><li>6.9</li><li>13.2</li><li>14.3</li><li>8</li><li>11.5</li><li>&lt;NA&gt;</li><li>67</li><li>72</li><li>74</li><li>62</li><li>56</li><li>66</li><li>65</li><li>59</li><li>61</li><li>69</li><li>74</li><li>69</li><li>66</li><li>68</li><li>58</li><li>64</li><li>66</li><li>57</li><li>68</li><li>62</li><li>59</li><li>73</li><li>61</li><li>61</li><li>57</li><li>58</li><li>57</li><li>67</li><li>81</li><li>79</li><li>76</li><li>78</li><li>74</li><li>67</li><li>84</li><li>85</li><li>79</li><li>82</li><li>87</li><li>90</li><li>87</li><li>93</li><li>92</li><li>82</li><li>80</li><li>79</li><li>77</li><li>72</li><li>65</li><li>73</li><li>76</li><li>77</li><li>76</li><li>76</li><li>76</li><li>75</li><li>78</li><li>73</li><li>80</li><li>77</li><li>83</li><li>&lt;NA&gt;</li><li>84</li><li>85</li><li>81</li><li>84</li><li>83</li><li>83</li><li>88</li><li>92</li><li>92</li><li>89</li><li>82</li><li>73</li><li>81</li><li>91</li><li>80</li><li>81</li><li>82</li><li>84</li><li>87</li><li>85</li><li>74</li><li>81</li><li>82</li><li>86</li><li>85</li><li>82</li><li>86</li><li>88</li><li>86</li><li>83</li><li>81</li><li>81</li><li>81</li><li>82</li><li>86</li><li>85</li><li>87</li><li>89</li><li>90</li><li>90</li><li>92</li><li>86</li><li>86</li><li>82</li><li>80</li><li>79</li><li>77</li><li>79</li><li>76</li><li>78</li><li>78</li><li>77</li><li>72</li><li>75</li><li>79</li><li>81</li><li>86</li><li>88</li><li>97</li><li>94</li><li>96</li><li>94</li><li>91</li><li>92</li><li>93</li><li>93</li><li>87</li><li>84</li><li>80</li><li>78</li><li>75</li><li>73</li><li>81</li><li>76</li><li>77</li><li>71</li><li>71</li><li>78</li><li>67</li><li>76</li><li>68</li><li>82</li><li>64</li><li>71</li><li>81</li><li>69</li><li>63</li><li>70</li><li>77</li><li>75</li><li>76</li><li>68</li><li>&lt;NA&gt;</li></ol>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 224
        },
        "id": "1y_1PZ1csn7J",
        "outputId": "fbb881a6-3114-4aa3-854c-75b9821b5cbc"
      },
      "source": [
        "b <- acast(T, month~variable, mean)      # 각 변수들의 month 평균\n",
        "b"
      ],
      "execution_count": 7,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  ozone    solar.r  wind      temp    \n",
              "5 23.61538 181.2963 11.622581 65.54839\n",
              "6 29.44444 190.1667 10.266667 79.10000\n",
              "7 59.11538 216.4839  8.941935 83.90323\n",
              "8 59.96154 171.8571  8.793548 83.96774\n",
              "9 31.44828 167.4333 10.180000 76.90000"
            ],
            "text/latex": "A matrix: 5 × 4 of type dbl\n\\begin{tabular}{r|llll}\n  & ozone & solar.r & wind & temp\\\\\n\\hline\n\t5 & 23.61538 & 181.2963 & 11.622581 & 65.54839\\\\\n\t6 & 29.44444 & 190.1667 & 10.266667 & 79.10000\\\\\n\t7 & 59.11538 & 216.4839 &  8.941935 & 83.90323\\\\\n\t8 & 59.96154 & 171.8571 &  8.793548 & 83.96774\\\\\n\t9 & 31.44828 & 167.4333 & 10.180000 & 76.90000\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA matrix: 5 × 4 of type dbl\n\n| <!--/--> | ozone | solar.r | wind | temp |\n|---|---|---|---|---|\n| 5 | 23.61538 | 181.2963 | 11.622581 | 65.54839 |\n| 6 | 29.44444 | 190.1667 | 10.266667 | 79.10000 |\n| 7 | 59.11538 | 216.4839 |  8.941935 | 83.90323 |\n| 8 | 59.96154 | 171.8571 |  8.793548 | 83.96774 |\n| 9 | 31.44828 | 167.4333 | 10.180000 | 76.90000 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A matrix: 5 × 4 of type dbl</caption>\n",
              "<thead>\n",
              "\t<tr><th></th><th scope=col>ozone</th><th scope=col>solar.r</th><th scope=col>wind</th><th scope=col>temp</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><th scope=row>5</th><td>23.61538</td><td>181.2963</td><td>11.622581</td><td>65.54839</td></tr>\n",
              "\t<tr><th scope=row>6</th><td>29.44444</td><td>190.1667</td><td>10.266667</td><td>79.10000</td></tr>\n",
              "\t<tr><th scope=row>7</th><td>59.11538</td><td>216.4839</td><td> 8.941935</td><td>83.90323</td></tr>\n",
              "\t<tr><th scope=row>8</th><td>59.96154</td><td>171.8571</td><td> 8.793548</td><td>83.96774</td></tr>\n",
              "\t<tr><th scope=row>9</th><td>31.44828</td><td>167.4333</td><td>10.180000</td><td>76.90000</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 286
        },
        "id": "EuxboUFAs69W",
        "outputId": "b4781659-eef2-4bfc-cc72-0a3a333fac0e"
      },
      "source": [
        "d <- cast(T, month~variable, mean, margins = c (\"grand_row\", \"grand_col\"))       # margins 관련 옵션으로 행과 열에 대한 소계를 산출\n",
        "d"
      ],
      "execution_count": 8,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  month ozone    solar.r  wind      temp     (all)   \n",
              "1 5     23.61538 181.2963 11.622581 65.54839 68.70696\n",
              "2 6     29.44444 190.1667 10.266667 79.10000 87.38384\n",
              "3 7     59.11538 216.4839  8.941935 83.90323 93.49748\n",
              "4 8     59.96154 171.8571  8.793548 83.96774 79.71207\n",
              "5 9     31.44828 167.4333 10.180000 76.90000 71.82689\n",
              "6 (all) 42.12931 185.9315  9.957516 77.88235 80.05722"
            ],
            "text/latex": "A cast\\_df: 6 × 6\n\\begin{tabular}{r|llllll}\n  & month & ozone & solar.r & wind & temp & (all)\\\\\n  & <fct> & <dbl> & <dbl> & <dbl> & <dbl> & <dbl>\\\\\n\\hline\n\t1 & 5     & 23.61538 & 181.2963 & 11.622581 & 65.54839 & 68.70696\\\\\n\t2 & 6     & 29.44444 & 190.1667 & 10.266667 & 79.10000 & 87.38384\\\\\n\t3 & 7     & 59.11538 & 216.4839 &  8.941935 & 83.90323 & 93.49748\\\\\n\t4 & 8     & 59.96154 & 171.8571 &  8.793548 & 83.96774 & 79.71207\\\\\n\t5 & 9     & 31.44828 & 167.4333 & 10.180000 & 76.90000 & 71.82689\\\\\n\t6 & (all) & 42.12931 & 185.9315 &  9.957516 & 77.88235 & 80.05722\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA cast_df: 6 × 6\n\n| <!--/--> | month &lt;fct&gt; | ozone &lt;dbl&gt; | solar.r &lt;dbl&gt; | wind &lt;dbl&gt; | temp &lt;dbl&gt; | (all) &lt;dbl&gt; |\n|---|---|---|---|---|---|---|\n| 1 | 5     | 23.61538 | 181.2963 | 11.622581 | 65.54839 | 68.70696 |\n| 2 | 6     | 29.44444 | 190.1667 | 10.266667 | 79.10000 | 87.38384 |\n| 3 | 7     | 59.11538 | 216.4839 |  8.941935 | 83.90323 | 93.49748 |\n| 4 | 8     | 59.96154 | 171.8571 |  8.793548 | 83.96774 | 79.71207 |\n| 5 | 9     | 31.44828 | 167.4333 | 10.180000 | 76.90000 | 71.82689 |\n| 6 | (all) | 42.12931 | 185.9315 |  9.957516 | 77.88235 | 80.05722 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A cast_df: 6 × 6</caption>\n",
              "<thead>\n",
              "\t<tr><th></th><th scope=col>month</th><th scope=col>ozone</th><th scope=col>solar.r</th><th scope=col>wind</th><th scope=col>temp</th><th scope=col>(all)</th></tr>\n",
              "\t<tr><th></th><th scope=col>&lt;fct&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><th scope=row>1</th><td>5    </td><td>23.61538</td><td>181.2963</td><td>11.622581</td><td>65.54839</td><td>68.70696</td></tr>\n",
              "\t<tr><th scope=row>2</th><td>6    </td><td>29.44444</td><td>190.1667</td><td>10.266667</td><td>79.10000</td><td>87.38384</td></tr>\n",
              "\t<tr><th scope=row>3</th><td>7    </td><td>59.11538</td><td>216.4839</td><td> 8.941935</td><td>83.90323</td><td>93.49748</td></tr>\n",
              "\t<tr><th scope=row>4</th><td>8    </td><td>59.96154</td><td>171.8571</td><td> 8.793548</td><td>83.96774</td><td>79.71207</td></tr>\n",
              "\t<tr><th scope=row>5</th><td>9    </td><td>31.44828</td><td>167.4333</td><td>10.180000</td><td>76.90000</td><td>71.82689</td></tr>\n",
              "\t<tr><th scope=row>6</th><td>(all)</td><td>42.12931</td><td>185.9315</td><td> 9.957516</td><td>77.88235</td><td>80.05722</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "8P0wgKedtIzr",
        "outputId": "cb2139b2-761b-4e93-c8cb-4a6b7fc79278"
      },
      "source": [
        "e <- cast(T, day~month, mean, subset = variable == \"ozone\")       # subset 기능으로 특정 변수(ozone)만을 처리\n",
        "e"
      ],
      "execution_count": 9,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "   day 5   6   7   8   9  \n",
              "1   1   41 NaN 135  39  96\n",
              "2   2   36 NaN  49   9  78\n",
              "3   3   12 NaN  32  16  73\n",
              "4   4   18 NaN NaN  78  91\n",
              "5   5  NaN NaN  64  35  47\n",
              "6   6   28 NaN  40  66  32\n",
              "7   7   23  29  77 122  20\n",
              "8   8   19 NaN  97  89  23\n",
              "9   9    8  71  97 110  21\n",
              "10 10  NaN  39  85 NaN  24\n",
              "11 11    7 NaN NaN NaN  44\n",
              "12 12   16 NaN  10  44  21\n",
              "13 13   11  23  27  28  28\n",
              "14 14   14 NaN NaN  65   9\n",
              "15 15   18 NaN   7 NaN  13\n",
              "16 16   14  21  48  22  46\n",
              "17 17   34  37  35  59  18\n",
              "18 18    6  20  61  23  13\n",
              "19 19   30  12  79  31  24\n",
              "20 20   11  13  63  44  16\n",
              "21 21    1 NaN  16  21  13\n",
              "22 22   11 NaN NaN   9  23\n",
              "23 23    4 NaN NaN NaN  36\n",
              "24 24   32 NaN  80  45   7\n",
              "25 25  NaN NaN 108 168  14\n",
              "26 26  NaN NaN  20  73  30\n",
              "27 27  NaN NaN  52 NaN NaN\n",
              "28 28   23 NaN  82  76  14\n",
              "29 29   45 NaN  50 118  18\n",
              "30 30  115 NaN  64  84  20\n",
              "31 31   37 NaN  59  85 NaN"
            ],
            "text/latex": "A cast\\_df: 31 × 6\n\\begin{tabular}{r|llllll}\n  & day & 5 & 6 & 7 & 8 & 9\\\\\n  & <int> & <dbl> & <dbl> & <dbl> & <dbl> & <dbl>\\\\\n\\hline\n\t1 &  1 &  41 & NaN & 135 &  39 &  96\\\\\n\t2 &  2 &  36 & NaN &  49 &   9 &  78\\\\\n\t3 &  3 &  12 & NaN &  32 &  16 &  73\\\\\n\t4 &  4 &  18 & NaN & NaN &  78 &  91\\\\\n\t5 &  5 & NaN & NaN &  64 &  35 &  47\\\\\n\t6 &  6 &  28 & NaN &  40 &  66 &  32\\\\\n\t7 &  7 &  23 &  29 &  77 & 122 &  20\\\\\n\t8 &  8 &  19 & NaN &  97 &  89 &  23\\\\\n\t9 &  9 &   8 &  71 &  97 & 110 &  21\\\\\n\t10 & 10 & NaN &  39 &  85 & NaN &  24\\\\\n\t11 & 11 &   7 & NaN & NaN & NaN &  44\\\\\n\t12 & 12 &  16 & NaN &  10 &  44 &  21\\\\\n\t13 & 13 &  11 &  23 &  27 &  28 &  28\\\\\n\t14 & 14 &  14 & NaN & NaN &  65 &   9\\\\\n\t15 & 15 &  18 & NaN &   7 & NaN &  13\\\\\n\t16 & 16 &  14 &  21 &  48 &  22 &  46\\\\\n\t17 & 17 &  34 &  37 &  35 &  59 &  18\\\\\n\t18 & 18 &   6 &  20 &  61 &  23 &  13\\\\\n\t19 & 19 &  30 &  12 &  79 &  31 &  24\\\\\n\t20 & 20 &  11 &  13 &  63 &  44 &  16\\\\\n\t21 & 21 &   1 & NaN &  16 &  21 &  13\\\\\n\t22 & 22 &  11 & NaN & NaN &   9 &  23\\\\\n\t23 & 23 &   4 & NaN & NaN & NaN &  36\\\\\n\t24 & 24 &  32 & NaN &  80 &  45 &   7\\\\\n\t25 & 25 & NaN & NaN & 108 & 168 &  14\\\\\n\t26 & 26 & NaN & NaN &  20 &  73 &  30\\\\\n\t27 & 27 & NaN & NaN &  52 & NaN & NaN\\\\\n\t28 & 28 &  23 & NaN &  82 &  76 &  14\\\\\n\t29 & 29 &  45 & NaN &  50 & 118 &  18\\\\\n\t30 & 30 & 115 & NaN &  64 &  84 &  20\\\\\n\t31 & 31 &  37 & NaN &  59 &  85 & NaN\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA cast_df: 31 × 6\n\n| <!--/--> | day &lt;int&gt; | 5 &lt;dbl&gt; | 6 &lt;dbl&gt; | 7 &lt;dbl&gt; | 8 &lt;dbl&gt; | 9 &lt;dbl&gt; |\n|---|---|---|---|---|---|---|\n| 1 |  1 |  41 | NaN | 135 |  39 |  96 |\n| 2 |  2 |  36 | NaN |  49 |   9 |  78 |\n| 3 |  3 |  12 | NaN |  32 |  16 |  73 |\n| 4 |  4 |  18 | NaN | NaN |  78 |  91 |\n| 5 |  5 | NaN | NaN |  64 |  35 |  47 |\n| 6 |  6 |  28 | NaN |  40 |  66 |  32 |\n| 7 |  7 |  23 |  29 |  77 | 122 |  20 |\n| 8 |  8 |  19 | NaN |  97 |  89 |  23 |\n| 9 |  9 |   8 |  71 |  97 | 110 |  21 |\n| 10 | 10 | NaN |  39 |  85 | NaN |  24 |\n| 11 | 11 |   7 | NaN | NaN | NaN |  44 |\n| 12 | 12 |  16 | NaN |  10 |  44 |  21 |\n| 13 | 13 |  11 |  23 |  27 |  28 |  28 |\n| 14 | 14 |  14 | NaN | NaN |  65 |   9 |\n| 15 | 15 |  18 | NaN |   7 | NaN |  13 |\n| 16 | 16 |  14 |  21 |  48 |  22 |  46 |\n| 17 | 17 |  34 |  37 |  35 |  59 |  18 |\n| 18 | 18 |   6 |  20 |  61 |  23 |  13 |\n| 19 | 19 |  30 |  12 |  79 |  31 |  24 |\n| 20 | 20 |  11 |  13 |  63 |  44 |  16 |\n| 21 | 21 |   1 | NaN |  16 |  21 |  13 |\n| 22 | 22 |  11 | NaN | NaN |   9 |  23 |\n| 23 | 23 |   4 | NaN | NaN | NaN |  36 |\n| 24 | 24 |  32 | NaN |  80 |  45 |   7 |\n| 25 | 25 | NaN | NaN | 108 | 168 |  14 |\n| 26 | 26 | NaN | NaN |  20 |  73 |  30 |\n| 27 | 27 | NaN | NaN |  52 | NaN | NaN |\n| 28 | 28 |  23 | NaN |  82 |  76 |  14 |\n| 29 | 29 |  45 | NaN |  50 | 118 |  18 |\n| 30 | 30 | 115 | NaN |  64 |  84 |  20 |\n| 31 | 31 |  37 | NaN |  59 |  85 | NaN |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A cast_df: 31 × 6</caption>\n",
              "<thead>\n",
              "\t<tr><th></th><th scope=col>day</th><th scope=col>5</th><th scope=col>6</th><th scope=col>7</th><th scope=col>8</th><th scope=col>9</th></tr>\n",
              "\t<tr><th></th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><th scope=row>1</th><td> 1</td><td> 41</td><td>NaN</td><td>135</td><td> 39</td><td> 96</td></tr>\n",
              "\t<tr><th scope=row>2</th><td> 2</td><td> 36</td><td>NaN</td><td> 49</td><td>  9</td><td> 78</td></tr>\n",
              "\t<tr><th scope=row>3</th><td> 3</td><td> 12</td><td>NaN</td><td> 32</td><td> 16</td><td> 73</td></tr>\n",
              "\t<tr><th scope=row>4</th><td> 4</td><td> 18</td><td>NaN</td><td>NaN</td><td> 78</td><td> 91</td></tr>\n",
              "\t<tr><th scope=row>5</th><td> 5</td><td>NaN</td><td>NaN</td><td> 64</td><td> 35</td><td> 47</td></tr>\n",
              "\t<tr><th scope=row>6</th><td> 6</td><td> 28</td><td>NaN</td><td> 40</td><td> 66</td><td> 32</td></tr>\n",
              "\t<tr><th scope=row>7</th><td> 7</td><td> 23</td><td> 29</td><td> 77</td><td>122</td><td> 20</td></tr>\n",
              "\t<tr><th scope=row>8</th><td> 8</td><td> 19</td><td>NaN</td><td> 97</td><td> 89</td><td> 23</td></tr>\n",
              "\t<tr><th scope=row>9</th><td> 9</td><td>  8</td><td> 71</td><td> 97</td><td>110</td><td> 21</td></tr>\n",
              "\t<tr><th scope=row>10</th><td>10</td><td>NaN</td><td> 39</td><td> 85</td><td>NaN</td><td> 24</td></tr>\n",
              "\t<tr><th scope=row>11</th><td>11</td><td>  7</td><td>NaN</td><td>NaN</td><td>NaN</td><td> 44</td></tr>\n",
              "\t<tr><th scope=row>12</th><td>12</td><td> 16</td><td>NaN</td><td> 10</td><td> 44</td><td> 21</td></tr>\n",
              "\t<tr><th scope=row>13</th><td>13</td><td> 11</td><td> 23</td><td> 27</td><td> 28</td><td> 28</td></tr>\n",
              "\t<tr><th scope=row>14</th><td>14</td><td> 14</td><td>NaN</td><td>NaN</td><td> 65</td><td>  9</td></tr>\n",
              "\t<tr><th scope=row>15</th><td>15</td><td> 18</td><td>NaN</td><td>  7</td><td>NaN</td><td> 13</td></tr>\n",
              "\t<tr><th scope=row>16</th><td>16</td><td> 14</td><td> 21</td><td> 48</td><td> 22</td><td> 46</td></tr>\n",
              "\t<tr><th scope=row>17</th><td>17</td><td> 34</td><td> 37</td><td> 35</td><td> 59</td><td> 18</td></tr>\n",
              "\t<tr><th scope=row>18</th><td>18</td><td>  6</td><td> 20</td><td> 61</td><td> 23</td><td> 13</td></tr>\n",
              "\t<tr><th scope=row>19</th><td>19</td><td> 30</td><td> 12</td><td> 79</td><td> 31</td><td> 24</td></tr>\n",
              "\t<tr><th scope=row>20</th><td>20</td><td> 11</td><td> 13</td><td> 63</td><td> 44</td><td> 16</td></tr>\n",
              "\t<tr><th scope=row>21</th><td>21</td><td>  1</td><td>NaN</td><td> 16</td><td> 21</td><td> 13</td></tr>\n",
              "\t<tr><th scope=row>22</th><td>22</td><td> 11</td><td>NaN</td><td>NaN</td><td>  9</td><td> 23</td></tr>\n",
              "\t<tr><th scope=row>23</th><td>23</td><td>  4</td><td>NaN</td><td>NaN</td><td>NaN</td><td> 36</td></tr>\n",
              "\t<tr><th scope=row>24</th><td>24</td><td> 32</td><td>NaN</td><td> 80</td><td> 45</td><td>  7</td></tr>\n",
              "\t<tr><th scope=row>25</th><td>25</td><td>NaN</td><td>NaN</td><td>108</td><td>168</td><td> 14</td></tr>\n",
              "\t<tr><th scope=row>26</th><td>26</td><td>NaN</td><td>NaN</td><td> 20</td><td> 73</td><td> 30</td></tr>\n",
              "\t<tr><th scope=row>27</th><td>27</td><td>NaN</td><td>NaN</td><td> 52</td><td>NaN</td><td>NaN</td></tr>\n",
              "\t<tr><th scope=row>28</th><td>28</td><td> 23</td><td>NaN</td><td> 82</td><td> 76</td><td> 14</td></tr>\n",
              "\t<tr><th scope=row>29</th><td>29</td><td> 45</td><td>NaN</td><td> 50</td><td>118</td><td> 18</td></tr>\n",
              "\t<tr><th scope=row>30</th><td>30</td><td>115</td><td>NaN</td><td> 64</td><td> 84</td><td> 20</td></tr>\n",
              "\t<tr><th scope=row>31</th><td>31</td><td> 37</td><td>NaN</td><td> 59</td><td> 85</td><td>NaN</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 255
        },
        "id": "375A4NHVuxtB",
        "outputId": "aa527033-eb38-4ec3-d802-5ddd38fd27b4"
      },
      "source": [
        "f <- cast(T, month~variable, range)    # range 기능은 min은 \"_X1\"이라는 변수를, max는 \"_X2\"라는 변수명을 끝에 붙여줌\n",
        "f"
      ],
      "execution_count": 10,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  month ozone_X1 ozone_X2 solar.r_X1 solar.r_X2 wind_X1 wind_X2 temp_X1 temp_X2\n",
              "1 5      1       115       8         334        5.7     20.1    56      81     \n",
              "2 6     12        71      31         332        1.7     20.7    65      93     \n",
              "3 7      7       135       7         314        4.1     14.9    73      92     \n",
              "4 8      9       168      24         273        2.3     15.5    72      97     \n",
              "5 9      7        96      14         259        2.8     16.6    63      93     "
            ],
            "text/latex": "A cast\\_df: 5 × 9\n\\begin{tabular}{r|lllllllll}\n  & month & ozone\\_X1 & ozone\\_X2 & solar.r\\_X1 & solar.r\\_X2 & wind\\_X1 & wind\\_X2 & temp\\_X1 & temp\\_X2\\\\\n  & <int> & <dbl> & <dbl> & <dbl> & <dbl> & <dbl> & <dbl> & <dbl> & <dbl>\\\\\n\\hline\n\t1 & 5 &  1 & 115 &  8 & 334 & 5.7 & 20.1 & 56 & 81\\\\\n\t2 & 6 & 12 &  71 & 31 & 332 & 1.7 & 20.7 & 65 & 93\\\\\n\t3 & 7 &  7 & 135 &  7 & 314 & 4.1 & 14.9 & 73 & 92\\\\\n\t4 & 8 &  9 & 168 & 24 & 273 & 2.3 & 15.5 & 72 & 97\\\\\n\t5 & 9 &  7 &  96 & 14 & 259 & 2.8 & 16.6 & 63 & 93\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA cast_df: 5 × 9\n\n| <!--/--> | month &lt;int&gt; | ozone_X1 &lt;dbl&gt; | ozone_X2 &lt;dbl&gt; | solar.r_X1 &lt;dbl&gt; | solar.r_X2 &lt;dbl&gt; | wind_X1 &lt;dbl&gt; | wind_X2 &lt;dbl&gt; | temp_X1 &lt;dbl&gt; | temp_X2 &lt;dbl&gt; |\n|---|---|---|---|---|---|---|---|---|---|\n| 1 | 5 |  1 | 115 |  8 | 334 | 5.7 | 20.1 | 56 | 81 |\n| 2 | 6 | 12 |  71 | 31 | 332 | 1.7 | 20.7 | 65 | 93 |\n| 3 | 7 |  7 | 135 |  7 | 314 | 4.1 | 14.9 | 73 | 92 |\n| 4 | 8 |  9 | 168 | 24 | 273 | 2.3 | 15.5 | 72 | 97 |\n| 5 | 9 |  7 |  96 | 14 | 259 | 2.8 | 16.6 | 63 | 93 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A cast_df: 5 × 9</caption>\n",
              "<thead>\n",
              "\t<tr><th></th><th scope=col>month</th><th scope=col>ozone_X1</th><th scope=col>ozone_X2</th><th scope=col>solar.r_X1</th><th scope=col>solar.r_X2</th><th scope=col>wind_X1</th><th scope=col>wind_X2</th><th scope=col>temp_X1</th><th scope=col>temp_X2</th></tr>\n",
              "\t<tr><th></th><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><th scope=row>1</th><td>5</td><td> 1</td><td>115</td><td> 8</td><td>334</td><td>5.7</td><td>20.1</td><td>56</td><td>81</td></tr>\n",
              "\t<tr><th scope=row>2</th><td>6</td><td>12</td><td> 71</td><td>31</td><td>332</td><td>1.7</td><td>20.7</td><td>65</td><td>93</td></tr>\n",
              "\t<tr><th scope=row>3</th><td>7</td><td> 7</td><td>135</td><td> 7</td><td>314</td><td>4.1</td><td>14.9</td><td>73</td><td>92</td></tr>\n",
              "\t<tr><th scope=row>4</th><td>8</td><td> 9</td><td>168</td><td>24</td><td>273</td><td>2.3</td><td>15.5</td><td>72</td><td>97</td></tr>\n",
              "\t<tr><th scope=row>5</th><td>9</td><td> 7</td><td> 96</td><td>14</td><td>259</td><td>2.8</td><td>16.6</td><td>63</td><td>93</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "vAT5CZOcxD6P"
      },
      "source": [
        "### (3) sqldf를 이용한 데이터 분석"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "VnrNpKxNvVTb",
        "outputId": "486d861b-d39e-478f-e9a4-267f61da8d15"
      },
      "source": [
        "install.packages(\"sqldf\")\n",
        "library(\"sqldf\")"
      ],
      "execution_count": 11,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Installing package into ‘/usr/local/lib/R/site-library’\n",
            "(as ‘lib’ is unspecified)\n",
            "\n",
            "also installing the dependencies ‘plogr’, ‘gsubfn’, ‘proto’, ‘RSQLite’, ‘chron’\n",
            "\n",
            "\n",
            "Loading required package: gsubfn\n",
            "\n",
            "Loading required package: proto\n",
            "\n",
            "Warning message:\n",
            "“no DISPLAY variable so Tk is not available”\n",
            "Loading required package: RSQLite\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        },
        "id": "-gxXVyfrvmFD",
        "outputId": "2382ba0e-70fb-4880-e97e-81a2857bbd24"
      },
      "source": [
        "data(iris)\n",
        "sqldf(\"select * from iris\")             # \" \" 안에 sql 조회할 내용을 표현"
      ],
      "execution_count": 12,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "    Sepal.Length Sepal.Width Petal.Length Petal.Width Species  \n",
              "1   5.1          3.5         1.4          0.2         setosa   \n",
              "2   4.9          3.0         1.4          0.2         setosa   \n",
              "3   4.7          3.2         1.3          0.2         setosa   \n",
              "4   4.6          3.1         1.5          0.2         setosa   \n",
              "5   5.0          3.6         1.4          0.2         setosa   \n",
              "6   5.4          3.9         1.7          0.4         setosa   \n",
              "7   4.6          3.4         1.4          0.3         setosa   \n",
              "8   5.0          3.4         1.5          0.2         setosa   \n",
              "9   4.4          2.9         1.4          0.2         setosa   \n",
              "10  4.9          3.1         1.5          0.1         setosa   \n",
              "11  5.4          3.7         1.5          0.2         setosa   \n",
              "12  4.8          3.4         1.6          0.2         setosa   \n",
              "13  4.8          3.0         1.4          0.1         setosa   \n",
              "14  4.3          3.0         1.1          0.1         setosa   \n",
              "15  5.8          4.0         1.2          0.2         setosa   \n",
              "16  5.7          4.4         1.5          0.4         setosa   \n",
              "17  5.4          3.9         1.3          0.4         setosa   \n",
              "18  5.1          3.5         1.4          0.3         setosa   \n",
              "19  5.7          3.8         1.7          0.3         setosa   \n",
              "20  5.1          3.8         1.5          0.3         setosa   \n",
              "21  5.4          3.4         1.7          0.2         setosa   \n",
              "22  5.1          3.7         1.5          0.4         setosa   \n",
              "23  4.6          3.6         1.0          0.2         setosa   \n",
              "24  5.1          3.3         1.7          0.5         setosa   \n",
              "25  4.8          3.4         1.9          0.2         setosa   \n",
              "26  5.0          3.0         1.6          0.2         setosa   \n",
              "27  5.0          3.4         1.6          0.4         setosa   \n",
              "28  5.2          3.5         1.5          0.2         setosa   \n",
              "29  5.2          3.4         1.4          0.2         setosa   \n",
              "30  4.7          3.2         1.6          0.2         setosa   \n",
              "⋮   ⋮            ⋮           ⋮            ⋮           ⋮        \n",
              "121 6.9          3.2         5.7          2.3         virginica\n",
              "122 5.6          2.8         4.9          2.0         virginica\n",
              "123 7.7          2.8         6.7          2.0         virginica\n",
              "124 6.3          2.7         4.9          1.8         virginica\n",
              "125 6.7          3.3         5.7          2.1         virginica\n",
              "126 7.2          3.2         6.0          1.8         virginica\n",
              "127 6.2          2.8         4.8          1.8         virginica\n",
              "128 6.1          3.0         4.9          1.8         virginica\n",
              "129 6.4          2.8         5.6          2.1         virginica\n",
              "130 7.2          3.0         5.8          1.6         virginica\n",
              "131 7.4          2.8         6.1          1.9         virginica\n",
              "132 7.9          3.8         6.4          2.0         virginica\n",
              "133 6.4          2.8         5.6          2.2         virginica\n",
              "134 6.3          2.8         5.1          1.5         virginica\n",
              "135 6.1          2.6         5.6          1.4         virginica\n",
              "136 7.7          3.0         6.1          2.3         virginica\n",
              "137 6.3          3.4         5.6          2.4         virginica\n",
              "138 6.4          3.1         5.5          1.8         virginica\n",
              "139 6.0          3.0         4.8          1.8         virginica\n",
              "140 6.9          3.1         5.4          2.1         virginica\n",
              "141 6.7          3.1         5.6          2.4         virginica\n",
              "142 6.9          3.1         5.1          2.3         virginica\n",
              "143 5.8          2.7         5.1          1.9         virginica\n",
              "144 6.8          3.2         5.9          2.3         virginica\n",
              "145 6.7          3.3         5.7          2.5         virginica\n",
              "146 6.7          3.0         5.2          2.3         virginica\n",
              "147 6.3          2.5         5.0          1.9         virginica\n",
              "148 6.5          3.0         5.2          2.0         virginica\n",
              "149 6.2          3.4         5.4          2.3         virginica\n",
              "150 5.9          3.0         5.1          1.8         virginica"
            ],
            "text/latex": "A data.frame: 150 × 5\n\\begin{tabular}{lllll}\n Sepal.Length & Sepal.Width & Petal.Length & Petal.Width & Species\\\\\n <dbl> & <dbl> & <dbl> & <dbl> & <fct>\\\\\n\\hline\n\t 5.1 & 3.5 & 1.4 & 0.2 & setosa\\\\\n\t 4.9 & 3.0 & 1.4 & 0.2 & setosa\\\\\n\t 4.7 & 3.2 & 1.3 & 0.2 & setosa\\\\\n\t 4.6 & 3.1 & 1.5 & 0.2 & setosa\\\\\n\t 5.0 & 3.6 & 1.4 & 0.2 & setosa\\\\\n\t 5.4 & 3.9 & 1.7 & 0.4 & setosa\\\\\n\t 4.6 & 3.4 & 1.4 & 0.3 & setosa\\\\\n\t 5.0 & 3.4 & 1.5 & 0.2 & setosa\\\\\n\t 4.4 & 2.9 & 1.4 & 0.2 & setosa\\\\\n\t 4.9 & 3.1 & 1.5 & 0.1 & setosa\\\\\n\t 5.4 & 3.7 & 1.5 & 0.2 & setosa\\\\\n\t 4.8 & 3.4 & 1.6 & 0.2 & setosa\\\\\n\t 4.8 & 3.0 & 1.4 & 0.1 & setosa\\\\\n\t 4.3 & 3.0 & 1.1 & 0.1 & setosa\\\\\n\t 5.8 & 4.0 & 1.2 & 0.2 & setosa\\\\\n\t 5.7 & 4.4 & 1.5 & 0.4 & setosa\\\\\n\t 5.4 & 3.9 & 1.3 & 0.4 & setosa\\\\\n\t 5.1 & 3.5 & 1.4 & 0.3 & setosa\\\\\n\t 5.7 & 3.8 & 1.7 & 0.3 & setosa\\\\\n\t 5.1 & 3.8 & 1.5 & 0.3 & setosa\\\\\n\t 5.4 & 3.4 & 1.7 & 0.2 & setosa\\\\\n\t 5.1 & 3.7 & 1.5 & 0.4 & setosa\\\\\n\t 4.6 & 3.6 & 1.0 & 0.2 & setosa\\\\\n\t 5.1 & 3.3 & 1.7 & 0.5 & setosa\\\\\n\t 4.8 & 3.4 & 1.9 & 0.2 & setosa\\\\\n\t 5.0 & 3.0 & 1.6 & 0.2 & setosa\\\\\n\t 5.0 & 3.4 & 1.6 & 0.4 & setosa\\\\\n\t 5.2 & 3.5 & 1.5 & 0.2 & setosa\\\\\n\t 5.2 & 3.4 & 1.4 & 0.2 & setosa\\\\\n\t 4.7 & 3.2 & 1.6 & 0.2 & setosa\\\\\n\t ⋮ & ⋮ & ⋮ & ⋮ & ⋮\\\\\n\t 6.9 & 3.2 & 5.7 & 2.3 & virginica\\\\\n\t 5.6 & 2.8 & 4.9 & 2.0 & virginica\\\\\n\t 7.7 & 2.8 & 6.7 & 2.0 & virginica\\\\\n\t 6.3 & 2.7 & 4.9 & 1.8 & virginica\\\\\n\t 6.7 & 3.3 & 5.7 & 2.1 & virginica\\\\\n\t 7.2 & 3.2 & 6.0 & 1.8 & virginica\\\\\n\t 6.2 & 2.8 & 4.8 & 1.8 & virginica\\\\\n\t 6.1 & 3.0 & 4.9 & 1.8 & virginica\\\\\n\t 6.4 & 2.8 & 5.6 & 2.1 & virginica\\\\\n\t 7.2 & 3.0 & 5.8 & 1.6 & virginica\\\\\n\t 7.4 & 2.8 & 6.1 & 1.9 & virginica\\\\\n\t 7.9 & 3.8 & 6.4 & 2.0 & virginica\\\\\n\t 6.4 & 2.8 & 5.6 & 2.2 & virginica\\\\\n\t 6.3 & 2.8 & 5.1 & 1.5 & virginica\\\\\n\t 6.1 & 2.6 & 5.6 & 1.4 & virginica\\\\\n\t 7.7 & 3.0 & 6.1 & 2.3 & virginica\\\\\n\t 6.3 & 3.4 & 5.6 & 2.4 & virginica\\\\\n\t 6.4 & 3.1 & 5.5 & 1.8 & virginica\\\\\n\t 6.0 & 3.0 & 4.8 & 1.8 & virginica\\\\\n\t 6.9 & 3.1 & 5.4 & 2.1 & virginica\\\\\n\t 6.7 & 3.1 & 5.6 & 2.4 & virginica\\\\\n\t 6.9 & 3.1 & 5.1 & 2.3 & virginica\\\\\n\t 5.8 & 2.7 & 5.1 & 1.9 & virginica\\\\\n\t 6.8 & 3.2 & 5.9 & 2.3 & virginica\\\\\n\t 6.7 & 3.3 & 5.7 & 2.5 & virginica\\\\\n\t 6.7 & 3.0 & 5.2 & 2.3 & virginica\\\\\n\t 6.3 & 2.5 & 5.0 & 1.9 & virginica\\\\\n\t 6.5 & 3.0 & 5.2 & 2.0 & virginica\\\\\n\t 6.2 & 3.4 & 5.4 & 2.3 & virginica\\\\\n\t 5.9 & 3.0 & 5.1 & 1.8 & virginica\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 150 × 5\n\n| Sepal.Length &lt;dbl&gt; | Sepal.Width &lt;dbl&gt; | Petal.Length &lt;dbl&gt; | Petal.Width &lt;dbl&gt; | Species &lt;fct&gt; |\n|---|---|---|---|---|\n| 5.1 | 3.5 | 1.4 | 0.2 | setosa |\n| 4.9 | 3.0 | 1.4 | 0.2 | setosa |\n| 4.7 | 3.2 | 1.3 | 0.2 | setosa |\n| 4.6 | 3.1 | 1.5 | 0.2 | setosa |\n| 5.0 | 3.6 | 1.4 | 0.2 | setosa |\n| 5.4 | 3.9 | 1.7 | 0.4 | setosa |\n| 4.6 | 3.4 | 1.4 | 0.3 | setosa |\n| 5.0 | 3.4 | 1.5 | 0.2 | setosa |\n| 4.4 | 2.9 | 1.4 | 0.2 | setosa |\n| 4.9 | 3.1 | 1.5 | 0.1 | setosa |\n| 5.4 | 3.7 | 1.5 | 0.2 | setosa |\n| 4.8 | 3.4 | 1.6 | 0.2 | setosa |\n| 4.8 | 3.0 | 1.4 | 0.1 | setosa |\n| 4.3 | 3.0 | 1.1 | 0.1 | setosa |\n| 5.8 | 4.0 | 1.2 | 0.2 | setosa |\n| 5.7 | 4.4 | 1.5 | 0.4 | setosa |\n| 5.4 | 3.9 | 1.3 | 0.4 | setosa |\n| 5.1 | 3.5 | 1.4 | 0.3 | setosa |\n| 5.7 | 3.8 | 1.7 | 0.3 | setosa |\n| 5.1 | 3.8 | 1.5 | 0.3 | setosa |\n| 5.4 | 3.4 | 1.7 | 0.2 | setosa |\n| 5.1 | 3.7 | 1.5 | 0.4 | setosa |\n| 4.6 | 3.6 | 1.0 | 0.2 | setosa |\n| 5.1 | 3.3 | 1.7 | 0.5 | setosa |\n| 4.8 | 3.4 | 1.9 | 0.2 | setosa |\n| 5.0 | 3.0 | 1.6 | 0.2 | setosa |\n| 5.0 | 3.4 | 1.6 | 0.4 | setosa |\n| 5.2 | 3.5 | 1.5 | 0.2 | setosa |\n| 5.2 | 3.4 | 1.4 | 0.2 | setosa |\n| 4.7 | 3.2 | 1.6 | 0.2 | setosa |\n| ⋮ | ⋮ | ⋮ | ⋮ | ⋮ |\n| 6.9 | 3.2 | 5.7 | 2.3 | virginica |\n| 5.6 | 2.8 | 4.9 | 2.0 | virginica |\n| 7.7 | 2.8 | 6.7 | 2.0 | virginica |\n| 6.3 | 2.7 | 4.9 | 1.8 | virginica |\n| 6.7 | 3.3 | 5.7 | 2.1 | virginica |\n| 7.2 | 3.2 | 6.0 | 1.8 | virginica |\n| 6.2 | 2.8 | 4.8 | 1.8 | virginica |\n| 6.1 | 3.0 | 4.9 | 1.8 | virginica |\n| 6.4 | 2.8 | 5.6 | 2.1 | virginica |\n| 7.2 | 3.0 | 5.8 | 1.6 | virginica |\n| 7.4 | 2.8 | 6.1 | 1.9 | virginica |\n| 7.9 | 3.8 | 6.4 | 2.0 | virginica |\n| 6.4 | 2.8 | 5.6 | 2.2 | virginica |\n| 6.3 | 2.8 | 5.1 | 1.5 | virginica |\n| 6.1 | 2.6 | 5.6 | 1.4 | virginica |\n| 7.7 | 3.0 | 6.1 | 2.3 | virginica |\n| 6.3 | 3.4 | 5.6 | 2.4 | virginica |\n| 6.4 | 3.1 | 5.5 | 1.8 | virginica |\n| 6.0 | 3.0 | 4.8 | 1.8 | virginica |\n| 6.9 | 3.1 | 5.4 | 2.1 | virginica |\n| 6.7 | 3.1 | 5.6 | 2.4 | virginica |\n| 6.9 | 3.1 | 5.1 | 2.3 | virginica |\n| 5.8 | 2.7 | 5.1 | 1.9 | virginica |\n| 6.8 | 3.2 | 5.9 | 2.3 | virginica |\n| 6.7 | 3.3 | 5.7 | 2.5 | virginica |\n| 6.7 | 3.0 | 5.2 | 2.3 | virginica |\n| 6.3 | 2.5 | 5.0 | 1.9 | virginica |\n| 6.5 | 3.0 | 5.2 | 2.0 | virginica |\n| 6.2 | 3.4 | 5.4 | 2.3 | virginica |\n| 5.9 | 3.0 | 5.1 | 1.8 | virginica |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 150 × 5</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>Sepal.Length</th><th scope=col>Sepal.Width</th><th scope=col>Petal.Length</th><th scope=col>Petal.Width</th><th scope=col>Species</th></tr>\n",
              "\t<tr><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;fct&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>5.1</td><td>3.5</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.9</td><td>3.0</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.7</td><td>3.2</td><td>1.3</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.6</td><td>3.1</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.0</td><td>3.6</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.4</td><td>3.9</td><td>1.7</td><td>0.4</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.6</td><td>3.4</td><td>1.4</td><td>0.3</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.0</td><td>3.4</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.4</td><td>2.9</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.9</td><td>3.1</td><td>1.5</td><td>0.1</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.4</td><td>3.7</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.8</td><td>3.4</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.8</td><td>3.0</td><td>1.4</td><td>0.1</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.3</td><td>3.0</td><td>1.1</td><td>0.1</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.8</td><td>4.0</td><td>1.2</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.7</td><td>4.4</td><td>1.5</td><td>0.4</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.4</td><td>3.9</td><td>1.3</td><td>0.4</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.1</td><td>3.5</td><td>1.4</td><td>0.3</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.7</td><td>3.8</td><td>1.7</td><td>0.3</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.1</td><td>3.8</td><td>1.5</td><td>0.3</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.4</td><td>3.4</td><td>1.7</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.1</td><td>3.7</td><td>1.5</td><td>0.4</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.6</td><td>3.6</td><td>1.0</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.1</td><td>3.3</td><td>1.7</td><td>0.5</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.8</td><td>3.4</td><td>1.9</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.0</td><td>3.0</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.0</td><td>3.4</td><td>1.6</td><td>0.4</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.2</td><td>3.5</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.2</td><td>3.4</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.7</td><td>3.2</td><td>1.6</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td><td>⋮</td></tr>\n",
              "\t<tr><td>6.9</td><td>3.2</td><td>5.7</td><td>2.3</td><td>virginica</td></tr>\n",
              "\t<tr><td>5.6</td><td>2.8</td><td>4.9</td><td>2.0</td><td>virginica</td></tr>\n",
              "\t<tr><td>7.7</td><td>2.8</td><td>6.7</td><td>2.0</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.3</td><td>2.7</td><td>4.9</td><td>1.8</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.7</td><td>3.3</td><td>5.7</td><td>2.1</td><td>virginica</td></tr>\n",
              "\t<tr><td>7.2</td><td>3.2</td><td>6.0</td><td>1.8</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.2</td><td>2.8</td><td>4.8</td><td>1.8</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.1</td><td>3.0</td><td>4.9</td><td>1.8</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.4</td><td>2.8</td><td>5.6</td><td>2.1</td><td>virginica</td></tr>\n",
              "\t<tr><td>7.2</td><td>3.0</td><td>5.8</td><td>1.6</td><td>virginica</td></tr>\n",
              "\t<tr><td>7.4</td><td>2.8</td><td>6.1</td><td>1.9</td><td>virginica</td></tr>\n",
              "\t<tr><td>7.9</td><td>3.8</td><td>6.4</td><td>2.0</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.4</td><td>2.8</td><td>5.6</td><td>2.2</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.3</td><td>2.8</td><td>5.1</td><td>1.5</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.1</td><td>2.6</td><td>5.6</td><td>1.4</td><td>virginica</td></tr>\n",
              "\t<tr><td>7.7</td><td>3.0</td><td>6.1</td><td>2.3</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.3</td><td>3.4</td><td>5.6</td><td>2.4</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.4</td><td>3.1</td><td>5.5</td><td>1.8</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.0</td><td>3.0</td><td>4.8</td><td>1.8</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.9</td><td>3.1</td><td>5.4</td><td>2.1</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.7</td><td>3.1</td><td>5.6</td><td>2.4</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.9</td><td>3.1</td><td>5.1</td><td>2.3</td><td>virginica</td></tr>\n",
              "\t<tr><td>5.8</td><td>2.7</td><td>5.1</td><td>1.9</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.8</td><td>3.2</td><td>5.9</td><td>2.3</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.7</td><td>3.3</td><td>5.7</td><td>2.5</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.7</td><td>3.0</td><td>5.2</td><td>2.3</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.3</td><td>2.5</td><td>5.0</td><td>1.9</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.5</td><td>3.0</td><td>5.2</td><td>2.0</td><td>virginica</td></tr>\n",
              "\t<tr><td>6.2</td><td>3.4</td><td>5.4</td><td>2.3</td><td>virginica</td></tr>\n",
              "\t<tr><td>5.9</td><td>3.0</td><td>5.1</td><td>1.8</td><td>virginica</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 412
        },
        "id": "j6eOCNyuvtBI",
        "outputId": "6d4ece47-1f56-4ada-dc83-1366865fe602"
      },
      "source": [
        "sqldf(\"select * from iris limit 10\")    # 데이터의 특정 행수만 조회(head와 같은 기능)"
      ],
      "execution_count": 13,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "   Sepal.Length Sepal.Width Petal.Length Petal.Width Species\n",
              "1  5.1          3.5         1.4          0.2         setosa \n",
              "2  4.9          3.0         1.4          0.2         setosa \n",
              "3  4.7          3.2         1.3          0.2         setosa \n",
              "4  4.6          3.1         1.5          0.2         setosa \n",
              "5  5.0          3.6         1.4          0.2         setosa \n",
              "6  5.4          3.9         1.7          0.4         setosa \n",
              "7  4.6          3.4         1.4          0.3         setosa \n",
              "8  5.0          3.4         1.5          0.2         setosa \n",
              "9  4.4          2.9         1.4          0.2         setosa \n",
              "10 4.9          3.1         1.5          0.1         setosa "
            ],
            "text/latex": "A data.frame: 10 × 5\n\\begin{tabular}{lllll}\n Sepal.Length & Sepal.Width & Petal.Length & Petal.Width & Species\\\\\n <dbl> & <dbl> & <dbl> & <dbl> & <fct>\\\\\n\\hline\n\t 5.1 & 3.5 & 1.4 & 0.2 & setosa\\\\\n\t 4.9 & 3.0 & 1.4 & 0.2 & setosa\\\\\n\t 4.7 & 3.2 & 1.3 & 0.2 & setosa\\\\\n\t 4.6 & 3.1 & 1.5 & 0.2 & setosa\\\\\n\t 5.0 & 3.6 & 1.4 & 0.2 & setosa\\\\\n\t 5.4 & 3.9 & 1.7 & 0.4 & setosa\\\\\n\t 4.6 & 3.4 & 1.4 & 0.3 & setosa\\\\\n\t 5.0 & 3.4 & 1.5 & 0.2 & setosa\\\\\n\t 4.4 & 2.9 & 1.4 & 0.2 & setosa\\\\\n\t 4.9 & 3.1 & 1.5 & 0.1 & setosa\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 10 × 5\n\n| Sepal.Length &lt;dbl&gt; | Sepal.Width &lt;dbl&gt; | Petal.Length &lt;dbl&gt; | Petal.Width &lt;dbl&gt; | Species &lt;fct&gt; |\n|---|---|---|---|---|\n| 5.1 | 3.5 | 1.4 | 0.2 | setosa |\n| 4.9 | 3.0 | 1.4 | 0.2 | setosa |\n| 4.7 | 3.2 | 1.3 | 0.2 | setosa |\n| 4.6 | 3.1 | 1.5 | 0.2 | setosa |\n| 5.0 | 3.6 | 1.4 | 0.2 | setosa |\n| 5.4 | 3.9 | 1.7 | 0.4 | setosa |\n| 4.6 | 3.4 | 1.4 | 0.3 | setosa |\n| 5.0 | 3.4 | 1.5 | 0.2 | setosa |\n| 4.4 | 2.9 | 1.4 | 0.2 | setosa |\n| 4.9 | 3.1 | 1.5 | 0.1 | setosa |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 10 × 5</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>Sepal.Length</th><th scope=col>Sepal.Width</th><th scope=col>Petal.Length</th><th scope=col>Petal.Width</th><th scope=col>Species</th></tr>\n",
              "\t<tr><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;fct&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>5.1</td><td>3.5</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.9</td><td>3.0</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.7</td><td>3.2</td><td>1.3</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.6</td><td>3.1</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.0</td><td>3.6</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.4</td><td>3.9</td><td>1.7</td><td>0.4</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.6</td><td>3.4</td><td>1.4</td><td>0.3</td><td>setosa</td></tr>\n",
              "\t<tr><td>5.0</td><td>3.4</td><td>1.5</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.4</td><td>2.9</td><td>1.4</td><td>0.2</td><td>setosa</td></tr>\n",
              "\t<tr><td>4.9</td><td>3.1</td><td>1.5</td><td>0.1</td><td>setosa</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 147
        },
        "id": "zsDxuYN_v6H8",
        "outputId": "8199e2aa-40df-45d2-bd95-23c9f0a93b25"
      },
      "source": [
        "sqldf(\"select count(*) from iris where species like 'se%'\")   # species 중 'se'로 시작되는 붓꽃 종류의 개수"
      ],
      "execution_count": 14,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  count(*)\n",
              "1 50      "
            ],
            "text/latex": "A data.frame: 1 × 1\n\\begin{tabular}{l}\n count(*)\\\\\n <int>\\\\\n\\hline\n\t 50\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 1 × 1\n\n| count(*) &lt;int&gt; |\n|---|\n| 50 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 1 × 1</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>count(*)</th></tr>\n",
              "\t<tr><th scope=col>&lt;int&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>50</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "ESBuLVADxRwo"
      },
      "source": [
        "### (4) plyr\n",
        "\n",
        "- 데이터를 분리(split)하고, 분할된 데이터에 특정 함수를 적용(apply), 결과를 재결합(combine) 처리하는 함수 제공\n",
        "- apply 함수와 multi-core 사용함수를 이용하면 for loop를 사용하지 않고 매우 간단하게 처리할 수 있고, apply 함수에 기반해 데이터와 출력변수를 동시에 배열로 치환하여 처리 가능"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "ye_IOpNN2E7O",
        "outputId": "ce812684-99d9-4916-ceff-357598b7587b"
      },
      "source": [
        "set.seed(1)   # 난수를 생성할 때마다 같은 값의 난수들을 생성\n",
        "runif(9, 0, 20)"
      ],
      "execution_count": 15,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "[1]  5.310173  7.442478 11.457067 18.164156  4.033639 17.967794 18.893505\n",
              "[8] 13.215956 12.582281"
            ],
            "text/latex": "\\begin{enumerate*}\n\\item 5.310173262842\n\\item 7.4424779927358\n\\item 11.4570672670379\n\\item 18.1641557998955\n\\item 4.03363862074912\n\\item 17.9677936993539\n\\item 18.893505372107\n\\item 13.2159558497369\n\\item 12.5822808779776\n\\end{enumerate*}\n",
            "text/markdown": "1. 5.310173262842\n2. 7.4424779927358\n3. 11.4570672670379\n4. 18.1641557998955\n5. 4.03363862074912\n6. 17.9677936993539\n7. 18.893505372107\n8. 13.2159558497369\n9. 12.5822808779776\n\n\n",
            "text/html": [
              "<style>\n",
              ".list-inline {list-style: none; margin:0; padding: 0}\n",
              ".list-inline>li {display: inline-block}\n",
              ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
              "</style>\n",
              "<ol class=list-inline><li>5.310173262842</li><li>7.4424779927358</li><li>11.4570672670379</li><li>18.1641557998955</li><li>4.03363862074912</li><li>17.9677936993539</li><li>18.893505372107</li><li>13.2159558497369</li><li>12.5822808779776</li></ol>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "okrxw1Zr2Ole",
        "outputId": "480109e0-1165-4dc2-fe1b-1dfd5b5423ab"
      },
      "source": [
        "set.seed(1)   # 난수를 생성할 때마다 같은 값의 난수들을 생성\n",
        "round(runif(9, 0, 20))"
      ],
      "execution_count": 16,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "[1]  5  7 11 18  4 18 19 13 13"
            ],
            "text/latex": "\\begin{enumerate*}\n\\item 5\n\\item 7\n\\item 11\n\\item 18\n\\item 4\n\\item 18\n\\item 19\n\\item 13\n\\item 13\n\\end{enumerate*}\n",
            "text/markdown": "1. 5\n2. 7\n3. 11\n4. 18\n5. 4\n6. 18\n7. 19\n8. 13\n9. 13\n\n\n",
            "text/html": [
              "<style>\n",
              ".list-inline {list-style: none; margin:0; padding: 0}\n",
              ".list-inline>li {display: inline-block}\n",
              ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
              "</style>\n",
              "<ol class=list-inline><li>5</li><li>7</li><li>11</li><li>18</li><li>4</li><li>18</li><li>19</li><li>13</li><li>13</li></ol>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 680
        },
        "id": "R3Eax1GBxQac",
        "outputId": "f7d0ad56-0146-46ec-ee0a-662db98ea6db"
      },
      "source": [
        "set.seed(1)   # 난수를 생성할 때마다 같은 값의 난수들을 생성\n",
        "\n",
        "# 2012 ~ 2014년 각각 6개를 만들고 count라는 변수에 난수를 생성하는 runif(생성할 난수의 수, 최솟값, 최댓값) 0에서 20 사이의 정수(round, 반올림) 9개를 저장\n",
        "d <- data.frame(year = rep(2012:2014, each = 6), count = round(runif(9, 0, 20)))\n",
        "d"
      ],
      "execution_count": 17,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "   year count\n",
              "1  2012  5   \n",
              "2  2012  7   \n",
              "3  2012 11   \n",
              "4  2012 18   \n",
              "5  2012  4   \n",
              "6  2012 18   \n",
              "7  2013 19   \n",
              "8  2013 13   \n",
              "9  2013 13   \n",
              "10 2013  5   \n",
              "11 2013  7   \n",
              "12 2013 11   \n",
              "13 2014 18   \n",
              "14 2014  4   \n",
              "15 2014 18   \n",
              "16 2014 19   \n",
              "17 2014 13   \n",
              "18 2014 13   "
            ],
            "text/latex": "A data.frame: 18 × 2\n\\begin{tabular}{ll}\n year & count\\\\\n <int> & <dbl>\\\\\n\\hline\n\t 2012 &  5\\\\\n\t 2012 &  7\\\\\n\t 2012 & 11\\\\\n\t 2012 & 18\\\\\n\t 2012 &  4\\\\\n\t 2012 & 18\\\\\n\t 2013 & 19\\\\\n\t 2013 & 13\\\\\n\t 2013 & 13\\\\\n\t 2013 &  5\\\\\n\t 2013 &  7\\\\\n\t 2013 & 11\\\\\n\t 2014 & 18\\\\\n\t 2014 &  4\\\\\n\t 2014 & 18\\\\\n\t 2014 & 19\\\\\n\t 2014 & 13\\\\\n\t 2014 & 13\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 18 × 2\n\n| year &lt;int&gt; | count &lt;dbl&gt; |\n|---|---|\n| 2012 |  5 |\n| 2012 |  7 |\n| 2012 | 11 |\n| 2012 | 18 |\n| 2012 |  4 |\n| 2012 | 18 |\n| 2013 | 19 |\n| 2013 | 13 |\n| 2013 | 13 |\n| 2013 |  5 |\n| 2013 |  7 |\n| 2013 | 11 |\n| 2014 | 18 |\n| 2014 |  4 |\n| 2014 | 18 |\n| 2014 | 19 |\n| 2014 | 13 |\n| 2014 | 13 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 18 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>year</th><th scope=col>count</th></tr>\n",
              "\t<tr><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>2012</td><td> 5</td></tr>\n",
              "\t<tr><td>2012</td><td> 7</td></tr>\n",
              "\t<tr><td>2012</td><td>11</td></tr>\n",
              "\t<tr><td>2012</td><td>18</td></tr>\n",
              "\t<tr><td>2012</td><td> 4</td></tr>\n",
              "\t<tr><td>2012</td><td>18</td></tr>\n",
              "\t<tr><td>2013</td><td>19</td></tr>\n",
              "\t<tr><td>2013</td><td>13</td></tr>\n",
              "\t<tr><td>2013</td><td>13</td></tr>\n",
              "\t<tr><td>2013</td><td> 5</td></tr>\n",
              "\t<tr><td>2013</td><td> 7</td></tr>\n",
              "\t<tr><td>2013</td><td>11</td></tr>\n",
              "\t<tr><td>2014</td><td>18</td></tr>\n",
              "\t<tr><td>2014</td><td> 4</td></tr>\n",
              "\t<tr><td>2014</td><td>18</td></tr>\n",
              "\t<tr><td>2014</td><td>19</td></tr>\n",
              "\t<tr><td>2014</td><td>13</td></tr>\n",
              "\t<tr><td>2014</td><td>13</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "SRE1CPgfx3ff",
        "outputId": "1e0f94b2-d177-40f7-c3c9-5877d4fca60d"
      },
      "source": [
        "install.packages(\"plyr\")\n",
        "library(plyr)"
      ],
      "execution_count": 18,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Installing package into ‘/usr/local/lib/R/site-library’\n",
            "(as ‘lib’ is unspecified)\n",
            "\n",
            "\n",
            "Attaching package: ‘plyr’\n",
            "\n",
            "\n",
            "The following objects are masked from ‘package:reshape’:\n",
            "\n",
            "    rename, round_any\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 192
        },
        "id": "hhFRSrJxyCCv",
        "outputId": "98416e54-5480-4f05-fb64-482fd65065eb"
      },
      "source": [
        "# ddply() 함수 : 데이터 프레임을 분할하고 함수를 적용한 뒤 결과를 데이터 프레임으로 반환\n",
        "# ddply(data, variables, fun = NULL)\n",
        "\n",
        "# adply() : 행 또는 컬럼 단위로 함수를 적용\n",
        "# ddply() : variables에 나열한 컬럼에 따라 데이터를 나눈 뒤 함수를 적용\n",
        "\n",
        "# ddply를 이용해 sd(표준편차), mean(평균)의 비율인 cv(변동계수)를 구하는 함수 (cv = sd / mean)\n",
        "ddply(d, \"year\", function(x){\n",
        "  mean.count = mean(x$count)\n",
        "  sd.count = sd(x$count)\n",
        "  cv = sd.count / mean.count\n",
        "  data.frame(cv.count = cv)\n",
        "})"
      ],
      "execution_count": 19,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  year cv.count \n",
              "1 2012 0.5985621\n",
              "2 2013 0.4382254\n",
              "3 2014 0.3978489"
            ],
            "text/latex": "A data.frame: 3 × 2\n\\begin{tabular}{ll}\n year & cv.count\\\\\n <int> & <dbl>\\\\\n\\hline\n\t 2012 & 0.5985621\\\\\n\t 2013 & 0.4382254\\\\\n\t 2014 & 0.3978489\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 3 × 2\n\n| year &lt;int&gt; | cv.count &lt;dbl&gt; |\n|---|---|\n| 2012 | 0.5985621 |\n| 2013 | 0.4382254 |\n| 2014 | 0.3978489 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 3 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>year</th><th scope=col>cv.count</th></tr>\n",
              "\t<tr><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>2012</td><td>0.5985621</td></tr>\n",
              "\t<tr><td>2013</td><td>0.4382254</td></tr>\n",
              "\t<tr><td>2014</td><td>0.3978489</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "iCS7q-Yt38af",
        "outputId": "6f6bae6b-7e27-456e-d709-e30445e40d47"
      },
      "source": [
        "d$count"
      ],
      "execution_count": 20,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              " [1]  5  7 11 18  4 18 19 13 13  5  7 11 18  4 18 19 13 13"
            ],
            "text/latex": "\\begin{enumerate*}\n\\item 5\n\\item 7\n\\item 11\n\\item 18\n\\item 4\n\\item 18\n\\item 19\n\\item 13\n\\item 13\n\\item 5\n\\item 7\n\\item 11\n\\item 18\n\\item 4\n\\item 18\n\\item 19\n\\item 13\n\\item 13\n\\end{enumerate*}\n",
            "text/markdown": "1. 5\n2. 7\n3. 11\n4. 18\n5. 4\n6. 18\n7. 19\n8. 13\n9. 13\n10. 5\n11. 7\n12. 11\n13. 18\n14. 4\n15. 18\n16. 19\n17. 13\n18. 13\n\n\n",
            "text/html": [
              "<style>\n",
              ".list-inline {list-style: none; margin:0; padding: 0}\n",
              ".list-inline>li {display: inline-block}\n",
              ".list-inline>li:not(:last-child)::after {content: \"\\00b7\"; padding: 0 .5ex}\n",
              "</style>\n",
              "<ol class=list-inline><li>5</li><li>7</li><li>11</li><li>18</li><li>4</li><li>18</li><li>19</li><li>13</li><li>13</li><li>5</li><li>7</li><li>11</li><li>18</li><li>4</li><li>18</li><li>19</li><li>13</li><li>13</li></ol>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 192
        },
        "id": "TkOZZcOT4G05",
        "outputId": "0ebf32a8-7fa3-4af1-e9ef-d153135894ba"
      },
      "source": [
        "# summarise() : 데이터의 요약 정보를 새로운 변수에 만드는 함수\n",
        "ddply(d, .(year), summarise, mean.count = mean(count))"
      ],
      "execution_count": 21,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  year mean.count\n",
              "1 2012 10.50000  \n",
              "2 2013 11.33333  \n",
              "3 2014 14.16667  "
            ],
            "text/latex": "A data.frame: 3 × 2\n\\begin{tabular}{ll}\n year & mean.count\\\\\n <int> & <dbl>\\\\\n\\hline\n\t 2012 & 10.50000\\\\\n\t 2013 & 11.33333\\\\\n\t 2014 & 14.16667\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 3 × 2\n\n| year &lt;int&gt; | mean.count &lt;dbl&gt; |\n|---|---|\n| 2012 | 10.50000 |\n| 2013 | 11.33333 |\n| 2014 | 14.16667 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 3 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>year</th><th scope=col>mean.count</th></tr>\n",
              "\t<tr><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>2012</td><td>10.50000</td></tr>\n",
              "\t<tr><td>2013</td><td>11.33333</td></tr>\n",
              "\t<tr><td>2014</td><td>14.16667</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 663
        },
        "id": "xV5fIpoO4zsp",
        "outputId": "65df11fd-e19f-4c47-eb13-92a1484978d7"
      },
      "source": [
        "# transform() : 연산 결과를 데이터 프레임의 새로운 컬럼에 저장하는 함수\n",
        "ddply(d, .(year), transform, total.count = sum(count))"
      ],
      "execution_count": 22,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "   year count total.count\n",
              "1  2012  5    63         \n",
              "2  2012  7    63         \n",
              "3  2012 11    63         \n",
              "4  2012 18    63         \n",
              "5  2012  4    63         \n",
              "6  2012 18    63         \n",
              "7  2013 19    68         \n",
              "8  2013 13    68         \n",
              "9  2013 13    68         \n",
              "10 2013  5    68         \n",
              "11 2013  7    68         \n",
              "12 2013 11    68         \n",
              "13 2014 18    85         \n",
              "14 2014  4    85         \n",
              "15 2014 18    85         \n",
              "16 2014 19    85         \n",
              "17 2014 13    85         \n",
              "18 2014 13    85         "
            ],
            "text/latex": "A data.frame: 18 × 3\n\\begin{tabular}{lll}\n year & count & total.count\\\\\n <int> & <dbl> & <dbl>\\\\\n\\hline\n\t 2012 &  5 & 63\\\\\n\t 2012 &  7 & 63\\\\\n\t 2012 & 11 & 63\\\\\n\t 2012 & 18 & 63\\\\\n\t 2012 &  4 & 63\\\\\n\t 2012 & 18 & 63\\\\\n\t 2013 & 19 & 68\\\\\n\t 2013 & 13 & 68\\\\\n\t 2013 & 13 & 68\\\\\n\t 2013 &  5 & 68\\\\\n\t 2013 &  7 & 68\\\\\n\t 2013 & 11 & 68\\\\\n\t 2014 & 18 & 85\\\\\n\t 2014 &  4 & 85\\\\\n\t 2014 & 18 & 85\\\\\n\t 2014 & 19 & 85\\\\\n\t 2014 & 13 & 85\\\\\n\t 2014 & 13 & 85\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.frame: 18 × 3\n\n| year &lt;int&gt; | count &lt;dbl&gt; | total.count &lt;dbl&gt; |\n|---|---|---|\n| 2012 |  5 | 63 |\n| 2012 |  7 | 63 |\n| 2012 | 11 | 63 |\n| 2012 | 18 | 63 |\n| 2012 |  4 | 63 |\n| 2012 | 18 | 63 |\n| 2013 | 19 | 68 |\n| 2013 | 13 | 68 |\n| 2013 | 13 | 68 |\n| 2013 |  5 | 68 |\n| 2013 |  7 | 68 |\n| 2013 | 11 | 68 |\n| 2014 | 18 | 85 |\n| 2014 |  4 | 85 |\n| 2014 | 18 | 85 |\n| 2014 | 19 | 85 |\n| 2014 | 13 | 85 |\n| 2014 | 13 | 85 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.frame: 18 × 3</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>year</th><th scope=col>count</th><th scope=col>total.count</th></tr>\n",
              "\t<tr><th scope=col>&lt;int&gt;</th><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>2012</td><td> 5</td><td>63</td></tr>\n",
              "\t<tr><td>2012</td><td> 7</td><td>63</td></tr>\n",
              "\t<tr><td>2012</td><td>11</td><td>63</td></tr>\n",
              "\t<tr><td>2012</td><td>18</td><td>63</td></tr>\n",
              "\t<tr><td>2012</td><td> 4</td><td>63</td></tr>\n",
              "\t<tr><td>2012</td><td>18</td><td>63</td></tr>\n",
              "\t<tr><td>2013</td><td>19</td><td>68</td></tr>\n",
              "\t<tr><td>2013</td><td>13</td><td>68</td></tr>\n",
              "\t<tr><td>2013</td><td>13</td><td>68</td></tr>\n",
              "\t<tr><td>2013</td><td> 5</td><td>68</td></tr>\n",
              "\t<tr><td>2013</td><td> 7</td><td>68</td></tr>\n",
              "\t<tr><td>2013</td><td>11</td><td>68</td></tr>\n",
              "\t<tr><td>2014</td><td>18</td><td>85</td></tr>\n",
              "\t<tr><td>2014</td><td> 4</td><td>85</td></tr>\n",
              "\t<tr><td>2014</td><td>18</td><td>85</td></tr>\n",
              "\t<tr><td>2014</td><td>19</td><td>85</td></tr>\n",
              "\t<tr><td>2014</td><td>13</td><td>85</td></tr>\n",
              "\t<tr><td>2014</td><td>13</td><td>85</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "y8SpcobV5Wa2"
      },
      "source": [
        "### (5) 데이터 테이블\n",
        "\n",
        "- 보다 빠른 그룹화(grouping)와 순서화(ordering)\n",
        "- 데이터 프레임보다 연산 속도가 빠름"
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "Wtpoqeht5Qnr",
        "outputId": "8a6c1069-edec-4de0-8544-0047fecde553"
      },
      "source": [
        "install.packages(\"data.table\")\n",
        "library(data.table)"
      ],
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "Installing package into ‘/usr/local/lib/R/site-library’\n",
            "(as ‘lib’ is unspecified)\n",
            "\n",
            "\n",
            "Attaching package: ‘data.table’\n",
            "\n",
            "\n",
            "The following objects are masked from ‘package:reshape2’:\n",
            "\n",
            "    dcast, melt\n",
            "\n",
            "\n",
            "The following object is masked from ‘package:reshape’:\n",
            "\n",
            "    melt\n",
            "\n",
            "\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 255
        },
        "id": "YK_fj4Kw5jMN",
        "outputId": "a56c5110-94a8-4fd6-e328-ee58da66b0a2"
      },
      "source": [
        "DT <- data.table(x = c(\"b\", \"b\", \"b\", \"a\", \"a\"), v = rnorm(5))    # rnorm(n, mean, sd) : 정규분포로부터 난수 생성 / rnorm(n) : 표준정규분포로부터 난수 n개 생성\n",
        "DT"
      ],
      "execution_count": 24,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  x v           \n",
              "1 b -1.539950042\n",
              "2 b -0.928567035\n",
              "3 b -0.294720447\n",
              "4 a -0.005767173\n",
              "5 a  2.404653389"
            ],
            "text/latex": "A data.table: 5 × 2\n\\begin{tabular}{ll}\n x & v\\\\\n <chr> & <dbl>\\\\\n\\hline\n\t b & -1.539950042\\\\\n\t b & -0.928567035\\\\\n\t b & -0.294720447\\\\\n\t a & -0.005767173\\\\\n\t a &  2.404653389\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.table: 5 × 2\n\n| x &lt;chr&gt; | v &lt;dbl&gt; |\n|---|---|\n| b | -1.539950042 |\n| b | -0.928567035 |\n| b | -0.294720447 |\n| a | -0.005767173 |\n| a |  2.404653389 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.table: 5 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>x</th><th scope=col>v</th></tr>\n",
              "\t<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>b</td><td>-1.539950042</td></tr>\n",
              "\t<tr><td>b</td><td>-0.928567035</td></tr>\n",
              "\t<tr><td>b</td><td>-0.294720447</td></tr>\n",
              "\t<tr><td>a</td><td>-0.005767173</td></tr>\n",
              "\t<tr><td>a</td><td> 2.404653389</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "yN2jT8Ge6CMc",
        "outputId": "75f3bc31-962a-420d-a6a9-738e956715a6"
      },
      "source": [
        "str(cars)    # str() : structure. 데이터 구조 확인"
      ],
      "execution_count": 25,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "'data.frame':\t50 obs. of  2 variables:\n",
            " $ speed: num  4 4 7 7 8 9 10 10 10 11 ...\n",
            " $ dist : num  2 10 4 22 16 10 18 26 34 17 ...\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 286
        },
        "id": "_DIL26uC6-uf",
        "outputId": "9907b46f-a289-4d1f-cfd6-73a6b60d1e1b"
      },
      "source": [
        "CARS <- as.data.table(cars)    # data.frame으로 된 'cars' 데이터를 테이블 형식으로 불러오고 CARS에 저장\n",
        "head(CARS)"
      ],
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  speed dist\n",
              "1 4      2  \n",
              "2 4     10  \n",
              "3 7      4  \n",
              "4 7     22  \n",
              "5 8     16  \n",
              "6 9     10  "
            ],
            "text/latex": "A data.table: 6 × 2\n\\begin{tabular}{ll}\n speed & dist\\\\\n <dbl> & <dbl>\\\\\n\\hline\n\t 4 &  2\\\\\n\t 4 & 10\\\\\n\t 7 &  4\\\\\n\t 7 & 22\\\\\n\t 8 & 16\\\\\n\t 9 & 10\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.table: 6 × 2\n\n| speed &lt;dbl&gt; | dist &lt;dbl&gt; |\n|---|---|\n| 4 |  2 |\n| 4 | 10 |\n| 7 |  4 |\n| 7 | 22 |\n| 8 | 16 |\n| 9 | 10 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.table: 6 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>speed</th><th scope=col>dist</th></tr>\n",
              "\t<tr><th scope=col>&lt;dbl&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>4</td><td> 2</td></tr>\n",
              "\t<tr><td>4</td><td>10</td></tr>\n",
              "\t<tr><td>7</td><td> 4</td></tr>\n",
              "\t<tr><td>7</td><td>22</td></tr>\n",
              "\t<tr><td>8</td><td>16</td></tr>\n",
              "\t<tr><td>9</td><td>10</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "X4vIWZys7YFk",
        "outputId": "1e93228e-ea88-4b8b-97d1-dadd3c5ee71e"
      },
      "source": [
        "tables()     # tables() : 모든 데이터 테이블 객체의 목록을 저장한 데이터 테이블을 반환. 크기, key, 용량 확인"
      ],
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   NAME NROW NCOL MB       COLS KEY\n",
            "1: CARS   50    2  0 speed,dist    \n",
            "2:   DT    5    2  0        x,v    \n",
            "Total: 0MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 34
        },
        "id": "6wwWdg2k7f1e",
        "outputId": "1780646c-d18e-4203-e5f3-cf02cdddc9ba"
      },
      "source": [
        "sapply(CARS, class)   # class 데이터 타입 확인"
      ],
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "    speed      dist \n",
              "\"numeric\" \"numeric\" "
            ],
            "text/latex": "\\begin{description*}\n\\item[speed] 'numeric'\n\\item[dist] 'numeric'\n\\end{description*}\n",
            "text/markdown": "speed\n:   'numeric'dist\n:   'numeric'\n\n",
            "text/html": [
              "<style>\n",
              ".dl-inline {width: auto; margin:0; padding: 0}\n",
              ".dl-inline>dt, .dl-inline>dd {float: none; width: auto; display: inline-block}\n",
              ".dl-inline>dt::after {content: \":\\0020\"; padding-right: .5ex}\n",
              ".dl-inline>dt:not(:first-of-type) {padding-left: .5ex}\n",
              "</style><dl class=dl-inline><dt>speed</dt><dd>'numeric'</dd><dt>dist</dt><dd>'numeric'</dd></dl>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 255
        },
        "id": "6UrlvfM1701t",
        "outputId": "7bacbf53-d095-4bc7-88f1-7d58af547c49"
      },
      "source": [
        "# key를 사용한 빠른 데이터 접근\n",
        "# Setkey(데이터 테이블, 정렬할 컬럼)\n",
        "setkey(DT, x)\n",
        "DT"
      ],
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  x v           \n",
              "1 a -0.005767173\n",
              "2 a  2.404653389\n",
              "3 b -1.539950042\n",
              "4 b -0.928567035\n",
              "5 b -0.294720447"
            ],
            "text/latex": "A data.table: 5 × 2\n\\begin{tabular}{ll}\n x & v\\\\\n <chr> & <dbl>\\\\\n\\hline\n\t a & -0.005767173\\\\\n\t a &  2.404653389\\\\\n\t b & -1.539950042\\\\\n\t b & -0.928567035\\\\\n\t b & -0.294720447\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.table: 5 × 2\n\n| x &lt;chr&gt; | v &lt;dbl&gt; |\n|---|---|\n| a | -0.005767173 |\n| a |  2.404653389 |\n| b | -1.539950042 |\n| b | -0.928567035 |\n| b | -0.294720447 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.table: 5 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>x</th><th scope=col>v</th></tr>\n",
              "\t<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>a</td><td>-0.005767173</td></tr>\n",
              "\t<tr><td>a</td><td> 2.404653389</td></tr>\n",
              "\t<tr><td>b</td><td>-1.539950042</td></tr>\n",
              "\t<tr><td>b</td><td>-0.928567035</td></tr>\n",
              "\t<tr><td>b</td><td>-0.294720447</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "sqRf8f-T7_Rc",
        "outputId": "90ad81f5-22b0-471c-cc05-65e51f78a7e1"
      },
      "source": [
        "# DT 테이블에 'x'가 key로 지정되어 있음\n",
        "tables()"
      ],
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "   NAME NROW NCOL MB       COLS KEY\n",
            "1: CARS   50    2  0 speed,dist    \n",
            "2:   DT    5    2  0        x,v   x\n",
            "Total: 0MB\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 192
        },
        "id": "dtD632ys8B6D",
        "outputId": "0ebe9034-0a04-4169-eb76-2d9c7d52b605"
      },
      "source": [
        "DT[\"b\"]                     # 'b'가 들어간 모든 데이터 표시"
      ],
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  x v         \n",
              "1 b -1.5399500\n",
              "2 b -0.9285670\n",
              "3 b -0.2947204"
            ],
            "text/latex": "A data.table: 3 × 2\n\\begin{tabular}{ll}\n x & v\\\\\n <chr> & <dbl>\\\\\n\\hline\n\t b & -1.5399500\\\\\n\t b & -0.9285670\\\\\n\t b & -0.2947204\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.table: 3 × 2\n\n| x &lt;chr&gt; | v &lt;dbl&gt; |\n|---|---|\n| b | -1.5399500 |\n| b | -0.9285670 |\n| b | -0.2947204 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.table: 3 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>x</th><th scope=col>v</th></tr>\n",
              "\t<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>b</td><td>-1.5399500</td></tr>\n",
              "\t<tr><td>b</td><td>-0.9285670</td></tr>\n",
              "\t<tr><td>b</td><td>-0.2947204</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "id": "IhO3OB9p8Jrv",
        "outputId": "02b27586-cf41-4880-f2fe-00a3f8820f8d"
      },
      "source": [
        "DT['b', mult = 'first']    # 'b'가 들어간 첫 번째 결과"
      ],
      "execution_count": 32,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  x v       \n",
              "1 b -1.53995"
            ],
            "text/latex": "A data.table: 1 × 2\n\\begin{tabular}{ll}\n x & v\\\\\n <chr> & <dbl>\\\\\n\\hline\n\t b & -1.53995\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.table: 1 × 2\n\n| x &lt;chr&gt; | v &lt;dbl&gt; |\n|---|---|\n| b | -1.53995 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.table: 1 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>x</th><th scope=col>v</th></tr>\n",
              "\t<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>b</td><td>-1.53995</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 129
        },
        "id": "ac-cjAep8Oji",
        "outputId": "00ba50f6-59b5-4116-f26c-e61d514369c9"
      },
      "source": [
        "DT['b', mult = 'last']    # 'b'가 들어간 마지막 결과"
      ],
      "execution_count": 33,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "  x v         \n",
              "1 b -0.2947204"
            ],
            "text/latex": "A data.table: 1 × 2\n\\begin{tabular}{ll}\n x & v\\\\\n <chr> & <dbl>\\\\\n\\hline\n\t b & -0.2947204\\\\\n\\end{tabular}\n",
            "text/markdown": "\nA data.table: 1 × 2\n\n| x &lt;chr&gt; | v &lt;dbl&gt; |\n|---|---|\n| b | -0.2947204 |\n\n",
            "text/html": [
              "<table class=\"dataframe\">\n",
              "<caption>A data.table: 1 × 2</caption>\n",
              "<thead>\n",
              "\t<tr><th scope=col>x</th><th scope=col>v</th></tr>\n",
              "\t<tr><th scope=col>&lt;chr&gt;</th><th scope=col>&lt;dbl&gt;</th></tr>\n",
              "</thead>\n",
              "<tbody>\n",
              "\t<tr><td>b</td><td>-0.2947204</td></tr>\n",
              "</tbody>\n",
              "</table>\n"
            ]
          },
          "metadata": {}
        }
      ]
    }
  ]
}