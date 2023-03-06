from django.shortcuts import render
# S28A0me19OqB8I//ohSAvw==fWpmjbwz6CSNxF27
# Create your views here.


from django.shortcuts import render


# Create your views here.
def home(request):
    import json
    import requests
    if request.method == 'POST':
        query = request.POST['query']
        api_url = 'https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(
            api_url + query, headers={'X-Api-Key': 'S28A0me19OqB8I//ohSAvw==fWpmjbwz6CSNxF27'})
        try:
            api = json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api = "There is some sort of error"
            print(e)
        return render(request, 'home.html', {'api': api})
    else:
        return render(request, 'home.html', {'query': 'Enter a valid query'})
    # When you hit home, whatever the results are

    # fetch home.html file
