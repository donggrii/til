import torch
from torchvision import datasets
from torchvision.transforms import ToTensor, Lambda

# ToTensor() : PIL Image 형태의 feature에서 normalized tensor 형태의 feature로 만들어주는 함수
#              1. PIL Image 또는 NumPy ndarray를 Float Tensor로 변환 ("H x W x C" -> "C x H x W")
#              2. 이미지 픽셀의 크기 값 [0, 255] -> [0., 1.]로 scaling
# Lambda() : Integer label을 one-hot encoding된 tensor 형태의 label로 만들어주기 위한 사용자 정의 함수
#            -> label 개수인 크기 10의 zero tensor를 만들고 scatter_()를 호출하여 integer label인 y에 해당하는 index에 1을 할당
ds = datasets.FashionMNIST(
    root = "data",
    train = True,
    download = True,
    transform = ToTensor(),
    target_transform = Lambda(lambda y: torch.zeros(10, dtype = torch.float).scatter_(dim = 0, index = torch.tensor(y), value = 1))
)