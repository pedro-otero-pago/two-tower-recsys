import torch
print("torch:", torch.__version__)
print("cuda disponible:", torch.cuda.is_available())
if torch.cuda.is_available():
    print("gpu:", torch.cuda.get_device_name(0))
    x = torch.randn(1000, 1000, device="cuda")
    print("matmul ok:", (x @ x).shape)