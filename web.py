{
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/yscho0000/ys/blob/main/web.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 6,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iibz0fNer4r-",
        "outputId": "70db57ef-7f0b-4990-fdd3-6b9f41f1060f"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "bash: cannot set terminal process group (525): Inappropriate ioctl for device\n",
            "bash: no job control in this shell\n",
            "\u001b[?2004h\u001b[?2004l\n",
            "\u001b[?2004h\u001b[?2004l\n",
            "\u001b[?2004h\u001b[01;34m/content\u001b[00m# ^C\n"
          ]
        }
      ],
      "source": [
        "!bash"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 4,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "id": "5CYoWqKbnJZH",
        "outputId": "b7a3f487-05d4-47cb-ea57-33e6f349bc12"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting streamlit\n",
            "  Downloading streamlit-1.45.0-py3-none-any.whl.metadata (8.9 kB)\n",
            "Requirement already satisfied: altair<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.0)\n",
            "Requirement already satisfied: blinker<2,>=1.5.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (1.9.0)\n",
            "Requirement already satisfied: cachetools<6,>=4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.5.2)\n",
            "Requirement already satisfied: click<9,>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (8.1.8)\n",
            "Requirement already satisfied: numpy<3,>=1.23 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.0.2)\n",
            "Requirement already satisfied: packaging<25,>=20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (24.2)\n",
            "Requirement already satisfied: pandas<3,>=1.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.2.2)\n",
            "Requirement already satisfied: pillow<12,>=7.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (11.2.1)\n",
            "Requirement already satisfied: protobuf<7,>=3.20 in /usr/local/lib/python3.11/dist-packages (from streamlit) (5.29.4)\n",
            "Requirement already satisfied: pyarrow>=7.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (18.1.0)\n",
            "Requirement already satisfied: requests<3,>=2.27 in /usr/local/lib/python3.11/dist-packages (from streamlit) (2.32.3)\n",
            "Requirement already satisfied: tenacity<10,>=8.1.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (9.1.2)\n",
            "Requirement already satisfied: toml<2,>=0.10.1 in /usr/local/lib/python3.11/dist-packages (from streamlit) (0.10.2)\n",
            "Requirement already satisfied: typing-extensions<5,>=4.4.0 in /usr/local/lib/python3.11/dist-packages (from streamlit) (4.13.2)\n",
            "Collecting watchdog<7,>=2.1.5 (from streamlit)\n",
            "  Downloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl.metadata (44 kB)\n",
            "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m44.3/44.3 kB\u001b[0m \u001b[31m2.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: gitpython!=3.1.19,<4,>=3.0.7 in /usr/local/lib/python3.11/dist-packages (from streamlit) (3.1.44)\n",
            "Collecting pydeck<1,>=0.8.0b4 (from streamlit)\n",
            "  Downloading pydeck-0.9.1-py2.py3-none-any.whl.metadata (4.1 kB)\n",
            "Requirement already satisfied: tornado<7,>=6.0.3 in /usr/local/lib/python3.11/dist-packages (from streamlit) (6.4.2)\n",
            "Requirement already satisfied: jinja2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (3.1.6)\n",
            "Requirement already satisfied: jsonschema>=3.0 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (4.23.0)\n",
            "Requirement already satisfied: narwhals>=1.14.2 in /usr/local/lib/python3.11/dist-packages (from altair<6,>=4.0->streamlit) (1.37.1)\n",
            "Requirement already satisfied: gitdb<5,>=4.0.1 in /usr/local/lib/python3.11/dist-packages (from gitpython!=3.1.19,<4,>=3.0.7->streamlit) (4.0.12)\n",
            "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2.9.0.post0)\n",
            "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas<3,>=1.4.0->streamlit) (2025.2)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.4.1)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2.4.0)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests<3,>=2.27->streamlit) (2025.4.26)\n",
            "Requirement already satisfied: smmap<6,>=3.0.1 in /usr/local/lib/python3.11/dist-packages (from gitdb<5,>=4.0.1->gitpython!=3.1.19,<4,>=3.0.7->streamlit) (5.0.2)\n",
            "Requirement already satisfied: MarkupSafe>=2.0 in /usr/local/lib/python3.11/dist-packages (from jinja2->altair<6,>=4.0->streamlit) (3.0.2)\n",
            "Requirement already satisfied: attrs>=22.2.0 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (25.3.0)\n",
            "Requirement already satisfied: jsonschema-specifications>=2023.03.6 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (2025.4.1)\n",
            "Requirement already satisfied: referencing>=0.28.4 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.36.2)\n",
            "Requirement already satisfied: rpds-py>=0.7.1 in /usr/local/lib/python3.11/dist-packages (from jsonschema>=3.0->altair<6,>=4.0->streamlit) (0.24.0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.11/dist-packages (from python-dateutil>=2.8.2->pandas<3,>=1.4.0->streamlit) (1.17.0)\n",
            "Downloading streamlit-1.45.0-py3-none-any.whl (9.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m9.9/9.9 MB\u001b[0m \u001b[31m75.7 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading pydeck-0.9.1-py2.py3-none-any.whl (6.9 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.9/6.9 MB\u001b[0m \u001b[31m109.4 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading watchdog-6.0.0-py3-none-manylinux2014_x86_64.whl (79 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m79.1/79.1 kB\u001b[0m \u001b[31m7.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: watchdog, pydeck, streamlit\n",
            "Successfully installed pydeck-0.9.1 streamlit-1.45.0 watchdog-6.0.0\n"
          ]
        }
      ],
      "source": [
        "!pip install streamlit"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 7,
      "metadata": {
        "id": "n7egVh7VmjLp",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "collapsed": true,
        "outputId": "4f2a27ef-be7e-4a23-db2b-5462d9143676"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2025-05-04 08:12:05.218 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.223 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.224 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.226 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.227 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.228 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.229 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.230 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.231 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.232 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.233 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.233 The `use_column_width` parameter has been deprecated and will be removed in a future release. Please utilize the `use_container_width` parameter instead.\n",
            "2025-05-04 08:12:05.234 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.235 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.236 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.237 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.237 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.238 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.239 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.240 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.240 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.241 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.242 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.242 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.243 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.244 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.245 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.245 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.246 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.246 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.247 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.248 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.248 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.249 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.249 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
            "2025-05-04 08:12:05.250 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
          ]
        }
      ],
      "source": [
        "import streamlit as st\n",
        "\n",
        "st.set_page_config(layout=\"wide\")\n",
        "\n",
        "# 학원 정보 (추후 데이터베이스 또는 설정 파일에서 불러올 수 있습니다.)\n",
        "academy_name = \"우리 동네 최고 학원\"\n",
        "academy_slogan = \"꿈을 향한 첫걸음, 저희 학원이 함께합니다.\"\n",
        "academy_description = \"\"\"\n",
        "저희 학원은 [학원의 특징 및 강점]을 바탕으로 최고의 교육 서비스를 제공합니다.\n",
        "[다양한 강좌/프로그램]을 통해 여러분의 성장을 지원하며, [차별화된 시스템]으로 학습 효과를 극대화합니다.\n",
        "\"\"\"\n",
        "courses = {\n",
        "    \"기초 영어 회화\": {\"대상\": \"초급\", \"시간\": \"매주 화/목 19:00-21:00\", \"수강료\": \"25만원\", \"소개\": \"영어를 처음 시작하는 분들을 위한 맞춤 강좌입니다.\"},\n",
        "    \"토익 점수 향상\": {\"대상\": \"중급\", \"시간\": \"매주 월/수 14:00-16:00\", \"수강료\": \"30만원\", \"소개\": \"단기간에 토익 목표 점수를 달성하도록 돕는 집중 강좌입니다.\"},\n",
        "    \"코딩 기초 부트캠프\": {\"대상\": \"초보\", \"시간\": \"매주 주말 10:00-17:00\", \"수강료\": \"45만원\", \"소개\": \"코딩의 기초를 탄탄하게 다지는 단기 집중 과정입니다.\"},\n",
        "}\n",
        "\n",
        "# 메인 페이지\n",
        "def main_page():\n",
        "    st.title(academy_name)\n",
        "    st.subheader(academy_slogan)\n",
        "    st.markdown(academy_description)\n",
        "    st.image(\"https://via.placeholder.com/800x300\", caption=\"학원 전경 (임시 이미지)\", use_column_width=True) # 실제 학원 이미지로 변경\n",
        "\n",
        "    st.subheader(\"주요 메뉴\")\n",
        "    col1, col2, col3 = st.columns(3)\n",
        "    with col1:\n",
        "        if st.button(\"강좌/프로그램\"):\n",
        "            st.session_state.page = \"courses\"\n",
        "            st.rerun()\n",
        "    with col2:\n",
        "        if st.button(\"예약 문의\"):\n",
        "            st.session_state.page = \"reservation\"\n",
        "            st.rerun()\n",
        "    with col3:\n",
        "        if st.button(\"자주 묻는 질문\"):\n",
        "            st.session_state.page = \"faq\"\n",
        "            st.rerun()\n",
        "\n",
        "# 강좌/프로그램 페이지\n",
        "def courses_page():\n",
        "    st.title(\"강좌 및 프로그램\")\n",
        "    for course, details in courses.items():\n",
        "        with st.expander(f\"**{course}**\"):\n",
        "            st.write(f\"**대상:** {details['대상']}\")\n",
        "            st.write(f\"**시간:** {details['시간']}\")\n",
        "            st.write(f\"**수강료:** {details['수강료']}\")\n",
        "            st.write(f\"**소개:** {details['소개']}\")\n",
        "            if st.button(f\"{course} 수강 신청\"):\n",
        "                st.success(f\"{course} 수강 신청이 완료되었습니다. (추후 결제 시스템 연동 필요)\") # 실제 예약 처리 로직 필요\n",
        "\n",
        "    if st.button(\"메인 페이지로 돌아가기\"):\n",
        "        st.session_state.page = \"main\"\n",
        "        st.rerun()\n",
        "\n",
        "# 예약 페이지\n",
        "def reservation_page():\n",
        "    st.title(\"예약 문의\")\n",
        "    st.subheader(\"상담 예약\")\n",
        "    with st.form(\"consultation_form\"):\n",
        "        name = st.text_input(\"이름\")\n",
        "        phone = st.text_input(\"연락처\")\n",
        "        email = st.text_input(\"이메일 (선택)\")\n",
        "        preferred_time = st.selectbox(\"상담 희망 시간\", [\"평일 오전\", \"평일 오후\", \"주말\"])\n",
        "        submitted = st.form_submit_button(\"상담 예약 신청\")\n",
        "        if submitted:\n",
        "            st.success(f\"{name}님, 상담 예약이 완료되었습니다. {preferred_time}에 연락드리겠습니다.\") # 실제 예약 처리 로직 필요\n",
        "\n",
        "    st.subheader(\"프로그램 예약\")\n",
        "    selected_course = st.selectbox(\"예약할 프로그램\", list(courses.keys()))\n",
        "    with st.form(\"program_reservation_form\"):\n",
        "        name_program = st.text_input(\"이름\")\n",
        "        phone_program = st.text_input(\"연락처\")\n",
        "        submitted_program = st.form_submit_button(f\"{selected_course} 예약 신청\")\n",
        "        if submitted_program:\n",
        "            st.success(f\"{name_program}님, {selected_course} 예약이 완료되었습니다. (추후 결제 시스템 연동 필요)\") # 실제 예약 처리 로직 필요\n",
        "\n",
        "    if st.button(\"메인 페이지로 돌아가기\"):\n",
        "        st.session_state.page = \"main\"\n",
        "        st.rerun()\n",
        "\n",
        "# 자주 묻는 질문 페이지\n",
        "def faq_page():\n",
        "    st.title(\"자주 묻는 질문\")\n",
        "    faq = {\n",
        "        \"수강료는 어떻게 되나요?\": \"각 강좌별 수강료는 상세 안내 페이지에서 확인하실 수 있습니다.\",\n",
        "        \"환불 규정은 어떻게 되나요?\": \"학원 내규에 따라 환불 규정이 적용됩니다. 자세한 내용은 문의해 주세요.\",\n",
        "        \"주차는 가능한가요?\": \"네, 학원 건물 내 주차장을 이용하실 수 있습니다.\",\n",
        "        \"수업 시간 변경이 가능한가요?\": \"개별적인 수업 시간 변경은 어렵습니다.\",\n",
        "    }\n",
        "    for question, answer in faq.items():\n",
        "        with st.expander(question):\n",
        "            st.write(answer)\n",
        "\n",
        "    if st.button(\"메인 페이지로 돌아가기\"):\n",
        "        st.session_state.page = \"main\"\n",
        "        st.rerun()\n",
        "\n",
        "# 페이지 상태 관리\n",
        "if \"page\" not in st.session_state:\n",
        "    st.session_state.page = \"main\"\n",
        "\n",
        "if st.session_state.page == \"main\":\n",
        "    main_page()\n",
        "elif st.session_state.page == \"courses\":\n",
        "    courses_page()\n",
        "elif st.session_state.page == \"reservation\":\n",
        "    reservation_page()\n",
        "elif st.session_state.page == \"faq\":\n",
        "    faq_page()\n"
      ]
    }
  ],
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyNQQioguQwKUwwY6Al4n1wO",
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