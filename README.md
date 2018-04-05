# PASCAL VOC DATA PARSING

\[한국어]  
  PASCAL VOC 데이터 셋은 **Annotaions** 와 **JPEGimage**로 나누어져 있습니다.  
**Annotation**은 **XML** 명세로 되어있으며,
각 물체의 클래스와 바운딩 박스 좌표로 이루어져 있습니다.  
분류기 모델을 학습시키기 위해서는 각 바운딩 박스 안에 있는 사진과 레이블을 가져와야 합니다.  

  본 프로젝트는 PASCAL VOC 데이터를 BeautifulSoup 과 opencv 라이브러리를 이용하여 가공합니다.
여러 이미지가 들어있는 데이터 셋에서 각 물체를 분리하여 224 x 224 크기로 변환을 하여 저장합니다. 
레이블은 [20 x 1] one hot encoding 으로 텍스트 파일로 저장합니다.  

\[English]  
  PASCAL VOC data set consist of **"Annotations"** and **"JPEGimage"**. Annotations are written in **XML** format which contain each object class and bounding box coordinates. You have to bring each bounding box and its photo and label in order to train the network.  

  This project processes on PASCAL VOC data with BeautifulSoup and opencv libs. Each photo contains many objects. It detaches each object, resizes to 224 x 224 and save to local storage. Label is saved in \*.txt with [ 20 x 1 ] one hot encoding. 

## 설치 방법

적당한 폴더에 PASCAL VOC 데이터를 받습니다.  
데이터는 다음 미러 사이트에서 내려받을 수 있습니다.  
> https://pjreddie.com/projects/pascal-voc-dataset-mirror/

Download PASCAL VOC dataset to proper folder.
You can get it from as below.
> https://pjreddie.com/projects/pascal-voc-dataset-mirror/
 
## 사용 예제
터미널 창에서 다음과 같이 실행하세요.
```sh
python3 voc_dataset_parsing_edited.py
```
## 개발 환경 설정
Python 3.x 버젼과, BeautifulSoup4, Opencv가 필요합니다.
```sh
pip3 install BeautifulSoup4
pip3 install opencv-python
```
 
## 업데이트 내역

* 0.0.1
    * 작업 진행 중
* 0.0.2
    * Add english document
 
## 정보

김동현 – seru_s@me.com

## 라이센스
MIT © henniekim

<!-- Markdown link & img dfn's -->
[npm-image]: https://img.shields.io/npm/v/datadog-metrics.svg?style=flat-square
[npm-url]: https://npmjs.org/package/datadog-metrics
[npm-downloads]: https://img.shields.io/npm/dm/datadog-metrics.svg?style=flat-square
[travis-image]: https://img.shields.io/travis/dbader/node-datadog-metrics/master.svg?style=flat-square
[travis-url]: https://travis-ci.org/dbader/node-datadog-metrics
[wiki]: https://github.com/yourname/yourproject/wiki
