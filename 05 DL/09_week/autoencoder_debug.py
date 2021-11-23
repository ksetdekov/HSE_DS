# %%
import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
from torch.utils.data import TensorDataset, DataLoader
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

import warnings
warnings.filterwarnings('ignore')


# %%
from sklearn.datasets import get_data_home
import sklearn
from torchsummary import summary

print(get_data_home())
sklearn.__version__

# %%
from sklearn.datasets import get_data_home
print(get_data_home())

# %%
from sklearn.datasets import fetch_lfw_people

lfw_people = fetch_lfw_people(data_home = '.', min_faces_per_person=0, resize=0.5, color=True,
                              slice_=(slice(94, 190, None), slice(78, 174, None)), download_if_missing=True)

# %%
from sklearn.model_selection import train_test_split

X = lfw_people.images
X = np.moveaxis(X, 3, 1)
IMG_SHAPE = X.shape[1:]

X = X.astype('float32') / 255.0
X_train, X_test = train_test_split(X, test_size=0.1, random_state=42)

# %%
dimenstion = X_train.shape[1:]

# %%
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(DEVICE)
EPOCHS = 40

# %%
from IPython import display  # выводить график обучения в онлайн режиме
from tqdm.auto import tqdm
import os

# %%
# Train your autoencoder
# Visualize progress in reconstruction and loss decay

def train(model, train_loader, val_loader, device=DEVICE, epochs=EPOCHS, path=''):

    train_loss = torch.tensor([0,0])
    val_loss = torch.tensor([0,0])
    train_loss_epoch = torch.tensor([0,0])
    val_loss_epoch = torch.tensor([0,0])

    for epoch in tqdm(range(epochs)):
        model.train()
        for X in train_loader:
            batch = X[0].to(device)  # [0] is needed due to X being a list
            reconstruction, _ = model(batch)
            loss = criterion(reconstruction, batch)
            loss.backward()

            optimizer.step()
            optimizer.zero_grad()

            train_loss.append(loss.detach().cpu().numpy())
        
        model.eval()
        with torch.no_grad():
            for X in val_loader:
                batch = X[0].to(device)  # [0] is needed due to X being a list
                reconstruction, _ = model(batch)

                loss = criterion(reconstruction, batch)
                val_loss.append(loss.cpu().numpy())

        train_loss_epoch.append(np.mean(train_loss))
        val_loss_epoch.append(np.mean(val_loss))

        if epoch % 5 == 0:
            print(
                f"After {epoch} epochs, training loss: {train_loss_epoch[-1]:.6f};   "
                f"val loss: {val_loss_epoch[-1]:.6f}")

        os.makedirs(path, exist_ok=True)
        torch.save(model.state_dict(), path + '/checkpoint.pt')

        train_loss_epoch = train_loss_epoch.to(device)
        val_loss_epoch = val_loss_epoch.to(device)

    return model, train_loss_epoch, val_loss_epoch

# %%
class CNNAutoencoder(nn.Module):

    def __init__(self, img_shape):
        """
        code_size это размерность кодированного представления (фичей на выходе)
        """
        super().__init__()
        
        def initialization(layer):
            if isinstance(layer, nn.Linear):
                torch.nn.init.xavier_uniform(layer.weight)
                layer.bias.data.fill_(0.)
    


        self.encoder = nn.Sequential(nn.Conv2d(in_channels=3, out_channels=32, kernel_size=3, stride=1, padding=1), # (48-3+1*2)/1+1 = 48
            nn.ELU(),
            nn.MaxPool2d(2), # (48-2+0)/2+1 = 24
            nn.Conv2d(in_channels=32, out_channels=64, kernel_size=3, stride=1, padding=1), # (24-3+1*2)/1+1 = 24
            nn.ELU(),
            nn.MaxPool2d(2), # (24-2+0)/2+1 = 12
            nn.Conv2d(in_channels=64, out_channels=128, kernel_size=3, stride=1, padding=1), # (12-3+1*2)/1+1 = 12
            nn.ELU(), 
            nn.MaxPool2d(2), # (12-2+0)/2+1 = 6
            nn.Conv2d(in_channels=128, out_channels=256, kernel_size=3, stride=1), # (6-3+0)/1+1 = 4
            nn.ELU(), 
            nn.AdaptiveMaxPool2d(1), # (4-4+0)/2+1 = 1
            nn.Flatten(),
            nn.Linear(256, 150)
            )

        self.decoder = nn.Sequential(nn.Linear(150, 150*4),
                                     nn.ReLU(),
                                     nn.Linear(150*4, 3*48*48))
        
        self.apply(initialization)
        
    def forward(self, x):
        print(x.shape, 'init')
        # x = torch.flatten(x, start_dim=0, end_dim=1)
        init_shape = x.shape
        print(x.shape, 'reshaped')

        latent_code = self.encoder(x)
        print(latent_code.shape, 'latent code')
        reconstruction = self.decoder(latent_code)
        print(reconstruction.shape, 'reconstructed')
        reconstruction = reconstruction.reshape(init_shape)
        
        # return latent_code
        return reconstruction, latent_code

    

# %%
autoencodercnn4 = CNNAutoencoder(dimenstion)
autoencodercnn4 = autoencodercnn4.to(DEVICE)

# %%
criterion = torch.nn.MSELoss()

print('input_shape', dimenstion)

# Use Adam optimizer
optimizer = optim.Adam(autoencodercnn4.parameters(), lr=1e-3)

# %%
summary(autoencodercnn4, ( 3, 48, 48))

# %%
X_train = torch.tensor(X_train, dtype=torch.float32)
X_test = torch.tensor(X_test, dtype=torch.float32)
dataset_train = TensorDataset(X_train)
dataset_test = TensorDataset(X_test)

BATCH_SIZE = 32

train_loader = DataLoader(dataset_train, batch_size=BATCH_SIZE, shuffle=True, num_workers=1)
test_loader = DataLoader(dataset_test, batch_size=BATCH_SIZE, shuffle=False, num_workers=1)

# %%
cnnmodel, cnn_train_loss, cnn_val_loss = train(autoencodercnn4, 
                                                  train_loader, test_loader, 
                                                  device=DEVICE, epochs=25, 
                                                  path='autoencodercnn')
torch.save(cnnmodel.state_dict(), 'cnnautoencoder' + '/cnn_auto_model_final.pt')

# %%



