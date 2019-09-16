from django.shortcuts import render, get_object_or_404,redirect
from webapp.forms import PlanForm
from webapp.models import Plan


def index_view(request, *args, **kwargs):
    plans = Plan.objects.all()
    context = {
        'plans': plans
    }
    return render(request, 'index.html', context)


def plan_view(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    return render(request, 'plan_view.html', context={
        'plan': plan
    })


def plan_create_view(request, *args, **kwargs):
    if request.method == 'GET':
        form = PlanForm()
        return render(request, 'plan_create.html', context={'form': form})
    elif request.method == 'POST':
        form = PlanForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            plan = Plan.objects.create(
                title=data['title'],
                text=data['text'],
                status=data['status'],
                deadline=data['deadline']
            )
            return redirect('view_plan', pk=plan.pk)
        else:
            return render(request, 'plan_create.html', context={'form': form})


def plan_edit(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'GET':
        form = PlanForm(data={
            'title': plan.title,
            'text': plan.text,
            'status': plan.status,
            'deadline': plan.deadline
        })
        return render(request, 'plan_edit.html', context={'form': form, 'plan': plan})
    elif request.method == 'POST':
        form = PlanForm(data=request.POST)
        if form.is_valid():
            data = form.cleaned_data
            plan.title = data['title']
            plan.text = data['text']
            plan.status = data['status']
            plan.deadline = data['deadline']
            plan.save()
            return redirect('view_plan', pk=plan.pk)
        else:
            return render(request, 'plan_edit.html', context={'form': form, 'plan': plan})


def delete_view(request, pk):
    plan = get_object_or_404(Plan, pk=pk)
    if request.method == 'GET':
        return render(request, 'plan_delete.html', context={'plan': plan})
    elif request.method == 'POST':
        plan.delete()
    return redirect('index')


def item_delete(request):
    values = request.POST.getlist('choice_item')
    Plan.objects.filter(pk__in=values).delete()
    return redirect('index')

