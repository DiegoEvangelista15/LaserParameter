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

def acessar_para(request, para_id):
    para = get_object_or_404(Parameter, pk=para_id)
    para_acessar = {'para': para}
    return render(request, 'acessar_para.html', para_acessar)

def delete_para(request, delete_id):   #TODO colocar uma segurança nessa função
    deleta_param = get_object_or_404(Parameter, pk=delete_id)
    deleta_param.delete()
    return redirect('listar_param')

def edita_para(request, edita_id):
    para = get_object_or_404(Parameter, pk=edita_id)
    param_edit = {'para' : para}
    return render(request, 'edita_para.html', param_edit)

def atualiza_para(request):
    if request.method == "POST":
        para_id = request.POST['para_id']
        p = Parameter.objects.get(pk=para_id)

        if request.POST['pierce_stage'] == '3':
        
            # basic para
            p.tipo = request.POST['tipo']
            p.potencia = request.POST['potencia']
            p.espessura = request.POST['espessura']
            p.material = request.POST['material']
            p.gas = request.POST['gas']
            p.cut_speed = request.POST['cut_speed']
            p.lift_height = request.POST['lift_height']
            p.cut_height = request.POST['cut_height']
            p.cut_pressure = request.POST['cut_pressure']
            p.peak_power = request.POST['peak_power']
            p.duty_cycle = request.POST['duty_cycle']
            p.pulse_frequency = request.POST['pulse_frequency']
            p.focus = request.POST['focus']
            p.laser_on_delay = request.POST['laser_on_delay']
            p.pierce_stage = request.POST['pierce_stage']
            
            # piercing 1
            p.step_time = request.POST['step_time']
            p.piercing_height = request.POST['piercing_height']
            p.piercing_gas = request.POST['piercing_gas']
            p.piercing_pressure = request.POST['piercing_pressure']
            p.piercing_peak_power = request.POST['piercing_peak_power']
            p.piercing_duty_cycle = request.POST['piercing_duty_cycle']
            p.piercing_frequency = request.POST['piercing_frequency']
            p.piercing_focus = request.POST['piercing_focus']
            p.piercing_time = request.POST['piercing_time']
            p.piercing_extra_blow = request.POST['piercing_extra_blow']
            # piercing 2
            p.step_time2 = request.POST['step_time2']
            p.piercing_height2 = request.POST['piercing_height2']
            p.piercing_gas2 = request.POST['piercing_gas2']
            p.piercing_pressure2 = request.POST['piercing_pressure2']
            p.piercing_peak_power2 = request.POST['piercing_peak_power2']
            p.piercing_duty_cycle2 = request.POST['piercing_duty_cycle2']
            p.piercing_frequency2 = request.POST['piercing_frequency2']
            p.piercing_focus2 = request.POST['piercing_focus2']
            p.piercing_time2 = request.POST['piercing_time2']
            p.piercing_extra_blow2 = request.POST['piercing_extra_blow2']
            # piercing 3
            p.step_time3 = request.POST['step_time3']
            p.piercing_height3 = request.POST['piercing_height3']
            p.piercing_gas3 = request.POST['piercing_gas3']
            p.piercing_pressure3 = request.POST['piercing_pressure3']
            p.piercing_peak_power3 = request.POST['piercing_peak_power3']
            p.piercing_duty_cycle3 = request.POST['piercing_duty_cycle3']
            p.piercing_frequency3 = request.POST['piercing_frequency3']
            p.piercing_focus3 = request.POST['piercing_focus3']
            p.piercing_time3 = request.POST['piercing_time3']
            p.piercing_extra_blow3 = request.POST['piercing_extra_blow3']

            p.save()
            return redirect('listar_param')

        elif request.POST['pierce_stage'] == '2':
        
            # basic para
            p.tipo = request.POST['tipo']
            p.potencia = request.POST['potencia']
            p.espessura = request.POST['espessura']
            p.material = request.POST['material']
            p.gas = request.POST['gas']
            p.cut_speed = request.POST['cut_speed']
            p.lift_height = request.POST['lift_height']
            p.cut_height = request.POST['cut_height']
            p.cut_pressure = request.POST['cut_pressure']
            p.peak_power = request.POST['peak_power']
            p.duty_cycle = request.POST['duty_cycle']
            p.pulse_frequency = request.POST['pulse_frequency']
            p.focus = request.POST['focus']
            p.laser_on_delay = request.POST['laser_on_delay']
            p.pierce_stage = request.POST['pierce_stage']
            
            # piercing 1
            p.step_time = request.POST['step_time']
            p.piercing_height = request.POST['piercing_height']
            p.piercing_gas = request.POST['piercing_gas']
            p.piercing_pressure = request.POST['piercing_pressure']
            p.piercing_peak_power = request.POST['piercing_peak_power']
            p.piercing_duty_cycle = request.POST['piercing_duty_cycle']
            p.piercing_frequency = request.POST['piercing_frequency']
            p.piercing_focus = request.POST['piercing_focus']
            p.piercing_time = request.POST['piercing_time']
            p.piercing_extra_blow = request.POST['piercing_extra_blow']
            # piercing 2
            p.step_time2 = request.POST['step_time2']
            p.piercing_height2 = request.POST['piercing_height2']
            p.piercing_gas2 = request.POST['piercing_gas2']
            p.piercing_pressure2 = request.POST['piercing_pressure2']
            p.piercing_peak_power2 = request.POST['piercing_peak_power2']
            p.piercing_duty_cycle2 = request.POST['piercing_duty_cycle2']
            p.piercing_frequency2 = request.POST['piercing_frequency2']
            p.piercing_focus2 = request.POST['piercing_focus2']
            p.piercing_time2 = request.POST['piercing_time2']
            p.piercing_extra_blow2 = request.POST['piercing_extra_blow2']
            
            p.save()
            return redirect('listar_param')

        elif request.POST['pierce_stage'] == '1':
        
            # basic para
            p.tipo = request.POST['tipo']
            p.potencia = request.POST['potencia']
            p.espessura = request.POST['espessura']
            p.material = request.POST['material']
            p.gas = request.POST['gas']
            p.cut_speed = request.POST['cut_speed']
            p.lift_height = request.POST['lift_height']
            p.cut_height = request.POST['cut_height']
            p.cut_pressure = request.POST['cut_pressure']
            p.peak_power = request.POST['peak_power']
            p.duty_cycle = request.POST['duty_cycle']
            p.pulse_frequency = request.POST['pulse_frequency']
            p.focus = request.POST['focus']
            p.laser_on_delay = request.POST['laser_on_delay']
            p.pierce_stage = request.POST['pierce_stage']
            
            # piercing 1
            p.step_time = request.POST['step_time']
            p.piercing_height = request.POST['piercing_height']
            p.piercing_gas = request.POST['piercing_gas']
            p.piercing_pressure = request.POST['piercing_pressure']
            p.piercing_peak_power = request.POST['piercing_peak_power']
            p.piercing_duty_cycle = request.POST['piercing_duty_cycle']
            p.piercing_frequency = request.POST['piercing_frequency']
            p.piercing_focus = request.POST['piercing_focus']
            p.piercing_time = request.POST['piercing_time']
            p.piercing_extra_blow = request.POST['piercing_extra_blow']
            
            p.save()
            return redirect('listar_param')

        else:

            # basic para
            p.tipo = request.POST['tipo']
            p.potencia = request.POST['potencia']
            p.espessura = request.POST['espessura']
            p.material = request.POST['material']
            p.gas = request.POST['gas']
            p.cut_speed = request.POST['cut_speed']
            p.lift_height = request.POST['lift_height']
            p.cut_height = request.POST['cut_height']
            p.cut_pressure = request.POST['cut_pressure']
            p.peak_power = request.POST['peak_power']
            p.duty_cycle = request.POST['duty_cycle']
            p.pulse_frequency = request.POST['pulse_frequency']
            p.focus = request.POST['focus']
            p.laser_on_delay = request.POST['laser_on_delay']
            p.pierce_stage = request.POST['pierce_stage']

            p.save()
            return redirect('listar_param')
#TODO realizar filtro
#TODO colocar mensagens de erro




