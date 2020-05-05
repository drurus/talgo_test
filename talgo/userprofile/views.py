from django.shortcuts import render, redirect
from django.views import generic
from .models import Activity, User, Shop
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.shortcuts import Http404

from .forms import CheckAnketaForm


@login_required
def index(request):
    """
    Функция отображения анкетирования
    """
    return render(request, 'index.html', context=prep_val(request))


def prep_val(req):
    """Начальные значения для формы"""
    cc = {}
    cnt_users = User.objects.all().count()
    activity_list = Activity.objects.all().values()
    cc = {
        'cnt_users': cnt_users,
        'activity_list': activity_list
    }
    return cc


@login_required
def add_user(request):
    if request.method == 'POST':
        form = CheckAnketaForm(request.POST)
        context = {'form': form}

        if form.is_valid():
            # print('form cleaned_data: ', form.cleaned_data)
            context.update(prep_val(request))
            user = User(login=f'''{form.cleaned_data['name']}_{form.cleaned_data['lastname']}'''.replace(' ', '_'),
                        name=form.cleaned_data['name'],
                        lastname=form.cleaned_data['lastname'],
                        age=form.cleaned_data['age'],
                        activity=Activity(form.cleaned_data['activity']),
                        email=form.cleaned_data.get('email', ''),
                        social=form.cleaned_data.get('social', '')
                        )
            user.save()
            return redirect('shop')
    else:
        return redirect('index')

    context = prep_val(request)
    context['error'] = form.errors.get('__all__', None)
    return render(request, 'index.html', context=context)


class UserProfileView(LoginRequiredMixin, generic.ListView):
    """
    userlist
    """
    model = User
    paginate_by = 2

    def get_context_data(self, **kwargs):
        context = super(UserProfileView, self).get_context_data(**kwargs)
        context['cnt_users'] = User.objects.all().count()

        return context


# class UserProfileViewName(LoginRequiredMixin, UserProfileView):
#     model = User

# def __init__(self, *args,**kwargs):
#     super().__init__(*args, **kwargs)


# def get_queryset(self):
#     return User.objects.filter(login__icontains='name')


# class UserProfileViewOther(UserProfileView):
#     model = User
#
#     def get_queryset(self):
#         return User.objects.filter(login__icontains='name')


class UserDetailView(LoginRequiredMixin, generic.DetailView):
    model = User

    def get_context_data(self, **kwargs):
        context = super(UserDetailView, self).get_context_data(**kwargs)
        context['cnt_users'] = User.objects.all().count()

        return context


class ShopItemsViewList(LoginRequiredMixin, generic.ListView):
    model = Shop
    paginate_by = 5
    # context_object_name = 'shop_list'


@login_required
def shop_bucket(request):
    if request.method == 'POST':
        print('bucket POST')
        print('form POST: ', request.POST)
        checks = request.POST.getlist('checks', [])
        context, cost = {}, 0

        selItems = Shop.objects.filter(code__in=checks).values()

        for el in selItems:
            print(el)
            cost += el.get('cost', 0)

        context['form'] = {
            'items': selItems,
            'cost': cost,
        }
    else:
        print('bucket GET')
        form = ShopForm(request.GET)
        context = {'form': form}

    return render(request, 'bucket.html', context=context)
