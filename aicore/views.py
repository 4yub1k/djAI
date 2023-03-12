import openai

from django.shortcuts import render
from django.views import generic
from django.conf import settings
from pathlib import Path


openai.api_key = settings.OPENAI_API_KEY
BASE_DIR = Path(__file__).resolve().parent


class Home(generic.TemplateView):
    """
    Edit to Modify Main "/" page.
    """
    template_name = "aicore/home.html"


def speech2Text(request):
    """
    Speech to Text.
    """
    if request.method == "POST":
        audio = request.FILES.get("audio")

        try:
            with open(f'{BASE_DIR}/audio/{audio.name}', 'wb+') as file:
                for chunk in audio.chunks():
                    file.write(chunk)
        except AttributeError:
            return render(request, "aicore/speech.html", {})

        audio_file = open(f'{BASE_DIR}/audio/{audio.name}', "rb")
        transcript = openai.Audio.translate("whisper-1", audio_file)    # {"text": "text"}

        return render(request, "aicore/speech.html", transcript)
    else:
        return render(request, "aicore/speech.html", {})


class Text2Image(generic.TemplateView):
    """
    Text to Image.
    """
    template_name = "aicore/image.html"

    def post(self, request, **kwargs):
        context = self.get_context_data(**kwargs)

        response = openai.Image.create(
            prompt=request.POST.get("text"),
            n=1,
            size=request.POST.get("size")
        )

        context["image"] = response['data'][0]['url']
        context["alt"] = request.POST.get("text")

        return self.render_to_response(context)
