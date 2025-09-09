from django.shortcuts import render

def show_main(request):
    context = {
        "app_name": "Goalie’s Safehouse",  # nama aplikasi
        "name": "Ilham Shahputra Hasim",
        "npm": "2406401193",
        "class": "PBP A"   
    }
    return render(request, "main.html", context)
