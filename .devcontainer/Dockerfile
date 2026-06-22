FROM python:3.12-slim

# Git इंस्टॉल करना ताकि आप अंदर से भी गिट कमांड्स चला सकें
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# वर्कस्पेस डायरेक्टरी सेट करना
WORKDIR /workspace