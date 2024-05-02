# [EN] BPIA_HAND Addon Introduction

**Notion Page**: [BPIA](https://yc2313.notion.site/BPIA-9d51d155828a4e2883c20509bc62116f?pvs=4)

**Creator**: 이승훈 / Lee Seunghun

**Instagram**: https://www.instagram.com/dodand3d

**Contact**: [lsh678902@gmail.com](mailto:lsh678902@gmail.com)

#### Introduction:

**BPIA_HAND**is an addon designed to simplify the implementation of real-time interaction using hands within Blender.

#### Key Features:

1. **Real-Time Interaction**: Streams external data into Blender in real-time using the UDP protocol, providing an interactive experience.
2. **Ease of Use**: Features a user-friendly UI that allows for interaction without the need for complex setup processes.
3. **Customization**: The nodes are neatly organized for easy reconfiguration.

**BPIA** is an open-source project and is freely available for use by anyone including students, artists, and developers. It can be used for both commercial and non-commercial purposes. If you use this addon in your projects, please share your experiences. Your valuable feedback will greatly assist in improving this addon. You can contact me via email or Instagram DM or share your experiences in the upcoming community.

# [KO] BPIA_HAND 애드온 소개

**Notion 페이지**: [BPIA](https://yc2313.notion.site/BPIA-9d51d155828a4e2883c20509bc62116f?pvs=4)

**만든이**: 이승훈 / Lee Seunghun

**인스타**: https://www.instagram.com/dodand3d

**연락처**: [lsh678902@gmail.com](mailto:lsh678902@gmail.com)

#### 소개:

**BPIA_HAND**는 블렌더에서 손을 이용한 실시간 인터렉션을 간편하게 구현하기 위한 애드온입니다.

#### 주요 기능:

1. **실시간 인터랙션**: UDP 프로토콜을 사용하여 외부 데이터를 블렌더로 실시간으로 스트리밍하며, 인터랙티브 경험을 제공합니다.
2. **간편한 조작**: 사용자 친화적인 UI를 통해 복잡한 설정 절차 없이 인터랙션을 시작할 수 있습니다.
3. **커스터마이징**: 노드를 깔끔하게 정리해 놓아, 재구성하기 쉽도록 만들었습니다.

**BPIA**는 오픈 소스 프로젝트로서, 누구나 무료로 사용할 수 있습니다. 학생, 예술가, 개발자를 포함한 모든 사용자가 상업적 목적을 포함하여 자유롭게 사용할 수 있으며, 사용 사례를 공유해주시기만 하면 됩니다. 프로젝트에서 사용하셨다면, 그 이용사례을 간단하게 정리해서 공유해주시면 감사하겠습니다. 여러분의 소중한 피드백은 이 애드온을 더욱 개선하는 데 큰 도움이 됩니다. 제 메일이나 인스타 DM으로 연락을 주시거나, 이후에 만들어질 커뮤니티에서 공유해주세요.

# Install

![BPIA설명서-001 (1)](https://github.com/engmung/BPIA/assets/122682380/a46fad35-2968-42b5-ae7e-267352b1b953)
![BPIA설명서-002](https://github.com/engmung/BPIA/assets/122682380/ec761caa-d599-45b1-9908-6bc3c7a09af2)
![003](https://github.com/engmung/BPIA/assets/122682380/6d85c2cf-50d5-4a0d-a717-3773801910e6)
![004![005](https://github.com/engmung/BPIA/assets/122682380/25aad903-dd8d-4726-bf63-c20eee1d01cb)
](https://github.com/engmung/BPIA/assets/122682380/ac5baa56-8f30-44c4-9130-8bb45b9ad236)
![006](https://github.com/engmung/BPIA/assets/122682380/c4184496-20bd-4fff-b7ec-43380fc034be)
![007](https://github.com/engmung/BPIA/assets/122682380/aaa5ce8c-27b3-4033-aaf8-4591ad1039dd)
![008](https://github.com/engmung/BPIA/assets/122682380/59df67e8-6bba-4e95-a6f9-4fcf86dd9f02)
![009](https://github.com/engmung/BPIA/assets/122682380/ceaaf269-b0ed-4f33-b9d4-74306c1d1d54)









## Installation method old version
### YouTube Tutorial

- in window,  
<a href="https://youtu.be/wLlfYv4ct08" target="_blank">
  <img src="http://img.youtube.com/vi/wLlfYv4ct08/0.jpg" alt="YouTube Video" width="800"/>
</a>

- in mac,  
<a href="https://youtu.be/p9ihn507yKE" target="_blank">
  <img src="http://img.youtube.com/vi/p9ihn507yKE/0.jpg" alt="YouTube Video" width="800"/>
</a>

### Installation Steps
1. First, download Python 3.11 version along with setting up PATH.
   <img width="800" alt="스크린샷 2024-01-29 085752" src="https://github.com/engmung/BPIA/assets/122682380/506ac684-ce20-43be-9fd7-5577e927b255">
   <img width="800" alt="스크린샷 2024-01-29 091737" src="https://github.com/engmung/BPIA/assets/122682380/aabe2fc4-2b4a-45a4-ae15-e284d61fb7de">

2. Install the downloaded zip file and extract it.

3. Install the required library.
   - In Windows, run the `install.bat` file.
   
   - In Mac:
     1. Select the BPIA-master folder in Finder and press `command+option+c` to copy the file path.
     2. Use Spotlight to open the terminal.
     3. Type `cd (paste your path)` in the terminal and press Enter. e.g., `cd /path/to/directory`.
     4. Type `pip3 install -r requirements.txt` in the terminal and press Enter.
    
4. Open the blender and run the script inside. Then the Start Intercept button to run it.
   - In Mac:
     1. Select the BPIA-master folder in Finder and press `command+option+c` to copy the file path.
     2. Use Spotlight to open the terminal.
     3. Type `cd (paste your path)` in the terminal and press Enter. e.g., `cd /path/to/directory`.
     4. Type `python3 udp.py` in the terminal and press Enter.
   <img width="800" alt="11111140" src="https://github.com/engmung/BPIA/assets/122682380/c4adddf5-642e-4746-b1e2-64342b12eea0">

## Usage
### Youtube Link..!
<a href="https://youtu.be/7j2dAO9sBbY" target="_blank">
  <img src="http://img.youtube.com/vi/7j2dAO9sBbY/0.jpg" alt="YouTube Video" width="800" />
</a>

## Feedback
I value your feedback and experiences with **BPIA**. If you have used this addon in your projects, please share your use cases, thoughts, or any issues you encountered. Your input is crucial for us to improve and enhance **BPIA**. 

Send your feedback and use cases to: [lsh678902@gmail.com](mailto:lsh678902@gmail.com)

I look forward to your creative projects and how **BPIA** has helped in transforming them into more colorful and vibrant creations.

