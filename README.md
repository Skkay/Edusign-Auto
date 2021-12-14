# Programmatically sign on Edusign

## Install
- Install requirements:
`python -m pip install -r requirements.txt`

## Usage
### Credentials
- Get your credentials: 
`python get_credentials.py --username your_edusign_username --password your_edusign_password`. This will print your JWT, school ID and student ID.

- Set your credentials in `.env` (or `.env.local`)

### Signature
- Signature must be a base64 encoded PNG image (**400x200**).
Upload and get your base64 using an online tool like https://base64.guru/converter/encode/image/png.

- Set your base64 output in `.env` (or `.env.local`)

### Run
`python main.py`
