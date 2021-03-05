# MCSL Wi-Fi Push

## Intro
- 같은 Wi-Fi에 접속한 기기 확인 (MAC Address 이용)

- Python Scapy
  
    - [Github](https://github.com/secdev/scapy)
    - [Docs](https://scapy.readthedocs.io/en/latest/introduction.html)
  

## Usage

OS : Windows 10

### 설치
    git clone https://github.com/ruthetum/mcsl-push.git
    cd mcsl-push


### 가상환경 설치
    pip install virtualenv
    pip install virtualenvwrapper-win


### 가상환경 생성 및 활성화
    virtualenv venv
    .\venv\Scripts\activate


### 모듈 설치
    pip install -r requirements.txt


### 실행
    python main.py


### 유의사항
- .env 파일에 Wi-Fi 라우터 주소와 접속 확인할 디바이스의 MAC 주소 작성
- winpcap 관련 error 발생 시 [winpcap](https://www.winpcap.org/install/) 설치
- **관리자 권한**(system32 or Sudo)으로 실행


## Result
![image](https://user-images.githubusercontent.com/59307414/110150401-947add80-7e22-11eb-8aee-fb4f247ad7a3.png)


## Reference
[![Video Label](https://i.ytimg.com/an_webp/a0t93T2TJLw/mqdefault_6s.webp?du=3000&sqp=CNyhiYIG&rs=AOn4CLAiWj44Odhbnt4Uk0ngU-rOr87ekQ)](https://www.youtube.com/watch?v=a0t93T2TJLw)

[Youtube 빵형의 개발도상국](https://www.youtube.com/channel/UC9PB9nKYqKEx_N3KM-JVTpg)