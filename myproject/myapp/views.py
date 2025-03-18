from django.shortcuts import render
from django.http import HttpResponse
import os
import datetime
import subprocess

def htop(request):
    name = "Saksham Jain"
    username = os.getenv("Saksham") or os.getenv("Dell")
    server_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S IST")
    top_output = subprocess.getoutput("top -b -n 1 | head -10")

    return HttpResponse(f"""
    <h1>Name: {name}</h1>
    <h2>Username: {username}</h2>
    <h2>Server Time: {server_time}</h2>
    <pre>{top_output}</pre>
    """)
