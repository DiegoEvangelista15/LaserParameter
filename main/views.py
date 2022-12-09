from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.contrib import auth, messages
from django.contrib.auth.models import User
from main.models import Parameter
from .forms import ParameterForm

def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        usuario = request.POST['usuario']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password2 == '1234':
            if usuario == '' or password == '':
                return redirect('index')
            user = auth.authenticate(request, username=usuario, password=password)
            if user is not None:
                auth.login(request, user)
                return redirect('main_page')
    return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')

def conta_usuario(request):
    return render(request, 'conta_usuario.html')

def criar_usuario(request):
    if request.method == 'POST':
        usuario = request.POST['username']
        email = request.POST['email']
        senha01 = request.POST['password']
        senha02 = request.POST['password2']

        if senha01 != senha02:
            return redirect('conta_usuario')
        user = User.objects.create_user(username=usuario, email=email, password=senha01)
        user.is_staff = True
        user.save()
        return redirect('index')
    return redirect('conta_usuario')

def main_page(request):
    return render(request, 'pagina_principal.html')

def criar_param(request):
    form = ParameterForm(request.POST)
    if form.is_valid():
        # parâmetros base
        tipo = request.POST['tipo']
        potencia = request.POST['potencia']
        espessura = request.POST['espessura']
        material = request.POST['material']
        gas = request.POST['gas']
        cut_speed = form.cleaned_data['cut_speed']
        lift_height = form.cleaned_data['lift_height']
        cut_height = form.cleaned_data['cut_height']
        cut_pressure = form.cleaned_data['cut_pressure']
        peak_power = form.cleaned_data['peak_power']
        duty_cycle = form.cleaned_data['duty_cycle']
        pulse_frequency = form.cleaned_data['pulse_frequency']
        focus = form.cleaned_data['focus']
        laser_on_delay = form.cleaned_data['laser_on_delay']
        pierce_stage = request.POST['pierce_stage']
        # piercing 1
        step_time = form.cleaned_data['step_time']
        piercing_height = form.cleaned_data['piercing_height']
        piercing_gas = form.cleaned_data['piercing_gas']
        piercing_pressure = form.cleaned_data['piercing_pressure']
        piercing_peak_power = form.cleaned_data['piercing_peak_power']
        piercing_duty_cycle = form.cleaned_data['piercing_duty_cycle']
        piercing_frequency = form.cleaned_data['piercing_frequency']
        piercing_focus = form.cleaned_data['piercing_focus']
        piercing_time = form.cleaned_data['piercing_time']
        piercing_extra_blow = form.cleaned_data['piercing_extra_blow']
        # piercing 1
        step_time2 = form.cleaned_data['step_time2']
        piercing_height2 = form.cleaned_data['piercing_height2']
        piercing_gas2 = form.cleaned_data['piercing_gas2']
        piercing_pressure2 = form.cleaned_data['piercing_pressure2']
        piercing_peak_power2 = form.cleaned_data['piercing_peak_power2']
        piercing_duty_cycle2 = form.cleaned_data['piercing_duty_cycle2']
        piercing_frequency2 = form.cleaned_data['piercing_frequency2']
        piercing_focus2 = form.cleaned_data['piercing_focus2']
        piercing_time2 = form.cleaned_data['piercing_time2']
        piercing_extra_blow2 = form.cleaned_data['piercing_extra_blow2']
        # piercing 3
        step_time3 = form.cleaned_data['step_time3']
        piercing_height3 = form.cleaned_data['piercing_height3']
        piercing_gas3 = form.cleaned_data['piercing_gas3']
        piercing_pressure3 = form.cleaned_data['piercing_pressure3']
        piercing_peak_power3 = form.cleaned_data['piercing_peak_power3']
        piercing_duty_cycle3 = form.cleaned_data['piercing_duty_cycle3']
        piercing_frequency3 = form.cleaned_data['piercing_frequency3']
        piercing_focus3 = form.cleaned_data['piercing_focus3']
        piercing_time3 = form.cleaned_data['piercing_time3']
        piercing_extra_blow3 = form.cleaned_data['piercing_extra_blow3']

        cria_para = Parameter.objects.create(
            tipo = tipo,
            potencia = potencia,
            espessura = espessura,
            material = material,
            gas = gas,
            cut_speed = cut_speed,
            lift_height = lift_height,
            cut_height = cut_height,
            cut_pressure = cut_pressure,
            peak_power = peak_power,
            duty_cycle = duty_cycle,
            pulse_frequency = pulse_frequency,
            focus = focus,
            laser_on_delay = laser_on_delay,
            pierce_stage = pierce_stage,
            #p1
            step_time = step_time,
            piercing_height = piercing_height,
            piercing_gas = piercing_gas,
            piercing_pressure = piercing_pressure,
            piercing_peak_power = piercing_peak_power,
            piercing_duty_cycle = piercing_duty_cycle,
            piercing_frequency = piercing_frequency,
            piercing_focus = piercing_focus,
            piercing_time = piercing_time,
            piercing_extra_blow = piercing_extra_blow,
            #p2
            step_time2 = step_time2,
            piercing_height2 = piercing_height2,
            piercing_gas2 = piercing_gas2,
            piercing_pressure2 = piercing_pressure2,
            piercing_peak_power2 = piercing_peak_power2,
            piercing_duty_cycle2 = piercing_duty_cycle2,
            piercing_frequency2 = piercing_frequency2,
            piercing_focus2 = piercing_focus2,
            piercing_time2 = piercing_time2,
            piercing_extra_blow2 = piercing_extra_blow2,
            #p3
            step_time3 = step_time3,
            piercing_height3 = piercing_height3,
            piercing_gas3 = piercing_gas3,
            piercing_pressure3 = piercing_pressure,
            piercing_peak_power3 = piercing_peak_power3,
            piercing_duty_cycle3 = piercing_duty_cycle3,
            piercing_frequency3 = piercing_frequency3,
            piercing_focus3 = piercing_focus3,
            piercing_time3 = piercing_time3,
            piercing_extra_blow3 = piercing_extra_blow3,

        )  
        cria_para.save()
        return redirect('listar_param')

    return render(request, 'criar_param.html', {'form': form})


def listar_param(request):
    parameter = Parameter.objects.all()
    return render(request, 'listar_param.html', {'parameter': parameter})

#TODO colocar as unidades
def acessar_para(request, para_id):
    para = get_object_or_404(Parameter, pk=para_id)
    para_acessar = {'para': para}
    return render(request, 'acessar_para.html', para_acessar)

#TODO fazer editar e deletar param


