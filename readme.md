# MCSL Wi-Fi Push

### Intro

- 같은 Wi-Fi에 접속한 기기 확인 (MAC Address 이용)

- Python Scapy
  
    - [Github](https://github.com/secdev/scapy)
    - [Docs](https://scapy.readthedocs.io/en/latest/introduction.html)
  
### Usage

OS : Windows 10

#### 설치
  <code>git clone https://github.com/ruthetum/mcsl-push.git</code>

  <code> cd mcsl-push</code>

#### 가상환경 설치
  <code>pip install virtualenv</code>
  
  <code>pip install virtualenvwrapper-win</code>

#### 가상환경 생성 및 활성화
  <code>virtualenv venv</code>
  
  <code>.\venv\Scripts\activate</code>

#### 모듈 설치
  <code>pip install -r requirements.txt</code>

#### 실행
  <code>python main.py</code>

#### 유의
- .env 파일에 Wi-Fi 라우터 주소와 접속 확인할 디바이스의 MAC 주소 작성
- winpcap 관련 error 발생 시 [winpcap](https://www.winpcap.org/install/) 설치
- **관리자 권한**(system32 or Sudo)으로 실행

### Result
![image](https://user-images.githubusercontent.com/59307414/110150401-947add80-7e22-11eb-8aee-fb4f247ad7a3.png)

### Reference
[Youtebe 빵형의 개발도상국](https://www.youtube.com/watch?v=a0t93T2TJLw)