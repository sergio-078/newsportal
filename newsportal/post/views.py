from django.shortcuts import render
from django.views.generic import DetailView, ListView, CreateView

from .models import Post
from .filters import PostFilter
from .forms import PostForm, SearchForm


# def about_func(request):
#     return render(request, 'newslist/about.html', {'title': 'О портале новостей'})


class PostDetail(DetailView):
    # Модель по которой мы хотим получать информацию по отдельной статье
    model = Post
    # Используем другой шаблон — post_detail.html
    template_name = "post/post_detail.html"
    # Название объекта, в котором будет выбранная пользователем статья
    context_object_name = "postdetail"
    #queryset = Post.objects.get(pk=pk)


class PostList(ListView):
    model = Post
    ordering = '-dateCreation'
    template_name = 'post/post_list.html'
    context_object_name = 'postlist'
    paginate_by = 2  # количество записей на странице

    # Переопределяем функцию получения списка товаров
    def get_queryset(self):
        # Получаем обычный запрос
        queryset = super().get_queryset()
        # Используем наш класс фильтрации.
        # self.request.GET содержит объект QueryDict, который мы рассматривали
        # в этом юните ранее.
        # Сохраняем нашу фильтрацию в объекте класса,
        # чтобы потом добавить в контекст и использовать в шаблоне.
        self.filterset = PostFilter(self.request.GET, queryset)
        # Возвращаем из функции отфильтрованный список товаров
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Добавляем в контекст объект фильтрации.
        context['filterset'] = self.filterset
        return context
class PostCreate(CreateView):
    # Указываем нашу разработанную форму
    form_class = PostForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'newslist/news_edit.html'

class PostSearch(CreateView):
    # Указываем нашу разработанную форму
    form_class = SearchForm
    # модель товаров
    model = Post
    # и новый шаблон, в котором используется форма.
    template_name = 'newslist/search.html'
