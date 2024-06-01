# Secure Communication Simulation

這個項目實現了安全通信模擬，涵蓋了Diffie-Hellman密鑰交換、RSA加密解密以及數字簽名。它旨在提供一個簡單的示例，展示如何在Python中使用`cryptography`庫進行密鑰交換和加密通信。

## 功能

- **Diffie-Hellman密鑰交換**：安全地在兩個參與者之間共享密鑰，不需要事先共享秘密。
- **RSA加密和解密**：使用RSA公鑰加密技術對消息進行加密和解密。
- **數字簽名**：利用私鑰生成數字簽名並使用對應的公鑰進行驗證。

## 開始使用

### 環境需求

確保你的機器已經安裝了Python 3.6或以上版本。此外，你需要安裝`cryptography`和`sympy`庫，是這個項目的主要依賴。

### 安裝

首先，你需要安裝所需的Python庫：

```bash
pip install cryptography
pip install sympy
```
### 運行程式

直接運行main

```bash
python main.py
```