# djAI
![Mediamodifier-Design-Template (2)](https://user-images.githubusercontent.com/45902447/224530941-a1e0bd24-43ec-4c7c-a9ec-3a08e5844b75.png)

**Speech2Text, Text2Image Using OpenAI GPT API.**

1. You can upload Audio, and it will extract the text from audio.
1. Generate Image for the given text, with custom pixel sizes.

*This is simple project without dB, tests, or any other complex things. You can run it easily!*

#### Download:
```
>> git clone https://github.com/4yub1k/djAI.git
>> cd djAI
```

#### Installation:
```
>> python -m venv .venv
>> .venv/Scripts/activate
>> pip install -r requirements.txt
```

#### Environment variables:
Make a `.env` file and add following to SECRETS.\
Get your Token : [OpenAI Token](https://platform.openai.com/account/api-keys)
```
SECRET_KEY=<YOUR DJANGO SECRET_KEY>
ALLOWED_HOSTS=127.0.0.1 localhost
DEBUG=True
OPENAI_API_KEY=<YOUR TOKEN>
```

#### Run:
```
>> py manage.py runserver
or
>> python3 manage.py runserver
```

## Project:

#### Speech2Text:
![image](https://user-images.githubusercontent.com/45902447/224529443-8f30c882-c49b-4e20-b400-44bb8e691a4e.png)
![image](https://user-images.githubusercontent.com/45902447/224529606-88a27119-1eb9-4c91-bcae-5b2b1fa138cc.png)

#### Text2Image:
![image](https://user-images.githubusercontent.com/45902447/224529627-0cc12bf5-0e18-4151-9244-c84453a1463c.png)
![image](https://user-images.githubusercontent.com/45902447/224529668-ca3a04c5-9a8a-443c-845d-72f579388f29.png)
![image](https://user-images.githubusercontent.com/45902447/224529723-513dd40b-5a73-49fa-9b35-19bc9c54e388.png)

*Feel free to use the project.* 😎
