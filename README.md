
# BPIA Addon Documentation

- [Introduction](#introduction)
  - [EN](#en-bpia-addon-introduction)
  - [KO](#ko-bpia-애드온-소개)
- [Install](#install)
  - [YouTube Tutorial](#youtube-tutorial)
  - [Installation Steps](#installation-steps)
- [Usage](#usage)
- [Feedback](#feedback)

## Introduction

### [EN] BPIA Addon Introduction

**Notion Page**: [BPIA](https://yc2313.notion.site/BPIA-9d51d155828a4e2883c20509bc62116f?pvs=4)

**Author**: 이승훈 / Lee Seunghun

**Contact**: [lsh678902@gmail.com](mailto:lsh678902@gmail.com)

#### Introduction:

**BPIA** is a robust tool tailored for students and artists, aimed at amplifying creativity via real-time interactions. This addon provides an intuitive interface within Blender, enabling the real-time manipulation of simulation nodes. With ease, users can incorporate interactive elements into their projects, enhancing the originality and dynamism of their art pieces or educational materials.

#### Key Features:

1. **Real-Time Interaction**: Seamlessly streams external data into Blender using the UDP protocol, offering a dynamic and interactive experience.
2. **Ease of Use**: The user-friendly UI allows for immediate interaction without the hassle of complex setup processes.
3. **Reset Functionality**: Effortlessly reset simulation nodes when they cease to function as expected, ensuring continuity in your creative process.

**BPIA** stands as an open-source project, freely accessible to everyone. Whether you're a student, artist, or developer, you can utilize this tool for commercial or non-commercial purposes. We encourage you to share your use cases with us. By sharing your experience with **BPIA** in your projects, you contribute to the enhancement of this tool and the growth of our community.

**Share Your Experience**: If **BPIA** has been a part of your project, kindly send your use cases to [lsh678902@gmail.com](mailto:lsh678902@gmail.com). 

Elevate your creativity with **BPIA**! We are excited to witness the transformation of your projects into more colorful and vibrant masterpieces.

---

### [KO] BPIA 애드온 소개

**Notion 페이지**: [BPIA](https://yc2313.notion.site/BPIA-9d51d155828a4e2883c20509bc62116f?pvs=4)

**저자**: 이승훈 / Lee Seunghun

**연락처**: [lsh678902@gmail.com](mailto:lsh678902@gmail.com)

#### 소개:

**BPIA**는 실시간 인터랙션 구현 에드온입니다. 카메라를 이용한 모션캡쳐로 간단한, 이동 인터렉션을 구현 하도록 도와줍니다. 

#### 주요 기능:

1. **실시간 인터랙션**: UDP 프로토콜을 사용하여 외부 데이터를 블렌더로 실시간으로 스트리밍하며, 인터랙티브 경험을 제공합니다.
2. **간편한 조작**: 사용자 친화적인 UI를 통해 복잡한 설정 절차 없이 즉시 인터랙션을 시작할 수 있습니다.
3. **재설정 기능**: 시뮬레이션 노드가 예상치 못하게 작동을 멈출 때 간편하게 재설정하여 문제를 해결할 수 있습니다.

**BPIA**는 오픈 소스 프로젝트로서, 누구나 무료로 사용할 수 있습니다. 학생, 예술가, 개발자를 포함한 모든 사용자가 상업적 목적을 포함하여 자유롭게 사용할 수 있으며, 사용 사례를 공유해주시기만 하면 됩니다. 여러분의 프로젝트에서 **BPIA**를 사용하셨다면, 그 경험을 간단하게 정리해서 공유해주시기 바랍니다. 여러분의 소중한 피드백은 이 애드온을 더욱 개선하는 데 큰 도움이 됩니다.

**사용료(공유해줘요)**: 프로젝트에서 **BPIA**를 사용하셨다면, 사용 사례를 다음 주소로 보내주세요: [lsh678902@gmail.com](mailto:lsh678902@gmail.com)

## Install

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
    
4. Open the blender and run the script inside. Then click BPIA Start and double-click the Stop Intercept button to run it.
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

