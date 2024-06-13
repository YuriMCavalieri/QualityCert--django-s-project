from django.shortcuts import render, redirect
from certificado.forms import UsuarioForms

def solicitar_certificado(request):
    if request.method == 'POST':
        form = UsuarioForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sucesso')
    else:
        form = UsuarioForms()
    return render(request, 'certificado/solicitar_certificado.html', {'form': form})

def sucesso(request):
    return render(request, 'certificado/sucesso.html')
