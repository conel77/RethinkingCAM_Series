# RethinkingCAM_Series

# Rethinking CAM & weakly supervised object localization

논문 리뷰 파트에서 리뷰하였던 Rethinking CAM을 활용하여 기존의 CAM을 Grad-CAM 과 Grad-CAM++ 로 변형하여 모델을 구축하는 과정을 진행하였습니다.

[논문 코드 구현 Github 링크](https://github.com/won-bae/rethinkingCAM/tree/master)

각 CAM 종류들이 성능이 논문만큼 나왔는지 확인하고, 기존에 존재하지 않았던 Grad-CAM++을 활용하면 성능이 어느정도 나오는지 확인해보아요 !

## Environments
pretrained O
datasets : CUB200-2011

## Grad-CAM & weakly supervised object localization
WSOL 에 변형된 rethinkingCAM이 아닌 기존에 구현되어있던 Grad-CAM 을 활용해서 모델을 변형해보았습니다. 

마지막에서 두번째 layer을 target layer 로 두었을 때 Top-1 Loc 을 확인해보겠습니다.
![](https://velog.velcdn.com/images/conel77/post/2901aca1-4f19-4c9f-af3d-e69b4d3f79d2/image.png)
기존 grad-CAM 논문에서 따로 실행한 Weakly supervised localization 에서 **Top-1 Loc을 보면 100-56.51= 43.49** 정도를 확인할 수 있는데, 

구현해본 결과 **Top-1 Loc은 42.51** 정도, Top-1 Cls 는 77.91 을 확인할 수 있었습니다.

![](https://velog.velcdn.com/images/conel77/post/9e60c273-6b97-4acf-a5fa-911c570dccc4/image.png)
데이터셋 종류가 논문에서는 ILSVRC-15 이며, 제가 진행한 데이터셋은 CUB200-2011 이였으므로 이부분에서 차이가 발생하였다고 판단하였습니다.

## Grad-CAM++ & weakly supervised object localization

이번에는 WSOL 에서 Grad-CAM++을 활용하여 진행해보았습니다.

Grad-CAM 과 Grad-CAM++ 의 경우, 논문에서 제시한 [CAM 모델들](https://github.com/jacobgil/pytorch-grad-cam/tree/master) 을 활용하여 진행하였습니다.

![](https://velog.velcdn.com/images/conel77/post/39ed5b23-94a8-49a2-aceb-8fe0de172def/image.png)

구현해본 결과 **Top-1 Cls 의 경우에는 77.91**, Top-1 Loc은 57.34 정도로 매우 잘 나오는 것을 확인할 수 있네요 !
