import torch

# Your code here

# Free up GPU memory
torch.cuda.empty_cache()


# alocate 64mb of memory
x = torch.empty(64 * 1024 * 1024, dtype=torch.uint8, device='cuda')
print(x.size())
