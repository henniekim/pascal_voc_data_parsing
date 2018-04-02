# PASCAL VOC DATA PARSING
> 이 프로젝트는 PASCAL VOC 데이터를 분류기 모델 학습에 적합하게 가공하기 위해 만들어졌습니다.

  PASCAL VOC 데이터 셋은 Annotaions 와 JPEGimage로 나누어져 있습니다.  
Annotation은 XML 명세로 되어있으며,
각 물체의 클래스와 바운딩 박스 좌표로 이루어져 있습니다.  
분류기 모델을 학습시키기 위해서는 각 바운딩 박스 안에 있는 사진과 레이블을 가져와야 합니다.  

  본 프로젝트는 PASCAL VOC 데이터를 BeautifulSoup 과 opencv 라이브러리를 이용합니다.  
여러 이미지가 들어있는 데이터 셋에서 각 물체를 분리하여 224 x 224 크기로 변환을 하여 저장합니다.  
레이블은 [20 x 1] one hot encoding 으로 텍스트 파일로 저장합니다.  

## 설치 방법

적당한 폴더에 PASCAL VOC 데이터를 받습니다.  
데이터는 다음 미러 사이트에서 내려받을 수 있습니다.  
> https://pjreddie.com/projects/pascal-voc-dataset-mirror/
 
## 사용 예제
터미널 창에서 다음과 같이 실행하세요.
```sh
python3 voc_dataset_parsing_edited.py
```
## 개발 환경 설정
 
모든 개발 의존성 설치 방법과 자동 테스트 슈트 실행 방법을 운영체제 별로 작성합니다.
 
```sh
pip3 install BeautifulSoup4 --user
```
 
## 업데이트 내역

* 0.0.1
    * 작업 진행 중
 
## 정보

김동현 – seru_s@me.com


<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
