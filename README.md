
# phishing-website

## 1. Create a Virtual Environment

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

## 3. Set Up HTTPS Certificate

Install the required dependencies:

```bash
sudo apt update
sudo apt install -y libnss3-tools curl
```
Download `mkcert`:

```bash
curl -JLO "https://dl.filippo.io/mkcert/latest?for=linux/amd64"
```

Make it executable and move it into your PATH:

```bash
chmod +x mkcert-v*-linux-amd64
sudo mv mkcert-v*-linux-amd64 /usr/local/bin/mkcert
```

Verify the installation:

```bash
mkcert -version
```

Install the local certificate authority:

```bash
mkcert -install
```

Create a certificate directory:

```bash
mkdir -p certs
```

Generate the localhost certificate and private key:

```bash
mkcert -key-file certs/localhost-key.pem \
       -cert-file certs/localhost.pem \
       localhost 127.0.0.1
```
Do not commit your private certificate key or root CA key

## 4. Run the Application

```bash
python app.py
```

The application runs locally at:
*HTTP:* http://127.0.0.1:5000
*HTTPS (if certificates are configured):* https://localhost:5000
