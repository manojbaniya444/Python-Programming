"""
Contains functionality for creating PyTorch DataLoaders for 
image classification data.
"""
import os
from torchvision import datasets, transforms
from torch.utils.data import DataLoader

NUM_WORKERS = os.cpu_count()

def create_dataloader(
    train_dir: str,
    test_dir: str,
    transform: transforms.Compose,
    batch_size: int,
    num_workers: int=NUM_WORKERS
):
  """
  create train and test dataloader:
  Takes train and test dir path and turns them into Pytorch dataset and dataloader.

  Args:
    train_dir: train directory
    test_dir: test directory
    transform: torchvision transform to perform on train and test dataset
    batch_size: batch_size
    num_workers: number of workers in dataloader
  
  Returns:
    A tuple of (train_dataloader, test_dataloader, class_name)
    Example usage:
      train_dataloader, test_dataloader, class_names = create_dataloader(
        train_dir=path/to/train_dir,
        test_dir=path/to/test_dir,
        transform=some_transform,
        batch_size=32,
        num_workers=4
      )
  """
  train_data = datasets.ImageFolder(train_dir, transform=transform)
  test_data = datasets.ImageFolder(test_dir, transform=transform)
  class_names = train_data.classes

  train_dataloader = DataLoader(
      train_data,
      batch_size=batch_size,
      shuffle=True,
      num_workers=num_workers
  )
  test_dataloader = DataLoader(
      test_data,
      batch_size=batch_size,
      shuffle=False,
      num_workers=num_workers
  )

  return train_dataloader, test_dataloader, class_names
